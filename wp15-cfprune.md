# WP15-CFPRUNE: Round-2 main attack on the W4.6 wall — idea 3

**Status: EXECUTED — NEGATIVE (FAILS, structural; see Step 6 verdict)**
**Date: 2026-06-12**

**ONE-LINE SUMMARY:** the coincidence graph IS continued-fraction-structured (exactly:
the damaging pairs of (ell,ell') are the approximation data of alpha*(ell,ell';q) =
(ell' ellbar_q mod q)/q — premise true), but p drops out of the alignment condition
EXACTLY, so the minor-arc certificates (M1)/(M2*) — p-conditions at fixed q — have no
grip; and the damaging mass is the CF-BLIND lattice mean 4HH'/q (numerics: 99.8% of
the mass), so even a perfect CF-prune (new certificate (M3), stated and shown
Family-B-countable) changes no exponent. Deficit x^{2 lam - 0.725} unchanged. New
deliverable D3: the entire wall is created at the positivity step (W4.4)(i) — E_a
provably carries the positive mean, prime-sampled truth is diagonal-grade; missing
input = equidistribution of {pbar_q} against the fibers of {h ellbar_q mod q}.

**Idea.** The coincidence graph (pairs (h,ell),(h',ell') with c | h·ell' − h'·ell, |k| small)
is continued-fraction-structured: a coincidence h ell' − h' ell = kc small relative to ell ell'
means h/ell and h'/ell' are neighbor-grade rational approximations of a COMMON real α*.
The minor-arc certificates (M1)/(M2*) of 07-minor.tex constrain the convergent structure of
the (p,q)-dependent reals on the minor set — if they (or a same-species new certificate)
constrain α*, the damaging coincidence sub-graph is PRUNED for certified (p,q), and the
W4.6 budget can be redone on the sparser graph.

Top cell: P = Q = x^{0.425}, A = x^{0.575}, R = x^{0.15}.

## Steps (all done)

- [x] Step 0: read wp15-phaselever.md (nonneg weights P1.2; macro-cluster), wp11-e3lb.md
      §4.7.1/.4 (W4.0–W4.8, fiber lemma W4.2), 07-minor.tex ((M1)/(M2*), D_R, lem:cf),
      08-major.tex (Family A/B counts, E1/E2), main.tex (spine statuses)
- [x] Step 1: identify the real α* approximated by damaging coincidences — DONE, see below.
      CENTRAL FINDING F1: α* is p-FREE (p drops out of the alignment condition EXACTLY)
- [x] Step 2: (M1)/(M2*) vs alpha* — NO grip: alpha* is p-free, certificates are
      p-conditions at fixed q; certified set has full q-marginal. Structural, not a
      weakness of the certificates
- [x] Step 3: pruned budget — even a perfect CF-prune (all alpha* golden-ratio-grade)
      leaves the lattice MEAN 4HH'/q per pair, exponent 2 lam - 0.425 unchanged;
      gain <= L^3 (worst-case-divisor vs truth), exponent gain 0.000
- [x] Step 4: (M3) stated; failure count 7 L^{-(B+1)} of q's — Family-B-countable,
      legal ledger entry, but prunes only Excess_CF: toothless by Step 3
- [x] Step 5: numerics (wp15_cfprune_probe.py) — mean-domination 1.0016; CF premise
      confirmed (corr +0.267); pruning keeps exactly the mean share; certification
      ratio 1.068 (no sparsification); all flatness checks pass
- [x] Step 6: tables identical to W4.5/W4.8 at both eta; VERDICT FAILS-[structural:
      wrong variable + CF-blind mean]; deliverables D1-D3

## Inputs (verified against the record)

- Object (wp11 §4.7.1, W4.0): D^pm_Lambda = Sum_{t=(ell,h)} chat^pm_h(ell) e(a_0 theta_t(q)),
  theta_t(q) = -h qbar_ell/ell mod 1, a_0 = pbar_q in [1,q), 0 < |h| <= H_ell = ceil(ell/(R+1)).
- Damaging terms (W4.4(iii)/W4.6, truth-grade note + wp15-phaselever Step 2): the j = 0
  coincidences q | w0 := h ell' - h' ell (cross-ell), where Delta_q = -(w0/q)/m exactly
  (m = ell ell'), F_q(Delta_q) = 1 - O(1/R) real positive, e(a_0 Delta_q) = 1 + O(1/R)
  (phase travel over a_0 in [1,q): q|w0|/(qm) <= 2/R) — NO oscillation in p, NO sign from
  the weights (P1.2: chat may be taken nonnegative-amplitude). Floor x^{2 lam - 0.425}.
- Certificates (07-minor): (M1) min(R, 1/(2||theta_mu||))/<mu> <= L^B for <mu> <= R,
  theta_mu = mu q/p - frac(lambda p/q); (M2*) every convergent denominator s <= R of q/p
  has s+/s <= R L^{-B}. Failure sets: Family A ≪ P L^{C+1-B} p's per q on q-average
  (prop:familyA mod E1), Family B ≪ PQ L^{B+1}/R pairs (p,q) (prop:familyB mod E2).

## STEP 1 — Which real do the damaging coincidences approximate? [DONE]

(1a) THE ALIGNMENT CONDITION, TRACED FROM THE ROOT CONDITION. The block term is
e(h nu_ell/ell) = e(a_0 theta_t(q)). Three-term reciprocity (q qbar_ell + ell ellbar_q
= 1 + jq ell) gives the EXACT Farey location of the root frequency:

    nu_ell/ell == (p ell)bar_q / q  -  a_0/(q ell)   (mod 1),   0 < a_0/(q ell) < 1/ell,

so each nu_ell/ell sits within 1/ell of the q-Farey point (p ell)bar_q/q. Two phases
align, h nu_ell/ell ≈ h' nu_ell'/ell' (mod 1, to accuracy < 1/q), iff

    h (p ell)bar_q == h' (p ell')bar_q   (mod q)
    <==>  [multiply by the UNIT p ell ell' mod q]   h ell' == h' ell  (mod q),

i.e. q | w0 — the j = 0 coincidence, and **p drops out EXACTLY** (the archimedean parts
h a_0/(q ell), h' a_0/(q ell') are each <= H_ell a_0/(q ell) < 1/R: macro-cluster-small).

    F1 (central finding): the damaging alignment real is determined by (q; ell, ell')
    ONLY. The conjectured (p,q)-dependence of alpha* is an illusion: a_0 = pbar_q
    multiplies BOTH sides of the alignment and cancels as a unit mod q. Consistently,
    the damaging mass itself is p-flat: at j = 0, e(a_0 Delta_q) = 1 + O(1/R)
    (wp15-phaselever P2.2), so no (p,q)-certificate can see it through the phase either.

(1b) THE REAL alpha*, EXACTLY. Fix the cross pair (ell, ell'), both prime ~ Lambda,
distinct, != q. The coincidence condition q | h ell' - h' ell is, with

    c := ell' ellbar_q mod q,        alpha*(ell,ell'; q) := c/q in (0,1),

equivalent to h' == c h (mod q). Since 0 < |h'| <= H_ell' < q/2 (Q-block; <= q at the top
block), the partner h' exists iff ||h alpha*|| <= H_ell'/q, and then h' = ch - jq with

    | alpha* - j/h |  =  |h'| / (h q)   <=   H_ell' / (|h| q).

So the damaging coincidences of the pair (ell,ell') are EXACTLY the approximation data
of the single real alpha* = (ell' ellbar_q mod q)/q: the h's are denominators of
quality-(H_ell'/q) rational approximations j/h to alpha* at heights |h| <= H_ell, and
consecutive damaging h's are CF-neighbor-grade (for |h| <= sqrt(qH/H')-grade they are
literal convergents/semiconvergents of alpha*). Equivalently: the coincidence pairs
(h,h') are the points of the determinant-q lattice Gamma(ell,ell';q) := {(u,v) in Z^2 :
u ell' == v ell (mod q)} in the box [-H_ell,H_ell] x [-H_ell',H_ell'], and the CF of
alpha* is the geometry of Gamma's successive minima. THE PREMISE OF IDEA 3 IS TRUE AND
NOW EXACT: the coincidence graph is continued-fraction-structured, fiber by fiber.
[Duality with (W4.2): the fiber lemma counts, for FIXED (t,t'), the q's with a
coincidence — divisor counting on jm - w0; here, for FIXED (ell,ell',q), the h-fiber is
CF-counting on alpha*. Two shadows of the same lattice Gamma.]

(1c) MEAN vs FLUCTUATION — where the CF structure actually lives. The per-pair count

    N(ell,ell') := #{(h,h'): 0<|h|<=H_ell, 0<|h'|<=H_ell', q | h ell' - h' ell}
                 =  4 H_ell H_ell' / q  +  E_CF(alpha*; H_ell, H_ell'/q),

where the MEAN term 4HH'/q is the lattice-density term — it depends only on
det Gamma = q, NOT on the CF of alpha* — and E_CF is the three-distance/CF fluctuation,
supported on pairs whose alpha* has a convergent denominator s <= q/H_ell' with large
gap s+/s (then N spikes to ~ H_ell/s). The chat-weighted version: with w_h(ell) the
nonnegative envelope (P1.2),

    Mass(q) = Sum_{ell != ell'} Sum_{coinc} w_h w_h' F_q
            = (1 - O(1/R)) [ Sum_{ell != ell'} ||w(ell)||_1 ||w(ell')||_1 / q  +  Excess_CF(q) ],

    MEAN TERM <= (m_1 N_Lambda)^2/q <= 97 Lambda^2/(L^2 Q)  =  x^{2 lam - 0.425 - o(1)}.

The mean term is the floor (truth-grade note of W4.5: per-pair kernel q-average ~ 6/Q,
L^0-grade; W4.7 E3 numerics). CONSEQUENCE FOR THE IDEA: any pruning that acts through
the CF/approximability of alpha* acts ONLY on Excess_CF; the mean term is CF-blind.

## STEP 2 — Do (M1)/(M2*) constrain alpha*? [DONE — NO, structurally]

WHAT THE CERTIFICATES CONSTRAIN: the CF of alpha = q/p below scale R, and the orbit
theta_mu = mu q/p - frac(lambda p/q) for <mu> <= R. Variables: the PAIR (p,q), with p
load-bearing (alpha and theta_mu both move with p at fixed q).

WHAT alpha* DEPENDS ON: alpha*(ell,ell'; q) = (ell' ellbar_q mod q)/q. Variables:
(q; ell, ell') — by F1, p does not appear. The only shared variable is q.

(2a) DIRECT CONSTRAINT: NONE. At fixed q, (M1)/(M2*) are conditions on p alone, while
the alpha*-family {(ell' ellbar_q mod q)/q : ell != ell' ~ Lambda} is a FIXED function
of q. The certificates' failure sets are sparse IN p AT EVERY q (Family A: ≪ P L^{C+1-B}
majors per q on q-average; Family B: ≪ P L^{B+1}/R per q on average): the certified
set has full q-marginal, 1 - o(1) per q. No q is excised. Since Mass(q) is p-free (F1),

    E[ Mass | (p,q) certified ]  =  E[ Mass ] (1 + o(1)):

conditioning on (M1)/(M2*) CANNOT sparsify the damaging graph — not because the
certificates are too weak, but because certification and damage live on disjoint
variables given q. This kills the idea's step (2) at the variable-dependency check,
for (M1)/(M2*) and for EVERY certificate whose content is about (p,q) at fixed q.

(2b) SPECIES CHECK (is alpha* even of the certified species?): q/p is a ratio of the
two cell primes — archimedean size ~ 1, CF accessible to lattice counting in (p,q).
alpha* = ell' ellbar_q/q is an INVERSE-RESIDUE rational — its CF is Kloosterman-sum
territory (the equidistribution of (s alpha*)_{s} is governed by Kloosterman sums
S(ell', a; q) via ellbar_q). The certificates never touch inverse residues: (M1)'s
theta_mu is bilinear in (mu, p, q) with NO modular inversion. Same-species extension
is possible (Step 4) but it must be a NEW certificate on q, not a consequence of
(M1)/(M2*).

## STEP 3 — The pruned-graph budget. [DONE — exponent unchanged]

Grant the STRONGEST conceivable CF-prune: every pair (ell,ell') whose alpha* has ANY
convergent denominator s <= H_ell with s+/s > T (any threshold T >= 3) is deleted from
the graph — i.e. every surviving alpha* is T-badly-approximable at all scales <= H_ell
(golden-ratio-grade for T = 3). Count the surviving damaging mass:

  - For T-regular alpha*, the three-distance law gives, for delta' := H_ell'/q with
    delta' H_ell ~ Lambda^2/(R^2 Q) = x^{2 lam - 0.725} (>= x^{0.125} >> 1 exactly on
    the FAILING blocks 2 lam >= 0.725; the blocks with delta' H < 1 are precisely those
    where (W4.4) already closes — the same closure exponent, no accident: delta' H IS
    the per-pair mean count):
        N(ell,ell') >= (1/T-grade) 4 H_ell H_ell' / q,
    POSITIVE-PROPORTIONAL TO THE MEAN. A T-regular real has ||h alpha*|| <= delta'
    for ~ 2 delta' H values of |h| <= H spread in ~ delta' s-spaced runs — regularity
    EQUIDISTRIBUTES the damaging h's, it does not remove them. The fiber-count lemma
    (W4.2) confirms on q-average: each (t,t') has its ~ 1.6/L prime divisors q ~ Q of
    w0 regardless of any CF condition on alpha* — divisor mass is conserved.
  - Therefore: pruned Mass(q) >= c_T x MEAN TERM = c_T x 97 Lambda^2/(L^2 Q), exponent
    2 lam - 0.425 — THE SAME EXPONENT as (W4.4)'s cross term; the prune shaves at most
    the polylog gap between the divisor-count worst case (363 L Lambda^2/Q) and the
    truth-grade mean (~ 10^2 Lambda^2/(L^2 Q)): a gain <= L^3, exponent gain 0.000.

REDONE W4.6 BUDGET: pruned floor x^{2 lam - 0.425 - o(1)} vs budget x^{0.3 - o(1)}
(eta = 0.05): deficit x^{2 lam - 0.725} on every block — IDENTICAL to W4.5/W4.8 and to
wp15-phaselever Step 5. The wall does not move because the wall IS the mean of the
coincidence graph, and the mean is the lattice-determinant term, blind to every
Diophantine property of alpha*.

## STEP 4 — The new same-species certificate (M3), stated and priced. [DONE — sound but toothless]

For completeness (the idea's step 4), the certificate that WOULD prune the CF-excess,
with its countability verified:

  (M3) [alpha*-regularity at level B, per block Lambda]. A prime q ~ Q is
  (M3)-certified if for all but N_Lambda^2 L^{-B} of the ordered pairs (ell, ell') of
  distinct primes ~ Lambda, every convergent denominator s <= H_ell of
  alpha*(ell,ell';q) satisfies s+/s <= L^{2B+3}.

FAILURE COUNT (Family-B machinery, transferred verbatim): a pair fails at scale s iff
||s alpha*|| < 1/(s L^{2B+3}), i.e. exists |r| <= q/(s L^{2B+3}) with
s ell' ellbar_q == r (mod q), i.e. q | s ell' - r ell. The integer s ell' - r ell is
NONZERO (ell | s ell' forces ell | s, impossible for 0 < s < ell; r = 0 gives
s ell' != 0) and of size < 4 Lambda Q < Q^3: at most 3 prime divisors q ~ Q per (s, r)
— THE SAME divisor count as (W4.2) and prop:familyB's |qs - pa| step. Summing:
#bad (q; ell,ell',s) <= Sum_{s <= H} 3(2q/(s L^{2B+3}) + 1) <= 7qL/L^{2B+3} per pair, so

    E_q[ # failing pairs ]  <=  N_Lambda^2 x 7 L^2 / L^{2B+3},
    P_q( q fails (M3) )     <=  7 L^{2 + B} / L^{2B+3}  =  7 L^{-(B+1)}     (Markov):

POLYLOG-COUNTABLE, Family-B species, no new input — (M3) may legally join the
major-arc ledger next to prop:familyA/B (its E2-analogue endpoint terms are the same
O(1)-per-(s,r) terms, removable the same way). AND IT IS TOOTHLESS: by Step 3, what
(M3) certifies is that Excess_CF(q) <= (mean term) x L^{-B}-grade for certified q —
it prunes the part of the mass that was never the wall. The pruned budget is Step 3's:
deficit x^{2 lam - 0.725} unchanged.

## STEP 5 — Numerics (wp15_cfprune_probe.py, .venv python). [DONE — CONFIRMS ALL FOUR]

Model x = 1e8 (wp11_w4_probe conventions): Q = P = 2512, R = 16, block Lambda = Q;
8 primes q ~ (Q, 2Q], 1500 ordered cross-pairs (ell, ell') each (~12k pairs), exact
j = 0 coincidence enumeration via h' == c h (mod q), c = ell' ellbar_q; chat-envelope
weights w_h = 1/(H+1) + min((R+1)/ell, 1/(pi h)) (the W4.4 chain's own envelope);
exact CF of every alpha*; (M1)/(M2*) toy certification (tau = 8, lambda = 1) on 40
primes p per q (319 cells, 19.7% certified).

  E1 MEAN-DOMINATION: total mass_full / mass_mean = 1.0016 — the damaging mass IS the
    lattice mean to +0.16%; per-q ratios 0.991..1.011 across all 8 q, NO q-fluctuation.
    Median per-pair N/N_mean = 0.985-0.989 (slightly < 1, mean restored by the CF tail
    — exactly the mean + spike-excess picture of (1c)).
  E2 CF-STRUCTURE PREMISE TRUE: corr(log G, N/N_mean) = +0.267; pairs with G >= p90
    (G = max convergent gap s+/s at s <= H) carry N/N_mean = 1.141 vs 0.987 for
    G <= median; max G = 3457 (a near-rational alpha*). The fluctuations ARE
    CF-structured, as idea 3 asserts — and they are +0.16% of the mass.
  E3 PRUNING IS TOOTHLESS: (M3)-pruning at T = 5/10/20/50 keeps 8.9/36.6/63.8/86.8%
    of pairs and 0.088/0.360/0.626/0.850 of the mass — pruned/its-own-mean =
    1.001/0.984/0.981/0.980 at every threshold: the surviving pairs carry EXACTLY
    their lattice-mean share (a golden-grade-only graph, T = 5, still sits at 1.001 x
    its mean). Total excess removable by perfect pruning: < 2% of the mean.
  E4 CERTIFICATION DOES NOT SPARSIFY: E[Mass | (p,q) certified]/E[Mass | all] = 1.068
    — i.e. conditioning on (M1)+(M2*) left the damaging mass UNCHANGED up to
    q-composition noise (the +6.8% is the trivial 1/q scaling: small-q cells certify
    more often in the toy and carry MORE mass — the sign is even adverse). Per-q table:
    full/mean in [0.991, 1.011] regardless of certification fraction (5%..33%). F1
    confirmed: the mass is p-free, certificates act on p.
  E5 FLATNESS: min F_q at coincidences = 0.99506 (pred 1 - O(1/R)); max a_0-phase
    travel q|Delta| = 0.0548 <= 2/R = 0.125; max Dirichlet-lever phase R|w0|/2m =
    0.439 rotations — no oscillation mechanism anywhere in the j = 0 sub-mass.

## STEP 6 — Budget tables and VERDICT. [DONE]

Pruned-graph floor = mean term = x^{2 lam - 0.425 - o(1)} per q (Steps 1c, 3, 5-E1).

eta = 0.05 (top cell P = Q = x^{0.425}, R = x^{0.15}; (W1.1) budget exponent 0.3):

  lam                          0.425   0.4737  0.50    0.55    0.575
  W4.4 cross floor (absolute)  0.425   0.5224  0.575   0.675   0.725
  CF-pruned floor (mean term)  0.425   0.5224  0.575   0.675   0.725
  deficit vs budget 0.3        0.125   0.2224  0.275   0.375   0.425
  pruning gain (exponent)      0.000   0.000   0.000   0.000   0.000

eta = 0.02 (cell P = Q = x^{0.47}, A = x^{0.53}, R = x^{0.06}; budget 0.12):

  lam                          0.47    0.50    0.53
  CF-pruned floor              0.47    0.53    0.59
  deficit vs budget 0.12       0.35    0.41    0.47

Both tables reproduce W4.5/W4.8 (and wp15-phaselever Step 5) EXACTLY; the prune buys
at most the L^3 between the divisor worst case (363 L Lambda^2/Q) and the truth-grade
mean (~10^2 Lambda^2/(L^2 Q)) — polylog, never an exponent.

### VERDICT: FAILS-[structural, two independent kills, each sufficient:

(i) WRONG VARIABLE: the alignment real is alpha*(ell,ell'; q) = (ell' ellbar_q mod q)/q
— p drops out of the alignment condition EXACTLY (a_0 = pbar_q multiplies both sides as
a unit mod q; Step 1a), and the j = 0 mass is p-flat to O(1/R) (E5). The minor-arc
certificates (M1)/(M2*) are p-conditions at fixed q with full q-marginal: conditioning
on them provably cannot change the damaging mass (E4: ratio 1.07, adverse sign, pure
q-composition). No certificate about (p,q) — present or future — can prune a p-free
mass.
(ii) CF-BLIND MEAN: the coincidence graph of the pair (ell,ell') is the determinant-q
lattice Gamma = {(u,v): u ell' == v ell (mod q)} in the H x H' box; its damaging count
= 4HH'/q (mean, depends only on det Gamma = q) + CF-fluctuation of alpha*. The mass is
the MEAN to +0.16% (E1), uniformly in q; CF pruning — even keeping only golden-ratio-
grade alpha* — removes mass exactly proportionally (pruned/own-mean = 0.98-1.00 at
every threshold, E3). The wall is the lattice density, not the Diophantine excess;
deficit x^{2 lam - 0.725} at eta = 0.05 (x^{2 lam - 0.59}-line at 0.02) unchanged.

POSITIVE DELIVERABLES: (D1) the premise of idea 3 is TRUE and now exact — the
coincidence graph is CF-structured fiber-by-fiber via alpha*, and (W4.2) is its
q-averaged shadow (fixed pair, divisor-count over q) while CF-counting is the
fixed-(ell,ell',q) shadow over h: two projections of one lattice Gamma. (D2) The (M3)
alpha*-regularity certificate is well-posed and Family-B-countable (failure fraction
<= 7 L^{-(B+1)} of q ~ Q, pure divisor counting — may join the major-arc ledger if any
future chain needs truth-grade rather than worst-case coincidence constants: it
converts the W4.3 constant 4.4 L^2/Q to ~ L^0 6/Q-grade, an L^2-class saving, no more).
(D3) Sharpened wall statement for the ledger: with P1.2 (nonnegative weights) and F1
(p-free, a_0-flat j = 0 mass), the W4.6 cancellation can come ONLY from the prime
sampling itself — E_a over all residues a mod q PROVABLY carries the positive mean
x^{2 lam - 0.425} (it is a sum of fiber-squares), while the truth at prime-sampled
a_0 = pbar_q is diagonal-grade (W4.7 E1): the entire deficit is created at the
positivity step (W4.4)(i), and what is missing is equidistribution of the N_P-point
set {pbar_q} against the fiber structure of {h ellbar_q mod q} — Kloosterman/Kuznetsov
territory, the same external species as W4.8's rider, now localized to one inequality.]

## Log

- Created file; read wp15-phaselever.md (P1.2 nonneg weights, macro-cluster, P2.1-P2.2),
  wp11-e3lb.md §4.7.1+§4.7.4 (W4.0-W4.8), 07-minor.tex ((M1)/(M2*), D_R, lem:cf),
  08-major.tex (Family A/B, E1/E2), main.tex spine.
- Step 1: traced the alignment real from the root condition via three-term reciprocity:
  nu_ell/ell == (p ell)bar_q/q - a_0/(q ell); alignment <=> h ell' == h' ell (mod q)
  after multiplying by the unit p ell ell' — F1: alpha* = (ell' ellbar_q mod q)/q is
  p-FREE. Coincidences of (ell,ell') = approximation data of alpha* at heights <= H,
  quality H'/q = lattice Gamma (det q) points in the H x H' box. Premise of idea 3
  exact; (p,q)-dependence refuted.
- Step 2: (M1)/(M2*) constrain (q/p, theta_mu) — p-conditions at fixed q, full
  q-marginal; alpha* is a fixed function of q: NO grip, structurally (variable
  disjointness, not certificate weakness). alpha* is inverse-residue species
  (Kloosterman), never touched by the minor machinery.
- Step 3: perfect CF-prune leaves the lattice mean 4HH'/q per pair (T-regular reals
  EQUIDISTRIBUTE damaging h's, don't remove them); pruned floor = x^{2 lam - 0.425},
  gain <= L^3, exponent gain 0.000. Deficit x^{2 lam - 0.725} unchanged.
- Step 4: (M3) stated (alpha*-regularity, level B); failure count <= 7 L^{-(B+1)}
  fraction of q by the (W4.2)/familyB divisor count — Family-B-countable, legal,
  toothless (prunes Excess_CF only).
- Step 5: probe wp15_cfprune_probe.py — mean-domination 1.0016 (excess +0.16%); CF
  correlation +0.267 (premise true); pruning keeps exactly mean share (0.98-1.00) at
  all thresholds; certification ratio 1.068 (no sparsification, adverse sign); F_q >=
  0.995, a_0-travel <= 0.055. All four predictions confirmed.
- Step 6: tables at eta = 0.05/0.02 identical to W4.5/W4.8; VERDICT
  FAILS-[structural: wrong variable (alpha* p-free) + CF-blind mean]. Deliverables
  D1-D3 recorded; D3 localizes the wall to the positivity step (W4.4)(i): missing
  input = equidistribution of {pbar_q} against the fibers of {h ellbar_q mod q}.
