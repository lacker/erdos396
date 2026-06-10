"""
Fine-anatomy-class check (WP2.3 item (iii); manuscript ledger D4).

Same design as empirics_d.py (the exact D-dagger integrand T_q(lambda) on
real populations), but with the cofactor restricted to FINE anatomy classes:

  class F1: P+(a) in (x^0.20, x^0.28]   (largest cofactor prime in a sub-box)
  class F2: P+(a) <= x^0.20             (very friable cofactor)
  class F0: all (bare class, control = original probe)

In all classes: exactly one simple band prime p | n, no cofactor prime > sqrt(2x).
If the conditional architecture is right, the decorated z stays O(1) in every
class (the decoration decorrelates from m mod q within each class).
"""
import numpy as np, math
from sympy import primerange, nextprime

x = 10**8
SQ = int((2*x)**0.5) + 1
B1 = int(round((2*x)**(1/3)))
PRIMES = np.array(list(primerange(2, SQ+1)), dtype=np.int64)
BOX_LO, BOX_HI = int(x**0.20), int(x**0.28)
print(f"x={x:.0e} band=({B1},{SQ-1}] box=({BOX_LO},{BOX_HI}]")

def build(q):
    M = (x - 1) // q
    m = np.arange(1, M+1, dtype=np.int64)
    n = 1 + q*m
    rem = n.copy()
    bandcnt = np.zeros(M, dtype=np.int16)
    bandp = np.zeros(M, dtype=np.int64)
    bad = np.zeros(M, dtype=bool)
    lpf_small = np.ones(M, dtype=np.int64)   # largest prime factor of n below band
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
            lpf_small[idx] = r               # ascending r: last write = largest
        else:
            sub //= r
            again = (sub % r) == 0
            sub[again] //= r
            rem[idx] = sub
            bandcnt[idx] += 1
            bad[idx] |= again
            bandp[idx] = r
    friable = (rem == 1)                     # no prime > sqrt(2x) left
    sel0 = (bandcnt == 1) & (~bad) & friable
    return m, bandp, lpf_small, sel0

def zscores(mm, w, q, lams):
    sw2 = float(np.sum(w*w))
    ph = -2j*math.pi*(mm % q)/q
    out = []
    for lam in lams:
        T = np.sum(w*np.exp(lam*ph))
        out.append(abs(T)/math.sqrt(sw2) if sw2 > 0 else float('nan'))
    return out

lams = list(range(1, 9))
for g in [0.40, 0.43]:
    q = int(nextprime(int(x**g)))
    m, bandp, lpf, sel0 = build(q)
    classes = {
        "F0 bare    ": sel0,
        "F1 box     ": sel0 & (lpf > BOX_LO) & (lpf <= BOX_HI),
        "F2 friable ": sel0 & (lpf <= BOX_LO),
    }
    print(f"\n--- gamma={g}, q={q} ---")
    for name, sel in classes.items():
        mm = m[sel]; p = bandp[sel]
        a = (1 + q*mm) // p
        w = ((a % p) >= ((p+1)//2)).astype(float) - 0.5
        zs = zscores(mm, w, q, lams)
        rms = float(np.sqrt(np.mean(np.array(zs)**2)))
        print(f" {name} N={len(mm):>6}  z(1..8)={[round(z,2) for z in zs]}  rms={rms:.2f}")
