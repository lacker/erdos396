#!/usr/bin/env python3
# Range-compatibility of the Baker-2012 bridge for E3-lb, top cell.
# Top cell: u = u' = 1/2 - 1.5*eta. Q = x^{u'}, A = x^{1-u}, R = x^{1-u-u'}.
# Hard sub-range: Lambda in (Q, min(Q^{3/2}, A)]  (exponents lam).
# Baker 2012: sum over primes n ~ N, modulus m: needs N >= m^{1/2+eps}.

EPS = 1e-9  # treat eps -> 0+; deficits reported at eps = 0

def cell(eta):
    u = up = 0.5 - 1.5*eta
    Q, A = up, 1 - u
    lam_lo, lam_hi = Q, min(1.5*Q, A)
    return u, up, Q, A, lam_lo, lam_hi

def check(N, mexp):
    """Baker condition N >= m^{1/2+eps}: margin = N - m/2 (exponents)."""
    margin = N - mexp/2
    return margin

for eta in (0.05, 0.02):
    u, up, Q, A, lam_lo, lam_hi = cell(eta)
    print(f"\n=== eta = {eta}: u=u'={u}, Q=x^{Q}, A=x^{A}, R=x^{1-u-up:.2f}, "
          f"hard sub-range lam in ({lam_lo}, {lam_hi}] ===")

    # grid over the hard sub-range (open at bottom)
    grid = [lam_lo + k*(lam_hi - lam_lo)/1000 for k in range(1, 1001)]

    # (i) q summed, length Q=x^{u'}, modulus ell1*ell2 ~ Lambda^2 = x^{2lam}
    margins = [check(up, 2*l) for l in grid]
    worst, best = min(margins), max(margins)
    ok = all(m > EPS for m in margins)
    print(f"(i)   var q,    N=x^{up}, m=l1l2=x^[{2*lam_lo:.4f},{2*lam_hi:.4f}]: "
          f"{'OK' if ok else 'FAIL'}; margin in [{worst:.4f},{best:.4f}] "
          f"-> max deficit {max(0,-worst):.4f} (at lam={lam_hi}), "
          f"min deficit {max(0,-best):.4f} (lam->Q+)")

    # (ii-a) one ell summed (double reciprocity, q fixed): N=x^lam, m=q=x^{u'}
    margins = [check(l, up) for l in grid]
    worst = min(margins)
    ok = all(m > EPS for m in margins)
    print(f"(iia) var ell,  N=x^[{lam_lo:.4f},{lam_hi:.4f}], m=q=x^{up}: "
          f"{'OK' if ok else 'FAIL'}; margin in [{worst:.4f},{max(margins):.4f}] "
          f"(eps can be taken up to {worst/up:.3f} at the seam)")

    # (ii-b) ell summed, q-square opened: N=x^lam, m=q1q2=x^{2u'}
    margins = [check(l, 2*up) for l in grid]
    worst, best = min(margins), max(margins)
    ok_strict = all(m > EPS for m in margins)
    # condition Lambda >= Q^{1+2eps}: OK for any fixed delta>0 with lam >= u'(1+2delta)
    print(f"(iib) var ell,  N=x^[{lam_lo:.4f},{lam_hi:.4f}], m=q1q2=x^{2*up}: "
          f"{'OK (open range, margin->0+ at lam->Q+)' if ok_strict else 'FAIL'}; "
          f"margin in ({worst:.4f},{best:.4f}]; "
          f"Lambda>=Q^(1+2eps) check: lam/u' in (1.000,{lam_hi/up:.4f}] -> "
          f"fixed-eps OK only on lam >= u'(1+2eps), seam sliver (Q,Q^(1+2eps)] excluded")

    # (iii) mixed (one flip): q summed vs single modulus ell1 ~ x^lam
    margins = [check(up, l) for l in grid]
    worst = min(margins)
    ok = all(m > EPS for m in margins)
    print(f"(iii) var q,    N=x^{up}, m=ell1=x^[{lam_lo:.4f},{lam_hi:.4f}]: "
          f"{'OK' if ok else 'FAIL'}; margin in [{worst:.4f},{max(margins):.4f}] "
          f"(need u'>=lam/2: {up}>={lam_hi/2:.4f}) "
          f"[CAVEAT: leftover e(h2*bar(ell2)/q) phase oscillates in q — not Baker's b*n/m shape]")

    # DOUBLE q-average rescue check (== iib): Lambda >= Q^{1+eps}?
    print(f"DOUBLE-q rescue: modulus q1q2=x^{2*up} vs ell-length x^lam, lam>{Q}: "
          f"Lambda>=Q^(1+eps) holds for all lam in (Q*(1+eps'),{lam_hi}] -- CHECK "
          f"(top of sub-range margin {lam_hi-up:.4f})")
