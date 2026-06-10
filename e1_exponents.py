#!/usr/bin/env python3
"""
WP8 E1 exponent scanner, v2.

Sizes are pairs (f, t): value = x^f * L^(t*B), B a large free polylog level.
Constant L-powers are ignored (absorbed in the absolute constant A of the
target QP*L^(A-B)); only B-coefficients matter at degenerate margins.
Acceptance of a contribution (f, t): f < target - TOL, or
(|f - target| <= TOL and t <= -1 + TOL).

Dyadic variables scanned over grids of f plus B-offsets t in {0,-1,-2,-3,-4}
(value x^f L^{tB}), constrained to lie in the allowed range, where range ends
themselves are (f,t)-pairs:
  m in [m0=(max(u-u',2u-2u',0),0),  M0=(1-u-u', -1)]
  h in [(0,0), (expSum, 0)]                  (h <= Q_frame; Vaaler with H=Q_frame)
  W in [Wmin=h*K/Qframe, Wmax=h*K]           (K=(em+u'-u, tm))
Derived: Nbar = max(h*x^{ratio}, 1); sigma_bar = h*Nbar/(2 m L^B) -> t -=1.

Counts nu at shell W (cumulative <= W), all times L^{O(1)} (ignored):
  A   = m W
  J0  = m W L^{B}            (J=0 sporadic; sum_{h''|lam} structure, sigma<=W folded)
  gated by (sigma_bar + W >= 1/2):
  B1  = mW + mW*(sig+W)/max(sig,1)          (J1)
      + (sig+W)*Nbar/h                       (J2: J-measure x mu-singleton<=1)
      + m*W*h/max(sig,1)                     (J3)
      + SING                                 (J4)
  B2  = (W+1) * ( m*h + SING )               (AP-union alternative)
  SING = min( h*Nbar,  Nbar*h^{1/2} + h^{3/2} )
  Jneq0 = min(B1, B2)
LF emptiness: if sigma_bar <= 1/4 (strict in (f,t)) and W < sigma_bar/8:
  only J0 contributes (A's J-window measure also needs an admissible J;
  we keep A anyway -- harmless).
Weight: w = K/W  (bottom shell W=Wmin gives Qframe/h).
Contribution = w * nu; compare to target (u+u', 0) with required t<=-1 at
equality.

Frames: q-frame (expSum=u', ratio=u-u') and p-frame (expSum=u, ratio=u'-u).
A band point passes if SOME frame has no violating term combination
(min over frames is legitimate: we choose the counting frame per (u,u')).
"""
import itertools

TOL = 1e-9
PAIRCAP = False
TOFF = (0, -1, -2, -3, -4)

def leq(a, b):  # size comparison (f,t): a <= b ?
    return a[0] < b[0] - TOL or (abs(a[0]-b[0]) <= TOL and a[1] <= b[1] + TOL)

def mx(a, b):   return a if leq(b, a) else b
def mn(a, b):   return a if leq(a, b) else b
def mul(a, b):  return (a[0]+b[0], a[1]+b[1])
def div(a, b):  return (a[0]-b[0], a[1]-b[1])

ONE = (0.0, 0)
HALF = (0.0, 0)   # 1/2 ~ 1 at this resolution

def scan_point(u, up, frame, ngrid=10):
    if frame == 'q': expSum, ratio = up, u - up
    else:            expSum, ratio = u, up - u
    target = u + up
    em0 = max(u - up, 2*(u - up), 0.0)
    eM0 = 1 - u - up
    if eM0 < em0 - TOL: return []
    viols = []
    # grids: f-values for m, h; W scanned over its own range similarly.
    def grid(lo, hi):
        pts = set()
        for i in range(ngrid+1):
            pts.add(lo + (hi-lo)*i/ngrid)
        return sorted(pts)
    for fm in grid(em0, eM0):
        for tm in TOFF:
            m = (fm, tm)
            if not (leq((em0,0), m) and leq(m, (eM0,-1))): continue
            K = (fm + up - u, tm)
            if not leq(ONE, K): continue          # live range K>=1
            for fh in grid(0.0, expSum):
                for th in TOFF:
                    h = (fh, th)
                    if not (leq(ONE, h) and leq(h, (expSum,0))): continue
                    N = mx(mul(h, (ratio, 0)), ONE)
                    sig = div(mul(h, N), m); sig = (sig[0], sig[1]-1)
                    Wmin = div(mul(h, K), (expSum, 0))
                    Wmax = mul(h, K)
                    if not leq(Wmin, Wmax): continue
                    fWlo, fWhi = Wmin[0], Wmax[0]
                    for fW in grid(min(fWlo,fWhi), max(fWlo,fWhi)):
                        for tW in TOFF:
                            W = (fW, tW)
                            if not (leq(Wmin, W) and leq(W, Wmax)): continue
                            w = div(K, W)   # = Qframe/h at bottom
                            # pair-cancellation cap: (1/h)|S_h(c-)-S_h(c+)|
                            # <= C*Delta*Qframe, Delta = 2 delta_mu |c'|:
                            # q-frame: P^2/(m^2 Q^2 L^B) -> Delta*Q = P^2/(m^2 Q L^B)
                            # p-frame: 1/(m^2 L^B)       -> Delta*P = P/(m^2 L^B)
                            if PAIRCAP:
                                if frame == 'q':
                                    dQ = (2*u - 2*fm - up, -2*tm - 1)
                                else:
                                    dQ = (u - 2*fm, -2*tm - 1)
                                w = mn(w, dQ)
                            # LF emptiness gate
                            lf_empty = leq(sig, (0.0,-1)) and (not leq(sig, W)) \
                                       and not leq((0.0,0), W)  # sig<"1/4", W<sig, W<1/2 -> only J0
                            # convergent-collapse: per (mu,k) at most O(1)
                            # convergent denominators s per dyadic block, so
                            # the cell count is capped by m*K, h-free:
                            CAP = mul(m, K)
                            terms = {}
                            terms['A']  = mn(mul(m, W), CAP)
                            J0a = (m[0]+W[0], m[1]+W[1]+1)          # m W L^{B+1}
                            J0b = mn((2*m[0]+W[0]-N[0],
                                      2*m[1]+W[1]-N[1]+1),           # m^2 W L^{B+2}/Nbar
                                     mul(m, h))                      # g <= h/h'' truncation
                            terms['J0'] = mn(mx(J0a, J0b), CAP)
                            hf = leq(HALF, mx(sig, W))
                            if hf and not lf_empty:
                                mxs = mx(sig, ONE)
                                # JA: mu-measure x J-harmonic AP part:
                                # sum_{J=a mod hg1,|J|<=2W} 1/|J| <= L/(hg1) + 1/J0
                                # first piece collapses to measure type m W L^2:
                                JA = mul(m, W)
                                # JB: mu-measure x J0-sporadic harmonic:
                                #   W<=sig/8:  m W h L^2 / sig   (J0 ~ sig)
                                #   else:      m W L^{O(1)}      (rho-average input)
                                if leq(mul(W, (0.0, 0)), sig) and W[0] < sig[0] - TOL:
                                    JB = div(mul(mul(m, W), h), mxs)
                                else:
                                    # rho-average (Lemma R): m W (1 + h/Nbar) L^{O(1)}
                                    JB = mul(mul(m, W), mx(ONE, div(h, N)))
                                J2 = mul(mx(sig, W), N)
                                SING = mn(mul(h, N),
                                          mx(mul(N, (0.5*h[0], h[1])),
                                             (1.5*h[0], h[1])))
                                B1 = mx(mx(JA, JB), mx(J2, SING))
                                B2 = mul(mx(W, ONE), mx(mul(m, h), SING))
                                terms['Jneq0'] = mn(mn(B1, B2), CAP)
                            for name, cnt in terms.items():
                                tot = mul(w, cnt)
                                bad = tot[0] > target + TOL or \
                                      (abs(tot[0]-target) <= TOL and tot[1] > -1 + TOL)
                                if bad:
                                    viols.append((name, fm, tm, fh, th, fW, tW,
                                                  round(tot[0]-target,6), tot[1]))
    return viols

def report(points, ngrid=10, label=""):
    print(f"=== {label} ===")
    allbad = {}
    for (u,up) in points:
        per = {}
        for frame in ('q','p'):
            v = scan_point(u, up, frame, ngrid)
            per[frame] = v
        ok = any(len(v)==0 for v in per.values())
        if not ok:
            # summarize worst by term name per frame
            s = {}
            for fr, v in per.items():
                names = {}
                for rec in v:
                    nm = rec[0]
                    key = (rec[7], rec[8])
                    if nm not in names or key > names[nm]:
                        names[nm] = key
                s[fr] = names
            allbad[(u,up)] = s
        print(f"(u,u')=({u:.4f},{up:.4f}): " +
              ("PASS (frame with 0 viols exists)" if ok else f"FAIL {s}"))
    return allbad

corners = [(1/3,1/3),(0.4,0.4),(1/3,0.5),(0.5,1/3),(0.36,0.36),(0.35,0.45),
           (0.45,0.35),(0.34,0.34),(0.49,0.34),(0.34,0.49)]
bad = report(corners, ngrid=12, label="corners & samples, grid 12")

grid_pts = [(1/3 + i*(1/6)/10, 1/3 + j*(1/6)/10) for i in range(11) for j in range(11)]
nfail = 0; fails = []
for (u,up) in grid_pts:
    ok = any(len(scan_point(u,up,f,8))==0 for f in ('q','p'))
    if not ok: nfail += 1; fails.append((round(u,4),round(up,4)))
print(f"\nband 11x11 grid: {nfail} FAIL cells")
print(fails[:30])

# robustness: finer band grid + per-frame check
import sys
fine = [(1/3 + i*(1/6)/16, 1/3 + j*(1/6)/16) for i in range(17) for j in range(17)]
qonly_fail, both_fail = [], []
for (u,up) in fine:
    vq = scan_point(u,up,'q',10)
    if vq:
        qonly_fail.append((round(u,4),round(up,4)))
        vp = scan_point(u,up,'p',10)
        if vp: both_fail.append((round(u,4),round(up,4)))
print(f"fine 17x17 grid: q-frame fails at {len(qonly_fail)} cells; both frames fail at {len(both_fail)}")
print("qfail:", qonly_fail[:12]); print("bothfail:", both_fail[:12])
# corner stress with very fine parameter grid
for pt in [(1/3,1/3),(0.5,1/3),(1/3,0.5),(0.5-1e-9,0.5-1e-9)]:
    v = scan_point(*pt,'q',24); w = scan_point(*pt,'p',24)
    print(f"stress ngrid=24 {pt}: q={len(v)} p={len(w)}")
