import numpy as np, math, cmath
from sympy import primerange, isprime

# Model test of the WP2.1 two-frequency reduction (digit layer, full AP, anatomy off)
X = 10**11
q = 4787; assert isprime(q)
lams = [1, 2]
ps = [p for p in primerange(3000, 60000) if p != q][::6][:260]

def lq(n, qq):
    return ((pow(int(n), qq-1, qq*qq) - 1)//qq) % qq

def fhat(mu, p):
    # Fourier coeff of centered indicator f(y)=1[y>=h]-1/2 on Z/p, h=(p+1)//2, at freq mu!=0
    h = (p+1)//2
    num = cmath.exp(-2j*math.pi*mu*h/p) - cmath.exp(-2j*math.pi*mu*p/p)
    den = 1 - cmath.exp(-2j*math.pi*mu/p)
    return (num/den)/p   # (1/p) * sum_{y=h}^{p-1} e(-mu y/p)

rows = []
sanity_done = False
for lam in lams:
    for p in ps:
        a0 = pow(p, -1, q)
        R = (X//p - a0)//q + 1
        if R < 50: continue
        t = np.arange(R, dtype=np.int64)
        amod = (a0 + q*t) % p
        w = (amod >= (p+1)//2).astype(float) - 0.5
        ph = np.exp(-2j*math.pi*((lam*(p % q)) % q)*(t % q)/q)
        V = np.sum(w*ph)
        if not sanity_done and R >= 60:
            # check linearized phase against true Fermat-quotient phase on 50 terms
            tv = 0
            for tt in range(50):
                a = a0 + q*tt
                tv += w[tt]*cmath.exp(2j*math.pi*lam*lq(a, q)/q)
            lin = np.sum(w[:50]*np.exp(-2j*math.pi*lam*pow(a0,-1,q)*(np.arange(50))/q))
            const = cmath.exp(2j*math.pi*lam*lq(a0, q)/q)
            print(f"sanity (p={p}): |true - const*linearized| = {abs(tv - const*lin):.2e}")
            sanity_done = True
        # resonance prediction
        best = (1e18, 0)
        pred = 0.0
        for mu in range(1, 301):
            th = (mu*q/p - lam*p/q) % 1.0
            d = min(th, 1.0-th)
            c = 2*abs(fhat(mu, p))
            pred += c*min(R, 1/(2*d) if d > 0 else R)
            if d < best[0]: best = (d, mu)
        z = abs(V)/math.sqrt(R/4)
        rows.append((lam, p, R, abs(V), z, pred, best[0]*2*R, best[1]))

rows.sort(key=lambda r: -r[3])
print(f"\nTop 12 by |V| (lam, p, R, |V|, z=|V|/sqrt(R/4), predicted_bound, resonance 2R*||theta||_min, mu*):")
for r in rows[:12]:
    print(f"  lam={r[0]} p={r[1]:>6} R={r[2]:>6} |V|={r[3]:>8.1f} z={r[4]:>6.1f} pred={r[5]:>8.1f} res={r[6]:>8.2f} mu*={r[7]}")

import statistics
zs = [r[4] for r in rows]
viol = [r for r in rows if r[3] > r[5]*1.05]
res = [r for r in rows if r[6] < 1.0]   # resonant: some freq within half-period of full range
print(f"\nN cases: {len(rows)}; z percentiles 50/90/99/max: "
      f"{np.percentile(zs,50):.2f}/{np.percentile(zs,90):.2f}/{np.percentile(zs,99):.2f}/{max(zs):.2f}")
print(f"prediction violated (|V| > 1.05*pred): {len(viol)} cases")
print(f"resonant cases (min ||theta|| < 1/(2R), mu<=300): {len(res)};  their median z: "
      f"{statistics.median([r[4] for r in res]) if res else float('nan'):.1f};  "
      f"non-resonant median z: {statistics.median([r[4] for r in rows if r[6] >= 1.0]):.2f}")
print(f"correlation(log|V|, -log res-dist): "
      f"{np.corrcoef(np.log([r[3]+1e-9 for r in rows]), -np.log([r[6]+1e-9 for r in rows]))[0,1]:.3f}")
agg_actual = sum(r[3] for r in rows); agg_triv = sum(r[2]/2 for r in rows)
print(f"aggregate sum|V| = {agg_actual:.0f}  vs trivial sum R/2 = {agg_triv:.0f}  (ratio {agg_actual/agg_triv:.4f})")
