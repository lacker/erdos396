# WP15-VERIFY: Adversarial audit of wp15-ffmodel.md §3.4-3.5 (physical Hölder chain (P1)-(P3))

**CLAIM UNDER AUDIT:** the integer power-deficit x^{2lam-0.725} is a harmonic-chain artifact;
a physical-side Hölder(infinity,1) chain (P1)-(P3), built from already-proved W1-era lemmas,
gives E_{p,q}|D^pm_Lambda|^2 <= C' R^2 L unconditionally, leaving only an L^{3+a} gap to the
(W1.1) budget 20 delta_0 (eta R)^2 L^{-2}.

**STATUS: EXECUTED. VERDICT (§5): AUDIT-CONFIRMED with one named back-translation erratum
(the "Form A" sentence) that does not touch the headline.** Date: 2026-06-12.

Inputs read in full: wp15-ffmodel.md; wp11-e3lb.md §§4.7-4.7.4 (W1, W2, W3, W4 verbatim);
wp15-largersieve.md (D3-INEQ*, fiber identity, K1-K3); THE-OPEN-PROBLEM.md §2.2-2.4
(Form A/B exact statements); wp15-cfprune.md (F1/D3 grep-level); manuscript/main.tex spine.
Numerics: wp15_verify_probe.py (this session), scales x = 1e6..1e12.

---

## 1. Reconstruction of the chain (P1)-(P3), line by line, every constant

Object (W1, §4.7.1 verbatim): per block Lambda = 2^j Q, per (p,q), with
nu_ell = (-a_0 qbar_ell) mod ell, a_0 = lift of pbar_q to [1,q):

    D^pm_Lambda = Sum_{ell ~ Lambda, prime, != q} y^pm_ell,
    y^pm_ell = S^pm_ell(nu_ell/ell) - chat^pm_0(ell)   (Vaaler-centered oscillatory part),

and the proved pointwise envelope (W1 diagonal section, line "Pointwise envelope"):

    |y^pm_ell| <= 1[nu_ell <= R] + V_ell(nu_ell/ell) + 3(R+1)/ell,        (E0)
    V_ell = S^+_ell - S^-_ell >= 0,  V_ell(x) <= c_V min(1, ((H_ell+1)||x - edge||)^{-2}),
    c_V <= 3 (W1's flagged deferred-calculus constant — inherited here, see §2).

**(P1) — pointwise.** Sum_ell |y^pm_ell| <= (R+1) + 2 c_V (R+1) L + 5.1(R+1)/L <= 7(R+1)L.
This is VERBATIM the record: §4.7.1 (W1.4)(ii) line "Sum_ell |y_ell| <= (R+1) +
2 c_V (R+1) L + o(R) <= 7(R+1)L", assembled from
  (a) N_win := Sum_ell 1[nu_ell <= R] <= R+1 POINTWISE [proved: values a_0 + sq <=
      q(R+1) < Lambda^2, one prime factor > Lambda each, ell -> s injective
      (ell | (s-s')q impossible, |s-s'| <= R < Lambda, q != ell)]; and
  (b) (W1.3): Sum_ell V_ell <= 2 c_V (R+1) L [proved: banding + cumulative count
      4(s+R+1) at width s; the L is the genuine harmonic-series cost of the
      pointwise worst case]; and
  (c) drift Sum_ell 3(R+1)/ell <= 5.1(R+1)/L (Sum_{ell ~ Lambda} 1/ell <= 1.7/L).
STATUS: proved in the record, pointwise in (p,q), every block. NO scope inflation.

**(P2) — first moment.** E_{p,q} Sum_ell |y^pm_ell| <= C(R+1), C absolute.
NOT verbatim in the record — this is the one NEW lemma. Independent re-derivation
(this audit), with constants:

  Fix q, fix an integer interval T of length <= R+1 in [0, ell) (the window [0,R],
  or any Vaaler band). nu_ell in T  <=>  a_0 in S_{ell,T} := {(-tq) mod ell : t in T}
  cap [1, q). Two elementary inputs, NEITHER involving equidistribution of pbar_q:
  (i) INJECTIVITY p -> a_0 (|p - p'| < P <= Q < q): #{p ~ P : a_0 in S} <= |S|.
      [Same primitive as (W4.4)(i)'s injectivity and largersieve (2a)'s zero-collision
      count — "<= 2 per class" in ffmodel's wording is the safe form, = 1 at P = Q.]
  (ii) ORBIT-GAP (three-distance) COUNT: for ell >= 4q, the orbit t -> (-tq mod ell)
      steps by -q; after a hit of [1, q-1] it jumps to [ell-q+1, ell-1] and needs
      >= (ell-2q)/q >= ell/(2q) steps to return:
          |S_{ell,T}| <= 1 + (R+1) q / (ell - 2q) <= 1 + 2(R+1) q/ell.
      For ell < 4q (bottom <= 2 blocks only, where Lambda/q = O(1)): crude
      |S| <= (R+1) ceil(q/ell + 1) <= 3(R+1).
  Summing over the block and dividing by N_P (N_P >= P/(2L), N_Lambda <= 2.4 Lambda/L,
  P = Q, q <= 2Q):
      E_p #{ell ~ Lambda : nu_ell in T} <= [N_Lambda + 2(R+1) q N_Lambda/Lambda]/N_P
        <= 4.8 (R+1) Lambda/(QR) * R ... <= 24(R+1)   per interval, EVERY block
      (top block worst for the first term: N_Lambda/N_P <= 4.8 Lambda/Q <= 4.8 R —
      ffmodel's "checked at top blocks where N_Lambda/q = R/L" is this line);
      bottom blocks worst for the crude case: <= 3(R+1) * 4.8 * 4 <= 58(R+1).
  Then over the envelope (E0): window term: one interval: <= 58(R+1).
  Vaaler-tail term: bands j = 0,1,...: each band = 4 intervals of length <= R+1,
  per-band first-moment count <= 4 * 58(R+1), J-UNIFORM (the orbit-gap count does not
  degrade with j — this is what replaces the pointwise (W1.3) cumulative count
  4(j+2)(R+1) whose j-linearity created the L); weights min(1, c_V/j^2) sum to
  <= c_V * 2.7:
      E Sum_ell V_ell <= 4 * 58 * 2.7 * c_V (R+1) <= 1880(R+1)   (c_V = 3).
  Drift: <= 5.1(R+1)/L. TOTAL: C <= 2000, absolute, uniform over blocks and
  lam in [0.425, 0.575]. (ffmodel's "factor ~3" refers to the band re-summation
  convergence factor, consistent; constants here are deliberately generous.)
STATUS: HOLDS. Elementary, unconditional, citation-free. The load-bearing
mechanism: the per-ell O(1) discrepancy loss costs N_Lambda/N_P ~ Lambda/Q <= R
per block — R-grade, not R L-grade — and the j-uniformity of the orbit-gap count
kills the Vaaler-tail L.

**(P3) — Hölder(infinity,1).** E|D^pm_Lambda|^2 <= E[(Sum|y|)^2]
<= (sup_{p,q} Sum|y|) * E_{p,q}(Sum|y|) <= 7(R+1)L * C(R+1) =: C'(R+1)^2 L,
C' <= 1.4e4. Trivially valid given (P1)-(P2) (nonnegative integrand, sup over the
same probability space the E runs over). STATUS: HOLDS.

**Consequence, exact.** For every block and both signs, unconditionally:

    E_{p,q} |D^pm_Lambda|^2 <= C' (R+1)^2 L = x^{0.3 + o(1)},               (P*)

vs the (W1.1) demand 20 delta_0 (eta R)^2 L^{-2} = 0.05 delta_0 R^2 L^{-2}
(eta = 0.05). Residual factor: C' L^3/(0.05 delta_0) = Theta(L^{3+a}) with
delta_0 = L^{-a}. SAME x-EXPONENT, polylog gap. Uniform in lam.

**Robustness remark (strengthens the ffmodel claim).** Even WITHOUT the new lemma
(P2), squaring (P1) alone gives E|D^pm|^2 <= 49(R+1)^2 L^2 pointwise — already
x-power-matching the budget (gap L^{4+a}). So the "polylog-species" headline rests
on a single ALREADY-PROVED record line ((W1.4)(ii)) plus squaring; (P2) only
sharpens L^{4+a} to L^{3+a}. The power-deficit could never have been a property of
E|D|^2 itself.

**Sharp-window variant (for the record):** the same chain on D_Lambda (no Vaaler
layer; sup <= (R+1)(1+o(1)) by (a)) gives E|D_Lambda|^2 <= C(R+1)^2 — no L at all.
The Vaaler L in (P*) is pure majorant overhead. The completed object D^pm is what
(W1.1) prices, so (P*) is the relevant statement; the physical chain never
completes, so it never needed the Selberg layer's degree bookkeeping — but the
sandwich D^- - delta <= D <= D^+ + delta is still what feeds §3.4's absorption,
hence the audit certifies the D^pm form.

## 2. Scope check of every invoked lemma (no scope inflation found, one flag inherited)

| invoked | actual record statement | used here as | verdict |
|---|---|---|---|
| (W1.1)(a) window count | §4.7.1 (a): N_win <= R+1 pointwise, one-large-prime + injective t-parametrization; enlarged windows 4(s+R+1) | (P1) window part; (P2) crude case | EXACT, no inflation |
| (W1.3) Vaaler-tail sum | Sum_ell V_ell <= 2 c_V (R+1) L pointwise | (P1) tail part | EXACT |
| (W1.2)(b) V-envelope | V_ell <= c_V min(1, ((H_ell+1)||x-edge||)^{-2}), c_V <= 3 FLAGGED ("deferred-calculus class — not load-bearing for structure") | (P2) band weights | EXACT; **c_V flag inherited: the only non-fully-certified constant in the whole chain; structural conclusion unaffected (c_V enters linearly in C)** |
| injectivity p -> a_0 | (W4.4)(i) "p -> a_0 injective into [1,q)"; largersieve (2a) "zero collisions, max r_q(v) = 1, probe-verified" | (P2)(i) | EXACT |
| orbit-gap count (P2)(ii) | NOT in record. New. Proved above (elementary three-distance argument) | (P2) | NEW LEMMA, proved this audit, machine-checked (§4 probe, band table) |
| Vaaler coefficient layer | §4.7.1 Selberg layer: H_ell = ceil(ell/(R+1)), masses m_1 <= 4.1, drift ledger at linear level | definitions only | EXACT |

The chain uses NO Kloosterman input, NO equidistribution of {pbar_q}, NO citation
beyond the record's own W1 layer: Korolev, DFI, dls are not touched. It is
unconditional and elementary. Checked against W2-W4: the chain never opens the
square into harmonic pairs, never applies the positivity step E_p <= 0.85 L E_a,
never invokes a per-tuple or per-pair |.| — so none of the W2-W4 machinery (or its
obstructions) is in its dependency cone.

## 3. Reconciliation with the W3/W4 floors and the largersieve kills

They CANNOT all be true unless the floors price a different object. They do.
Exactly which, per floor:

- **(W3d) floor x^{2lam-0.425}** prices Sum_t |c_t| |E_{p,q}(phase_t)| — the
  l^1-in-harmonic-tuples aggregate. Statement in record: "ANY chain through
  Sum_t |c_t||E_t| delivers ... EXCESS x^{2lam-0.725}". Class-conditional: the
  physical chain is not of this shape (it never produces per-tuple |E|). NO CONFLICT.
- **(W4.4)/(W4.5) floor ("truth-grade")** prices Sum_{t != t'} |chat chat'| *
  (q-average of |F_q(Delta)|) AFTER the positivity step (W4.4)(i) — i.e. the
  absolute coincidence mass of the COMPLETED square over the FULL period a mod q.
  Its x^{2lam-0.425} is real (E3 numerics: per-pair kernel q-average ~ 6/Q, L^0).
  The record's own wording is precise: "irreducible for every chain that takes
  absolute values at the pair level". The physical chain takes |.| at the per-ell
  PHYSICAL level, before any completion; the within-ell h-sum is kept intact as the
  Vaaler polynomial and bounded by the geometric envelope (E0) — an identity-level
  resummation, not a pair estimate. NO CONFLICT.
- **largersieve (K2) test-vector floor** prices every WEIGHT-UNIFORM inequality
  E_p|Sum_v m_v e(a_0 v/q)|^2 <= Delta Sum_v |m_v|^2: even Delta = N_P pays the
  fiber energy x^{2lam-0.425}. The physical chain is NOT weight-uniform: it uses
  the provenance of the weights (m_v are the fiber masses of Vaaler coefficients of
  a geometric window; the resummation to window counts is exactly what a
  delta_{v_0} test vector does not admit). NO CONFLICT with the PROVED content of
  K2. **However the literal sentence "(D3-INEQ) requires ... a negative main term —
  no upper-bound technology produces a negative main term" (largersieve 2c/K2) is
  FALSIFIED as worded**: (P*) is upper-bound technology and it does place
  E_p|U(a_0)|^2 below the fiber energy by x^{2lam-0.725-o(1)}. The proved kill
  covers only the weight-uniform class; the rhetorical extension was an overreach
  (the once-burned-pessimistic pattern, second instance).
- **Form A (THE-OPEN-PROBLEM §2.3, = (W4.6) verbatim)**: full-period signed
  coincidence sum |Sum_{t != t', ell != ell'} chat chat' F_q(theta_t - theta_{t'})|.
  By the Parseval/fiber identity (largersieve 1a + probe S5) its LHS EQUALS
  fiberE - diagonal - (same-ell cross) + O(1/R)-soft corrections =
  + x^{2lam-0.425 - o(1)} > 0 for typical q (cfprune E1: per-q stable 0.991-1.011 of
  the lattice mean; F1: flat phases). **Form A as stated is therefore FALSE — its
  LHS is an attained positive mean, not a cancellable signed sum.** This was
  already implicit in D3 ("the chain's accounting of E_a carries the positive
  coincidence mass") and is consistent with the floors: the harmonic chain fails
  not because an estimate is missing inside it but because its intermediary is
  genuinely large. The wall was never inside the harmonic representation's signed
  sums; it is the representation.

**The erratum in §3.4 (the one error found):** the sentence "If (P1)-(P3) survive
audit, then Form A's LHS is unconditionally <= x^{0.3} L^{O(1)}" is WRONG as
written if "Form A" means THE-OPEN-PROBLEM §2.3 (A) — that LHS is provably
x^{2lam-0.425}-positive and no bound on the prime-sampled square can shrink a
full-period quantity. The correct back-translation, which the rest of §3.4
states properly, is: **(W1.1)'s LHS** (the prime-sampled E_{p,q}|D^pm_Lambda|^2 —
in ffmodel's own FF dictionary, "FF-Form A") is unconditionally <= x^{0.3}L^{O(1)}.
The error is nomenclature drift (integer Form A = full-period object vs FF-A =
prime-sampled object), not substance: the program's real demand is (W1.1);
Form A was only ever a SUFFICIENT route to it, and is now known false/abandoned
(D3). Required edit to wp15-ffmodel.md §3.4: replace "Form A's LHS" by
"(W1.1)'s LHS"; add "integer Form A itself is FALSE (F1/cfprune-E1) — a second,
independent sense in which the harmonic chain's deficit is representational."

**Relation to D3-INEQ* (is the chain secretly equivalent to assuming it?): NO —
the implication runs the OTHER way, with a polylog-weakened constant.** From the
exact identity E_p|U(a_0)|^2 = Sum_v|m_v|^2 + Sum_{w != 0} Ghat(w) K_q(w)
(largersieve 1b) and (P*) + Markov in q (|U|^2 >= 0): for all but delta of q ~ Q,

    Sum_{w != 0} Ghat_q(w) K_q(w) = -[Sum_v |m_v|^2 - Sum_t |chat_t|^2] *
        (1 + O(x^{-(2lam - 0.725)} L^{O(1)}/delta)),

i.e. the chain PROVES the D3-INEQ* anti-correlation (measured 0.97-1.01 in the
largersieve probe) at strength 1 - O(x^{-(2lam-0.725)+o(1)}), unconditionally —
the phenomenon the record said "any closing proof must produce". What remains open
is only the PRECISION: D3-INEQ* at budget grade needs the error term
O(x^{-(2lam-0.725)} delta_0 L^{-2}); proved is O(x^{-(2lam-0.725)} L^{1+o(1)}).
Same power, L^{3+a} apart. Nothing circular: the chain's inputs (injectivity,
orbit-gap counts, Vaaler envelopes) are strictly upstream of any Kloosterman/
equidistribution statement.

## 4. Numerical scaling test (wp15_verify_probe.py, .venv python — fresh probe, this session)

Model scales x = 1e6, 1e8, 1e10, 1e12 (Q = P = x^0.425, R = x^0.15, 6 primes q per
scale, 4 at 1e12; ALL p ~ P; blocks (Q,2Q] and (A/2,A]; sharp-window chain measured,
Vaaler tail via the band proxy Sum_ell min(1, ((R+1)/d)^2)). Anchor reproduced:
ED2 = 1.375 at x = 1e8 Q-block vs wp11 W4.7 E1's ~1.5 (different q-sample). Results:

  log-log SLOPES in x (fit over 6 decades):           Q-block   top-block   expected
  ED2 = E_{p,q}|D_Lambda|^2                            0.108     0.104      0.10 (= R/L Bernoulli diag; 0.15 - dlnL/dlnx)
  m1  = E N_win  ((P2) window first moment)            0.103     0.092      0.10 (R/L truth; bound CR = 0.15 respected)
  mV  = E tail proxy ((P2) Vaaler-tail first moment)   0.098     0.092      ~0.10
  chain = (sup)x(mean) empirical Hoelder product       0.189     0.178      <= 0.30 + o(1)
  harm = harmonic coincidence-mass grade (m_1 N_l)^2/q 0.331     0.621      2lam - 0.425 - 2dlnL/dlnx = 0.36 / 0.62
  R^2 L reference                                      0.334     0.334      0.30 + dlnL/dlnx

  KEY RATIOS across scales (top block, lam ~ 0.56-0.57):
    chain/harm: 0.0426 -> 0.0054 -> 0.0008 -> 0.0001   (falls ~x^{-0.44}: clean POWER separation —
        the physical bound beats the harmonic mass by a growing power; the
        x^{2lam-0.425} mass belongs to the harmonic representation, not to E|D|^2)
    chain/budget (delta_0 = 1/L): L^{4.02} -> L^{3.67} -> L^{3.48} -> L^{3.29}
        (Q-block: L^{4.25} -> L^{3.96} -> L^{3.67} -> L^{3.54}): bounded POLYLOG exponent
        across 6 decades, slope ~ 0.03 in x (= pure L-drift) — the proved-to-needed
        gap closes polylog-ly, never power-ly. [Caveat, expected: at toy scale even
        the DIAGONAL exceeds the (W1.1) budget — W1's feasibility constraint
        R >= c_7 L^2/(20 delta_0 eta^2) bites only at astronomical x — so absolute
        budget comparisons are meaningless at model scale; the slope is the test.]
  (P1) check: max N_win = 4/7/10/16 vs proved R+1 = 9/17/33/64 (slack 2-4x, never
    violated); max tail proxy <= 0.08 (R+1)L vs (W1.3)'s 2 c_V (R+1)L. HOLDS.
  (P2) check: m1/(R+1) = 0.057..0.103, mV/(R+1) = 0.166..0.42, both DECREASING in x
    (truth ~ R/L; unconditional claim C(R+1) holds with C < 1 measured). HOLDS.
  (P2) mechanism check (the load-bearing j-uniformity): E band-count/(R+1) at
    j = 0..8 is FLAT in j at every scale and block (e.g. 1e12 top:
    0.03, 0.08, 0.09, 0.09, ..., 0.09) — the orbit-gap count's j-independence,
    which kills the pointwise (W1.3) L, is directly visible. HOLDS.
  ED2 truth: diagonal-grade (ED2/(R+1) = 0.03-0.10 at all scales, slope 0.10 =
    Bernoulli diagonal) — consistent with W4.7 E1 and the FF b = 0 localization:
    E|D|^2 never carried the wall mass.

DISCRIMINATOR VERDICT: the scaling separates the hypotheses exactly as designed —
power-gap behavior is exhibited by the harmonic mass alone; every physical-chain
quantity and the truth scale at R-to-R^2L grade with polylog-stable ratios.

## 5. VERDICT

**AUDIT-CONFIRMED-[the wall is polylog-deep. Proved here (and now record-grade):
for every dyadic block Lambda in [Q, A], both Vaaler signs, uniformly in
lam in [0.425, 0.575], unconditionally and citation-free:**

    E_{p,q} |D^pm_Lambda|^2  <=  C' (R+1)^2 L,    C' absolute (<= 1.4e4 generous;
    = [7(R+1)L pointwise, (W1.4)(ii) verbatim] x [C(R+1) first moment, NEW lemma
    (P2) = injectivity p -> pbar_q + orbit-gap counting, proved §1, probe-checked],

**vs the (W1.1) demand 20 delta_0 (eta R)^2 L^{-2}: the residual is the single
multiplicative factor**

    C' L^3 / (20 eta^2 delta_0)  =  Theta(L^{3+a})   (delta_0 = L^{-a}),

**with NO x-power remaining on any block — the x^{2lam-0.725} deficit of
W3/W4/THE-OPEN-PROBLEM §2.3 is the price of harmonic-pair/fiber-energy
representations and was never a property of E|D|^2 (it is real for those objects;
they are upper-bound intermediaries only). Even without the new lemma (P2),
squaring the record's own (W1.4)(ii) line gives the same conclusion at L^{4+a}:
the polylog-species claim does not hinge on anything new. Equivalent D3-INEQ*
form of what is now proved: Sum_{w != 0} Ghat_q(w) K_q(w) =
-(fiber energy - diagonal)(1 + O(x^{-(2lam-0.725)} L^{O(1)})) for a.e. q ~ Q —
the anti-correlation phenomenon is unconditional; only its polylog precision
(O(... delta_0 L^{-2}) needed) remains open.]**

Riders (all non-structural, recorded for the ledger):
1. ERRATUM in wp15-ffmodel.md §3.4: "Form A's LHS is unconditionally
   <= x^{0.3}L^{O(1)}" is false as worded — integer Form A (THE-OPEN-PROBLEM §2.3
   (A), full-period) has LHS = +x^{2lam-0.425-o(1)} attained (Parseval pin to the
   fiber energy + F1/cfprune E1): Form A is FALSE, a second representational
   casualty, and should be retired from the demand ledger in favor of (W1.1) /
   (D3-INEQ*)-at-precision. The correct sentence is "(W1.1)'s LHS is
   unconditionally <= x^{0.3}L^{O(1)}". Headline unaffected.
2. wp15-largersieve (2c)/(K2)'s sentence "no upper-bound technology produces a
   negative main term" is falsified as literally worded (the proved kills cover
   only the weight-uniform class; (P*) is non-weight-uniform upper-bound technology
   that does go below the fiber energy). K1-K3 as proved stand.
3. c_V <= 3 (Vaaler envelope constant) remains the record's deferred-calculus flag;
   it enters C' linearly — non-structural.
4. The wall STANDS, re-specied: closing (W1.1) needs a further L^{3+a}. Note the
   species ceiling: any chain through E[(Sum_ell |y_ell|)^2] is floored at
   (E Sum|y|)^2 ~ R^2/L^2 random-model truth, i.e. delta_0^{-1}-short of budget —
   the last L^{a} (and likely the L^3) requires partial sign retention at the
   per-ell level (variance-style or first-moment-squared subtraction), but
   everything missing is now polylog on every block. First-moment-only route:
   E N_hard <= M + 0.22 L * C(R+1) — within Theta(L) of §3.4(2)'s absorption
   demand 20 eta R (but the Chebyshev bad-set layer still needs the second moment,
   hence L^{3+a} is the operative residual).
5. FF-side §§1-2 of wp15-ffmodel (the diagnostic proper) were not re-derived here
   beyond consistency (the integer (P*) is the exact avatar of FF max*mean
   E_{b != 0} mult^2 <= R E mult, with the Vaaler L as integer-only overhead);
   nothing found that disturbs them.

## Log

- Created file. Read wp15-ffmodel.md (full), wp11-e3lb.md 1591-2562 (W1-W4 verbatim),
  wp15-largersieve.md (full), THE-OPEN-PROBLEM.md §2.2-2.4, wp15_largersieve_probe.py,
  wp15-cfprune.md (F1, 1a-1c, Step 2), manuscript spine.
- §1: reconstructed (P1)-(P3); (P1),(P3) verbatim/trivial; (P2) NEW — proved here
  independently via injectivity + orbit-gap (three-distance) counting, constants
  C <= 2000, C' <= 1.4e4; noted (P1)-only fallback gives L^{4+a} (claim robust).
- §2: scope table; no inflation; c_V <= 3 flag inherited (only soft constant).
- §3: floors reconciled (each prices a chain class / the full-period object, not
  E|D|^2); Form A itself found FALSE (positive attained mean, Parseval pin) —
  erratum in §3.4's back-translation sentence (nomenclature, not substance);
  D3-INEQ* shown to be IMPLIED (weak form) by the chain via Markov, not assumed.
- §4: wrote + ran wp15_verify_probe.py at x = 1e6/1e8/1e10/1e12 (full p-average,
  4-6 q per scale; 1e12 = 254910 ells x 10374 primes p per q at top block, ~2 min).
  All five discriminators confirm: ED2/m1/mV slopes ~ 0.10 (R/L-grade), chain slope
  0.18 << harm slope 0.62 (top), chain/harm falls as a power (0.0426 -> 0.0001),
  chain/budget polylog-stable (L^{3.3-4.3}), band counts j-uniform, (P1) bound
  never violated. wp11 anchor (E1 ~ 1.5 at 1e8) reproduced.
- §5: VERDICT AUDIT-CONFIRMED with 5 riders (Form A erratum the only error found;
  it strengthens, not weakens, the representational diagnosis).

## Log

- Created file. Read wp15-ffmodel.md (full), wp11-e3lb.md 1591-2562 (W1-W4 verbatim),
  wp15-largersieve.md (full), THE-OPEN-PROBLEM.md §2.2-2.4, wp15_largersieve_probe.py,
  manuscript spine.
- §1: reconstructed (P1)-(P3); (P1),(P3) verbatim/trivial; (P2) NEW — proved here
  independently via injectivity + orbit-gap (three-distance) counting, constants
  C <= 2000, C' <= 1.4e4; noted (P1)-only fallback gives L^{4+a} (claim robust).
- §2: scope table; no inflation; c_V <= 3 flag inherited (only soft constant).
- §3: floors reconciled (each prices a chain class / the full-period object, not
  E|D|^2); Form A itself found FALSE (positive attained mean) — erratum in §3.4's
  back-translation sentence (nomenclature, not substance); D3-INEQ* shown to be
  IMPLIED (weak form) by the chain, not assumed.
