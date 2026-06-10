"""
Tier A model ladder. v1 (pure cross-prime independence) overpredicts ~6x.
Hypothesized mechanism: conditional on an element being sqrt(2n)-smooth, its
log-mass is redistributed into medium primes, multiplying the number of carry
'coin flips'. v1 treats prime events as independent and misses this.

Ladder (each step replaces one modeled ingredient with the real thing):
  v1  : product of per-prime marginals (cross-prime independence). [done]
  v2  : sample k+1 IID random integers in [A,B], use their REAL joint
        factorizations; simulate the carry digits (exact digit-chain sim,
        legitimate by CRT independence across primes). Captures within-element
        cross-prime correlation; assumes independence ACROSS elements.
  v2b : same, but the k+1 elements are a REAL consecutive window n,..,n-k.
        Captures consecutive-integer factorization correlations too.
  v0  : everything real = empirical density. (exact_scan.py)

Gaps:  v1->v2 = within-element correlation;  v2->v2b = consecutiveness;
       v2b->v0 = digit-model error (should be ~0 by CRT).
"""
import sys, json, math, time
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np

rng = np.random.default_rng(777)

NMAX = 2_000_001
spf = np.zeros(NMAX + 1, dtype=np.int32)
for p in range(2, int(NMAX ** 0.5) + 1):
    if spf[p] == 0:
        sl = spf[p * p::p]
        sl[sl == 0] = p


def factorize(x):
    f = {}
    while x > 1:
        p = int(spf[x])
        if p == 0:
            p = x
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        f[p] = e
    return f


def sim_success(p, e, n, i, rstate):
    """
    Simulate whether prime power p^e || (n-i) gets >= e carries, given
    n ≡ i (mod p^e), digits above level e uniform (exact in distribution).
    Positions j with p^j <= n: chain-uniform. One extra free carry if
    n < p^(L'+1) <= 2n (then n mod p^(L'+1) = n >= p^(L'+1)/2).
    """
    # L' = max j with p^j <= n
    Lp = 0
    q = 1
    while q * p <= n:
        q *= p
        Lp += 1
    free = 1 if q * p <= 2 * n else 0
    U = Lp - e  # uniform positions j = e+1 .. L'
    if U < 0:
        U = 0
    if U + free < e:
        return False
    if e == 0:
        return True
    # simulate chain t uniform in [0, p^U)
    pe = p ** e
    t = int(rstate.integers(0, p ** U)) if U > 0 else 0
    c = free
    pj = pe
    tm = 1
    for j in range(e + 1, Lp + 1):
        pj *= p
        tm *= p
        r = i + pe * (t % tm)
        if 2 * r >= pj:
            c += 1
            if c >= e:
                return True
    return c >= e


def small_prime_factor(k, A, B, Pdirect, N=400_000):
    """F_small = prod_{p<=Pdirect} (1 - f_p) by direct MC (exact marginals;
    cross-prime independence among the handful of small primes is retained)."""
    from heuristic import f_direct, PRIMES
    F = 1.0
    for p in PRIMES[PRIMES <= Pdirect]:
        F *= (1 - f_direct(int(p), k, A, B, N=N))
    return F


def v2_density(k, A, B, N=40_000, consecutive=False):
    Pdirect = max(31, 2 * k + 3)
    Fs = small_prime_factor(k, A, B, Pdirect)
    hits = 0
    for _ in range(N):
        if consecutive:
            n = int(rng.integers(A, B + 1))
            elems = [(n - i, i, n) for i in range(k + 1)]
        else:
            ms = rng.integers(A, B + 1, k + 1)
            elems = [(int(ms[i]), i, int(ms[i]) + i) for i in range(k + 1)]
        ok = True
        for (m, i, nval) in elems:
            for p, e in factorize(m).items():
                if p <= Pdirect:
                    continue
                if not sim_success(p, e, nval, i, rng):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            hits += 1
    cond = hits / N
    return Fs * cond, Fs, cond


if __name__ == "__main__":
    RANGES = [(5_000, 20_000), (50_000, 200_000), (500_000, 2_000_000)]
    out = {}
    t0 = time.time()
    for (A, B) in RANGES:
        for k in [1, 2, 3, 4, 5]:
            d2, Fs, c2 = v2_density(k, A, B, N=40_000, consecutive=False)
            d2b, _, c2b = v2_density(k, A, B, N=40_000, consecutive=True)
            out[f"{A}-{B}|k={k}"] = {"v2": d2, "v2b": d2b, "F_small": Fs,
                                     "cond_v2": c2, "cond_v2b": c2b}
            print(f"[{A},{B}] k={k}: v2={d2:.6f}  v2b={d2b:.6f}  "
                  f"(F_small={Fs:.4f}, cond v2={c2:.4f}, v2b={c2b:.4f})  "
                  f"{time.time()-t0:.0f}s", flush=True)
    with open("/home/claude/erdos396/model_v2.json", "w") as f:
        json.dump(out, f, indent=1)
    print("saved")

