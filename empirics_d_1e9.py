import numpy as np, math, cmath
from sympy import primerange, nextprime

x = 10**9
SQ = int((2*x)**0.5) + 1          # 14143
B1 = int(round((2*x)**(1/3)))     # ~585  band lower edge (x-proxy)
PRIMES = np.array(list(primerange(2, SQ+1)), dtype=np.int64)
print(f"x={x:.0e}  band=({B1},{SQ-1}]  #primes<=sqrt(2x): {len(PRIMES)}")

gammas = [0.37, 0.40, 0.43, 0.46, 0.48]
QS = [int(nextprime(int(x**g))) for g in gammas]
print("q strata:", list(zip(gammas, QS)))

def build_population(q):
    M = (x - 1) // q
    m = np.arange(1, M+1, dtype=np.int64)
    n = 1 + q*m
    rem = n.copy()
    bandcnt = np.zeros(M, dtype=np.int16)
    bandp   = np.zeros(M, dtype=np.int64)
    bad     = np.zeros(M, dtype=bool)        # band prime with multiplicity >= 2
    for r in PRIMES:
        r = int(r)
        if r == q: continue
        m0 = (-pow(q, -1, r)) % r
        start = m0 if m0 != 0 else r
        idx = np.arange(start, M+1, r, dtype=np.int64) - 1
        if idx.size == 0: continue
        sub = rem[idx]
        if r <= B1:
            while True:
                dv = (sub % r) == 0
                if not dv.any(): break
                sub[dv] //= r
            rem[idx] = sub
        else:
            sub //= r
            again = (sub % r) == 0
            sub[again] //= r
            rem[idx] = sub
            bandcnt[idx] += 1
            bad[idx] |= again
            bandp[idx] = r
    # after sieving: rem is 1 or a prime > sqrt(2x) (part of cofactor a)
    sel = (bandcnt == 1) & (~bad)
    p = bandp[sel]; nn = n[sel]; mm = m[sel]
    a = nn // p
    return M, mm, p, a

def probe(q):
    M, mm, p, a = build_population(q)
    Npop = len(mm)
    digit = (a % p) >= ((p+1)//2)            # n-side slot-2 digit condition
    w = digit.astype(float) - 0.5            # centered decoration  (the E_q weight)
    sw2 = float(np.sum(w*w))                 # = Npop/4
    interior = (p.astype(float)**2) <= x/2   # n-side top-digit determinism guard
    res = {"q": q, "M": M, "Npop": Npop, "digit_rate": float(digit.mean()),
           "digit_rate_int": float(digit[interior].mean()) if interior.any() else float('nan'),
           "frac_interior": float(interior.mean())}
    zs, zs_int, Ts = [], [], {}
    lams = list(range(1, 9)) + [q//7, q//3, (2*q)//5]
    ph_all  = -2j*math.pi*(mm % q)/q
    for lam in lams:
        T = np.sum(w * np.exp(lam*ph_all))
        z = abs(T)/math.sqrt(sw2)
        zs.append(z); Ts[lam] = T
        wi = w[interior]; mi = mm[interior]
        Ti = np.sum(wi * np.exp(lam*(-2j*math.pi*(mi % q)/q)))
        zs_int.append(abs(Ti)/math.sqrt(float(np.sum(wi*wi))) if interior.any() else float('nan'))
    res["z_small"] = [round(z,2) for z in zs[:8]]
    res["z_mid"]   = [round(z,2) for z in zs[8:]]
    res["z_int_small"] = [round(z,2) for z in zs_int[:8]]
    res["rms_z"] = round(float(np.sqrt(np.mean(np.array(zs)**2))),2)
    res["T1"] = Ts[1]; res["sw2"] = sw2
    # unweighted control on same pop (population-shape effect, for reference)
    ctrlz = []
    for lam in [1,2,3]:
        Tc = np.sum(np.exp(lam*ph_all))
        ctrlz.append(round(abs(Tc)/math.sqrt(Npop),2))
    res["ctrl_z123"] = ctrlz
    return res

results = [probe(q) for q in QS]
print(f"\n{'q':>7} {'gam':>5} {'M':>7} {'Npop':>6} {'P(dig)':>7} {'P(dig|int)':>9} {'%int':>5}  z(lam=1..8) | rms_z | ctrl(unw) z123")
agg = {1:0+0j, 2:0+0j, 3:0+0j}; aggw = 0.0
for g, r in zip(gammas, results):
    print(f"{r['q']:>7} {g:>5} {r['M']:>7} {r['Npop']:>6} {r['digit_rate']:>7.4f} {r['digit_rate_int']:>9.4f} {r['frac_interior']:>5.2f}  {r['z_small']} | {r['rms_z']} | {r['ctrl_z123']}")
    aggw += r["sw2"]
print(f"\nInterior-only z (lam=1..8) per stratum:")
for g, r in zip(gammas, results):
    print(f"  gamma={g}: {r['z_int_small']}")
# phase-aligned cross-q aggregate at h=1 (fixed harmonic across the band)
for h in [1]:
    Tagg = sum(rr["T1"] for rr in results)
    print(f"\nCross-q aligned aggregate h=1: |sum_q T_q(1)|/sqrt(sum sw2) = {abs(Tagg)/math.sqrt(aggw):.2f}")
