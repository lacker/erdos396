# WP15: Phase-lever + R-averaging attack on the W4.6 wall

**Status: EXECUTED — NEGATIVE (FAILS, structural; see Step 7 verdict)**
**Date: 2026-06-12**

**ONE-LINE SUMMARY:** the Dirichlet-kernel phase e(-R w0/(2m)) travels at
most ~3 rotations over the entire (p,q)-cell because the Selberg truncation
already confines the family to the 1/R-wide macro-cluster (W4.1); the kill
region is EMPTY, >= 1/3 of the coincidence mass is positively aligned and
lever-immune, and the W4.6 deficit x^{2 lam - 0.725} is unchanged. Numerics
confirm (rotation max 3.003 attained; R-average yield 0.339 vs fixed-R
0.338). New unconditional fact: the Vaaler coefficients are exact-phase x
NONNEGATIVE-amplitude (P1.2), so W4.6's weights may be taken nonnegative —
no coefficient-level sign structure exists; cancellation must come from the
q-arithmetic.

## Goal

MAIN ATTACK on W4.6: exploit the explicit Dirichlet-kernel phase of the completion
coefficients c_h(ell) on the window [0,R] mod ell, combined with averaging over the
(p,q)-cell (which sweeps R = x/(pq) over a relative-length-~1 interval), to kill the
signed coincidence mass on the cross-denominator graph c | h ell' - h' ell.

Top cell: P = Q = x^{0.425}, A = x^{0.575}, R = x/(pq) ~ x^{0.15}, L = log x.

## Steps

1. [x] Exact completion coefficients c_h(ell) with phase (Dirichlet kernel) — P1.1/P1.2.
2. [x] Product phase on a coincidence pair = -R k c/(2 ell ell') exactly — P2.1/P2.2.
3. [x] R-average: kill region EMPTY; retained = full graph; crux answer NO.
4. [x] Honest single (p,q)-cell average: implementable, moot; arm halved.
5. [x] Budget table eta = 0.05/0.02: deficits unchanged, = W4.5/W4.8 lines.
6. [x] Numerics: confirmed (max travel 3.003; yield 0.339; core 0.32).
7. [x] Verdict: FAILS-[structural — see Step 7].

## Inputs (verified against the record)

- Object (wp11-e3lb §4.7.1): D_Lambda(p,q) = Sum_{ell ~ Lambda prime, != q}
  (1[nu_ell <= R] - (R+1)/ell), nu_ell = (-a_0 qbar_ell) mod ell, a_0 = pbar_q.
  Selberg layer: degree H_ell = ceil(ell/(R+1)), coefficients chat^pm_h(ell),
  |chat_h| <= 1/(H_ell+1) + min((R+1)/ell, 1/(pi|h|)), masses m_1 = 4.1.
- Variance target (W1.1): E_{p,q}|D^+_Lambda|^2 <= 20 delta_0 (eta R)^2 L^{-2},
  derived from §3.4(2)'s absorption E_{p,q} N_hard <= C eta R — a CELL-AVERAGE
  demand (confirmed §3.4(2) and wp9-theorem1prime link 7 feed: only the
  (p,q)-average + Markov/Chebyshev layer is consumed). R-averaging is legal.
- W4.6 wall: signed mass Sum_{t != t', ell != ell'} chat_t conj(chat_{t'})
  F_q(theta_t - theta_{t'}) on the coincidence graph; absolute floor (W4.4)
  cross term 363 L Lambda^2/Q = x^{2 lam - 0.425 + o(1)} vs budget x^{0.3-o(1)}:
  deficit x^{2 lam - 0.725}. Floors derived for ABSOLUTE coefficients (W4.3-W4.4).
- Coincidence graph parameter (W4.2): w0 := h ell' - h' ell != 0 (= k c in
  Form B language, c the modulus), q-coincidences at level j: q | (j m - w0),
  m := ell ell'; the j = 0 level is q | w0, kernel F_q ~ 1.

## STEP 1 — Exact completion coefficients of the window [0,R] mod ell, with phase. [DONE]

The exact (sharp-window) completion coefficient is the discrete Fourier
coefficient of 1_{[0,R]} on Z/ell:

    c_h(ell) := (1/ell) Sum_{r=0}^{R} e(-hr/ell).

Geometric sum, z = e(-h/ell):  Sum_{r=0}^R z^r = (z^{R+1}-1)/(z-1)
  = z^{R/2} (z^{(R+1)/2} - z^{-(R+1)/2})/(z^{1/2} - z^{-1/2}), so EXACTLY

    c_h(ell) = e(-hR/(2ell)) * sin(pi h (R+1)/ell) / (ell sin(pi h/ell)).   (P1.1)

PHASE: phi_h(ell) = -hR/(2ell) — i.e. e(-h * center/ell) with center = R/2
the midpoint of the discrete window {0,...,R}. The remaining factor
K_h(ell) := sin(pi h(R+1)/ell)/(ell sin(pi h/ell)) is REAL, and for
0 < |h| <= H_ell = ceil(ell/(R+1)) it is NONNEGATIVE up to the last-index
sliver: pi|h|(R+1)/ell <= pi(1 + (R+1)/ell), so sin >= -O((R+1)/ell) only at
|h| = H_ell, else >= 0. (Convention note: completing the length-(R+1) window
centered at (R+1)/2 instead replaces R by R+1 in the phase; the two differ by
e(-h/(2ell)), immaterial below — we use the exact discrete (P1.1).)

THE SAME PHASE STRUCTURE HOLDS FOR THE FULL VAALER/SELBERG COEFFICIENTS —
this is the load-bearing observation (the lever acts on chat^pm, not just on
a "main term"). Selberg's construction for the interval I = [alpha, beta]
(here alpha = -1/(2ell), beta = (R + 1/2)/ell: length (R+1)/ell, center
c* = R/(2ell), matching chat^pm_0 = (R+1)/ell pm O(1/(H+1)) of W1):

    S^pm(x) = (beta-alpha) + V_H(x-beta) - V_H(x-alpha)
              pm (1/(2H+2))[Delta_{H+1}(x-beta) + Delta_{H+1}(x-alpha)],

with V_H Vaaler's approximation to the sawtooth (hat{V_H}(h) =
-(2 pi i h)^{-1} jhat(h/(H+1)), jhat real even, 0 <= jhat <= 1) and
Delta_{H+1} the Fejer kernel (real nonnegative coefficients). Using
e(-h beta) -+ e(-h alpha) = e(-h c*) * { -2i sin(pi h(R+1)/ell) or
2 cos(pi h(R+1)/ell) }:

    chat^pm_h(ell) = e(-hR/(2ell)) * a^pm_h(ell),                       (P1.2)
    a^pm_h(ell) = jhat(h/(H+1)) sin(pi h(R+1)/ell)/(pi h)
                  pm (1 - |h|/(H+1)) cos(pi h(R+1)/ell)/(H+1)   — REAL.

So the ENTIRE Selberg coefficient factors as the explicit Dirichlet phase
e(-hR/(2ell)) times a real amplitude; the symmetric window makes the sawtooth
and Fejer corrections share the center-phase. Moreover for the MAJORANT sign
(the one (W1.1) uses) a^+_h >= 0 for all |h| <= H/(1+o(1)): pi h(R+1)/ell
runs over [0, pi], where sin >= 0, jhat >= 0, Fejer term >= 0 — the Selberg
truncation H_ell = ceil(ell/(R+1)) sits exactly at the FIRST ZERO of the
window transform: within it the amplitudes are single-signed. (Two facts for
later: (i) the lever's phase is fully explicit on every coefficient; (ii) no
sign cancellation is available from the amplitudes themselves.)

## STEP 2 — Product phase on a coincidence pair. [DONE]

In E_p|D|^2 only frequency DIFFERENCES occur: the (t, t') term of the
opened square (t = (ell,h), t' = (ell',h'), conj(chat_{t'}) picked up by
|.|^2) is

    chat_t conj(chat_{t'}) e(a_0 (theta_t - theta_{t'}))
      = a_t a_{t'} e( phi_h(ell) - phi_{h'}(ell') ) e(a_0 Delta_q),

and by (P1.2) the explicit product phase is EXACTLY

    phi_h(ell) - phi_{h'}(ell') = -(R/2)(h/ell - h'/ell')
      = -R (h ell' - h' ell) / (2 ell ell') = -R w0/(2m) = -R k c/(2m),  (P2.1)

m = ell ell', w0 = h ell' - h' ell = k c (Form B: c | w0, k = w0/c; at the
j = 0 coincidence level c = q and k = w0/q). [(R+1) in place of R under the
centered-window convention; difference e(-+ w0/(2m)), |w0|/m <= 2/R: a
rotation by < 1/R of a turn — immaterial.] So after the a_0-average (the
positivity step (W4.4)(i), which is EXACT on the cross terms — the kernel
F_q(Delta_q) is computed, not bounded), the signed coincidence mass is

    Sum_{t != t', ell != ell'} a_t a_{t'} e(-R w0/(2m)) F_q(Delta_q),    (P2.2)

with a_t a_{t'} >= 0 (majorant sign, Step 1) and, at the dominant j = 0
coincidence level (q | w0, Delta_q = -(w0/q)/m, q||Delta_q|| = |w0|/m
<= 2/R << 1): F_q = e(-(q+1)w0/(2qm)) sin(pi w0/m)/(q sin(pi w0/(qm)))
= 1 - O(1/R), real positive, NO a_0-oscillation. Every sign/oscillation in
the j = 0 sub-mass therefore lives in the single explicit factor
e(-R w0/(2m)) — exactly the lever the brainstorm proposes. (Higher levels
j != 0 carry the extra explicit sign (-1)^j e(-w0/(2m) + n/(2m))-type phases
from the Dirichlet kernel F_q; they are kernel-damped by 2^{-k} and are not
where the floor lives — W4.7/E3: truth ~ 6/Q is j-small dominated.)

## STEP 3 — The R-average: kill threshold vs graph support. [DONE — NEGATIVE]

LEGALITY (checked): §3.4(2) and wp9-theorem1prime link 7 consume only the
(p,q)-CELL-average E_{p,q} N_hard <= C eta R plus a Markov/Chebyshev layer;
nothing downstream needs per-(p,q) variance. Averaging the phase over the
cell sweep of R = x/(pq) is legal. At FIXED q (forced: theta_t(q) and the
coincidence structure must be held fixed), p sweeps (P, 2P] and R sweeps
(R1, 2R1], R1 := x/(2Pq) ~ x^{0.15}: a factor-2 interval, relative length 1.
Over the whole cell R sweeps a factor 4. Idealize first (best case for the
idea — step 4 does the honest coupling): R uniform on (R1, 2R1], independent
of a_0.

PER-PAIR GAIN. Averaging e(-R w0/(2m)) over R in (R1, 2R1] (amplitudes
a_t(R), kernels vary smoothly: total variation O(sup) — partial summation,
no extra loss beyond constants):

    gain(w0) ~ min(1, 2m/(R1 |w0|)),   killed iff |w0| >> m/R1.       (P3.1)

SUPPORT OF THE GRAPH (the fatal computation, two lines):
  - UPPER: Selberg truncation |h| <= H_ell = ceil(ell/(R+1)) means
    |h/ell| <= 1/(R+1) <= 1/R1 — W4.1's macro-cluster, verbatim. So
    |w0|/m = |h/ell - h'/ell'| <= 2/R1: MAX PHASE TRAVEL over the sweep
    = R1 * (2/R1) / 2 = ONE rotation.                                 (P3.2)
  - LOWER (coincidences): j = 0 needs q | w0, w0 != 0: |w0| >= q > Q.
    So coincidence frequencies |w0|/m in [Q/m, 2/R1], phase travel in
    [R1 Q/(2m), 1] = [x^{-(2lam-0.575)}, 1].

KILL REGION = {|w0| >= L m/R1} = EMPTY SET. The retained sub-graph is the
ENTIRE coincidence graph. Retained mass = full mass up to a constant:
with u = h/ell, u' = h'/ell' ~ flat on [-1/(R+1), 1/(R+1)] (Step 1: |a_h|
~ (R+1)/ell flat over |h| <= H — the triangular-difference law), the mass
fraction with travel >= 1/2 rotation is <= 1/4 (and -> 0 as R -> 2R1); so

    R-averaged signed j=0 coincidence mass >= (3/4 - o(1)) * (aligned part),

and an explicitly POSITIVELY-ALIGNED CORE survives: pairs with |w0| <=
m/(6 R1) have |phase| <= R1|w0|/m <= 1/6 turn POINTWISE across the whole
sweep, so Re e(-Rw0/(2m)) >= cos(pi/3) = 1/2; their mass fraction
(triangular law, checked against the q|w0 multiple-count m/(6R1q) vs
2m/(R1 q): consistent) is >= 1/6 - 1/144 ~ 0.16. With a_t a_{t'} >= 0 and
F_q = 1 - O(1/R) at j = 0 (Step 2), this core is a sum of terms with real
part >= (1/2)(a_t a_{t'}) — NO cancellation mechanism left inside it: the
R-averaged signed coincidence mass is >= 0.08 x (full absolute j=0 mass)
= x^{2 lam - 0.425 - o(1)}-grade, i.e. the FULL FLOOR, reduced only by an
absolute constant.

STRUCTURAL IDENTITY (why this could never work): (completion degree) x
(window-center sweep) = (ell/(R+1)) x (R/2)/ell ~ 1/2 — the Selberg
truncation H_ell = ceil(ell/(R+1)) is tuned to the window length, and the
window center moves by exactly the window length. R-averaging is
power-equivalent to convolving the window indicator with a length-~R0
mollifier; a length-(R0) window is ALREADY maximally smooth at its own
scale — the Vaaler layer saturates this smoothing, and idea 2 is idea-D1.2
(the Selberg repair) in disguise. Sharper version: to oscillate the
smallest coincidence (|w0| = Q) by >> 1 the lever arm would need length
>> 2m/Q = x^{2 lam - 0.425} >= x^{0.425}; available arm: x^{0.15}. Arm
deficit x^{2 lam - 0.575}, which is x^{0.15} WORSE than even the W4.6 mass
deficit x^{2 lam - 0.725}. And even a PERFECT kill of all |w0| > T lands at
budget only if T <= x^{0.575}, retaining mass fraction T R1/(2m) >=
(coincidences exist iff T >= Q) Q R1/(2m) = x^{0.725 - 2 lam}-grade —
EXACTLY the budget ratio with zero margin, and the required arm x^{2 lam
- 0.575} >= x^{0.275} is not available. CRUX ANSWER: NO — the R-average
does not reduce the coincidence mass below the budget; it reduces it by a
factor between 1 and ~12.

## STEP 4 — Honest bookkeeping: R = R(p,q) inside the average. [DONE]

R is not a free parameter: at fixed q the sweep variable is p, which drives
BOTH a_0 = pbar_q (arithmetic) and R = x/(pq) (archimedean). Four couplings,
each priced:

(4a) FAMILY DRIFT: H_ell = ceil(ell/(R+1)) is (p,q)-dependent — T_lin
itself moves. Repair: fix ONE degree per ell for the whole cell,
H_ell := ceil(ell/(R_cell + 1)), R_cell := min cell R = x/(4PQ); Vaaler
holds at any degree, constants (m_1, drift) move by <= 2. Removes the
family's R-dependence at constant cost. [OK]

(4b) CENTERING DRIFT: chat_0 = (R(p,q)+1)/ell pm 2/(H+1) — W1's drift
ledger (12.1 eta(R+1)) was POINTWISE in (p,q): tolerates R(p,q) verbatim.
The variance target (eta R)^2 with moving R: use R_cell on the right of
(W1.1); constants inflate by <= 16, absorbed in the absolute C. [OK]

(4c) POSITIVITY vs COUPLING — the real issue. The (W4.4)(i) step (discard
p-primality: E_p -> (0.85 L/q) Sum_{a mod q}) requires the summand to
depend on p ONLY through a_0; with R(p) inside the phase it does not. Two
repairs priced:
  - SLICING: cut p ~ P into K slices, freeze R per slice. Positivity then
    costs 0.85 K L (each slice covers N_P/K of q residues); the freezing
    error run through the same W4.4 chain carries cross mass ~ (W4.4 cross)
    / K^2. Net optimum over K: K = O(1) — slicing buys NOTHING (to kill the
    freezing error needs K >= x^{lam - 0.3625}, power-sized, while the
    frozen part's floor is multiplied by K). [NO RESCUE]
  - MELLIN SEPARATION: separate the archimedean dependence by Fourier/
    Mellin in log p. The coefficient p -> chat_h(ell; x/(pq)) has total
    variation O(|chat|) over the sweep BECAUSE the phase travels <= 1
    rotation (P3.2 again): separation costs only O(L) mass and restores
    positivity exactly. But this works precisely because the lever has no
    grip: TV-affordability and rotation count are the SAME number. A lever
    with power-many rotations would have power-sized separation cost. The
    mechanism is self-limiting: (grip) x (affordability) = O(1). [OK BUT
    MOOT — reinstates Step 3's bound, nothing better]

(4d) ARM LENGTH, honest: at fixed q the sweep is R in (R1, 2R1] (factor 2,
not the cell's factor 4) — the honest arm is HALF the idealized one of
Step 3; the q-sweep cannot be added (theta_t(q) must stay fixed for the
coincidence structure; varying q re-randomizes the graph, which is the
W4.3 average already spent). Step 3's verdict holds a fortiori.

CONCLUSION: the honest cell average is implementable (4a+4b+4c-Mellin at
polylog cost), and under it the retained signed coincidence mass is the
SAME x^{2 lam - 0.425 - o(1)} floor as Step 3, constant-factor reduced.
The R-dependence does not break the W1/W4 bookkeeping — but the lever it
feeds is structurally toothless.

## STEP 5 — Budget table. [DONE]

Retained = R-averaged signed coincidence mass (Steps 3-4): exponent equals
the W4.4 cross floor (reduction factor in [1, ~12], exponent gain 0.000).

eta = 0.05 (cell P = Q = x^{0.425}, R = x^{0.15}; (W1.1) budget exponent
2r = 0.3); lam = log_x Lambda:

  lam                         0.425   0.4737  0.50    0.55    0.575
  W4.4 cross floor (absolute) 0.425   0.5224  0.575   0.675   0.725
  retained after R-average    0.425   0.5224  0.575   0.675   0.725
  deficit vs budget 0.3       0.125   0.2224  0.275   0.375   0.425
  lever arm needed 2m/Q       0.425   0.5224  0.575   0.675   0.725
  lever arm available (R)     0.15    0.15    0.15    0.15    0.15
  arm deficit                 0.275   0.3724  0.425   0.525   0.575

eta = 0.02 (cell P = Q = x^{0.47}, A = x^{0.53}, R = x^{0.06}; budget 0.12):

  lam                         0.47    0.50    0.53
  W4.4 cross floor            0.47    0.53    0.59
  retained after R-average    0.47    0.53    0.59
  deficit vs budget 0.12      0.35    0.41    0.47
  arm deficit (2lam - 0.53)   0.41    0.47    0.53

Both rows reproduce W4.5/W4.8's deficit lines EXACTLY: the phase lever +
R-average changes no exponent at either eta. Note the arm deficit EXCEEDS
the mass deficit by x^{0.15} (eta = 0.05) / x^{0.06} (eta = 0.02) uniformly:
this lever family is strictly weaker than what the wall requires even
before honesty costs.

## STEP 6 — Numerics (wp15_phaselever_probe.py, .venv python). [DONE — CONFIRMS]

Model x = 1e8 (wp11_w4_probe conventions): Q = P = 2512, cell R(p,q) in
[3, 15], Lambda = Q block, j = 0 coincidence graph q | w0 enumerated
exactly (6 primes q, 4000 (ell,ell')-pairs each, 2.2e7 coincidences;
honest R-dependence: degrees, amplitudes, phases all move with R on the
grid; F_q exact). Results (aggregate):

  - min |w0|/q = 1, max rotations over the FULL cell sweep = 3.003
    (= (R_max-R_min)/(R_min+1) exactly — the P3.2 support bound, attained).
  - Mass-weighted rotation histogram [0,.125,.25,.5,1,2,inf]:
    [0.342, 0.284, 0.304, 0.070, 3e-5, 0]: 93% of coincidence mass at
    < 1/2 rotation; mass beyond 1 rotation: 3e-5. KILL REGION EMPTY.
  - S_abs = 3.799; |S(Rbar)|/S_abs = 0.338 (fixed-R signed);
    |avg_R S|/S_abs = 0.339 — the R-average yields ZERO reduction beyond
    the fixed-R constant (0.338 -> 0.339, slightly UP); per-pair sinc
    theory retains 0.886 of absolute mass.
  - Aligned core (travel <= 1/6 turn): 36% of mass; its R-averaged real
    part = 0.321 x S_abs — a positively-aligned, lever-immune sub-mass of
    ~1/3 of the full floor, as computed in Step 3 (0.08 was the
    conservative bound; truth ~ 0.32).

Prediction verified on all four counts: constant-grade ratio, empty kill
region, surviving positive core, sinc-consistency.

## STEP 7 — VERDICT. [DONE]

FAILS-[structural, two independent ways quantified:
(i) SUPPORT: the retained near-diagonal IS the whole graph. The Selberg
truncation H_ell = ceil(ell/(R+1)) confines all frequencies to W4.1's
macro-cluster |h/ell| <= 1/(R+1), so every coincidence pair has
|w0|/m <= 2/R1 while the R-sweep arm is only ~R1: max phase travel <= ~3
rotations across the entire (p,q)-cell (numerics: 3.003, attained); the
kill region {travel >> 1} is EMPTY; >= 1/3 of the coincidence mass is
positively aligned (travel <= 1/6 turn, a_t a_{t'} >= 0, F_q = 1 - O(1/R))
and survives ANY R-average at >= 1/2 strength. Retained-mass exponent =
floor exponent x^{2 lam - 0.425 - o(1)}: deficit x^{2 lam - 0.725}
unchanged at both eta = 0.05 and 0.02 (Step 5 tables = W4.5/W4.8 verbatim).
(ii) ARM: even granting a perfect kill above any threshold T, coincidences
need T >= Q and the surviving [Q, T]-mass meets the budget only with zero
margin at T = x^{0.575}, whose oscillation needs arm x^{2 lam - 0.575} >=
x^{0.275} vs the available x^{0.15} — the arm deficit exceeds the mass
deficit by x^{0.15} uniformly.
STRUCTURAL IDENTITY: (completion degree) x (window sweep) = (ell/R) x
(R/ell) = 1 — R-averaging is power-equivalent to mollifying the window at
its OWN length scale, which the Vaaler layer (D1.2 repair) already
saturates; ideas 1+2 are the Selberg truncation in disguise. The lever is
self-limiting: its grip (rotation count) and its bookkeeping affordability
(TV of coefficients in p, Step 4c) are the SAME O(1) number.
POSITIVE DELIVERABLES: (P1.2) the full Vaaler/Selberg coefficients factor
as exact Dirichlet phase x real amplitude, amplitudes single-signed within
the truncation (majorant sign) — so NO sign structure for W4.6 can come
from the coefficients themselves: any future signed attack must source
cancellation from the q-arithmetic (qbar_m residues / j != 0 kernel signs)
— this sharpens wp13 §4's Form A/B statement: the weights ĉĉ' may be taken
NONNEGATIVE; the (4a) uniform-degree and (4c) Mellin-separation devices
(legal, polylog cost) are reusable for any future cell-average lever.
W4.6 remains the wall; external-input species unchanged.]

## Log

- Created file; read wp11-e3lb.md §4.7.1/.2/.4 + §3.4, wp13 §4, wp9-t1' link 7.
- Step 1 done: exact phase e(-hR/(2ell)) on c_h AND on the full Vaaler chat^pm_h
  (P1.1/P1.2); majorant amplitudes nonnegative within the truncation.
- Step 2 done: pair phase = -R w0/(2m) = -R k c/(2m) exactly (P2.1); at j = 0
  the kernel is 1 - O(1/R) real positive and the lever phase is the ONLY
  oscillation (P2.2).
- Step 3 done, NEGATIVE: kill region {|w0| >= Lm/R1} is EMPTY (max phase
  travel = 1 rotation, by macro-cluster support W4.1); positively-aligned
  core >= 0.08 x full floor survives any R-average. Crux answer: NO.
- Step 4 done: honest coupling implementable (uniform degree + Mellin
  separation, polylog cost; drift/target tolerate R(p,q)); honest arm =
  half of idealized; Step 3 verdict unchanged a fortiori.
- Step 5 done: budget tables at eta = 0.05/0.02 — retained exponent = W4.4
  cross floor at every lam; arm deficit exceeds mass deficit by x^{0.15}.
- Step 6 done: probe (wp15_phaselever_probe.py) confirms all predictions;
  R-average yield 0.339 of absolute (constant-grade), aligned core 0.32.
- Step 7 done: VERDICT FAILS-[retained near-diagonal = full graph; support
  x arm = O(1); positive core ~ 1/3 of floor]. File complete; steps box
  updated. Deliverable for future attacks: W4.6 weights may be taken
  nonnegative (P1.2).
