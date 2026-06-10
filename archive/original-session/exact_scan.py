"""
Exact empirical witness densities for k=1..5 over three magnitude ranges,
to compare against the Tier A independence model.

Uses a smallest-prime-factor sieve for fast factorization; the divisibility
test is the verified Kummer digit criterion (no big integers).
"""
import sys, json, time
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np
from divcheck import carries

RANGES = [(5_000, 20_000), (50_000, 200_000), (500_000, 2_000_000)]
KS = [1, 2, 3, 4, 5]
NMAX = max(b for _, b in RANGES)

t0 = time.time()
spf = np.zeros(NMAX + 1, dtype=np.int32)
for p in range(2, int(NMAX ** 0.5) + 1):
    if spf[p] == 0:
        sl = spf[p * p::p]
        sl[sl == 0] = p
print(f"sieve done {time.time()-t0:.1f}s", flush=True)


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


results = {}
for (A, B) in RANGES:
    counts = {k: 0 for k in KS}
    kmax = max(KS)
    # rolling factorizations of n, n-1, ..., n-kmax
    facs = [factorize(A - i) if A - i > 1 else {} for i in range(kmax + 1)]
    for n in range(A, B + 1):
        if n > A:
            facs.pop()
            facs.insert(0, factorize(n))
        # cumulative needs as k grows; reuse carries per (n,p)
        need = {}
        cc = {}
        ok = True
        for k in KS:
            if ok:
                # extend window from previous k (KS consecutive-ish: handle gaps generally)
                pass
        # build incrementally over window indices
        need = {}
        cc = {}
        alive = True
        ki = 0
        for k in range(0, kmax + 1):
            for p, e in facs[k].items():
                need[p] = need.get(p, 0) + e
                if alive:
                    if p not in cc:
                        cc[p] = carries(n, p)
                    if cc[p] < need[p]:
                        alive = False
            if k in counts and alive:
                counts[k] += 1
            if not alive and k >= max(KS):
                break
            # once dead, stays dead (monotone in k) -> can break early
            if not alive:
                break
    total = B - A + 1
    results[f"{A}-{B}"] = {str(k): (counts[k], counts[k] / total) for k in KS}
    print(f"range [{A},{B}] done at {time.time()-t0:.1f}s: "
          + ", ".join(f"k={k}:{counts[k]} ({counts[k]/total:.6f})" for k in KS), flush=True)

with open("/home/claude/erdos396/exact_densities.json", "w") as f:
    json.dump(results, f, indent=1)
print("saved", flush=True)

