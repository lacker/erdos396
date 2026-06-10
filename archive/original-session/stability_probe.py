"""
Is D0 = {m : m | C(2m,m)} a stable set (Hildebrand sense)?
Stable would require: for each fixed d, density{n : 1_{D0}(n) != 1_{D0}(dn)} = 0.
If membership of n and dn were independent: disagreement ~ 2 c1 (1 - c1) ~ 0.202.
"""
import sys
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np
from divcheck import carries

NMAX = 1_500_000
spf = np.zeros(NMAX + 1, dtype=np.int32)
for p in range(2, int(NMAX ** 0.5) + 1):
    if spf[p] == 0:
        sl = spf[p * p::p]; sl[sl == 0] = p

def fac(x):
    f = {}
    while x > 1:
        p = int(spf[x]) or x
        e = 0
        while x % p == 0: x //= p; e += 1
        f[p] = e
    return f

def inD0(m):
    return all(carries(m, p) >= e for p, e in fac(m).items())

X = 300_000
base = np.array([inD0(n) for n in range(2, X)])
print(f"P(n in D0), n<{X}: {base.mean():.4f}")
for d in (2, 3, 5):
    dil = np.array([inD0(d * n) for n in range(2, X)])
    dis = float(np.mean(base != dil))
    print(f"d={d}: disagreement rate {dis:.4f}  P(dn in D0)={dil.mean():.4f}  "
          f"(independence would give ~{2*base.mean()*(1-base.mean()):.4f}; stable would need ~0)")
