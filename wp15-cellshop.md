# WP15 — Cell shopping against the W4.6 wall (cheap arithmetic check)

STATUS: COMPLETE (this session). Question: does any asymmetric cell
(u, u') in the open band (1/3, 1/2)^2 dissolve or substantially reduce
the W4.6 wall (wp11-e3lb §4.7.4, deficit x^{2 lam - 0.725} at the
symmetric top cell)? NO NEW ESTIMATES — pure re-arithmetic of the proved
(W4.4) chain and of the §3.4 (b3) absorption conditions as functions of
(u, u', lam). Numeric provenance: /tmp/wp15_scan.py (.venv python),
output transcribed in §3.

Sources: wp11-e3lb.md §3.4 (b3 conditions), §4.3.4 (Korolev window),
§4.7.1-4.7.4 (W1/W2/W4 chains); wp9-b0-audit.md §§2-3, 5, 6 (lb-class,
3/10 cutoff, ledger); wp12-cdagger-lb-diagnosis.md §2 Route 2 + §4 (C†
cell preference); manuscript 09-anatomy.tex (prop:one-large),
07-minor.tex ((M2*) + structural-gap remark), 10-remaining.tex +
citations.md (GS x^{20/39}, DGS x^{3/5}).

Conventions. P = x^u (a-side band prime = E3 dilation side), Q = x^{u'}
((n-1)-side band prime = E3 modulus side), R = x^r, r := 1 - u - u' > 0,
A = x^{1-u} = QR (a-side cofactor ceiling), y = x^{3/10} (lb friable
cutoff, forced by DGS — see §3 C5), hard sub-range Lambda = x^lam,
lam in (u', 1-u] (max(y, Q) = Q since u' > 1/3 > 3/10). Symmetric
reference cells u = u' = 0.425 (eta = 0.05) and 0.47 (eta = 0.02).
"Deficit" = (chain exponent) - (budget exponent), positive = FAIL.

## 1. The (b3) hard mass and the generalized absorption requirement

Hard-range Mertens mass, exact:

    kappa_a(u, u') := Sum_{Q < ell <= A} 1/ell = log((1-u)/u') + o(1),

and the b-side mirror (moduli against p, cofactor b <= x^{1-u'}):
kappa_b = log((1-u')/u). At the symmetric top cells kappa = 6 eta + O(eta^2)
(0.3023 / 0.1202) — O(eta) BECAUSE u' is within O(eta) of both 1/2 and
1-u. At a general cell kappa is a CONSTANT: e.g. (u,u') = (0.45, 0.35)
gives kappa_a = log(0.55/0.35) = 0.452 — not small in any parameter.

THE ABSORPTION REQUIREMENT, recomputed in general (W1's aggregation,
constants kept). The (b3) sandwich charges to the class count, per
(p,q) off the delta_0-set:

    loss <= M + drift + deviation
         <= kappa R (Mertens main) + 2 kappa R (Vaaler drift, W1's
            12.1 eta = 2 x 6.05 eta line) + s R (Chebyshev deviation,
            s freely small)  =  (3 + o(1)) kappa R,

against the a-side class main term c_0(u) R, c_0(u) = rho(u_f) =
1 - log(10(1-u)/3) for u_f := (1-u)/(3/10) in [1,2] (Dickman; friable
t-count along the AP mod q). So the absorption condition (a-side, and
its u<->u' mirror) is no longer "kappa = O(eta)" but the CONSTANT-level
inequality

    (ABS_a)   3 log((1-u)/u')  <  rho(10(1-u)/3)   (with margin),
    (ABS_b)   3 log((1-u')/u)  <  rho(10(1-u')/3),

the constant 3 being FORCED (1 from the Mertens main term + 2 from the
Vaaler drift at per-ell degree; the deviation s is free). Numbers on the
diagonal u = u' = t: LHS/RHS = 0.91/0.349 at t = 0.425 (fails — the
eta = 0.05 cell is absorption-marginal already, consistent with W1's
C = 20 sitting above the ledger constant), 0.60/0.394 at t = 0.45
(fails), 0.36/0.431 at t = 0.47 (passes), 0.21/0.46 at t = 0.4825
(passes 2.2x). The absorption wedge is a NARROW NEIGHBORHOOD OF THE TOP
CORNER u = u' = 1/2 - O(eta): lowering u' alone inflates
kappa_a = log((1-u)/u') while rho stays put, so off-diagonal cells die
FASTER. CONSEQUENCE: any cell with u' substantially below 1-u
(kappa_a = Theta(1)) changes the absorption target from "O(eta) loss"
to "constant loss >= main term" — the (b3) dodge ITSELF dies there,
before W4 is even reached. [Checked against the wp9-b0-audit §3
bottom-cell datum u = u' = 0.34: kappa = log(0.66/0.32) ≈ 0.72 ✓,
hopeless against rho(2.2)-grade.]

## 2. The deficit surface: where 0.725 came from

Re-derivation of every exponent in the (W4.4) chain at a general cell.

(i) POSITIVITY COST (W4.4(i)). p -> a_0 = pbar_q into [1, q):
  - u <= u' (P <= Q < q): injective; cost q/N_P ~ (Q/P) L:
    exponent (u' - u).
  - u > u' (P > Q): injectivity fails; multiplicity <= 2P/q + 1, cost
    (2P/q)(q/N_P) ~ 2L: exponent 0.
  Cost exponent: (u' - u)^+ + o(1).

(ii) THE THREE MASSES (per block, before the positivity factor; from
(W3.4) Parseval mass 7(R+1)/Lambda per ell, m_1 = 4.1 per-ell L^1 mass,
and the fiber-count corollary (W4.3) E_q[kernel] <= c_8 L^2/Q —
divisor-counting, cell-free*):
  - diagonal:   Sum_t |chat_t|^2 ~ R/L:                exponent r;
  - same-ell:   N_Lambda m_1^2 c_8 L^2/Q ~ Lambda L/Q: exponent lam - u';
  - cross-ell:  (m_1 N_Lambda)^2 c_8 L^2/Q ~ Lambda^2/Q:
                exponent 2 lam - u'.
  [*(W4.2)'s "<= 3 prime divisors q ~ Q" used |n_j| < Q^4, i.e.
  u' + 2 lam < 4u'. For cells with lam_top = 1-u >= 1.5 u' the divisor
  count becomes ceil((2 - 2u + u')/u') > 3 — a CONSTANT change only;
  the L^2/Q exponent is cell-independent. No constraint.]

(iii) THE BUDGET (W1.1). Target E|D^pm_Lambda|^2 <= c delta_0 (s R)^2
J^{-2}-grade, J = #blocks ~ r L/log 2: exponent 2r - o(1) = 2(1-u-u'),
at every cell with r > 0 (corner trim). [Soundness at every cell: the
signed random-model rms of the off-diagonal is ~ x^{r - (u+u')/2}, so
the signed room is budget - rms = 1 - (u+u')/2 > 0 ALWAYS — the wall
stays proof-side, not truth-side, at every cell; = 0.575 at the
symmetric 0.425-cell ✓ (W3d).]

(iv) THE DEFICIT SURFACE (cross-ell term, the unique failing one —
diagonal closes iff r > 0; same-ell closes iff (u'-u)^+ < r, i.e.
2u' < 1 ✓ always):

    D(u, u', lam) = (u'-u)^+ + (2 lam - u') - 2(1 - u - u')
                  = 2 lam + 2u + u' - 2 + (u'-u)^+ ,
                    lam in (u', 1 - u].

  Decomposition of the symmetric 0.725: deficit = 2 lam - [2 - u - 2u']
  with 2 - u - 2u' = 2r (budget) + u' (q-average saving, fiber count)
  = 0.3 + 0.425 at u = u' = 0.425 ✓ (0.12 + 0.47 = 0.59 at 0.47 ✓).
  So "0.725" = budget exponent + one full power of Q — nothing else.

  D is increasing in lam: the wall is the TOP BLOCK lam = 1 - u
  (always nonempty: ell <= a <= A, ell = a admissible):

    D_top^a(u, u') = u' + (u' - u)^+ ,

  b-side mirror (wp9-b0-audit §5b two-sided form; swap u <-> u'):

    D_top^b(u, u') = u + (u - u')^+ ,

  JOINT WALL  W(u,u') = max(D_top^a, D_top^b) = max(u,u') + |u - u'|.

  Bottom block (lam = u'+): D_bot^a = 2u + 3u' - 2 + (u'-u)^+, which IS
  negative below the line 2u + 3u' = 2 (u >= u') — low cells close the
  bottom blocks — but the top block NEVER closes:

    D_top^a >= u' > 1/3   on the whole open band,

  and the joint wall W >= max(u,u') > 1/3, minimized ONLY on the
  diagonal u = u' (asymmetry adds |u - u'| to the mirror side: an
  asymmetric cell is strictly counterproductive in the two-sided form).

  WHY the cancellation: raising u shortens the hard range (top exponent
  2(1-u) falls by 2du) but shrinks the budget 2r by exactly 2du; the
  net at the top block is u' + (u'-u)^+ — the MODULUS-side exponent
  alone survives. The wall is the q-average-saving ceiling: one factor
  1/Q (fiber count / divisor counting) is all the chain extracts from
  the q-variable; top-block closure needs Q >= A^2/R^2 = x^{2u'}
  ((W4.4)'s closure condition generalized), i.e. u' <= 0 — impossible
  at EVERY cell, with shortfall exactly x^{u'} (+ the positivity cost
  x^{(u'-u)^+}).

## 3. Numerical scan over admissible cells

Grid 0.3334..0.4998, step 0.0002 (678,976 band cells), /tmp/wp15_scan.py.

CONSTRAINTS, verified per cell:
- C1 (M2*) top trims: u, u' <= 1/2 - margin (structural-gap exemption
  x^{2u-1} <= L^{-B} of 07-minor's remark, and its q/p mirror).
- C2 corner trim: r = 1-u-u' >= 2*margin (R >= polylog; blocks exist).
- C3 q < ell / R < Q: lam > u' by construction; R < Q ⟺ 1-u < 2u',
  AUTOMATIC on the band (1-u < 2/3 < 2u') — 0 violations found.
- C4 one-large exactness (prop:one-large at the lb cutoff y = x^{3/10},
  forced by DGS conductor range x^{3/5}, wp9-b0-audit §2 item 3):
  A = x^{1-u} <= y^2 ⟺ u >= 2/5; mirror u' >= 2/5. [wp9-b0-audit §5b's
  "u' > 1/3" suffices only for the band floor (2x)^{1/3} of manuscript
  09; at the 3/10 lb cutoff the honest constraint is 2/5. GS-only
  variant (cutoff 10/39): u >= 19/39 = 0.487 — nearly empty band.]
- C5 absorption (§1): 3 log((1-u)/u') < rho(10(1-u)/3), + mirror.
- C6 Korolev middle-regime window (4.3.4: q^{85/96} <= P, 2P <=
  q^{107/96}) for the citation-bearing layers (soft range/(*)/W3.3):
  u/u' in [85/96, 107/96] = [0.885, 1.115]. The W4 chain itself is
  citation-free — C6 is a program-consistency constraint, not a wall
  input.

RESULTS (min of the max-over-lam deficit; "joint" = two-sided
W = max(u,u') + |u-u'| per §2):

  | constraint set            | a-side wall min        | joint wall min |
  |---|---|---|
  | band only (C1-C3)         | 0.3334 at (0.3334,0.3334) | 0.3334 (same) |
  | + one-large C4            | 0.4002 at (0.4002,0.4002) | 0.4002 (same) |
  | + absorption C5           | 0.4368 at (0.4980,0.4368) | 0.4650 at (0.4650,0.4650) |
  | + Korolev C6              | 0.4416 at (0.4922,0.4416) | 0.4650 (same) |

  Cells with max-over-lam deficit <= 0: ZERO, on the bare band already
  (a-side and joint), before any of C4-C6. Bottom-block-only closure
  (D_bot^a <= 0, the region 2u + 3u' <= 2) covers 208,634 band cells —
  but none survive C5, and the top block fails everywhere regardless.

ROBUSTNESS of the absorption floor (diagonal cells, constant c_abs in
place of the forced 3): c_abs = 1 (impossible — Mertens main term
alone): t >= 0.4169; c_abs = 2 (drift halved, hypothetically):
t >= 0.4508; c_abs = 3 (actual): t >= 0.4649. Even the maximally
charitable one-sided reading (c_abs = 1, u = 0.5-, no one-large) leaves
wall >= 0.3616. The wall is pinned in [0.42, 0.4825] for every honest
reading, vs the references 0.425 (eta = 0.05, itself absorption-
marginal at constant level) and 0.47 (eta = 0.02): CELL-SHOPPING BUYS
AT MOST 0.005 against the eta = 0.02 reference.

DEFICIT-SURFACE TABLE D(u,u',lam) = (u'-u)^+ + 2 lam + 2u + u' - 2,
five equispaced lam in [u', 1-u], a-side (mirror top in last column):

  | (u, u')          | r    | C4 C5 C6        | deficits at lam grid                                | mirror top |
  |---|---|---|---|---|
  | (.425,.425) ref-05 | .150 | ok FAIL ok    | +.125 +.200 +.275 +.350 +.425                       | +.425 |
  | (.470,.470) ref-02 | .060 | ok ok ok      | +.350 +.380 +.410 +.440 +.470                       | +.470 |
  | (.4825,.4825) safe | .035 | ok ok ok      | +.4125 +.4300 +.4475 +.4650 +.4825                  | +.4825 |
  | (.465,.465) edge   | .070 | ok ok(1.00x) ok | +.325 +.360 +.395 +.430 +.465                     | +.465 |
  | (.498,.430) u-heavy| .072 | ok FAIL FAIL  | +.286 +.322 +.358 +.394 +.430                       | +.566 |
  | (.430,.498) u'-heavy| .072 | ok FAIL FAIL | +.422 +.458 +.494 +.530 +.570                       | +.430 |
  | (.498,.336) extreme| .166 | FAIL FAIL FAIL| +.004 +.087 +.170 +.253 +.336                       | +.660 |
  | (.400,.400) 1L-floor| .200| ok FAIL ok    | +.000 +.100 +.200 +.300 +.400                       | +.400 |
  | (.336,.336) floor  | .328 | FAIL FAIL ok  | -.320 -.156 +.008 +.172 +.336                       | +.336 |

Readings. (i) The extreme u-heavy corner (0.498, 0.336) shows the
maximal one-sided gain: bottom block nearly closes (+0.004) and the
a-side top falls to +0.336 — but it fails one-large (u' < 2/5: the
b-side unwinding is not even exact), fails absorption by 2.4x/4x
(kappa_a = 0.40 — the hard mass is Theta(1), the (b3) dodge dead),
fails Korolev, and its MIRROR wall is +0.66: strictly worse than the
symmetric reference in the two-sided form. (ii) Every constraint
verified at the best admissible cell (0.465, 0.465): C1-C3 ok,
C4 ok (0.465 > 0.4), C5 marginal-pass (0.4207 < 0.4215 — 1.002x;
the 0.4825 cell passes 2.2x), C6 ok (ratio 1); deficit at top block
+0.465. (iii) Overcrowding (W4.5) transfers: #T_lin = x^{2 lam - r}
>= x^{u + 3u' - 1} (bottom block), and #T_lin >> N_Q = x^{u'} ⟺
u + 2u' > 1, true STRICTLY on the whole band (u + 2u' > 1/3 + 2/3) —
so the duality cap holds on every block at every cell: no large-sieve
arrangement beats the (W4.4) level anywhere on the band.
(iv) C† tension (wp12 §4): C†-Route-2 room x^{1-2u} per side = x^{0.07}
at t = 0.465, x^{0.035} at 0.4825 — positive (preference satisfied
weakly), but cell-shopping for C† (down-band) and for absorption
(top corner) pull oppositely, exactly the recorded tension; W is flat
enough on the wedge (0.465..0.4825) that the choice barely matters.

## 4. Verdict

**WALL-CELL-INDEPENDENT — proof:** the max-over-lam deficit of the
proved (W4.4) chain at cell (u, u') is

    D_top^a = u' + (u' - u)^+  >  u'  >  1/3

on the WHOLE open band (the hard range always reaches A = x^{1-u}, and
the chain's entire q-saving is the single factor 1/Q from the fiber
count (W4.2-W4.3), while every gain from moving u cancels exactly
against the budget 2r = 2(1-u-u'): §2(iv)). The infimum 1/3 (cell
(1/2, 1/3+), or the diagonal floor) is unattainable AND inadmissible:
one-large exactness forces u, u' >= 2/5 (wall >= 0.4002), the (b3)
absorption inequality 3 log((1-u)/u') < rho(10(1-u)/3) + mirror forces
the top-corner wedge (joint wall >= 0.4650 at the actual constant 3;
>= 0.4169 even at the impossible constant 1), asymmetry is strictly
counterproductive two-sided (adds |u-u'| to the mirror wall), and zero
cells on the bare band — let alone admissible ones — have max-over-lam
deficit <= 0. Best admissible cell: symmetric (0.465, 0.465), residual
deficit +0.465 (top block), vs +0.47 at the eta = 0.02 reference —
a 0.005 cosmetic gain; the eta = 0.05 reference (deficit 0.425) is
itself absorption-INVALID at constant level (3 kappa = 0.91 vs
rho = 0.35), so the honest wall is ~0.465, slightly WORSE than wp11's
headline number. Cell-shopping is exhausted: the W4.6 wall's external-
input demand (Kuznetsov-class sums of Kloosterman sums, or cross-moduli
coincidence counting beating divisor-counting on q-average — wp11
(W4.8)) stands at every admissible cell, with the required saving now
parametrized as x^{u' + (u'-u)^+ + eps} below the absolute-value floor
on the coincidence graph, i.e. essentially one full power of Q.

Downstream deltas: (1) wp11 §4.7's eta = 0.05 numerics are budget
references only — at constant level the (b3) absorption needs the
eta <= 0.02-grade cells (W1's C = 20 exceeds the ledger constant
rho(10(1-u)/3) ≈ 0.43 unless kappa <= rho/3, §1); worth a one-line
erratum flag in wp11 §4.7.1. (2) wp12's "joint cell slightly below the
top" suggestion is bounded: absorption caps the descent at
t >= 0.465 - (constant-sharpening margin <= 0.05); C† gains at most
x^{0.07} of room within the admissible wedge. (3) The b-side mirror of
E3-lb (wp9-b0-audit §5b) needs u' >= 2/5 for exact one-large unwinding
at the 3/10 cutoff — the audit's "u' > 1/3" is a band-floor slip; at
all cells under discussion (>= 0.4) it is moot, but the statement
should be corrected when E3-lb is restated.
