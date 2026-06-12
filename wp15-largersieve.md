# WP15-LARGERSIEVE: Round-3 attack on the D3-localized wall — idea 7 (Gallagher's larger sieve / fiber restriction)

**Status: EXECUTED — NEGATIVE (FAILS, structural; see Step 5 verdict)**
**Date: 2026-06-12**

**ONE-LINE SUMMARY:** the larger sieve has no grip on the D3 wall, three ways:
its collision primitive Sum_{p != p'} #{q : q | p - p'} is EXACTLY ZERO (q > P),
its best-possible constant Delta = N_P still pays the fiber energy
Sum_v |m_v|^2 = x^{2 lam - 0.425} (over budget before any sampling loss — the
single-fiber test vector floors the ENTIRE weight-uniform sieve class), and the
hoped support lever is absent (fibers are MANY: S_V/q = 1 - o(1), occupancy
#T_lin/q >= x^{0.275}; the macro-cluster compresses WITHIN fibers, making m_v
positive — adverse). Deficit x^{2 lam - 0.725} unchanged. New deliverable: the
missing input sharpened to the signed asymptotic (D3-INEQ*) — the off-fiber
Kloosterman form must equal -(1 - o(1)) x (within-fiber energy), verified
numerically at 0.97-1.01 strength per q.

**Target.** The D3 localization (wp15-cfprune.md): the entire W4.6 deficit is created
at the positivity step (W4.4)(i); the missing input is equidistribution of the
N_P-point set {pbar_q} against the fibers of {h ellbar_q mod q}. Weights are
nonnegative (P1.2, wp15-phaselever.md): the q-arithmetic is the ONLY cancellation
source. Attack: Gallagher's larger sieve / fiber-restriction at exactly this
inequality — exploit that the fiber-mass m_v(q) is supported on FEW residues v mod q
(macro-cluster), so restricted-residue counting may beat the trivial q/N_P loss.

Top cell: P = Q = x^{0.425}, A = x^{0.575}, R = x^{0.15}, L = log x.
Deficit to beat: x^{2 lam - 0.725} (eta = 0.05), lam in [0.425, 0.575].

## Steps (all done)

1. [x] D3 object exact: fibers F_v, masses m_v, (W4.4)(i) demand = (D3-INEQ);
       j = 0 coincidence graph = within-fiber pairs; floor = fiber energy.
2. [x] Larger-sieve formulations: collision primitive ZERO; energy form
       mean-conserving; test-vector kill Delta >= N_P floors the whole class;
       "no-Kloosterman" second-moment route exits the divisor species.
3. [x] Fiber-support count: S_V/q = 1 - o(1) (fibers MANY, occupancy >= x^{0.275});
       hybrid lever priced exactly: gain = 1. Macro-cluster acts within fibers
       (adverse: makes m_v positive).
4. [x] Numerics (probe confirms all five) + budget tables eta = 0.05/0.02:
       identical to W4.5/W4.8, gain exponent 0.000.
5. [x] VERDICT: FAILS-[structural: K1 empty primitive, K2 test-vector floor,
       K3 no support lever]; deliverable (D3-INEQ*).

## Inputs (verified against the record)

- (W4.0): D^pm_Lambda = Sum_{t=(ell,h)} chat^pm_h(ell) e(a_0 theta_t(q)),
  theta_t(q) = -h qbar_ell/ell mod 1, a_0 = pbar_q in [1,q),
  0 < |h| <= H_ell = ceil(ell/(R+1)), ell ~ Lambda prime != q.
  #T_lin <= 4.8 Lambda^2/((R+1)L) = x^{2 lam - 0.15 - o(1)}.
- (W4.4)(i): E_p|D|^2 <= 0.85 L (1/q) Sum_{a mod q} |Sum_t chat_t e(a theta_t)|^2
  — discards p-primality; this is where x^{2 lam - 0.725} is created (D3).
- (W4.2) fiber-count lemma: fixed t != t', #{q ~ Q: ||Delta_q|| < 2^k/q} <= 2^{k+4}
  (divisor counting on jm - w0, w0 = h ell' - h' ell != 0).
- P1.2: chat^pm_h = e(-hR/(2ell)) a_h, a_h >= 0 (majorant sign).
- F1 (cfprune): the j = 0 coincidence mass is p-free and a_0-flat;
  E_a over ALL a mod q provably carries the positive mean x^{2 lam - 0.425}.
- 05-deep-large-sieve.tex proof pattern (thm:dls): orthogonality -> fibers ->
  Cauchy-Schwarz within fibers -> fiber-size bound (prop:fiber), energy
  E = Sum_v f_v^2 <= (max f_v)(Sum f_v) (prop:energy).
- Gallagher's larger sieve: if S subset [1,N] occupies <= nu(q) residues mod q
  for each q in a set Q* of primes (or prime powers), then
  #S <= (Sum_{q in Q*} log q - log N) / (Sum_{q in Q*} (log q)/nu(q) - log N),
  valid when the denominator is positive. Wins when nu(q)/q is SMALL.

## STEP 1 — The D3 object, exactly. [DONE]

(1a) FIBERS AND MASSES. Fix q ~ Q prime. By three-term reciprocity (cfprune 1a),
theta_t(q) = -h qbar_ell/ell ≡ v_t/q - h/(q ell) (mod 1), v_t := h ellbar_q mod q,
with archimedean correction |h|/(q ell) <= 1/(q(R+1)) — so over the FULL a-range
[1,q) the correction phase a·h/(q ell) travels <= 1/(R+1) of a turn: O(1/R)-soft.
Define the fibers and masses

    F_v := {t = (ell,h) in T_lin : h ellbar_q ≡ v (mod q)},   v in Z/q,
    m_v := Sum_{t in F_v} chat_t      (P1.2: = Sum e(-hR/(2ell)) a_t, a_t >= 0),

and the pure fiber aggregate U~(a) := Sum_v m_v e(av/q) = U(a)(1 + O(1/R)).
KEY IDENTITY (makes cfprune's alpha*-picture a fiber statement): for t != t',

    v_t - v_{t'} ≡ (h ell' - h' ell)(ell ell')bar_q = w0 mbar_q (mod q),

so  v_t = v_{t'}  <=>  q | w0  <=>  the j = 0 coincidence: THE j = 0 COINCIDENCE
GRAPH IS EXACTLY THE UNION OF WITHIN-FIBER PAIRS, ∪_v F_v x F_v minus diagonal.
Within a fiber the relative phases are flat (cfprune E5: F_q >= 0.995, travel
<= 2/R), so the masses are effectively nonnegative: |m_v| ~ Sum_{t in F_v}
(envelope) — no within-fiber cancellation exists (P1.2). Hence the FIBER ENERGY

    Sum_v |m_v|^2 = Sum_t |chat_t|^2 + (j=0 coincidence mass)
                  = x^{0.15} + x^{2 lam - 0.425 - o(1)}   per q   (PROVED positive;
    cfprune E1: per-q ratios to the lattice mean 0.991..1.011 — q-stable),

and Parseval: (1/q) Sum_{a mod q} |U~(a)|^2 = Sum_v |m_v|^2.

(1b) THE (W4.4)(i) INEQUALITY AND ITS EXACT REPLACEMENT DEMAND. The chain's step:
p -> a_0 = pbar_q injective (|p - p'| < P <= Q < q), so by positivity

    E_p |U(a_0)|^2 <= (q/N_P) (1/q) Sum_{a mod q} |U(a)|^2
                    = 0.85 L Sum_v |m_v|^2 (1 + O(1/R)),

which is x^{2 lam - 0.425 + o(1)} >= x^{0.425+o(1)}: over the (W1.1) budget
x^{0.3 - o(1)} by x^{2 lam - 0.725}. The D3-localized missing input, precisely:

    (D3-INEQ)  For all but delta_0 N_Q/L of q ~ Q:
       (1/N_P) Sum_{p ~ P} | Sum_v m_v e(pbar_q v/q) |^2  <=  x^{0.3 - o(1)},
    equivalently, expanding (the w = 0 term is forced, E_p e(0) = 1):
       Sum_v |m_v|^2  +  Sum_{w != 0} Ghat(w) K_q(w)  <=  x^{0.3 - o(1)},
    Ghat(w) := Sum_v m_{v+w} mbar_v  (autocorrelation, Ghat(0) = Sum|m_v|^2),
    K_q(w) := (1/N_P) Sum_{p ~ P} e(w pbar_q / q)  (incomplete Kloosterman over primes).

(1c) THE SIGN STRUCTURE — what (D3-INEQ) really demands. Since Sum_v |m_v|^2 =
x^{2 lam - 0.425} >= x^{0.425} > budget, (D3-INEQ) REQUIRES

    Sum_{w != 0} Ghat(w) K_q(w)  =  - Sum_v |m_v|^2 (1 + O(x^{-(2 lam - 0.725)})):

a NEGATIVE evaluation of the off-fiber Kloosterman bilinear form, at (1 - o(1)) of
the full fiber energy. NOT an upper-bound statement. Truth check at toy scale
(x = 1e8, W4.7 E1 + cfprune E1): fiber energy ≈ diagonal + 22 per q (Q-block,
(Sum|chat|)^2/q = 236^2/2512), measured E_p|U(pbar_q)|^2 ≈ 1.5: the cross part is
empirically ≈ -0.93 x (within-fiber mass). The cancellation is REAL — the sampled
set {pbar_q} (density N_P/q ~ 1/(0.85L) in Z/q) anti-correlates with the fiber
spikes at (1 - o(1)) strength. That anti-correlation is the object to be proved.

## STEP 2 — Larger-sieve formulations, each computed. [DONE — all floored]

(2a) DIRECT LARGER SIEVE OVER THE q-FAMILY (Gallagher, the p-count form). The
larger sieve's ONLY primitive is the collision energy over the modulus family:

    Sum_{q ~ Q} Sum_{v mod q} r_q(v)^2,   r_q(v) := #{p ~ P : pbar_q ≡ v}
      = N_P N_Q + Sum_{p != p'} #{q ~ Q : q | p - p'}  =  N_P N_Q + 0,

EXACTLY: |p - p'| < P <= Q < q forces zero collisions. The {pbar_q} system is
PERFECTLY spread (r_q(v) <= 1 for every v, every q): Gallagher's hypothesis is
saturated trivially and its conclusion degenerates to the injectivity already
consumed at (W4.4)(i). Quantitatively, Gallagher #S <= (Sum log q - log N)/
(Sum (log q)/nu(q) - log N) applied to p's restricted to nu(q) classes mod q:
our only sub-1 density is the sample itself, nu(q) = N_P ~ q/(0.85L): the
denominator gain Sum_q (log q)/nu(q) ~ L x (trivial): maximal gain factor ~ L —
POLYLOG, vs power deficit x^{2 lam - 0.725}. No grip.

(2b) ENERGY FORM Sum_q Sum_v m_v(q) r_q(v)-species, vs the 05 fiber/energy
pattern. Manuscript 05's pattern (thm:dls): orthogonality -> fibers -> CS within
fibers -> fiber-size bound. Transferring to the D3 object: the damage is

    D(q) := Sum_p |U~(pbar_q)|^2 = Sum_{a mod q} r_q(a) |U~(a)|^2,

a CROSS-correlation of two fiber systems: the sample fibers r_q (self-energy
N_P N_Q, (2a)) and the mass fibers m_v ((W4.2)-controlled across q). The 05 proof
pattern (CS within fibers + fiber-size bound) yields exactly the (W4.4) chain:
E_q D(q)/N_P <= 0.85 L [diag + (W4.3) coincidence mass] — the floor again. The
alternative Cauchy split D(q) <= (Sum r_q^2)^{1/2} (Sum_a |U~(a)|^4)^{1/2} =
N_P^{1/2} q^{1/2} ((1/q)Sum|U~|^4)^{1/2} >= N_P^{1/2} q^{1/2} Sum_v|m_v|^2:
WORSE than the floor by (q/N_P)^{1/2} ~ L^{1/2}. Cauchy loses on a nonneg sum.

(2c) THE TEST-VECTOR KILL (closes the whole class). Every sieve-type inequality —
large, larger, restricted-residue, dispersion-with-absolute-values, any mixture —
is WEIGHT-UNIFORM: it has the shape

    Sum_{p ~ P} |Sum_v m_v e(pbar_q v/q)|^2  <=  Delta(q,P) Sum_v |m_v|^2
    (or its q-averaged version with Delta' uniform over weight families).

Test vector m = delta_{v_0}: LHS = N_P, so Delta >= N_P ALWAYS (and Delta' >= N_P:
the fiber diagonal passes through every q). But even the PERFECT constant
Delta = N_P (zero sampling loss, full square-root orthogonality) gives

    D(q)/N_P <= Sum_v |m_v|^2 = x^{2 lam - 0.425 - o(1)}  >  budget x^{0.3}:

THE FLOOR IS THE FIBER ENERGY ITSELF, and it sits over budget BEFORE any sampling
loss is paid. The deficit x^{2 lam - 0.725} is invariant over the entire class of
weight-uniform inequalities. (D3-INEQ) requires going BELOW Ghat(0), i.e. a
negative main term from w != 0 — no upper-bound technology produces a negative
main term. This is the same theorem as cfprune's "CF-blind mean" and phaselever's
"positive core", one level up: THE WALL IS A NONNEGATIVE MEAN (now: the fiber
energy); sieves control fluctuations around means, never means.

(2d) "KLOOSTERMAN NOT NEEDED IF second moments over q suffice" — COMPUTED: NO.
The hoped route: control Var_q[D(q) - N_P Sum_v|m_v(q)|^2] by (W4.2)-style divisor
counting, then Markov in q. Opening the square produces
Sum_q Sum_{p,p'} Sum_{w,w' != 0} Ghat_q(w) Ghat_q(w') e((w pbar_q - w' p'bar_q)/q):
the q-aspect phases carry pbar_q INSIDE e(./q) — the multiply-by-q trick of (W4.2)
(which kills inverses when the denominator m = ell ell' is q-free) does NOT apply
when the denominator IS q. These are sums of incomplete Kloosterman sums in the
q-aspect: Linnik/Kuznetsov species, precisely W4.8's external rider. Divisor
counting cannot reach them; the "no-Kloosterman" hope exits the elementary species
at exactly this line. Moreover even PERFECT variance control (D(q) = its q-mean
for every q) lands on the mean N_P Sum_v|m_v|^2 = the floor (2c): second moments
over q are doubly insufficient — wrong species AND mean-conserving.

(2e) LEVEL-SET / INCIDENCE VARIANT (the last sieve shape): declare B_T(q) :=
{a : |U~(a)|^2 > T}; Chebyshev |B_T(q)| <= q Sum|m_v|^2/T. The damage above level
T is (incidences) x T; in the BEST case (random-model incidences, {pbar_q}
perfectly equidistributed in every B_T(q)): Sum_p 1[pbar_q in B_T] ~ N_P |B_T|/q,
giving damage ~ N_P Sum_v|m_v|^2 AT EVERY LEVEL T — the level-set decomposition
CONSERVES the mean, deficit-independent of T. And Gallagher applied to the
persistently-bad set S_bad = {p : pbar_q in B_T(q) for >= half of q ~ Q} does
bound #S_bad <= P x^{-delta} when |B_T|/q = x^{-delta} (power-small spike sets) —
but the damage is the INCIDENCE count, not the persistent-p count: a p bad for
o(N_Q) of q evades S_bad while its incidences still carry full mass. The larger
sieve bounds the wrong aggregate, and the right aggregate equals the mean.

## STEP 3 — Fiber-support count: are the fibers FEW? [DONE — NO: support = q(1 - o(1))]

The Montgomery/larger-sieve hybrid wins iff the v-support S_V := #{v : m_v != 0}
satisfies S_V/q < x^{-delta}. The macro-cluster intuition ("all frequencies within
1/R of each other => v-support ~ q/R = x^{0.275}-sized") is FALSE for F_lin(q):

  - The macro-cluster |h/ell| <= 1/(R+1) is a property of the q-FREE pair family
    F_pair = {h/ell} (W4.1(a)) and, after multiplication by mbar_q, of the
    coincidence DIFFERENCES (v_t - v_{t'} = w0 mbar_q with |w0|/m <= 2/R). It
    compresses WITHIN-fiber geometry, not the fiber positions.
  - The fiber positions v_t = h ellbar_q mod q are unit-DILATES of the intervals
    [±H_ell]: per ell, 2H_ell values scattered mod q (three-distance/Beatty, gaps
    ~ q/2H_ell, pseudo-randomized by ellbar_q — W4.1(b) verbatim); the union over
    N_Lambda ~ Lambda/L primes ell throws #T_lin = x^{2 lam - 0.15} points at
    q = x^{0.425} classes.
  - OCCUPANCY: #T_lin/q = x^{2 lam - 0.575} >= x^{0.275} >> 1 on EVERY block
    (eta = 0.02: x^{2 lam - 0.53} >= x^{0.41}). Coupon-collector regime: every
    class is hit; typical fiber size f_v ~ x^{2 lam - 0.575}, support
    S_V = q(1 - o(1)). [Consistency: within-fiber pair count = j = 0 coincidence
    count ~ #T_lin^2/q = x^{4 lam - 0.725} (W4.6 line), and Sum f_v^2 / (Sum f_v)^2
    ~ 1/q — flat fiber profile, no spike compression. Verified numerically below.]

PRICE OF THE HYBRID, EXACT: gain factor = S_V/q = 1 - O(x^{-(2 lam - 0.575)}) —
identically 1 in exponent. The only sub-1 density in the problem is the SAMPLE
{pbar_q}: nu(q)/q = N_P/q ~ 1/(0.85 L) — polylog, already priced at 0.85 L in
(W4.4)(i); it is the COST of positivity, not a lever. So the hybrid's lever
support/q < 1 is structurally ABSENT: fibers are MANY (essentially all of Z/q),
each carrying x^{2 lam - 0.575} flat mass. ADVERSE TWIST: the macro-cluster,
which the idea hoped would compress the support, instead acts WITHIN fibers,
where it makes the masses m_v phase-flat, i.e. POSITIVE (cfprune E5) — it is
the reason the fiber energy is irreducibly large. The structure is exactly
inverted relative to what a larger sieve needs.

## STEP 4 — Numerics + budget tables. [DONE]

NUMERICS (wp15_largersieve_probe.py, .venv python; model x = 1e8: Q = P = 2512,
R = 16, Lambda = Q block, N_Lambda = N_P = 306, 8 primes q ~ Q; exact sharp-window
coefficients with P1.2 phase; m_v assembled exactly; full period by FFT):

  S_V/q = 0.9996 at EVERY q (support = all of Z/q: fibers are MANY — Step 3
    confirmed; the 0.0004 deficit is the q - #T_lin-occupancy noise).
  fiber energy = 10.57..10.70 per q (diag 1.29 + within-fiber 9.3), q-stable
    to 1% — the x^{2 lam - 0.425} floor, per q (cfprune E1 reconfirmed).
  Parseval exact: full-period mean |U~|^2 = fiber energy to all digits (S5).
  PRIME-SAMPLED energy = 1.16..1.58 ~ DIAGONAL (1.29): sampled/fiber-energy
    = 0.108..0.148 (mean 0.123). The off-fiber Kloosterman part cancels 97-101%
    of the within-fiber mass at every q — the D3 anti-correlation is real,
    pointwise in q, and is what any closing proof must produce.
  max_v r_q(v) = 1 at every q: ZERO collisions — the larger-sieve primitive is
    exactly empty (2a confirmed).

BUDGET TABLES. Best obtainable from ANY weight-uniform sieve inequality =
Delta_min/N_P x fiber energy = 1 x Sum_v|m_v|^2 = x^{2 lam - 0.425} (2c);
support lever S_V/q = 1 (Step 3); sample-density lever = 0.85 L (polylog).

eta = 0.05 (top cell P = Q = x^{0.425}, R = x^{0.15}; (W1.1) budget 0.3):

  lam                            0.425   0.4737  0.50    0.55    0.575
  fiber energy (the sieve floor) 0.425   0.5224  0.575   0.675   0.725
  best sieve-class bound         0.425   0.5224  0.575   0.675   0.725
  deficit vs budget 0.3          0.125   0.2224  0.275   0.375   0.425
  larger-sieve gain (exponent)   0.000   0.000   0.000   0.000   0.000
  support lever S_V/q            1       1       1       1       1

eta = 0.02 (cell P = Q = x^{0.47}, A = x^{0.53}, R = x^{0.06}; budget 0.12):

  lam                            0.47    0.50    0.53
  fiber energy floor             0.47    0.53    0.59
  deficit vs budget 0.12         0.35    0.41    0.47

Both tables reproduce W4.5/W4.8, wp15-phaselever Step 5, and wp15-cfprune Step 6
EXACTLY: idea 7 changes no exponent at either eta.

## STEP 5 — VERDICT. [DONE]

### VERDICT: FAILS-[structural, three independent kills, each sufficient:

(K1) EMPTY PRIMITIVE: the larger sieve's only engine is the collision energy
Sum_q Sum_v r_q(v)^2 - N_P N_Q = Sum_{p != p'} #{q ~ Q : q | p - p'} = 0 EXACTLY
(|p - p'| < P <= Q < q; probe: max r_q(v) = 1 at every q). The {pbar_q} system is
perfectly spread over the modulus family: Gallagher degenerates to the injectivity
already consumed at (W4.4)(i), and the only sub-1 restriction density in the
problem is the sample itself (N_P/q ~ 1/(0.85L)): maximal gain polylog L vs power
deficit x^{2 lam - 0.725}.

(K2) TEST-VECTOR FLOOR: every weight-uniform inequality (the entire sieve class:
large/larger/restricted/dispersion-with-|.|, q-averaged or not) has constant
Delta >= N_P (single-fiber test vector m = delta_{v_0}), and even the PERFECT
constant Delta = N_P lands on Sum_v |m_v|^2 = x^{2 lam - 0.425} — the fiber energy
is over budget BEFORE any sampling loss. (D3-INEQ) needs the sampled energy BELOW
the fiber diagonal, i.e. a NEGATIVE main term -(1 - o(1)) Sum|m_v|^2 from the
off-fiber Kloosterman bilinear form Sum_{w != 0} Ghat(w) K_q(w): upper-bound
technology cannot produce a negative main term. Third instance of the program's
mean-wall theorem (phaselever: positive core; cfprune: CF-blind lattice mean;
here: sieve-blind fiber energy).

(K3) NO SUPPORT LEVER: the fibers are MANY, not few — occupancy #T_lin/q =
x^{2 lam - 0.575} >= x^{0.275} >> 1, support S_V = q(1 - o(1)) (probe: 0.9996).
The macro-cluster does NOT compress the v-support (it lives in the q-free pair
family / within-fiber differences); it acts WITHIN fibers, making m_v phase-flat
and hence POSITIVE — the macro-cluster is the reason the fiber energy is
irreducible, the exact inversion of what a restriction sieve needs.

Plus the species exit (2d): second-moments-over-q of the SAMPLED energy carry
pbar_q inside e(./q) — the (W4.2) multiply-by-q trick fails when the denominator
IS q; "Kloosterman not needed" is false at exactly that line.

POSITIVE DELIVERABLES: (D1) the exact fiber form of the D3 wall: v_t - v_{t'} =
w0 mbar_q (mod q), so the j = 0 coincidence graph = the within-fiber pair set
∪_v F_v x F_v, and the W4.6 floor = the fiber energy Sum_v |m_v|^2, per q,
q-stable (probe). (D2) The needed input, sharpened from D3's "equidistribution"
to a precise signed asymptotic with its truth verified numerically per q:

    (D3-INEQ*)  Sum_{w != 0 mod q} Ghat_q(w) K_q(w)
                = - [ Sum_v |m_v|^2 - Sum_t |chat_t|^2 ] (1 + o(1))
                  for a.e. q ~ Q
    (Ghat = autocorrelation of fiber masses, K_q(w) = E_p e(w pbar_q/q)):

the incomplete-Kloosterman-over-primes sums must anti-correlate with the fiber
autocorrelation at strength 1 - o(1) (measured: 0.97-1.01 at all 8 toy q's).
This is an EVALUATION (Kuznetsov/spectral or dispersion-with-signs species —
W4.8's external rider, unchanged), not a bound; no inequality uniform over
nonnegative fiber masses is even of the right shape. (D3) Exact larger-sieve
non-applicability certificate for the ledger: collision count over the q-family
is identically zero at P <= Q — any future sieve-flavored idea must first exhibit
a nonempty collision/restriction primitive, which requires moduli q < P (outside
the cell geometry) or multi-prime moduli (outside the family).]

Wall stands. Deficit x^{2 lam - 0.725} (eta = 0.05) / x^{2 lam - 0.59}-line
(eta = 0.02) unchanged. Honesty over closure: idea 7 is structurally the wrong
tool species for a sign-definite mean; the D3 localization survives intact and
is now stated as the single signed asymptotic (D3-INEQ*).

## Log

- Created file. Read wp15-cfprune.md (D3, F1, alpha* structure), wp15-phaselever.md
  (P1.2 nonneg weights, macro-cluster P3.2), wp11-e3lb.md §4.7.4 (W4.0-W4.8, W4.2),
  manuscript/sections/05-deep-large-sieve.tex (thm:dls fiber/energy pattern,
  prop:fiber, prop:energy, cor:ap), main.tex (spine).
- Step 1: fibers F_v = {t : h ellbar_q ≡ v}, masses m_v = Sum chat_t; identity
  v_t - v_{t'} = w0 mbar_q (mod q) => j = 0 coincidences = within-fiber pairs;
  fiber energy = diag + x^{2 lam - 0.425}, q-stable; (D3-INEQ) stated; its truth
  requires the off-fiber Kloosterman form to be NEGATIVE at (1 - o(1)) strength.
- Step 2: (2a) collision energy over q-family = N_P N_Q + 0 exactly (q > P):
  Gallagher degenerate; (2b) energy form = (W4.4) chain or worse (Cauchy loses
  L^{1/2}); (2c) test-vector kill: Delta >= N_P, perfect Delta still pays fiber
  energy — entire weight-uniform class floored at x^{2 lam - 0.425}; (2d) second
  moments over q of sampled energy carry pbar_q inside e(./q): not (W4.2)-species,
  Kloosterman IS needed; (2e) level-set/incidence variant conserves the mean at
  every level T; Gallagher bounds persistent-p sets, not incidences.
- Step 3: v-support = unit-dilates of intervals, occupancy #T_lin/q =
  x^{2 lam - 0.575} >= x^{0.275} >> 1: S_V = q(1 - o(1)); hybrid gain = 1 exactly;
  macro-cluster compresses within-fiber differences (makes m_v positive, adverse),
  not fiber positions. Premise "v-support ~ R-sized" FALSE.
- Step 4: probe wp15_largersieve_probe.py (8 primes q, exact m_v, FFT period):
  S_V/q = 0.9996; fibE 10.6 (diag 1.29 + 9.3), q-stable 1%; Parseval exact;
  sampled energy 1.16-1.58 ~ diag, sampled/fibE = 0.108-0.148; max r_q(v) = 1.
  Budget tables = W4.5/W4.8 verbatim; gain exponent 0.000 at both eta.
- Step 5: VERDICT FAILS-[structural: K1 empty collision primitive, K2 test-vector
  floor (sieve-blind fiber energy = third instance of the mean-wall theorem),
  K3 support lever absent]. Deliverables D1 (fiber form of the wall), D2
  ((D3-INEQ*), measured 0.97-1.01), D3 (non-applicability certificate: any sieve
  idea needs moduli < P or multi-prime moduli). File complete.
