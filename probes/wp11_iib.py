import math

def eta0(rho):
    # Korolev 2018 Thm 3 saving in q-exponents (wp11 Sec 2.3), valid 1 < rho < 7/4
    if rho <= 107/96: return 1/128 + rho/20
    return (7/4 - rho)/10

for eta in (0.05, 0.02):
    u = up = 0.5 - 1.5*eta          # top-cell midpoint convention (Sec 2.0/2.4)
    r = 1 - u - up
    lo, hi = up, 1-u                # hard sub-range lam in (Q, A]
    lams = [lo+1e-9 + (hi-lo)*i/1000 for i in range(1001)]
    rows = {
      'b1_trivial 2(lam-r)':            [2*(l-r) for l in lams],
      'b1_weil 3lam-u\'-2r':            [3*l-up-2*r for l in lams],
      'b1_weil surplus over trivial':   [l-up for l in lams],
      'b1_god 2lam-u\'-2r':             [2*l-up-2*r for l in lams],
      'b2_korolev lam-r-2u\'eta0':      [l-r-2*up*eta0(l/up) for l in lams],
      'b2_needed eta0=(lam-r)/2u\'':    [(l-r)/(2*up) for l in lams],
      'b2_ceiling lam-r-u\'=lam-(1-u)': [l-r-up for l in lams],
      'degen 2(lam-(1-u))':             [2*(l-(1-u)) for l in lams],
    }
    print(f"=== eta={eta}: u=u'={u:.3f}, r={r:.3f}, hard lam in ({lo:.3f},{hi:.3f}] ===")
    for k,v in rows.items():
        print(f"  {k:34s} min {min(v):+.4f}  max {max(v):+.4f}")
    # masses (3/10-threshold support per wp9 link 6e)
    hard = math.log((1-u)/up); tot = math.log((1-u)/0.3)
    print(f"  ell-mass hard (Q,A] = {hard:.4f}  total (x^0.3,A] = {tot:.4f}  frac = {hard/tot:.3f}  6eta = {6*eta:.3f}")
    # audit corner convention u=u'=1/2-2eta
    uc = 0.5-2*eta
    print(f"  corner u=u'={uc}: hard mass log((1-u)/u') = {math.log((1-uc)/uc):.4f} (audit cites ~4eta={4*eta})")
    # best corner u'=1/2-eta, u=1/2-eta:
    ub = 0.5-eta
    print(f"  best corner u=u'={ub}: hard mass = {math.log((1-ub)/ub):.4f}")
    print()
