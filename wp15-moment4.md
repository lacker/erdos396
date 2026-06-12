# WP15: Cheap reformulation check — 4th moment in place of the variance at the (b3)/Chebyshev layer

STATUS: EXECUTED (this session), verdict MOMENT4-NEUTRAL (§5).
Question: does replacing E|D_Lambda|^2
(target (W1.1) = 20 delta_0 (eta R)^2 L^{-2}, wp11-e3lb §4.7.1) by
E|D_Lambda|^4 change the W4.6 budget favorably? Top cell P = Q = x^{0.425},
A = x^{0.575}, R = x^{0.15}, eta = 0.05, L = log x, J <= 0.22 L dyadic
blocks Lambda = 2^j Q in [Q, A]; lam := log_x Lambda in [0.425, 0.575].

## 1. The 4th-moment Chebyshev requirement (M4.1)

What §3.4(2)'s (b3)-absorption consumes (wp11-e3lb §4.7.1, verbatim
layer): outside a (p,q)-set of probability <= delta_0,
N_hard <= C eta R, C absolute. From W1's exact decomposition
N_hard = M + Sum_Lambda D_Lambda + O(1), Selberg majorant
D_Lambda <= D^+_Lambda + delta^+_Lambda, Sum_Lambda delta^+ <=
12.1 eta(R+1), it suffices that P_{p,q}(Sum_Lambda D^+_Lambda > eta R)
<= delta_0. At the 2nd level this was (W1.1) via Cauchy-Schwarz over
the J <= 0.22 L blocks + Chebyshev. The 4th-level replacement, exact:

MARKOV ON |D|^4 WITH THE DYADIC UNION FOLDED IN by the power mean
|Sum_{j<=J} a_j|^4 <= J^3 Sum_j |a_j|^4 (Holder, exact):

    P_{p,q}( Sum_Lambda D^+_Lambda > eta R )
      <= (eta R)^{-4} E |Sum_Lambda D^+_Lambda|^4
      <= (eta R)^{-4} J^3 Sum_Lambda E |D^+_Lambda|^4
      <= (0.22 L)^4 (eta R)^{-4} max_Lambda E |D^+_Lambda|^4.

So it SUFFICES, for every dyadic block and the majorant sign:

    E_{p,q} |D^+_Lambda|^4  <=  400 delta_0 (eta R)^4 L^{-4},   (M4.1)

since (0.22)^4 x 400 = 0.937: probability <= 0.94 delta_0 <= delta_0
— the SAME delta_0-exceptional-set conclusion, C = 20 unchanged
(N_hard <= M + 12.1 eta(R+1) + eta R + O(1) <= 20 eta R off the bad
set; bad set pays <= 2 delta_0 (R+1) as in W1). First-moment form
also survives: E N_hard <= 18.2 eta(R+1)
+ Sum_Lambda (E|D^+_Lambda|^4)^{1/4} + O(1) <= 18.2 eta(R+1)
+ 0.22 L (400 delta_0)^{1/4} eta R / L <= 20 eta R ((400 delta_0)^{1/4}
<= 4.5). [Alternative union: per-block threshold eta R/J + union bound
needs E|D|^4 <= delta_0 (eta R)^4 J^{-5} — one J worse; (M4.1) via the
power mean is the right form, as (W1.1) was via CS.]

BUDGET ARITHMETIC. (M4.1)'s right side = x^{0.6 - o(1)} (delta_0
polylog) vs (W1.1)'s x^{0.3 - o(1)}: the budget exponent DOUBLES —
the 4th moment buys an extra (eta R)^2 = x^{0.3} of budget. The whole
question: do the 4-tuple coincidence masses grow by more or less than
x^{0.3} over their 2-tuple counterparts. Floors: E|D^+|^4 >=
(E|D^+|^2)^2 >= (diagonal truth)^2 = x^{0.3 - o(1)}, so (M4.1) is not
floor-blocked, with room x^{0.3 - o(1)} — DOUBLE the 2nd level's
x^{0.15} of diagonal room. So far favorable; the off-diagonal classes
decide (§2).

## 2. The 4-tuple expansion of E_{p,q}|D|^4 — class-by-class

Work at the linear level of (W4.0)(b) (no flip, no smooth factor, no
a_0-truncation, none exists here): D^pm_Lambda = Sum_{t in T_lin}
c_t e(a_0 theta_t(q)), c_t := chat^pm_h(ell), theta_t(q) =
-h qbar_ell/ell, #T_lin <= 4.8 Lambda^2/((R+1)L). Masses (W1/W3.4):
||c||_1 <= m_1 N_Lambda <= 9.84 Lambda/L; ||c||_2^2 <= 16.8 (R+1)/L;
sup_t |c_t| <= 2(R+1)/Lambda. The positivity step (W4.4)(i) applies
VERBATIM to the 4th power (|.|^4 >= 0 pointwise in a; cost 0.85 L):

  E_{p,q}|D^pm_Lambda|^4 <= 0.85 L E_q Sum_{t1,t2,t3,t4}
      c_{t1} c_{t2} conj(c_{t3} c_{t4}) F_q(Theta),
  Theta := theta_{t1} + theta_{t2} - theta_{t3} - theta_{t4},
  |F_q(Theta)| <= min(1, 1/(2 q ||Theta||)).

CRT-combination (W2(ii), iterated): with m := product of the DISTINCT
ells of the tuple, Theta == -w qbar_m / m (mod 1), w = w(t1..t4) the
integer Sum_i eps_i h_i (m/ell_i) with within-ell h-sums collapsed;
|w| <= 8m/(R+1) + 4m/Lambda < m/2. Tuples classify by (w = 0?) and
the ell-pattern (4 slots): (1,1,1,1), (2,1,1), (2,2), (3,1), (4).

CLASS A — FULL DIAGONAL (w = 0, F_q == 1 identically in q; "pairs of
pairs"). Any singleton ell forces w != 0 (w == eps_i h_i (m/ell_i)
!= 0 mod ell_i), so resonance requires pattern (2,2) or (4) with all
within-ell numerators = 0 mod ell, hence = 0 exactly (|sums| <
2H_ell or 4H_ell < ell): Class A = the three perfect pairings
({t3,t4} = {t1,t2}, or both z^2-pairs internally cancelling t2 = -t1,
t4 = -t3) + the same-ell-quadruple zero-sums h1+h2-h3-h4 = 0:

  mass(A) <= 3 ||c||_2^4 + N_Lambda m_1^3 sup|c_t|
          <= 3 (16.8(R+1)/L)^2 + 331 (R+1)/L  <=  850 (R+1)^2/L^2.

Contribution <= 0.85 L x 850 (R+1)^2/L^2 = x^{0.3 + o(1)} vs budget
x^{0.6 - o(1)}: CLOSED, room x^{0.3 - o(1)}, every block. [2nd level:
diagonal x^{0.15} vs x^{0.3}, room x^{0.15}. The resonant class is
exactly self-squaring — variance^2 against budget^2 — so its room
DOUBLES in exponent. Favorable, but it was never the binding class.]

CLASS B — THE 2+2 COINCIDENCES (non-resonant, <= 2 distinct ells:
patterns (2,2) and (3,1)). Theta == -(alpha qbar_ell/ell +
beta qbar_ell'/ell'), (alpha, beta) != (0,0), |alpha| <= 2 or 3 H_ell:
EXACTLY the (W4.2) cross-case frequency-pair object with (h, -h') ->
(alpha, beta); w = alpha ell' + beta ell != 0, |w| <= 18 Lambda^2/R
< m/2, |n_j| <= (2^k + 2) m < Q^4. LEMMA (W4.2) and (W4.3) apply
VERBATIM (the proof used only w != 0, |w| < m/2, m <= 4 Lambda^2):
per-tuple kernel q-average <= c_8 L^2/Q, c_8 = 4.4. ANSWER to the
prompt's question: YES — these are already controlled by the PROVED
per-pair machinery; note it is the W4.2/W4.3 fiber count (the proved
x^{-0.425+o(1)}-per-pair replacement that §4.7 built AFTER V1-V3)
that does it, not §4.6's V1-V3 citation chain itself (V3's per-h
x^{-0.0245} would be far too weak here, as it was at the 2nd level).
Mass: each repeated ell carries TWO independent h-slots at cost
(Sum_h |c_h(ell)|)^2 <= m_1^2 = O(1) — the second pair rides on the
SAME ells, no new ell-sum:

  mass(B) <= 3 (m_1^2 N_Lambda)^2 [(2,2)] + 4 m_1^4 N_Lambda^2 [(3,1)]
          <= 7 m_1^4 N_Lambda^2 <= 1.2e4 Lambda^2/L^2,
  contribution <= 0.85 L x 1.2e4 Lambda^2/L^2 x 4.4 L^2/Q
               <= 4.5e4 L Lambda^2/Q = x^{2 lam - 0.425 + o(1)}.

KEY FACT: same exponent as (W4.4)'s 2nd-moment cross term — NOT its
square (variance^2-TYPE in structure, variance^1 in mass). Against
the doubled budget x^{0.6}: Class B CLOSES iff lam <= 0.5125 — the
lower blocks Lambda <= x^{0.5125}, where the identical species failed
on EVERY block at the 2nd level; top blocks miss by <= x^{0.125}.
A real (if partial) gain on this class.

CLASS C-3 — pattern (2,1,1), 3 distinct ells (the trichotomy hides
it; priced for honesty). mass <= 6 m_1^4 N_Lambda^3 <= 2.4e4
Lambda^3/L^3; m ~ Lambda^3, w != 0 via either singleton, |n_j| <=
(2^k+2) 8 Lambda^3 <= x^{2.15+o(1)} < Q^6: <= 5 prime divisors q ~ Q,
fiber <= 2^{k+5}, kernel average <= 2 c_8 L^2/Q. Contribution <=
0.85 L x 2.4e4 Lambda^3/L^3 x 8.8 L^2/Q <= 1.8e5 Lambda^3/Q =
x^{3 lam - 0.425 + o(1)} in [x^{0.85}, x^{1.3}] vs x^{0.6}: FAILS on
every block by x^{3 lam - 1.025} in [x^{0.25}, x^{0.7}].

CLASS C-4 — THE GENUINELY 4-LINKED CLUSTER (4 distinct ells; the only
new object of the reformulation). m = ell1 ell2 ell3 ell4 in
[Lambda^4, 16 Lambda^4] <= x^{2.3+o(1)}; w != 0 (nonzero mod each
ell_i), |w| < m/2. The fiber lemma GENERALIZES at trivial cost:
|n_j| = |jm - w| <= (2^k + 2) m <= x^{2.725 + o(1)} < Q^7 = x^{2.975}
: <= 6 prime divisors q ~ Q per j, fiber count <= 6(2(2^k+1)+1) <=
2^{k+5}, per-tuple kernel q-average <= 2 c_8 L^2/Q = 8.8 L^2/Q =
x^{-0.425+o(1)} — the SAME single factor of 1/Q as for pairs: the
four frequencies CRT-collapse to ONE frequency w/m, one scalar
coincidence condition q | jm - w; linkage arity does NOT multiply
constraints. Trivial (absolute) bound on the class:

  contribution(C-4) <= 0.85 L ||c||_1^4 x 8.8 L^2/Q
    <= 7.1e4 Lambda^4/(L Q) = x^{4 lam - 0.425 - o(1)}
    in [x^{1.275}, x^{1.875}]   vs budget x^{0.6}:
  DEFICIT x^{4 lam - 1.025} in [x^{0.675}, x^{1.275}],

vs the 2nd level's binding deficit x^{2 lam - 0.725} in [x^{0.125},
x^{0.425}]: WORSE by exactly x^{2 lam - 0.3} = x^{0.55}..x^{0.85}.
Mechanism: the tuple mass squares (||c||_1^2 -> ||c||_1^4: factor
x^{2 lam - o(1)}), the budget gains only (eta R)^2 = x^{0.3}, and the
kernel still pays only one 1/Q. 2 lam > 0.3 on every block.

THE SUP-CAPPED CHAIN (the cheap upper road — 4th moment can never be
WORSE than neutral). Pointwise |D^pm_Lambda| <= Sum_ell |y^pm_ell| <=
7(R+1)L (W1's (a)+(W1.3), proved), so with (W4.4) [proved]:

  E|D^pm_Lambda|^4 <= (7(R+1)L)^2 E|D^pm_Lambda|^2
    <= 49 (R+1)^2 L^2 [14.3(R+1) + 152 Lambda L^2/Q + 363 L Lambda^2/Q]
    =  x^{0.45+o(1)} + x^{lam - 0.125 + o(1)} + x^{2 lam - 0.125 + o(1)};

first two terms close (<= x^{0.45} <= x^{0.6}); the cross term vs
x^{0.6} gives DEFICIT x^{2 lam - 0.725} — numerically IDENTICAL to
(W4.8). The sup-cap (7(R+1)L)^2 = x^{0.3+o(1)} eats exactly the extra
budget (eta R)^2 = x^{0.3}: the 4th-moment demand factors through the
2nd-moment demand with NO contraction and NO loss. Best 4th-level
chain = min(direct: 4 lam - 1.025, sup-capped: 2 lam - 0.725) =
2 lam - 0.725 on every block, achieved only by factoring THROUGH the
variance — the remaining estimate is literally (W4.6), unchanged
(both sides of its demand multiplied by (eta R)^2).

## 3. Random-model room at the 4th level (Monte Carlo)

wp15_moment4_probe.py (.venv python, this session; x = 1e8 model:
Q = P = 2512, R = 16, A = 39811, L = 18.42; 2000 (p,q)-samples,
sharp window; blocks Lambda = Q, 4Q, A/2; wp11_w4_probe conventions).

M1 (4th-moment truth): kappa := E D^4 / (3 (E D^2)^2):

  block:                Q      4Q     A/2
  arith E D^2:          1.414  0.921  0.711
  arith E D^4:          7.39   2.58   1.18    (s.e. 0.95/0.27/0.08)
  arith kappa:          1.23   1.01   0.78
  random-model kappa:   1.24   1.12   1.26   (Bernoulli pred D4 = 7.56/5.69/5.11)

E D^4 ~ 3 (E D^2)^2-grade on every block, Gaussian-like, NO heavy
tail; the arithmetic 4th moment sits AT or BELOW the random model
(0.78 at A/2 — same sub-random signature as W4.7 E1's variance
ratios 0.73/0.82). So (M4.1) is TRUE in the random model: truth
~ 3 V^2 = x^{0.3 - o(1)} vs budget x^{0.6 - o(1)}.

ROOM COMPARISON (the question asked): room at 4th level =
x^{0.6 - 0.3} = x^{0.3}, vs 2nd level x^{0.3 - 0.15} = x^{0.15}:
the room is LARGER — it doubles in exponent (truth squares, budget
squares, and truth < budget squares the ratio). The reformulated
target is even less floor-blocked than (W1.1). The obstruction was
never the truth of the target; it is provability, and that worsens
(§2, §4).

M2 (the arity question, measured): per-tuple kernel q-average
E_q min(1, 1/(2q||Theta_q||)), 800 random tuples each, block Q:

  2-linked pairs:    mean 0.00250, max 0.00889  (bound c_8 L^2/Q = 0.594)
  4-linked clusters: mean 0.00250, max 0.00808  (bound 2c_8 L^2/Q = 1.189)
  ratio 4/2 = 0.999;  1/Q reference 6/Q = 0.00239.

The 4-linked coincidence measure is NUMERICALLY IDENTICAL to the
2-linked one (both ~ 6/Q, L^0-grade truth, as W4.7 E3 found for
pairs): linkage arity buys ZERO extra constraints — the CRT collapse
of §2 (four frequencies -> one frequency w/m, one fiber condition
q | jm - w) is the truth, not an artifact of the divisor bound.

## 4. The 4-linked class vs the 2-linked: relative mass and the deficit map

ANSWER TO THE KEY QUESTION: NO — the genuinely-4-linked class does
NOT have smaller relative mass. Per tuple, a coincidence
||Theta_q|| < 1/q is ONE scalar constraint regardless of arity (the
four phases CRT-collapse to a single frequency w/m; §2 C-4, measured
in §3 M2 at ratio 0.999): relative coincidence measure 1/Q-grade,
SAME as for pairs — the hoped-for "more constraints per tuple" does
not exist. Meanwhile the tuple mass SQUARES (||c||_1^2 -> ||c||_1^4,
factor x^{2 lam}) and the budget gains only (eta R)^2 = x^{0.3}:

  deficit map (native chains):  2 lam - 0.725  -->  4 lam - 1.025
                              = (2 lam - 0.725) + (2 lam - 0.3),

i.e. the deficit WORSENS by x^{2 lam - 0.3} = x^{0.55}..x^{0.85} on
the native 4-fold absolute chain. Through the sup-capped chain (§2)
it stays EXACTLY self-similar: deficit x^{2 lam - 0.725}, unchanged —
the (W4.6) self-similarity one level up. Moment-raising is a third
member of the non-contracting family: square-opening, completion +
fiber-counting, and now moment-raising all map the gap to itself or
worse; per extra power of |D| the budget gains x^{0.15} (one eta R)
while the new coincidence mass gains x^{lam} >= x^{0.425}. Higher
moments (6th, 8th, ...) only widen this: the moment hierarchy points
the WRONG way for absolute-value chains, and is exactly neutral for
sup-capped ones.

## 5. Verdict

VERDICT: MOMENT4-NEUTRAL-[best 4th-level chain = sup-cap
(7(R+1)L)^2 x (W4.4), deficit x^{2 lam - 0.725} IDENTICAL to W4.8,
remaining estimate literally (W4.6) unchanged; the native 4-linked
route is strictly HARDER than W4.6: it would need signed cancellation
x^{4 lam - 1.025 + eps} on the 4-linked coincidence graph vs (W4.6)'s
x^{2 lam - 0.725 + eps}, with the same single-1/Q coincidence
structure and m ~ Lambda^4 conductors even further from any pinned
citation]. The reformulation does NOT change the W4.6 budget
favorably. Honest gains, for the record: (M4.1) is sound with
doubled room x^{0.3} (§1, §3); Class A room doubles; Class B (2+2)
closes on blocks lam <= 0.5125 where the 2nd-level cross term failed
everywhere — but the binding class is the new 4-linked one, and it
more than consumes the gain.

EXPONENT TABLE (top cell, eta = 0.05; lam in [0.425, 0.575];
2nd-level budget 0.3, 4th-level budget 0.6; all + o(1)):

  | level | class / chain               | exponent       | deficit vs budget        |
  |---|---|---|---|
  | 2nd   | diagonal (W4.4)             | 0.15           | closed, room 0.15        |
  | 2nd   | cross term (W4.4, binding)  | 2 lam - 0.425  | 2 lam - 0.725: 0.125..0.425 |
  | 4th   | Class A (pairs of pairs)    | 0.30           | closed, room 0.30        |
  | 4th   | Class B (2+2, W4.2 verbatim)| 2 lam - 0.425  | closes iff lam <= 0.5125; else <= 0.125 |
  | 4th   | Class C-3 ((2,1,1))         | 3 lam - 0.425  | 3 lam - 1.025: 0.25..0.7 |
  | 4th   | Class C-4 (4-linked, trivial)| 4 lam - 0.425 | 4 lam - 1.025: 0.675..1.275 |
  | 4th   | sup-cap x (W4.4) [BEST]     | 2 lam - 0.125  | 2 lam - 0.725: 0.125..0.425 |

(eta = 0.02, lam in [0.47, 0.53], budgets 0.12/0.24: sup-cap deficit
2 lam - 0.59 = 0.35..0.47, identical to W4.8; native C-4 deficit
4 lam - 0.71 = 1.17..1.41. Same verdict.)

STATUS: EXECUTED, negative-neutral. Deliverables: (M4.1) the correct
4th-moment target with the dyadic union (power-mean J^3, constant
400); the five-class pricing of E|D|^4 with the fiber lemma extended
to arity 3, 4 (constants 2^{k+5}, kernel 2 c_8 L^2/Q, proved,
divisor-counting only); the arity-invariance of the coincidence
measure (proved + measured at 0.999); the sup-cap neutrality
identity. No change to the program frontier: (W4.6) remains the one
estimate, exactly as stated in wp11-e3lb §4.7.4.
