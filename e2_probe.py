"""
E2 / Family-B diagnosis probe (manuscript Hypothesis E2, Prop familyB).

For band prime pairs (p,q) at model scale, compute the continued-fraction
convergent denominators of q/p up to R = x/(pq), the gap ratios s+/s, and
the functional D_R = sum sqrt(s+/s).

Checks: (1) tail law  #{pairs: some gap ratio > G} ~ C * Npairs * log/G;
        (2) E[D_R] and E[D_R^2] are polylog-small (manuscript Prop familyB);
        (3) the structural first gap ~ p/q (u>u' geometry) shows up and is
            correctly excluded by the threshold's top-trim exemption.
"""
import numpy as np
from sympy import primerange

X = 10**11

def cf_denoms(num, den, cap):
    """convergent denominators of num/den (0<num<den) with successors, s <= cap"""
    a = []
    n, d = num, den
    while d:
        a.append(n//d); n, d = d, n % d
    # denominators q_k: q_{-1}=0, q_0=1, q_k = a_k q_{k-1} + q_{k-2}
    qs = [1]
    qprev, qcur = 0, 1
    for ak in a[1:]:
        qprev, qcur = qcur, ak*qcur + qprev
        qs.append(qcur)
    out = []
    for i in range(len(qs)-1):
        if qs[i] <= cap:
            out.append((qs[i], qs[i+1]))
    return out

def run(tag, Plo, Phi, npq, Qlo, Qhi, nq):
    ps = [int(p) for p in primerange(Plo, Phi)][:npq]
    qs = [int(q) for q in primerange(Qlo, Qhi)][:nq]
    print(f"\n=== {tag}: {len(ps)} p in ({Plo},{Phi}), {len(qs)} q in ({Qlo},{Qhi}) ===")
    Ds, D2s, maxgaps, firstgaps = [], [], [], []
    for p in ps:
        for q in qs:
            if p == q: continue
            R = X//(p*q)
            if R < 4: continue
            pairs = cf_denoms(q % p, p, R) if q % p else []
            if not pairs: continue
            ratios = [sp/s for s, sp in pairs]
            D = sum(r**0.5 for r in ratios)
            Ds.append(D); D2s.append(D*D)
            maxgaps.append(max(ratios)); firstgaps.append(ratios[0])
    Ds = np.array(Ds); maxg = np.array(maxgaps)
    N = len(Ds)
    Rtyp = X/(np.mean(ps)*np.mean(qs))
    print(f" pairs={N}, typical R={Rtyp:.0f}, E[D_R]={Ds.mean():.2f}, E[D_R^2]={np.mean(D2s):.1f}, "
          f"median first gap={np.median(firstgaps):.1f} (struct ~ p/q={np.mean(ps)/np.mean(qs):.2f})")
    print(f" tail of max gap ratio (prediction ~ C/G):")
    for G in [10, 30, 100, 300, 1000]:
        frac = float((maxg > G).mean())
        print(f"   P(maxgap > {G:>4}) = {frac:.4f}   frac*G = {frac*G:.2f}")

run("u>u' (P/Q ~ 6)", 20000, 40000, 250, 5000, 6000, 70)
run("u<u' (P/Q ~ 1/12)", 1500, 3000, 150, 24000, 30000, 120)
