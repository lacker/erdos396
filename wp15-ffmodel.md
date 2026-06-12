# WP15: Function-Field Model of the Missing Estimate (Round-3 idea 10 — diagnostic)

**STATUS: EXECUTED. VERDICT (split, see §4): FF-PROVABLE in the large-r regime
[mechanism: physical resummation + unit-avoidance of the single resonant residue b = 0 +
Weil II in the r-direction with GOS-poly(D) Betti control]; FF-WALL-PERSISTS at fixed r
[the wall is combinatorial: sub-conductor CRT-hit dispersion / prime-detection in a
one-candidate-per-class family — RH-class inputs are already saturated and do not touch it].
SIDE-DISCOVERY (must be audited): translated back, the physical-representation bound
appears to prove the integer estimate up to POLYLOG — the x^{2lam-0.725} power-deficit looks
representation-dependent (an artifact of the harmonic chain). See §3.5, flagged loudly.**

Date: 2026-06-12. Inputs: wp15-cfprune.md (D3, F1), THE-OPEN-PROBLEM.md §2/§3.2/§3.3/ADDENDUM,
wp11-e3lb.md §4.7.1 (W1) + §4.7.4 (W4.0–W4.8), main.tex spine. This is a diagnostic, not a
proof for the paper; the deliverable is clarity of mechanism.

---

## 0. The integer-side object being modeled (fixed, from D3)

- (D3, positivity-step form): the entire deficit x^{2lam-0.725} is created at (W4.4)(i):
  E_p |D|^2 <= 0.85 L * E_{a mod q} |D(a)|^2; the chain's accounting of E_a carries the
  positive coincidence mass x^{2lam-0.425} while prime-sampled truth is diagonal-grade
  x^{0.15}. Missing input: equidistribution of {pbar_q} against the fibers of
  {h ellbar_q mod q}, nonnegative weights (ADDENDUM).
- (W4.6/Form A): |Sum_{ell != ell'} Sum_{h,h'} chat chat' F_q(w0 qbar_m/m)| <= x^{0.3-o(1)},
  w0 = h ell' - h' ell, m = ell ell'; absolute floor x^{2lam-0.425} attained; demanded signed
  saving x^{2lam-0.725}. Scales: q ~ x^{0.425}, ell ~ x^{lam}, lam in [0.425, 0.575],
  H_ell ~ ell/R, R = x^{0.15}, window [0,R].
- Structural facts the model must reproduce: (F1) p-free alignment, flat phases at
  coincidences; (SS) self-similarity of the harmonic ladder; (PV) window far below
  square-root density; (OC) overcrowding #T_lin >> q.
- IMPORTANT bookkeeping fact recovered from §4.7.1 (W1): the real budget is
  (W1.1)  E_{p,q}|D^+_Lambda|^2 <= 20 delta_0 (eta R)^2 L^{-2},
  and the L^{-2} (plus delta_0 = L^{-a}) is LOAD-BEARING: the aggregation Chebyshevs over
  J = 0.22 L blocks. "x^{0.3-o(1)} with polylogs immaterial" is shorthand valid for the
  routes audited (all power-short); the demand itself is R^2 L^{-2-a}-grade.

## 1. The dictionary and the exact F_r[T] analogue

Fix a prime power r; D = the degree analogue of log x (x ~ r^D, L = log x <-> D up to log r).

| integer side | F_r[T] side |
|---|---|
| n ~ x | monic f, deg f = D |
| prime p, q ~ x^{0.425} | monic irreducibles P, Q, deg = d_q = ceil(0.425 D); N_P ~ r^{d_q}/d_q |
| prime ell ~ x^{lam} | irreducible ell(T), deg = d_ell = lam D |
| window [0, R], R = x^{0.15} | W = {nu : deg nu < d_R}, d_R = 0.15 D — an F_r-SUBSPACE |
| harmonics 0 < |h| <= H_ell ~ ell/R | h != 0, deg h < d_H := d_ell - d_R (so "H = ell/R" exactly) |
| e(x) | e_F(f) := psi(c_{-1}(f)), c_{-1} = coeff of T^{-1} in F_r((1/T)) |
| ||beta|| | r^{deg of fractional part}; ultrametric |
| a_0 = lift of pbar_q to [1,q) | b_P := lift of (P mod Q)^{-1} to {deg < d_q} (F_r-linear section) |
| Vaaler S^pm, coefficients (2.1) | EXACT: 1_W(nu) = r^{-d_R'} Sum_{deg h < d_H} e_F(h nu / ell); chat_h = r^{d_R - d_ell} = R/ell, CONSTANT >= 0 |
| F_q(beta) = q^{-1} Sum_a e(a beta) | F_Q(f) = 1[ ||f|| < r^{-d_q} ]  — EXACT INDICATOR |

Three exact simplifications the ultrametric buys (each verified by direct computation):
(i) NO completion error: the window indicator's Fourier expansion over the subspace dual is
exact; weights are constant and nonnegative (the ADDENDUM's P1.2 holds trivially).
(ii) SHARP kernel: F_Q is an indicator; coincidence <=> ||theta_t - theta_{t'}|| < r^{-d_q}
<=> (W4.2-computation, j-sum collapses to j = 0 only, since deg w0 < d_m forces j = 0)
<=> Q | w0 := h ell' - h' ell. The integer side's |j| <= 2 fiber becomes a single fiber.
(iii) Exact lattice mean: #{(h,h'): Q | h ell' - h' ell} in the d_H x d_H' coefficient box is
F_r-LINEAR-algebra: kernel dimension d_H + d_H' - d_q generically, count = HH'/q exactly
(= x^{2lam - 0.725} >= 1 per pair on every failing block) — the integer mean 4HH'/q, with the
CF fluctuation absorbed into rank-deficiency strata (Mahler: FF lattice counts are exact).

**The analogue estimate (FF-Form A).** With D(b) := Sum_{ell, deg ell = lam D, irred, != Q}
( 1[ deg( lift(b) * Qbar_ell mod ell ) < d_R ] - r^{d_R - d_ell} ), b in k_Q := F_r[T]/(Q):

    (FF-A)  E_{P irred, deg P = d_q} |D(b_P)|^2  <=  delta_0 r^{0.3 D} / D^2 - grade,
            uniformly in lam in [0.425, 0.575], for all but delta_0 N_Q/D-grade of the Q.

Floor check (model fidelity): the analogue of the (W4.4) chain gives, after positivity
(P -> b_P injective into k_Q, cost 0.425 D ~ L) and the sharp kernel,
E_b |D(b)|^2 >= Sum_{coincident pairs} chat chat' = N_Lambda^2 / q = r^{(2lam - 0.425)D - o(D)}:
the SAME attained floor, same exponent, now with constant nonnegative weights and identically-1
phases at coincidences — F1 is exact in FF (b_P multiplies both sides of the alignment as a
unit mod Q and cancels). The model is faithful to the wall's stated geometry.

**The D3 fibers, algebraized.** The summand of D(b_P) as a function of P: the map
a |-> e_F(lift(a) * (-h Qbar_ell/ell)) is psi(lambda_t(a)) for an F_r-linear functional
lambda_t on k_Q composed with nothing else; by finite-field duality lambda_t(a) =
Tr_{k_Q/F_r}(beta_t a), so the phase is

    Phi_t(P) = psi_Q( beta_t * (P mod Q)^{-1} ),    beta_t in k_Q,   psi_Q = psi o Tr.

The D3 object "equidistribution of {pbar_q} against the fibers of {h ellbar_q mod q}" becomes:
equidistribution of {(P mod Q)^{-1}} against the additive characters psi_Q(beta_t *) — and the
FIBERS are the level sets of t |-> beta_t. Computed exactly:

    beta_t = beta_{t'}  <=>  c_{-1}(b * n/m) = 0 for all deg b < d_q  <=>  deg n < d_m - d_q
            <=>  Q | h ell' - h' ell   — the fibers of t |-> beta_t ARE the coincidence classes.

So in FF the coincident pairs have IDENTICALLY EQUAL phases as functions of P: no
equidistribution statement about {Pbar mod Q}, however strong (even perfect), cancels a
coincident pair. With nonnegative weights this looks like an irreducible floor — but see §2.

## 2. The diagnostic: what survives full RH (Weil II) — and the resummation it forces

### 2.1 Physical resummation: the wall mass is a single point

Because the completion is exact, D(b) resums in closed form (RH = ell/R exactly):

    D(b) = mult(b) - mean,   mult(b) := #{ (ell, s) : deg s < d_R, ell | lift(b) - sQ }.

Elementary anatomy of mult:
- For b != 0: lift(b) - sQ != 0 always (degrees: deg b < d_q <= deg sQ for s != 0; b != 0 at
  s = 0), of degree <= 0.575 D < 2 lam D, hence AT MOST ONE irreducible factor of degree
  lam D per s, and distinct s force distinct ell (ell | (s - s')Q with deg(s-s') < d_R < d_ell
  is impossible). So  mult(b) <= R  pointwise, all b != 0.
- For b = 0: s = 0 admits EVERY ell:  mult(0) = N_Lambda = r^{lam D}/(lam D).

Consequence (exact, elementary): E_{b in k_Q} mult^2 = N_Lambda^2/q  [the b = 0 point]
+ O(R * E mult) [everything else] = r^{(2lam-0.425)D - o(D)} + O(r^{0.3 D - o(D)}).
THE ENTIRE WALL MASS x^{2lam-0.425} IS THE SINGLE NON-UNIT RESIDUE b = 0 (plus
rank-deficient strata of polylog measure). Cross-check against §1's harmonic accounting: the
coincident-pair mass (flat phases, nonneg weights, "irreducible") and the b = 0 spike are the
SAME number computed in two bases; the noncoincident pairs conspire NEGATIVELY at every
b != 0 and reinforce at b = 0 — the conspiracy is just the complete-subgroup-sum identity
Sum_{deg h < d_H} e_F(h nu/ell) = H * 1_W(nu). The "self-similar wall" is the harmonic
shadow of a delta at zero.

And: b_P = lift((P mod Q)^{-1}) is a UNIT — the prime sample avoids b = 0 for free. D3's
localization ("the entire wall is created at the positivity step") is hereby CONFIRMED and
EXPLAINED: in FF the positivity step E_P <= (q/N_P) E_{b in k_Q} loses exactly the inclusion
of the zero residue, and nothing else of power size.

### 2.2 What remains after the spike is removed, and what RH does to it

For b != 0, max * mean gives E mult^2 <= R * E mult = r^{0.3D}/D-grade — within D^{1+a} of
the budget delta_0 r^{0.3D}/D^2. The residual question is pair-decorrelation (max*mean ->
Poisson), i.e. with w := mult^2:

    (CORE)   Sum_{b != 0} w(b) * ( pi_b - N_P/q )  <=  delta_0 * N_P * r^{0.3D}/D^2,
    pi_b := #{P irred : b_P = b} = 1[ Q + lift(b^{-1}) is irreducible ]  in {0,1},

the last identity because deg P = deg Q + monicity leaves EXACTLY ONE candidate per class:
P = Q + lift(b^{-1}). Three findings, each checked:

(a) ABELIAN RH IS ALREADY SATURATED AND USELESS HERE. Class-count variance
Sum_b (pi_b - N_P/q)^2 = N_P (1 - N_P/q) exactly (monicity pigeonhole: P ≡ P' mod Q with
deg(P - P') < deg Q forces P = P') — Poisson-grade WITHOUT RH. Weil's RH for Dirichlet
L-functions over F_r(T) (a theorem) adds nothing to it; Cauchy-Schwarz of (CORE) against it
loses D^{1/2}: short by D^{1/2}/delta_0. The needed statement is the WEIGHTED correlation
itself, which CS cannot see — and which is the original question (circularity, as on the
integer side).

(b) THE HARMONIC/SPECTRAL ROUTE REPRODUCES THE CONDUCTOR MISMATCH VERBATIM UNDER RH.
Expanding pi_b - density in multiplicative characters of k_Q^*: Sum_P psi_Q(beta/P(theta)) =
(q-1)^{-1} Sum_chi tau(chi, beta) Sum_P chi(P); Weil gives |Sum_P chi(P)| <= d_q r^{d_P/2}/d_P
per character (full RH-grade), |tau| = q^{1/2}: total q^{1/2} * r^{d_P/2} = q at d_P = d_q:
TRIVIAL. The loss is the CHARACTER MULTIPLICITY (q characters at conductor q against
argument length q), not the per-character bound — the exact FF incarnation of §3.3(a)/(e)
(Polya-Vinogradov barrier; Kloosterman-over-primes below the Fouvry-Michel length threshold;
"deep in the Selberg range"). RH does not move it. Equivalently in zeros: the d_q ~ 0.425 D
inverse zeros of each L(chi) all sit on |alpha| = r^{1/2} (RH), and the residual factor
D^{1/2..1} is their worst-case COHERENCE at degree n = d_q — a zero-angle equidistribution
question (vertical Sato-Tate), strictly beyond RH.

(c) THE GEOMETRIC (LARGE-r) ROUTE CLOSES IT — the one genuinely FF-only input. (CORE) is a
weighted count of F_r-points on explicit varieties: the quadruple family (ell, s, ell', s')
pins b (CRT + box), and the weight asks irreducibility of F(b) = Q + lift(b^{-1}) — all maps
(inversion mod Q, F_r-linear lift, divisibility) are algebraic over F_r. Fibered into 1–2
parameter slices, Grothendieck-Ogg-Shafarevich bounds the relevant Betti/Swan data by
poly(D), and Weil II gives per-slice square-root cancellation in the r-direction: relative
error r^{-1/2} poly(D) < delta_0 = D^{-a} once r >= poly(D). (At full dimension the Betti
numbers are C^D — the classical FF caveat — so the honest regime split is below; the
Sawin-Shusterman vanishing technology is the known instrument for pushing such statements to
fixed r >= absolute constant in related families: short-interval factorization statistics,
twin irreducibles; whether it covers THIS family — inverse-lift composed weights, the
"depth-one Fermat-quotient" species of §5.2 — is open, and at genuinely fixed small r nothing
known applies.)

### 2.3 Answer to THE DIAGNOSTIC QUESTION

- Under RH alone (Weil's RH for L-functions of F_r(T), per-character square-root — the
  honest analogue of GRH): THE WALL PERSISTS at fixed r. The blocking factor is not
  arithmetic depth; it is the multiplicity/coherence loss (b): a COMBINATORIAL/STRUCTURAL
  wall. Its core, stripped bare (no exponentials, no primes needed in the all-unit version):

      (CORE-COMB)  #{ (ell, s, ell', s') : the CRT class of (sQ mod ell, s'Q mod ell')
                     meets the box {deg < d_q} }  =  (expected)(1 + O(delta_0)),

  a SUB-CONDUCTOR BOX-DISPERSION count: box q = x^{0.425}, moduli ell ell' = x^{0.85..1.15}
  >= box^2 (fewer than one box point per class), family x^{2lam+0.3}, demanded relative
  precision polylog. This is Form B's "signed divisor-correlation with no exponentials,"
  re-derived from the FF side — consistency check passed.
- What falls under RH-plus-geometry (large r): everything — but the input that does the work
  is square-root cancellation in the r-DIRECTION (Frobenius averaging over the horizontal
  family of all residue/parameter configurations at fixed combinatorial shape). That
  direction is the rigorous avatar of the RANDOM MODEL (§3.1): FF geometry PROVES the random
  model in the ensemble limit. The integer side has no horizontal family (one point in the
  ensemble); hence no integer analogue of this input exists even conjecturally as an
  L-function statement. Naming the missing integer technology precisely: a deterministic
  substitute for ensemble averaging = a dispersion/Titchmarsh-divisor-type theorem AT THE
  EDGE p ~ q (one prime per class), for the divisor-correlation weight mult^2 against
  {pbar_q}, to relative precision delta_0 L^{-O(1)} — polylog-deep, not power-deep (§3.5).

## 3. Mechanism extraction (proof sketch in the provable regime) + back-translation

### 3.1 FF proof sketch (r >= poly(D); unconditional in r-power saving)

1. Exact completion (subspace duality) — no Vaaler layer; weights constant nonnegative.
2. Resummation to physical space: D(b) = mult(b) - mean; identify the resonant locus
   {b = 0} + rank-deficient strata; prove E_{b != 0} via max*mean to r^{0.3D}/D-grade.
3. Unit-avoidance: b_P != 0; positivity step taken WITHIN units only — no power loss.
4. Pair-decorrelation: write E_P mult(b_P)^2 - mean^2 as a weighted point count over the
   (ell, s, ell', s')-variety with the irreducibility weight pi_b = 1[Q + lift(b^{-1}) irred];
   slice into curves/surfaces; per slice, Weil II + GOS gives main term * (1 + O(r^{-1/2} D^C)).
5. Sum slices; total relative error r^{-1/2} poly(D) < delta_0. (FF-A) follows, uniformly in
   lam, for all Q (no exceptional set needed in this regime). QED-sketch.

The object that "sees the signs": the middle cohomology of the slice varieties — i.e. the
cancellation lives in H^i_c of the CRT-incidence family in the r-direction, NOT in any
L-function over the T-direction. The signs were never arithmetic: after resummation there
are no signs left, only a variance-of-counts statement (the harmonic "signs" were the Fourier
transform of positivity-of-counts minus a delta at zero).

### 3.2 Why the integer-side harmonic ladder could not see this

The ladder (W1 -> W4) enters through the completed square and prices every pair by |F_q|:
in the physical basis that is exactly pricing the delta-at-zero spike as if it were spread
over all residues. The FF model makes the artifact visible because its kernel is sharp; the
integer kernel's tails smear the same accounting. Self-similarity (SS) is explained: the
harmonic chain regenerates its own artifact at every generation; no contraction is possible
because the artifact is created by the basis choice, not by the estimate's content.

### 3.3 The fixed-r persistent wall, named (the combinatorial core)

(CORE-COMB) above; equivalently: Poisson-grade pair-decorrelation of window hits
{ell | b - sQ} over a box smaller than the pair-conductor. Every known FF instrument is
either abelian (saturated, loses the multiplicity factor) or geometric (needs the
r-direction). At r fixed, D -> infinity — the true analogue of Z — the gap D^{1+a} between
max*mean and Poisson stands, EVEN WITH RH. The wall is structural/combinatorial:
it is about counting lattice/CRT hits in sub-conductor boxes to relative polylog precision,
i.e. about the rigidity of small boxes against ~x^{0.85+} conductors — no oscillation, no
sign, no L-function in it.

### 3.4 BUT: the wall's SIZE re-measured (the major reframing)

In the physical representation the deficit is NOT a power of x — on either side. FF:
max*mean gives r^{0.3D} D^{O(1)} vs budget delta_0 r^{0.3D} D^{-2}: gap D^{3+a}. Integer
side, same chain (all three sub-lemmas are in the program's own W1 toolkit):
  (P1) pointwise window/Vaaler-band counts: Sum_ell |y_ell| <= 7(R+1)L  [(W1.1)(a) + (W1.3),
       proved pointwise in (p,q) in §4.7.1];
  (P2) first moment: E_{p,q} Sum_ell |y_ell| <= C(R+1)  [progression-discrepancy O(1) per ell
       for {-sq mod ell} hitting [1,q], plus <= 2 primes p per residue class mod q; checked
       at top blocks where N_Lambda/q = R/L];
  (P3) Hoelder(infinity, 1):  E_{p,q} |D^pm_Lambda|^2 <= sup(Sum|y|) * E(Sum|y|) <= C' R^2 L.
If (P1)-(P3) survive audit, then Form A's LHS is unconditionally <= x^{0.3} L^{O(1)} — the
power-deficit tables (W4.5/W4.8, THE-OPEN-PROBLEM §2.3) describe the harmonic chain only,
and the TRUE distance from proved to needed is L^{3+a}-grade (C' R^2 L vs
20 delta_0 (eta R)^2 L^{-2}), uniformly in lam. The "attained floor" x^{2lam-0.425} is
attained by the absolute-value HARMONIC sum, which bounds nothing physical from below.

### 3.5 AUDIT FLAG (read first if acting on this file)

§3.4 contradicts the record's framing ("every gap in this problem is a power of x",
THE-OPEN-PROBLEM §2.1) and therefore needs independent verification before anything is built
on it. Specific checkpoints: (i) (P3)'s validity is trivial; the load is on (P2) — the
per-ell O(1) discrepancy bound summed over ell costs N_Lambda/q = up to R/L, checked, but the
Vaaler-tail banding at all dyadic widths must be re-summed with the same care (sketch in this
session: converges, factor ~3); (ii) the chain proves (W1.1) only up to L^{3+a}, so the
program's wall AS STATED stands — what changes is its species: polylog, not power; (iii) toy
numerics are consistent (at x = 1e8: physical chain ~1e4 vs harmonic chain ~1.7e7 vs measured
truth 1.5 vs budget ~0.04 delta_0) but cannot distinguish L^3 from x^{0.125} at toy scale —
the claim is structural, not numerical. If (P1)-(P3) fail audit, §§1-2 (the FF diagnostic
proper) are unaffected.

## 4. VERDICT

**FF-PROVABLE-[large-r regime; mechanism: exact-completion resummation localizes the wall
mass onto the single non-unit residue b = 0, which prime sampling avoids for free; the
remaining pair-decorrelation is closed by Weil II square-root cancellation in the
r-direction (Frobenius averaging over the horizontal CRT-incidence family, Betti control by
Grothendieck-Ogg-Shafarevich on slices). The RH-input that does the work is the GEOMETRIC
one — the rigorous random-model/ensemble direction — whose integer analogue does not exist.]**

**FF-WALL-PERSISTS-[fixed r, even under full RH: the wall is combinatorial. Core:
sub-conductor box-dispersion (CORE-COMB) — count CRT-class hits of a box of size q inside
moduli ell ell' >= q^2 over a family of x^{2lam+0.3} quadruples to relative polylog
precision; equivalently Poisson-vs-max*mean pair-decorrelation of window hits at
inverse-prime points (Titchmarsh-divisor-at-the-edge species). Abelian RH is saturated (the
class-count variance is already exactly Poisson by a monicity pigeonhole); the loss is
character multiplicity / zero coherence, beyond RH on both sides.]**

Combined reading for the program: the missing integer technology is NOT a stronger
Kloosterman/L-function input (FF says RH-strength arithmetic does not touch the core); it is
(1) [if §3.4 survives audit] nothing at the power level — the physical Hoelder chain already
matches the demand's x-exponent unconditionally — plus (2) a polylog-depth dispersion for
divisor-correlation weights against {pbar_q} at the p ~ q edge, the depth-zero sibling of
§5.2's C-dagger estimate (same genus, same "fewer than one element per class" signature).
The two open bricks of the program are therefore plausibly ONE brick, both polylog-deep.

## Log

- Created file; read wp15-cfprune.md (D3, F1, j=0 anatomy), THE-OPEN-PROBLEM.md (§2 Forms
  A/B, §3.2 floor, §3.3 obstruction map, ADDENDUM nonneg weights), wp11-e3lb.md §4.7.4
  (W4.0-W4.8) and §4.7.1 (W1 object, (W1.1) budget with load-bearing L^{-2}), main.tex spine.
- Step 1 (dictionary): windows = F_r-subspaces => exact completion, constant nonneg weights;
  F_Q = sharp indicator; coincidence <=> Q | h ell' - h' ell exactly (j = 0 only); lattice
  mean exact by linear algebra; floor x^{2lam-0.425} reproduced; F1 exact. D3 phases
  algebraized: Phi_t(P) = psi_Q(beta_t (P mod Q)^{-1}); fibers of t -> beta_t = coincidence
  classes (proved by the c_{-1}-coefficient computation).
- Step 2 (diagnostic): physical resummation D(b) = mult(b) - mean; mult(b) <= R for b != 0,
  mult(0) = N_Lambda: wall mass = the single residue b = 0; prime sample avoids it (units).
  Remaining gap D^{1+a} (max*mean vs Poisson). Abelian RH saturated (monicity pigeonhole
  gives exact Poisson class-variance; CS loses D^{1/2}; character expansion of
  Kloosterman-over-primes trivial at d_P = d_q — conductor mismatch reproduced VERBATIM under
  RH). Geometric Weil II in the r-direction closes it for r >= poly(D) via slicing + GOS;
  fixed small r: open, wall persists, combinatorial core (CORE-COMB) named.
- Step 3: proof sketch (provable regime) + mechanism: cancellation lives in H^i_c of the
  CRT-incidence family in the r-direction = rigorous random model; signs were the Fourier
  shadow of counts-minus-delta. Back-translation produced §3.4: integer-side physical
  Hoelder chain (P1)-(P3) appears to give E|D^pm|^2 <= C R^2 L unconditionally — power
  deficit is representation-dependent; AUDIT FLAG §3.5 attached (contradicts record framing;
  three checkpoints listed; W1's own toolkit contains all pieces, applied there only to
  Diag/Near, never to Gen).
- Step 4: split verdict recorded above.
