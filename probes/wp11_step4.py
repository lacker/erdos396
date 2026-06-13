# WP11 STEP 4 exponent arithmetic, orientation (ii-a), top cell u=u'=1/2-1.5*eta
# Per-q completed bound (idealized, O(L^2) coefficient mass, no PS loss):
#   |E_Lambda(q)| <~ Lambda * q^{-eta0(rho)} * L^{O(1)},  rho = lam/u'
# Target per q (link 7 scale): R * L^{-c-C-5},  R = x^r, r = 1-u-u'
# Deficit (x-exponent): d = lam - u'*eta0(rho) - r ; route works iff d < 0.
# eta0 from Korolev 2018 Thm 3 (b=0, arbitrary modulus), q-exponents:
#   middle regime q^{85/96} <= N <= q^{107/96}: Delta << (q^{1/16} N^{2/5})^{-1/8}
#       => eta0 = 1/128 + rho/20
#   top regime   q^{107/96} <= N <= q^{7/4}:    Delta << (N q^{-7/4})^{1/10}
#       => eta0 = (7/4 - rho)/10
# Also test the absolute ceiling eta0 = 1/2 (Weil-grade, unattainable for primes).
import numpy as np
def eta0_korolev(rho):
    if rho < 85/96 or rho > 7/4: return None
    if rho <= 107/96: return 1/128 + rho/20
    return (7/4 - rho)/10
for eta in (0.05, 0.02):
    u = up = 0.5 - 1.5*eta
    r = 1 - u - up
    lam_lo, lam_hi = up, min(1.5*up, 1-u)   # hard sub-range (Q, A], cap = A
    lams = np.linspace(lam_lo + 1e-9, lam_hi, 1001)
    rows = []
    for lam in lams:
        rho = lam/up
        e0 = eta0_korolev(rho)
        assert e0 is not None, (eta, lam, rho)
        d_kor  = lam - up*e0 - r
        d_weil = lam - up*0.5 - r
        rows.append((lam, rho, e0, d_kor, d_weil))
    rows = np.array(rows)
    print(f"eta={eta}: u=u'={u}, r={r:.3f}, hard sub-range lam in ({lam_lo},{lam_hi}]")
    print(f"  rho=lam/u' in ({rows[0,1]:.4f},{rows[-1,1]:.4f}]  (Thm3 needs [5/8+,7/4-]: "
          f"top margin {7/4-rows[-1,1]:.4f}, bottom margin {rows[0,1]-5/8:.4f})")
    print(f"  eta0(Korolev Thm3) in [{rows[:,2].min():.4f},{rows[:,2].max():.4f}]")
    print(f"  deficit d_kor : min {rows[:,3].min():.4f} at lam={rows[np.argmin(rows[:,3]),0]:.4f}, "
          f"max {rows[:,3].max():.4f} at lam={rows[np.argmax(rows[:,3]),0]:.4f}")
    print(f"  deficit d_weil(eta0=1/2): min {rows[:,4].min():.4f}, max {rows[:,4].max():.4f}")
    # degenerate sector h = 0 mod q: trivial mass (Lambda/q)*log ~ x^{lam-u'}*L; vs target x^r
    dg = rows[:,0] - up   # exponent of Lambda/q
    print(f"  degenerate-sector exponent lam-u' in ({dg.min():.4f},{dg.max():.4f}] vs r={r:.3f}: "
          f"exceeds target iff lam-u'>r: first lam where = {up+r:.4f} (cap {lam_hi:.4f})")
    print()
