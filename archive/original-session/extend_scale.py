"""
One more decade: exact sampled densities at n ~ 10^9 for k=1,2.
Vectorized trial division by primes <= sqrt(2e9) ~ 44721 finds all small prime
factors; any remaining cofactor > 1 is a single prime > sqrt(B) (so the window
is non-smooth and automatically fails -- but we record it exactly anyway).
"""
import sys, time, json
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np
from divcheck import carries

rng = np.random.default_rng(999)
A, B = 500_000_000, 2_000_000_000
KMAX = 2
KS = [1, 2]
N = 120_000
PDIRECT = 31

t0 = time.time()
PL = int((2 * B) ** 0.5) + 1
sieve = np.ones(PL + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(PL ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
primes = np.nonzero(sieve)[0]
print(f"{len(primes)} primes to {PL}, {time.time()-t0:.0f}s", flush=True)

ns = rng.integers(A, B + 1, N, dtype=np.int64)
# window matrix: column i = n - i
X = np.stack([ns - i for i in range(KMAX + 1)], axis=1)  # (N, KMAX+1)
cof = X.copy()
# per-sample factor store: list of dicts {p: total exponent in window so far per element}
fac = [[{} for _ in range(KMAX + 1)] for _ in range(N)]

for p in primes:
    p = int(p)
    m = (cof % p) == 0
    if not m.any():
        continue
    rows, cols = np.nonzero(m)
    for r, c in zip(rows.tolist(), cols.tolist()):
        x = int(cof[r, c])
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        cof[r, c] = x
        fac[r][c][p] = e
print(f"trial division done {time.time()-t0:.0f}s", flush=True)

agg = {k: {"all": 0, "med": 0, "small": 0, "med_and_small": 0} for k in KS}
for r in range(N):
    n = int(ns[r])
    need = {}
    cc = {}
    small_ok = True
    med_ok = True
    for k in range(0, KMAX + 1):
        f = dict(fac[r][k])
        c = int(cof[r, k])
        if c > 1:
            f[c] = f.get(c, 0) + 1  # big prime cofactor
        for p, e in f.items():
            tot = need.get(p, 0) + e
            need[p] = tot
            if (p <= PDIRECT and small_ok) or (p > PDIRECT and med_ok):
                if p not in cc:
                    cc[p] = carries(n, p)
                if cc[p] < tot:
                    if p <= PDIRECT:
                        small_ok = False
                    else:
                        med_ok = False
        if k in agg:
            a = agg[k]
            if small_ok: a["small"] += 1
            if med_ok: a["med"] += 1
            if small_ok and med_ok: a["all"] += 1; a["med_and_small"] += 1
        if not small_ok and not med_ok:
            break

out = {}
for k in KS:
    a = agg[k]
    Pmed = a["med"] / N
    out[k] = {"D_emp": a["all"] / N, "P_med": Pmed, "P_small": a["small"] / N,
              "P_small_given_med": (a["med_and_small"] / a["med"]) if a["med"] else None,
              "hits": a["all"], "N": N}
    print(f"[5e8,2e9] k={k}: D_emp={a['all']/N:.6f} ({a['all']} hits)  "
          f"P_med={Pmed:.5f}  P_small={a['small']/N:.4f}  "
          f"P(small|med)={(a['med_and_small']/a['med']) if a['med'] else float('nan'):.4f}",
          flush=True)
with open("/home/claude/erdos396/empirical_1e9.json", "w") as fh:
    json.dump(out, fh, indent=1)
print(f"total {time.time()-t0:.0f}s saved")

