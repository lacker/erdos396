# WP9: Adversarial verification of wp8-e3.md and wp8-cdagger.md

Referee: WP9 verification agent. Date: 2026-06-10.
Status: COMPLETE. Verdicts: wp8-e3.md UPHELD-WITH-REPAIRS; wp8-cdagger.md UPHELD.

## Scope

1. wp8-e3.md — Prop S (machine-checked root-sum reduction), Theorem T1 (unconditional E3 minus frequency cap, via exact CF-spacing + spaced large sieve + one-large-prime variance, (M2*) once, strengthened corner trim), reduction P2, lower-bound P3, probes.
2. wp8-cdagger.md — BFI-dispersion negative result with quantified deficits at (0.35,0.35), (0.45,0.45); pair-to-single conductor reduction; Chebyshev lower-bound; B=0 audit flag.

Special scrutiny ordered: T1's spaced-large-sieve application (spacing claims, lambda-cancellation in differences), variance claim V <= R+1.

## Sources read

wp8-e3.md, wp8-cdagger.md (full); manuscript/sections: 11-typeII.tex (hyp:E3),
07-minor.tex (def:minor-conditions (M1)/(M2*), lem:cf, thm:minor, cor:minor),
06-reduction.tex (lem:linearization, prop:two-freq, theta_mu),
09-anatomy.tex (prop:one-large, prop:species), 08-major.tex (Families A/B,
prop:digit-assembly), 04-architecture.tex (trim registry, est:Ddagger),
14-lemmaC-reduction.tex (hyp:Cdagger, prop:C-cov, prop:C-single, lem:DMV),
lemma-alpha-beta.md.

## Findings log

### A. wp8-e3.md, Prop S (root-sum reduction) — VERIFIED

Checked line by line:
- a = a0+qt <= x/p + q (a0<q, qR=x/p). At u=1/3 corner: a <= x^{2/3}+2x^{1/2}
  < 2^{2/3}x^{2/3} = y^2 for large x. Correct, with the explicit 2^{2/3} room.
- a < y^2 => at most one prime factor > y with multiplicity (prop:one-large
  logic); hence 1[P+(a)>y] = sum_{ell>y, ell|a} 1 exactly (0 or 1). Correct.
- Exchange of sums: ell | a0+qt iff t = nu_ell := (-a0*qbar) mod ell, valid
  only for ell != q; ell = q is in the range (y, A_max] in-band (q > x^{1/3} ~ y)
  but never divides a0+qt since (a0,q)=1. The ell != q exclusion is correctly
  stated and load-bearing. ell = p needs no exclusion (p may divide a).
- ell > y > R in-band (u+u' > 2/3) forces s=0 in t = nu_ell + s*ell: at most
  one hit per ell; injectivity t -> unique large prime factor. Correct.
- Probe rerun: see C below.
Verdict on Prop S: CORRECT.

### B. wp8-e3.md, Theorem T1 — step-by-step audit

Notation check: Sigma(theta) = E(theta) + kappa'*G(theta) with
eps_t = omega(a0+qt) - kappa' is an identity (ranges 0<=t<=R consistent). OK.
kappa' = sum_{y<ell<=A_max, ell!=q} 1/ell = log(log A_max/log y) + o(1)
<= log 2 + o(1) < 1. OK. |eps_t| <= 1 hence V := sum eps_t^2 <= R+1 -- the
flagged variance claim is TRIVIALLY TRUE (does not even need the one-large-
prime injection; that only sharpens to kappa'(1-kappa')R, marked unused). OK.

Step (1) main term: kappa'*sum_mu |G(theta_mu)|/<mu> with |G| <=
min(R+1, 1/(2||theta_mu||)) = X_mu + O(1); the +O(1) sums to O(log p),
absorbed. This is eq:minor-start's RHS (x2); thm:minor's PROOF bounds exactly
sum_mu X_mu/<mu> (the theorem statement is phrased for |V_p|, but the proof
bounds the dominating sum -- citation-form nitpick only). cor:minor under
(M1)+(M2*): << sqrt(R) L^{B/2+4} + R L^{2-B}. Under the strengthened trim
sqrt(R) >= L^{B/2+2c+8}: sqrt(R)L^{B/2+4} <= R L^{-2c-4}; R L^{2-B} <=
R L^{-2c-6} for B >= 2c+8. Both << R L^{-c-2}. CHECKS.

Step (2) spacing / lambda-cancellation (ordered scrutiny): theta_mu is linear
in mu with mu-independent shift -lambda p/q, so theta_{mu1}-theta_{mu2} =
(mu1-mu2) q/p mod 1 EXACTLY -- the lambda term cancels identically. Correct.
With alpha = q/p in lowest terms (p,q distinct primes), lem:cf(1) (statusP in
07-minor) gives ||k alpha|| >= ||s alpha|| >= 1/(s+s^+) >= 1/(2s^+) for
0 < k < s^+. Hence any window of W <= s^+ consecutive mu has pairwise
spacing >= 1/(2s^+), and points are distinct mod 1 (||k q/p|| > 0 for k < p;
all windows used have W <= s^+ <= p). Correct. The two dyadic intervals
(mu and p-mu branches) are sieved separately, so no cross-interval spacing
is needed. Correct.

Step (3) large sieve: Montgomery-Vaughan form sum_j |S(x_j)|^2 <=
(N + delta^{-1}) sum|a_t|^2 with N = R+1 coefficients; the proof actually
uses (R+1+2s^+) -- consistent. delta = 1/(2s^+) <= 1/4 in all uses
(s^+ > M >= mu_0 in Regime I, s^+ > R in Regime II). CHECKS.

Step (4) Regime I (mu_0 <= M <= R): s := largest convergent denominator <= M
exists (s=1 always a denominator); maximality gives s^+ > M >= |I| so the
whole interval is one window. (M2*) applies since s <= M <= R: s^+ <=
s R L^{-B} <= M R L^{-B}. Cauchy-Schwarz + sieve:
M^{-1/2}[(R+1+2MRL^{-B})V]^{1/2} <= sqrt(2RV/M) + sqrt(2RVL^{-B}).
Dyadic sum: first piece geometric from M = mu_0, total << sqrt(RV/mu_0)
<= sqrt(2) R L^{-c-3} (V <= 2R, mu_0 = L^{2c+6}); second piece x (3L blocks
x 2 intervals) <= sqrt(2) R L^{1-B/2} <= sqrt(2) R L^{-c-3} (B >= 2c+8).
ALL CHECKS, including the constant bookkeeping.

Step (5) Regime II (R < M < p): s_0 = largest denominator <= R, so
s_0^+ >= R+1 automatic, and (M2*) at s_0 <= R gives s_0^+ <= R^2 L^{-B}.
Windows of W = min(M, s_0^+): count <= M/W + 1 <= 2M/W (W <= M). Per-window
differences < W <= s_0^+, spacing 1/(2s_0^+). Aggregate
[2/W * (R+1+2s_0^+) * V]^{1/2}:
  - s_0^+ >= M: W = M > R; (2/M)(R+1) <= 2+2/M, 4 s_0^+/M <= 4 R L^{-B}
    (s_0^+ <= s_0 R L^{-B}, s_0 <= R < M); bound <= 2 sqrt(2R) + 2 sqrt(2) R L^{-B/2}. OK.
  - s_0^+ < M: W = s_0^+ >= R+1; 2(R+1)/s_0^+ + 4 <= 6; bound <= sqrt(12R). OK.
Per block O(sqrt R + R L^{-B/2}); x <= 3L blocks x 2: << L sqrt R + R L^{1-B/2}
<< R L^{-c-3} under sqrt R >= L^{B/2+2c+8} >= L^{c+4} and B >= 2c+8. CHECKS.

Assembly (6): |Sigma| <= |E| + kappa'|G| splits the full mu-sum into
(core |E|) + (main term, step 1) + (tail |E|, steps 4-5). T1 statement
follows. THEOREM T1 IS CORRECT AS PROVED (modulo the cosmetic items below).

T1 audit discrepancies (non-fatal):
- COSMETIC (E3-1): the claim "(M2*) enters exactly once / only in steps
  (4),(5)" is wrong: step (1) consumes cor:minor, which uses (M2*) (both for
  D_R <= L sqrt(R L^{-B}) and for R/s_0 <= R L^{-B}). No validity impact --
  minor p means (M1)+(M2*) anyway -- but the inputs audit overstates economy.
- COSMETIC (E3-2): "no use of R<p" is fair: regimes are defined by M vs R and
  both arguments are unconditional in the geometry; checked.
- COSMETIC (E3-3): step (1) cites thm:minor's statement where its proof's
  intermediate bound (on sum X_mu/<mu>) is what is used; should be restated
  as a corollary of the proof. No mathematical content at risk.

### C. wp8-e3.md probes -- rerun (2026-06-10)

- `.venv/bin/python e3_probe.py 2e6`: Prop S exact identity, 15 trials at each
  of (0.34,0.34),(0.40,0.40),(0.34,0.48),(0.48,0.34): **0 mismatches / 60**.
  Probe code audited: LHS is the literal E3 inner sum, RHS the root sum with
  the ell != q exclusion; P+ computation correct. REPRODUCES.
- `.venv/bin/python e3_probe2.py`: N4 corner table reproduces (margins 0.0
  exactly at (1/3,1/3); a<y^2 boundary at u=1/3 correctly flagged as the
  2^{2/3}-constant case). N2 full mu-aggregate (5 pairs, x=2e6, (0.36,0.36)):
  tail/(sqrt(R) log x) = 0.12-0.18, inside the report's 0.12-0.27. N3
  dispersion ratios E_q|E|^2/V = 0.76-1.40 (means), medians 0.46-1.05, max
  6.4, V/R ~ 0.23 -- matches the report's 0.71-1.40 / max 6.4 / 0.21-0.26.
  FFT indexing in the probe audited (theta_mu = mu q/p - beta handled via
  nu = mu*q mod p; correct). REPRODUCES.
- COSMETIC (E3-6): the committed probe mains run a SUBSET of the
  configurations described in S6 (no x=2e7 runs, 5 not 13 pairs, 4 not 10 p);
  the reproduced subset matches all claimed ranges, but full provenance would
  need the larger runs re-executed.

### D. wp8-e3.md, Section 4 (small-mu main term, E3-dagger, P2)

- Small-mu main term: (M1) (valid: mu_0 = L^{2c+6} <= R under the trim)
  gives kappa'|G(theta_mu)| <= <mu> L^B + O(1), so the core main-term total
  <= 2 mu_0 L^B + O(log mu_0) ~ 2 L^{B+2c+6} << R L^{-c-2} since the
  strengthened trim gives R >= L^{B+4c+16} >= L^{B+3c+8}. CHECKS; the free
  swap |E| <-> |Sigma| on the core range is justified.
- P2 (T1 + E3-dagger => E3): per fixed core mu, Cauchy-Schwarz over (p,q) +
  E3-dagger + main-term swap give E_{p,q}|E| << R L^{-c-4}; summing
  sum_{<mu><=mu_0} 1/<mu> <= 5 log(mu_0) = O(L^eps) gives << R L^{-c-2}; T1
  remainder sums to pi(P) R L^{-c-2}. E3's normalization matches. CHECKS.
- Diagonal accounting: E_{p,q} V <= R+1 << R^2 L^{-2c-8} iff R >= ~L^{2c+8},
  implied by trim. Requirement "R L^{2c+8} << R^2" correctly identified as
  pure polylog. CHECKS.
- Arithmetic-shape discussion (Kloosterman fractions, three inverse layers,
  Lambda in (Q, Q^{3/2}] hard sub-range): qualitative routing, no theorem
  claimed; internally consistent with lemma-alpha-beta.md S5 and with
  u+2u' > 1 <=> A < Q^2 (checked: 1-u < 2u' iff u+2u' > 1).

### E. wp8-e3.md, Section 5 (P3 / E3-lb) -- TWO GAPS FOUND

- GAP (E3-4, lambda-uniformity of E3-lb): E3-lb is stated PER fixed lambda
  ("for each 0<|lambda|<=L^C ... #{q bad} <= delta_0 pi(Q)"), but the
  lower-bound consumer discards q from the sandwich WHOLESALE, and each
  retained q must be good for ALL L^C harmonics lambda simultaneously
  (the digit assembly aggregates over lambda with weights 1/<lambda>). The
  union bound over lambda inflates the bad set to delta_0 L^C pi(Q) -- not
  constant density. P3 as stated does not follow from E3-lb as stated.
  MINIMAL FIX: restate E3-lb with the lambda-quantifier inside the event
  (Bad = {q : exists lambda <= L^C with ...}), i.e. demand the bad set be
  lambda-uniform; same plausibility class, polylog-many events. Downstream
  impact: none once restated; P3's argument is then correct (5 log mu_0 *
  pi(P) R L^{-c-4} << pi(P) R L^{-c-2} checks). NOTE: the sibling report
  wp8-cdagger.md gets this exact point RIGHT in C-dagger-lb (union over the
  O(L^{2C}) harmonics is taken inside the statement) -- confirming the
  omission here is an oversight, not a convention.
- GAP (E3-5, "variance form implies E3-lb" exponents): S5 item 1 claims
  E_{p,q}|E(theta_mu)|^2 <= delta_0^2 L^{-2c-10} R^2/L^2 per core mu implies
  E3-lb "by Chebyshev + Markov over p". Check: Chebyshev at the needed
  per-(q,p,mu) threshold ~ R L^{-c-4} gives per-mu bad-pair fraction
  <= delta_0^2 L^{-2c-12+2c+8} = delta_0^2 L^{-4}; the union over the
  2 mu_0 = 2 L^{2c+6} core frequencies (and over L^C lambda, per E3-4)
  costs L^{2c+6+C}, leaving delta_0^2 L^{2c+2+C} -- DIVERGES. The stated
  exponent is short by the core-frequency count (and the lambda union).
  MINIMAL FIX: strengthen the variance hypothesis to
  <= delta_0^2 R^2 L^{-(4c+18+C)} (any polylog works; the target E3-dagger
  has polylog room). Downstream impact: none -- the variance form is still
  strictly weaker than an asymptotic and of the same difficulty class; but
  as printed the implication chain is quantitatively false.

### F0. wp8-cdagger.md -- verification

**Section 1 (pair -> single reduction).**
- Phase identity a*vartheta_{h,k} = hb/p1 + k a p1/p2 (b = p2 a): trivial
  algebra, and the dispersion form phi_{p2,m}(ell) == a*vartheta mod 1
  (residue form, exact divisions (m ell+1)/p_i) machine-checked in exact
  rational arithmetic, 300 random (p1,p2,h,k,a): 0 failures.
- Axis-harmonic exact identity sum_{p2} w(p2) V(p1,p2;vartheta_{h,0}) =
  sum_{b<=x/p1} g(p1 b - 1) e(hb/p1) c0(b): machine-checked with random
  complex w, g, 20 trials: 0 failures. The cutoff IS clean in b (a <= R
  iff b <= x/p1). Conductor bookkeeping (b mod p1 <-> n mod p1^2 on
  n == -1 mod p1; 2u1 > 2/3 > 3/5 band-wide, beyond GS/DGS) consistent with
  prop:C-single's demotion note and lem:beta primitivity. CHECKS.
- COSMETIC (CD-2): "the two stand or fall together" overstates: only the
  AXIS harmonics of C-dagger-pair reduce to (divisor-weighted) C-dagger-
  single; the fall direction (single hard => pair hard) is justified, the
  stand direction is not. The body text is correctly scoped; the Status
  bullet is loose.

**Section 2 (BFI dispersion -- the ordered checks).**
- Budget: |Sigma|^2 <= N*D, target x^{1-u1}L^{-c-1} => D-budget
  x^{1-2u1+mu}L^{-2c-2}. CHECKS.
- D1 = x^{1-u1}L^{-1}; within budget iff M >= p1 L^{2c+1} (mu > u1). CHECKS.
- D2: emptiness for M < p1 P2 (mu < u1+u2) checks (|m-m'| < M < p1p2).
  Differenced phase Delta-phi = -j*ell*vartheta_{h,k} and its CONSTANCY on
  the AP ell == ell0 mod p1p2 (increment -js(h p2^2 + k p1^2) == 0 mod 1):
  machine-checked exactly (300 configs x 4 AP steps): 0 failures. Count
  x^{1+mu-2u1-u2}L^{-1}: saves x^{u2}. CHECKS.
- D3: CRT compatibility forces m == m' (p1) (gcd of moduli = p1). Quadruple
  count (P2^2/L^2)(M^2/p1), class density 1/(p1p2p2') over N: main term
  x^{1+mu-2u1}L^{-2} = budget x L^{2c}: SATURATION CONFIRMED. Sub-one-per-
  class: D = p1p2p2' = x^{u1+2u2} > x >= N since u1+2u2 = (u1+u2)+u2 >
  2/3+1/3 = 1. CHECKS.
- Optimistic-Weil deficit: D3_err = (P2^2/L^2)(M/p1) sqrt(D) =
  x^{mu+3u2-u1/2}; <= budget iff 3u2 + (3/2)u1 <= 1; mu-INDEPENDENT
  (closes the shorten-N loophole). At (0.35,0.35): deficit exponent
  3(.35)+1.5(.35)-1 = 0.575; at (0.45,0.45): 1.025. Benchmark deficits
  (u1+u2)-3/5: 0.10 and 0.30. ALL RECOMPUTED INDEPENDENTLY; table rows
  (q, R, conductor p1^2, admissible mu window [u1+eps, u1+u2), eta <= 0.05
  at (0.45,0.45)) all check. Band floor: 3u2+1.5u1 > 3/2 strictly (open
  band) -- report's ">=" is a boundary-cosmetic.
- NOTE (CD-4, direction of optimism): granting sqrt(D) per (p2,p2',delta)
  m-AGGREGATE concedes a factor ~M beyond per-quadruple Weil + trivial
  m-sum; failure under a STRONGER-than-provable bound makes the negative
  robust. Accounting direction verified correct.
- NOTE (CD-5): benchmarks GS x^{20/39} and DGS x^{3/5} match the
  manuscript's own citations (prop:C-single); BFI x^{4/7} standard;
  Maynard x^{11/21} not independently verified (decorative, non-binding --
  the binding comparison is 2/3 > 3/5, which is exact).
- Self-check (iii) (joint dispersion conductor p1p1'p2p2' ~ x^{1.4} at
  (0.35,0.35), worse): arithmetic checks.
- g-intact orientations: form coefficients p1p2 ~ x^{2/3+} vs lengths
  R < x^{1/3} / P2 < x^{1/2}: outside log-Elliott (fixed/slow coefficients
  only). Qualitative routing, fairly characterized.
- The negative verdict is correctly scoped to THIS ANGLE (method autopsy),
  with the empirical truth-evidence (z: 13.1 -> 0.78) honestly attributed
  to unextractable D3-aggregate cancellation. VERDICT ON S2: the
  computation is CORRECT and the negative is robust.

**Lower-bound section (C-dagger-lb).**
- Chebyshev closure RECOMPUTED: per-harmonic variance
  sigma^2 = delta_0 R^2 L^{-2c-2C-10}. At threshold T = R L^{-c-3} the
  per-harmonic exceptional fraction is sigma^2/T^2 = delta_0 L^{-2C-4};
  union over the O(L^{2C}) box harmonics: <= delta_0 L^{-4} <= delta_0,
  with room. On good pairs the assembled weighted sum is
  sum_{h,k} T/(4<h><k>) << (C log L)^2 * R L^{-c-3} << R L^{-c-2} << RL^{-c}.
  THE EXPONENT -2c-2C-10 IS CORRECTLY CALIBRATED
  to absorb both the L^{2C} union and the L^2 weight mass. CLOSES WITH
  ROOM. (Contrast: wp8-e3.md S5 item 1 fails this same calibration --
  finding E3-5.)
- COSMETIC (CD-1): "0<<h><k><=L^{2C}" should be the harmonic box
  0<|h|,|k|<=L^C of prop:C-cov; the union count O(L^{2C}) and weights
  are computed for the box, so no quantitative impact.
- NOTE (CD-3): clause (a) (majors discarded at density O(L^{-pos}))
  inherits the manuscript's standing claim (08-major preamble) that
  worst-case-per-q Family-A/B versions suffice for the lower-bound track
  without E1/E2; the report does not flag this conditionality. Reliance,
  not an error introduced by this WP.
- B=0 audit flag: honestly scoped ("not checked here", "bookkeeping
  check"). Plausibility cross-checked against the manuscript: with
  B(n)=B(n-1)=0, the only forced beyond-GS conductors (band-prime slot-2,
  p^2 in (x^{2/3},x)) are absent; deeper slots at sub-band primes use the
  chooseable-position device (prop:C-single remark, p^{j-1} <= x^{1/2});
  primes > x^{1/2} have the deterministic FK top digit. Positive density
  of the subclass: standard anatomy measure + Lemma B. So the flag's
  premise is plausible; its validation is correctly assigned to the
  S06/S15 gluing audit. PROPERLY FLAGGED, NOT OVERCLAIMED.

### F. wp8-e3.md bookkeeping deltas (S7.7)

- B = max(C+c+4, 2c+8): consistent with prop:digit-assembly (B=C+c+4) and
  Family A's B >= C+c+3; Family B's count PQ L^{B+1}/R grows with B but
  R >= x^{eta''} under the registered corner trim swallows any polylog:
  the "strengthened corner trim" sqrt R >= L^{B/2+2c+8} is FREE given trim
  registry item 2 (R >= x^{eta''}). CHECKS.
- Boundary ell-range wobble (A_max depends on q): correctly flagged;
  immaterial for T1 (identity used at full range). OK.

## Consolidated findings

| ID | Report | Class | Finding | Minimal fix | Downstream |
|----|--------|-------|---------|-------------|-----------|
| E3-1 | wp8-e3 | COSMETIC | "(M2*) used exactly once / only steps (4),(5)" false: step (1) uses it via cor:minor | reword inputs audit | none |
| E3-2 | wp8-e3 | (cleared) | "no band geometry used" claim verified | -- | -- |
| E3-3 | wp8-e3 | COSMETIC | step (1) cites thm:minor's statement; needs its proof's intermediate bound on sum X_mu/<mu> | state a corollary of thm:minor's proof | none |
| E3-4 | wp8-e3 | GAP | E3-lb stated per-lambda; consumer discards q wholesale, union over L^C lambdas breaks constant density | put lambda-quantifier inside the bad-set event | P3 then correct as argued |
| E3-5 | wp8-e3 | GAP | S5 item-1 "variance form implies E3-lb": exponent short by the core-mu count L^{2c+6} (+L^C lambda union); Chebyshev/Markov diverges as stated | strengthen variance hypothesis to ~delta_0^2 R^2 L^{-(4c+18+C)} (still polylog-room vs E3-dagger truth) | hierarchy of weak forms survives |
| E3-6 | wp8-e3 | COSMETIC | committed probe mains run a subset of the S6 configurations | rerun larger configs or trim S6 prose | none |
| CD-1 | wp8-cdagger | COSMETIC | harmonic set "<h><k><=L^{2C}" should be the box |h|,|k|<=L^C | reword | none |
| CD-2 | wp8-cdagger | COSMETIC | "stand or fall together" overstates the axis-only reduction | weaken to "single hard => pair hard" | none |
| CD-3 | wp8-cdagger | NOTE | major-discard clause silently inherits 08-major's "worst-case-per-q suffices for lb-track" stance (E1/E2-free claim not re-proved) | add a conditionality flag | none if 08-major stands |
| CD-4 | wp8-cdagger | (cleared) | optimistic-Weil grant direction verified (concedes ~M beyond Weil): negative is robust | -- | -- |
| CD-5 | wp8-cdagger | NOTE | Maynard x^{11/21} benchmark not independently verified (decorative) | pin in citations.md | none |

Machine checks run for this verification: e3_probe.py (60/60 exact),
e3_probe2.py (N2/N3/N4 reproduce), plus a fresh exact-rational check of
wp8-cdagger's three identities (phase identity 300/300; D2 differenced
phase + AP-constancy 300x4 / all exact; axis pair->single identity 20/20)
and an independent recomputation of the full exponent table.

## Verdicts

**wp8-e3.md: UPHELD-WITH-REPAIRS.**
The headline claims survive adversarial re-derivation: Prop S is correct
(and re-verified by machine, including the ell != q subtlety); Theorem T1
is correct as proved -- the ordered scrutiny points all clear (the
lambda-cancellation in mu-differences is an exact identity; the CF spacing
windows are correctly sized W <= s^+ with lem:cf(1) giving 1/(2s^+); the
M-V large sieve is applied per window with the right N = R+1; V <= R+1 is
trivially true); P2 (T1 + E3-dagger => E3) checks including all polylog
exponents. The repairs: E3-4 and E3-5 (both in S5, the lower-bound-variant
section) -- the exceptional-set form must be made lambda-uniform and the
variance-form exponent strengthened by the core-frequency count; both are
restatements of HYPOTHESES (targets), polylog-cheap, with no effect on T1,
P2, or the headline reduction. Stated confidences (~0.85/~0.9) are fair.

**wp8-cdagger.md: UPHELD.**
Every checkable claim verified: the dispersion computation is correct
(budget, D1, D2 emptiness + phase annihilation, D3 CRT structure and exact
budget saturation); the deficit exponent 3u2 + (3/2)u1 - 1 is right,
mu-independent, = 0.575 at (0.35,0.35) and 1.025 at (0.45,0.45), > 1/2
band-wide; the optimistic-Weil accounting errs on the side that makes the
NEGATIVE robust; the pair->single conductor reduction is an exact identity
(machine-checked) with the correct conclusion that the conductor halves to
p1^2 but never reaches modulus p1; the C-dagger-lb Chebyshev argument
closes with room (its exponent is correctly calibrated where wp8-e3's S5
analogue is not); the B=0 escape is honestly flagged, not claimed, and its
premise survives a plausibility cross-check against prop:C-single's
chooseable-position device. Residual items are cosmetic wording (CD-1,
CD-2) and two reliance notes (CD-3, CD-5). The negative method-verdict at
confidence ~0.85 is, if anything, conservative.
