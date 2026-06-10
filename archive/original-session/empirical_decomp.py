"""
Exact (sampled) empirical densities with decomposition.

For each sampled n and k: evaluate the true condition with REAL digits, split by
prime size at Pdirect=31:
   small_ok = all primes p<=31 satisfied
   med_ok   = all primes p>31 satisfied   (includes smoothness automatically)
   all_ok   = small_ok AND med_ok          (= witness)
Outputs per (range,k): D_emp, P(med_ok), P(small_ok), P(small_ok|med_ok).

Comparisons this enables:
   P(med_ok)            vs v2b conditional rate  -> validates digit simulation
   P(small_ok|med_ok)   vs F_small (=P(small_ok)) -> small x medium correlation
"""
import sys, json, time
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np
from divcheck import carries

rng = np.random.default_rng(123123)
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


PDIRECT = 31
KS = [1, 2, 3, 4, 5]
KMAX = max(KS)
RANGES = [(5_000, 20_000), (50_000, 200_000), (500_000, 2_000_000)]
N = 300_000

t0 = time.time()
results = {}
for (A, B) in RANGES:
    ns = rng.integers(A, B + 1, N)
    agg = {k: {"all": 0, "med": 0, "small": 0, "med_and_small": 0} for k in KS}
    for idx in range(N):
        n = int(ns[idx])
        need = {}
        cc = {}
        small_ok = True
        med_ok = True
        for k in range(0, KMAX + 1):
            x = n - k
            if x > 1:
                for p, e in factorize(x).items():
                    tot = need.get(p, 0) + e
                    need[p] = tot
                    # only re-check if this prime could now fail
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
                if small_ok:
                    a["small"] += 1
                if med_ok:
                    a["med"] += 1
                if small_ok and med_ok:
                    a["all"] += 1
                    a["med_and_small"] += 1
            if not small_ok and not med_ok:
                # both dead; everything monotone, but we still need per-k flags
                # only if some k in KS not yet recorded -> they'd all be False
                if k >= KMAX:
                    break
                # fast-forward: remaining ks all False
                for kk in KS:
                    if kk > k:
                        pass
                break
        # note: ks > break point correctly get no increments (all False)
    out = {}
    for k in KS:
        a = agg[k]
        D = a["all"] / N
        Pmed = a["med"] / N
        Psm = a["small"] / N
        Psm_given_med = (a["med_and_small"] / a["med"]) if a["med"] else float("nan")
        out[k] = {"D_emp": D, "P_med": Pmed, "P_small": Psm,
                  "P_small_given_med": Psm_given_med, "hits": a["all"]}
        print(f"[{A},{B}] k={k}: D_emp={D:.6f} ({a['all']} hits)  "
              f"P_med={Pmed:.5f}  P_small={Psm:.4f}  "
              f"P(small|med)={Psm_given_med:.4f}", flush=True)
    results[f"{A}-{B}"] = out
    print(f"range done {time.time()-t0:.0f}s", flush=True)

with open("/home/claude/erdos396/empirical_decomp.json", "w") as f:
    json.dump(results, f, indent=1, default=float)
print("saved")

