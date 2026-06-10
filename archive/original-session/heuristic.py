"""
Tier A heuristic model for Erdos 396 witness density.

Model: D(k; [A,B]) = product over primes p of  P_p,
where P_p = Pr_n[ sum_{i<=k} v_p(n-i) <= #carries_p(n) ]  for n uniform in [A,B].

Each P_p marginal is computed by Monte Carlo against the TRUE distribution of n
(no digit-uniformity assumption), so the only modeling assumption is
INDEPENDENCE ACROSS PRIMES. Comparing the product to exact empirical densities
therefore isolates cross-prime correlations.

Prime regimes:
  * p <= Pdirect = max(31, 2k+3):  direct MC (failure prob not small).
  * Pdirect < p <= Pmax = isqrt(2B): importance-sampled MC conditioned on the
    rare event n mod p <= k (prob (k+1)/p), so f_p = (k+1)/p * g_p with g_p the
    conditional failure rate.
  * p > Pmax (so p > sqrt(2n) for ALL n in range): such p must not divide any
    n-i. Within one element these events are mutually exclusive (p,q > sqrt(x)
    => pq > x), so P(element clean) = 1 - sum 1/p EXACTLY; across the k+1
    elements we assume independence:  ((1 - s))^(k+1),  s = sum_{Pmax<p<=n*} 1/p
    computed from an exact prime reciprocal sum.
"""
import sys, json, math, time
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np

rng = np.random.default_rng(396396)

# ---------- primes up to 2e6 (for exact reciprocal sums and prime lists) ----------
PMAXSIEVE = 2_000_000
sieve = np.ones(PMAXSIEVE + 1, dtype=bool)
sieve[:2] = False
for p in range(2, int(PMAXSIEVE ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
PRIMES = np.nonzero(sieve)[0].astype(np.int64)
RECIP = 1.0 / PRIMES
CUMRECIP = np.cumsum(RECIP)

def recip_sum(lo, hi):
    """sum of 1/p over primes p with lo < p <= hi (hi <= 2e6)."""
    i = np.searchsorted(PRIMES, lo, side="right")
    j = np.searchsorted(PRIMES, hi, side="right")
    return CUMRECIP[j - 1] - (CUMRECIP[i - 1] if i > 0 else 0.0) if j > i else 0.0

# ---------- vectorized v_p and carries ----------
def vp_vec2(x, p):
    x = x.copy()
    v = np.zeros_like(x)
    while True:
        m = (x % p == 0) & (x > 0)
        if not m.any():
            return v
        x[m] //= p
        v[m] += 1

def carries_vec(n, p, two_B):
    c = np.zeros_like(n)
    q = p
    while q <= two_B:
        c += (2 * (n % q) >= q)
        q *= p
    return c
    # note: if q > 2n elementwise then n mod q = n and 2n < q, condition auto-false.

# ---------- per-prime failure probabilities ----------
def f_direct(p, k, A, B, N=400_000):
    n = rng.integers(A, B + 1, N, dtype=np.int64)
    need = np.zeros(N, dtype=np.int64)
    for i in range(k + 1):
        need += vp_vec2(n - i, p)
    have = carries_vec(n, p, 2 * B)
    f = float(np.mean(need > have))
    return f

def f_conditioned(p, k, A, B, N=20_000):
    """f_p = (k+1)/p * Pr[fail | n mod p = u, u uniform in 0..k]."""
    u = rng.integers(0, k + 1, N, dtype=np.int64)
    lo_q = (A - u + p - 1) // p
    hi_q = (B - u) // p
    q = (rng.random(N) * (hi_q - lo_q + 1)).astype(np.int64) + lo_q
    n = u + q * p
    need = vp_vec2(n - u, p)          # only i=u is divisible since p > 2k+1
    have = carries_vec(n, p, 2 * B)
    g = float(np.mean(need > have))
    return (k + 1) / p * g, g

def model_density(k, A, B, n_star=None, verbose=False):
    if n_star is None:
        n_star = int(math.sqrt(A * B))
    Pdirect = max(31, 2 * k + 3)
    Pmax = math.isqrt(2 * B)
    logD = 0.0
    budget = {}
    # small primes
    small = 0.0
    for p in PRIMES[PRIMES <= Pdirect]:
        f = f_direct(int(p), k, A, B)
        small += -math.log(1 - f)
    budget["small p<=%d" % Pdirect] = small
    logD -= small
    # medium primes, grouped by digit count L at n*
    med = {}
    for p in PRIMES[(PRIMES > Pdirect) & (PRIMES <= Pmax)]:
        p = int(p)
        f, g = f_conditioned(p, k, A, B)
        L = int(math.log(2 * n_star) / math.log(p))
        key = f"L={L}" if L <= 4 else "L>=5"
        med[key] = med.get(key, 0.0) + (-math.log(1 - f))
    for key in sorted(med):
        budget[key] = med[key]
        logD -= med[key]
    # large primes: exact exclusive sum, independent across elements
    s = recip_sum(Pmax, n_star)
    smooth_term = -(k + 1) * math.log(1 - s)
    budget["smooth p>sqrt(2B)"] = smooth_term
    logD -= smooth_term
    D = math.exp(logD)
    if verbose:
        print(f"  k={k} [{A},{B}]: D_model={D:.6f}  (-log budget: "
              + ", ".join(f"{k2}:{v:.3f}" for k2, v in budget.items()) + ")")
    return D, budget

if __name__ == "__main__":
    RANGES = [(5_000, 20_000), (50_000, 200_000), (500_000, 2_000_000)]
    out = {}
    t0 = time.time()
    for (A, B) in RANGES:
        for k in [1, 2, 3, 4, 5]:
            D, budget = model_density(k, A, B, verbose=True)
            out[f"{A}-{B}|k={k}"] = {"D_model": D, "budget": budget}
        print(f"range done {time.time()-t0:.1f}s", flush=True)
    with open("/home/claude/erdos396/model_densities.json", "w") as f:
        json.dump(out, f, indent=1)
    print("saved")

