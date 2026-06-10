# WP9: Adversarial verification of wp8-e1.md (E1) and wp8-e2.md (E2)

Referee: WP9 verification agent. Date: 2026-06-10.
Status: COMPLETE. Verdicts: E2 UPHELD; E1 UPHELD-WITH-REPAIRS (one
GAP-class repair mandatory — sum branch / Pythagorean tangency; see end).

## Findings

### E2 (wp8-e2.md) — line-by-line check of the proof

**Step 0 (witness truncation): VERIFIED.** For distinct primes p,q and a
non-final convergent denominator s of q/p: s < p (denominators increase to
the final denominator p), p∤s, p∤q, so ||s q/p|| >= 1/p; lem:cf(1) gives
||s alpha|| <= 1/s+ < 1/(s G_0); hence s < p/G_0 <= 2P/G_0. Both uses of
primality are exactly as flagged. Correct.

**Lemma R1: VERIFIED.** Partition into <= H/r+1 blocks of <= r consecutive h;
residues hb mod r distinct within a block ((b,r)=1); at most one h with r|h
contributes N; the rest contribute sum_{j=1}^{r-1} 1/(2||j/r||) <=
sum_{j<=r/2} r/j <= r(log r + 1). Bound (H/r+1)(N + r(log r+1)) follows.

**Lemma R2: VERIFIED.** Periodization of a smooth bump at scale delta;
Phi_hat(h) = delta*eta_hat(delta h); properties (i)-(iii) standard. Needs
delta <= 1/8, supplied by G_0 >= 8.

**Step 1 (majorization order): VERIFIED.** Truncation applied BEFORE the
prime->integer relaxation of q; each failing pair assigned to one witness;
triple count (p,s,q) with s integer in dyadic block and q integer only
enlarges. The p|qs spikes (possible when 2Q > P, since (s,p)=1 forces p|q)
land in the h ≡ 0 mod p terms and are covered by the N-term of R1. Sound.

**Steps 2-3: VERIFIED.** delta_k = 2^{-k}/G_0 >= 1/(sG_0) on the block;
A=3 decay; dyadic j-ranges: coefficient <= delta_k 2^{-3(j-1)}, R1 with
H_j = 2^{j+1}/delta_k, r=p prime, (s,p)=1 (s < p/G_0 < p). j-sums:
sum 2^{-3j} 2^{j+1}/p = O(1/p), sum 2^{-3j} delta_k = O(delta_k). The
truncation makes the effective H ~ 2^k G_0 <= 2p, so H/p = O(1). Correct.

**Step 4 (assembly): VERIFIED.** Per block: P * 2^k * [4 delta_k (Q+1) +
C(1/p + delta_k)(Q + p log 2p)] <= PQ/G_0 + (2^k + P/G_0)(Q+PL)
<= PQ/G_0 + (3P/G_0)(Q+PL), using 2^k <= 2P/G_0 (truncation) for every
block. Times <= O(L) blocks: PQ L^{B+1}/R + P^2 L^{B+2}/R. Correct.

**Finding E2-1 [CONSTANT].** "K+1 <= log_2 x <= L" is false: log_2 x =
L/log 2 ~ 1.44 L > L. Number of blocks is <= 2L, a factor-2 constant
absorbed by the implied constant. Minimal fix: replace "<= L" by "<= 2L"
(or use ceil(log_2)). Downstream impact: none (absolute constant).

**Finding E2-2 [COSMETIC].** The Theorem's failing-set definition
"exists convergent denominator s <= R with s+ > s G_0" leaves implicit that
s must be non-final (s+ exists); Step 0 uses this ("s has a successor").
On the band R < P < p so all s <= R are non-final and (M2*) only ever
inspects non-final s — consistent with 07-minor.tex. Minimal fix: one
clause in the statement. Also: the two CF representations of a rational
([...,a_n] = [...,a_n - 1, 1]) should be fixed by convention in the
write-up. No downstream impact.

**Finding E2-3 [COSMETIC].** alpha = q/p is declared in (0,1) in
07-minor.tex but q > p occurs on half the band (u < u'); convergent
denominators of q/p and of {q/p} coincide, and ||s q/p|| >= 1/p is
unaffected, so E2's proof is insensitive. A pre-existing manuscript
hygiene item, not an E2 error.

**Downstream re-verification (prop:digit-assembly): VERIFIED.** New bound
has L^{B+2} on the P^2 term (and the honest 1/pi(Q) conversion adds one L
to each term, which the manuscript's own accounting had elided: it wrote
P L^{B+1}/R per q where P L^{B+2}/R is correct — a pre-existing factor-L
slip, harmless). Requirements: R >= L^{B+c+4} — implied by corner trim
sqrt(R) >= L^{B/2+c+5} (gives R >= L^{B+2c+10}, room to spare); and
x^{2u-1} L^{B+c+5} <= 1 — power-saving under the top trim. prop:digit-
assembly stands with the SAME B = C+c+4 and the same trims. The modified
count PQ L^{B+1}/R + P^2 L^{B+2}/R is tolerated with room. Confirmed.

**Consumers of hyp:E2 checked:** prop:familyB and prop:digit-assembly
(08-major), prop:C-cov(2) (14-lemmaC), status tables (04, 10). All
audited below — wp8-e2's claim that prop:familyB is the only mathematical
consumer of hyp:E2 is correct.

### E1 (wp8-e1.md) — structural checks

**§1.1 (integer p): VERIFIED.** lem:branch counts integer p explicitly;
prop:familyA only upper-bounds an excluded set. No prime-p input needed.

**§1.2 (prime q -> integer q at cost L): VERIFIED.** N_q >= 0 termwise;
the chain pi(Q)^{-1} sum_{q prime} sum_mu N_q <= (Q/pi(Q))[sum_mu 2
delta_mu P + P L^{A-B}] is correct; the extra L^{A+1} is absorbed by
re-choosing the free parameter B (chosen last in prop:digit-assembly).
Note B also sits inside delta_mu, M_0 and the minor/major split, but E1-flat
is claimed uniformly in B, so the re-choice is legitimate.

**§2 (moving-interval decomposition): VERIFIED.** g(p) = mu q/p - lambda p/q
strictly decreasing; window = [c(k+delta)q, c(k-delta)q] with
c(t) = (sqrt(t^2+4 lambda mu) - t)/(2 lambda) solving lambda c^2 + tc - mu
= 0; counting #((a,b] cap Z) = b - a - psi(b) + psi(a); slopes independent
of q. Edge/clip bookkeeping matches lem:branch. (Integer-endpoint psi
convention is a write-up detail.) Report's own numerics: 0 mismatches.

**§2.1 (trivial pieces, closed band): VERIFIED.** For mu <= m_0 the
k-range is <= C(lambda P/Q + 1); summing over mu <= M_0 = R L^{-B} gives
<= C' P L^{C-B} x^{1-u-2u'} + P L^{-B} <= 2C' P L^{C-B} since u + 2u' >= 1
on the closed band (equality only at (1/3,1/3) — the L^{-B} from M_0 is
what saves the corner). Matches rem:E1-signed.

**§3.2 (resonance identity): RE-DERIVED, exact.** Substituting n = sc - y
into lambda n^2 + tsn - mu s^2 gives -y(2 lambda n + ts + lambda y)
identically (since lambda c^2 + tc - mu = 0). With J := mu s^2 - ksn -
lambda n^2 and sigma := delta_mu s n: |J -+ sigma| = eta |2 lambda n + ts +
lambda y|. Two-sided magnitude ~ s*Kbar checked: with the m_0 sharpening
(m >= 100 max(P/Q, lambda P^2/Q^2, 1)) all live k ~ Kbar, lambda n <=
ts/50, |lambda y| <= lambda/s <= lambda n; all terms positive. Correct,
including in the P < Q half-band.

**F1-F5: RE-DERIVED, all correct.** F1: {mu s^2 - ksn} = s(s,n)Z, so J=0
solvable iff s(s,n) | lambda n^2 iff s/(s,n) | lambda; J=0 forces
sigma <= W i.e. sn <= 4mWL^B. F2: trivial. F3: |J|>=1 and |J-+sigma|<=W
force sigma >= 1-W (quantization). F4: <=3 convergent denominators per
dyadic block (s_{i+2} >= 2 s_i), 2 signs. F5: sigma(mu) strictly monotone.

**Term zoo: derivations reconstructed.** I was able to reconstruct
complete derivations for A, J0 (both alternatives incl. the g <= 2 sbar/h''
truncation), JA (AP-harmonic, step s*g1), JB (sporadic least-|J| harmonic;
Lemma-R branch), J2 (sigma-measure x density sum_{s,n} 1/(s g1) ~ Nbar),
SING (trivial sbar*Nbar), B2 ((F5) union bound) — each from
#mu(J) <= 2mW g1/(|J| n) + 1 summed over admissible J in AP of step s*g1.
The zoo is coherent; sketches in the report are terse but not wrong.

**Lemma R sketch: CHECKED, sound with one small omission.** Steps
(i),(iii),(iv) check (rho_a(s) <= 4^{omega} sqrt((a,s)) * lambda-factor;
sum_{j} sqrt((j,s))/j <= L sum_{d|s} d^{-1/2}; average of 4^omega tau over
s ~ sbar is L^{O(1)}). Step (ii) as written drops the rho_0(s)/s term
(residues x with lambda x^2 ≡ 0 mod s, where d_0 = s): rho_0(s)/s <=
4^{omega} sqrt((lambda,s)*s)/s = L^{O(1)}/sqrt(s)-scale — absorbed. The
report itself flags p=2/squarefull/(lambda,s) cases as owed. GAP only at
write-up grade, as self-declared.

**§3.1 (CF/Ostrowski lemma): classical-shaped, citable; flagged as owed.**
The form |sum_{q in I} psi(cq)| << L^2 + L sum_{s_i <= Q} (1/s_i)
min(Q, 1/eta_i) is the standard Ostrowski/Lerch partial-sum bound with
shift-uniformity (discrepancy of {nc+b} = that of {nc}); the L-factors are
generous. Consequences (i)-(iv) all check. Half-page write-up owed, as the
report says.

(Scanner verification below.)

### E1 — exponent ledger (e1_exponents.py) rerun + adversarial variants

**Committed scanner rerun (.venv/bin/python e1_exponents.py): FULL PASS**,
exactly as reported — all 10 corner/sample points, 11x11 band grid, 17x17
fine grid (q-frame alone: 0 violations), ngrid=24 stress at all four
corners: 0 violations.

**Scanner-soundness probes (my variants, /tmp/e1_scan_variants.py):**
1. *t-grid depth*: committed TOFF stops at -4 while derived Wmin can sit at
   t=-8; I extended TOFF to -8 AND forced the exact bottom shell W=Wmin
   into the scan: **0 violations**. Concern moot.
2. *Lemma-G ablation*: committed file still encodes the Gauss-sum SING
   alternative (contradicting the report's "Dropped"); I reran with
   SING = trivial sbar*Nbar only: **0 violations** — the report's ablation
   claim is confirmed; Lemma G is genuinely not load-bearing.
3. *Encoding bug in the dead branch* [CONSTANT, moot]: the committed SING
   encodes h^{1/2}, h^{3/2} with t-coefficients h[1], h[1] instead of
   h[1]/2, 1.5*h[1] — the h^{1/2} one understates a count (unsound
   direction). Moot by (2); minimal fix: delete the Gauss-sum alternative
   from the script (it is declared dropped anyway).
4. *Lemma-R ablation* (JB else-branch -> trivial m*W*sbar): **FAILS at
   (1/3,1/3), (0.34,0.34), (0.36,0.36)** — exactly the lower-left diagonal
   the report names. The scanner is non-vacuous and Lemma R is the unique
   non-formal load-bearing input, as claimed.
5. 9x9 band grid with trivial SING + deep TOFF: 0 violations.

**Scanner encoding vs report term zoo: MATCHES.** A, J0 (both
alternatives + CAPC), gate max(sigma,W)>=1/2 (F3), LF-emptiness, JA, JB
(two branches incl. Lemma R), J2, SING, B2, CAPC, weight K/W with bottom
shell Q/sbar, m,h,W ranges, acceptance criterion (f < u+u' strict, or
equality with t <= -1) — all faithful to §3.4 at the (x^f, L^{tB})
resolution. The acceptance criterion is the right one given B is chosen
last (constant L-powers absorbed into A). One stale docstring ("Vaaler
with H=Q_frame"; h is now the convergent-denominator scale) [COSMETIC].

### E1 — Finding E1-1 [GAP — the load-bearing finding of this review]

**The §1 parenthetical "(Negative lambda / the mu -> p-mu 'sum branch'
mu q/p + lambda p/q is cognate ... everything below applies verbatim)" is
FALSE, and the downstream-consumed form of E1 genuinely needs that branch.**

Chain of facts (each checked against the manuscript):
- prop:two-freq (06-reduction) has mu in (0,p), |f_mu| <= 1/(2<mu>),
  <mu> = min(mu, p-mu); (M1) (07-minor def) quantifies over ALL mu with
  0 < <mu> <= R. thm:minor's proof uses the (M1) floor on BOTH halves.
- For upper-half mu = p - mutilde: theta_mu = mu q/p - lambda p/q ==
  -(mutilde q/p + lambda p/q) mod 1 (since p*(q/p) = q is an integer).
  So (M1)-failure includes the SUM-branch resonances
  ||mutilde q/p + lambda p/q|| < 1/(2 mutilde L^B), mutilde <= R L^{-B}.
- eq:conic (08-major) claims (M1) fails "exactly when" the
  difference-branch conic holds for mu <= RL^{-B} — WRONG ("exactly"):
  the sum branch is silently dropped. lem:branch, hyp:E1, and
  prop:familyA's proof inherit this: they count only the difference
  branch. This is a pre-existing MANUSCRIPT gap which wp8-e1 noticed and
  waved through with "applies verbatim".
- Why verbatim fails: g_+(p) = mutilde q/p + lambda p/q is NOT monotone;
  it has a minimum at p* = q sqrt(mutilde/lambda) with critical value
  g_+(p*) = 2 sqrt(lambda mutilde) — INDEPENDENT of q. So the
  "endpoints equidistribute as q varies" mechanism is structurally absent
  at the tangency: when 2 sqrt(lambda mutilde) is within ~delta of an
  integer (worst case lambda*mutilde a perfect square, e.g. mutilde =
  lambda, where 2 sqrt(lambda mutilde) = 2 lambda exactly), EVERY q has a
  tangency window of length ~ q mutilde^{-1/4} lambda^{-3/4} L^{-B/2}
  (square-root of the window: stationary phase), not the O(1)-per-(q,mu,k)
  error that §2.1's trivial treatment assigns to mu <= m_0 (the tangency
  sits exactly at mutilde ~ lambda P^2/Q^2 ~ m_0).
- Concrete failure: mu = p - lambda gives ||lambda (p^2+q^2)/(pq)|| =
  lambda d^2/(pq) (p = q+d), so ALL p with |d| < sqrt(pq)/(lambda sqrt(2)
  L^{B/2}) are (M1)-major — a "Pythagorean strip" of width ~ Q L^{-B/2} /
  lambda around p ~ q, for EVERY q. Per-q major count >= ~P L^{-B/2-1},
  versus prop:familyA's claimed P L^{C+1-B}: FALSE for large B. An E1
  analogue with the same bound P L^{1-B} for the sum branch is FALSE
  (the strip is a positive main-term-level count, linear in q — no
  q-average or cancellation can remove it).
- NUMERICALLY CONFIRMED (/tmp/sum_branch_probe.py, model x=10^10,
  P=Q=2154, L^B=30, lambda=1): predicted strip half-width 278 vs
  difference-diagonal ~18; observed per-q failures with mu<=4: sum branch
  66-129, difference branch 19-32 (the latter matching the budgeted main
  term ~P/L^B * density); the sum-branch excess matches the strip
  prediction (2*278/log P ~ 72) quantitatively.

**Classification: GAP** (not FATAL to the program; FATAL to the report's
headline scope). The recorded difference-branch machinery is untouched —
this is a scope-bridging error, but it guards the bridge from E1-flat to
"the form actually consumed downstream", which is exactly what the
verdict line claims.

**Minimal fix (route identified, checked for feasibility):**
(i) For mutilde >= C*m_0 the sum branch IS verbatim: g_+ is monotone on
(P,2P] (|g'| >= (mutilde Q/4P^2)(1-1/25) after the same m_0 sharpening),
one interval per (q,mu,k), endpoints linear in q, cognate resonance
identity with |2 lambda n - ts - lambda y| ~ s*Kbar (lambda n <= ts/50 as
before). (ii) For mutilde <= C*m_0: split (P,2P] at p* into two monotone
halves (run §2 verbatim on each, with one extra edge term at p*) and add
a NEW elementary tangency-strip count: per lambda there are O(1) exact
tangencies (need integer k ~ 2 lambda P/Q, so the regime is EMPTY for
u' > u + (C+1) loglog/log — only the u >= u' half-band is affected), each
contributing ~ Q mutilde^{-1/4} lambda^{-3/4} L^{-B/2} majors per q;
near-tangencies (dist Delta > delta) contribute the Delta-graded
two-interval windows, summing to L^{-B+O(1)} levels. Total new familyA
term: ~ P L^{-B/2 + O(C)} per q. (iii) Downstream: contribution
R * P L^{-B/2+O(C)} <= pi(P) R L^{-c-1} iff B >= 2c + O(C) + 6 — B is
free and chosen last; replace B = C+c+4 by B = max(C+c+4, 2C+2c+10) in
prop:digit-assembly and tighten the corner trim accordingly (polylog
cost, already-registered type). (iv) Manuscript: eq:conic must read
<mu> <= RL^{-B} with the +/- lambda p^2 branch; lem:branch needs a
sum-branch sibling whose error term carries the additional
delta^{1/2}-tangency term; hyp:E1/rem:E1-signed restated per branch.

**Downstream impact if unrepaired:** prop:familyA is false as stated (its
proof is incomplete AND its bound is exceeded by the strip), hence
prop:digit-assembly's major-side accounting fails on the u >= u'
half-band. With the fix, everything survives with the retuned B.

### E1 — other findings

**Finding E1-2 [CONSTANT].** §1.2/§7 claim the absorbed exponent A is
"absolute", but Lemma R carries L^{O(C)} (lambda-gcd factor) and the
lambda-sum costs L^C: A = O(C), not absolute. Harmless: B is chosen after
C anyway (B = C+c+4 already C-dependent). Minimal fix: say "A = O(C),
independent of B". No downstream impact.

**Finding E1-3 [COSMETIC].** Lemma R sketch step (ii) drops the residues
with lambda x^2 ≡ 0 mod s (where d_0 = s): adds rho_0(s)/s <=
4^{omega(s)} sqrt((lambda,s)/s)-scale — absorbed by step (iv)'s average.
Should appear in the owed write-up. (The report already owes the
p=2/squarefull/(lambda,s) cases; this joins them.)

**Finding E1-4 [COSMETIC].** psi-convention at integer window endpoints
(#((a,b] cap Z) vs closed windows) is an O(1)-per-clipped-window detail,
covered by the clip budget; needs one line in the write-up.

**Positive findings (E1):** the §2 decomposition, §2.1 closed-band
uniformity (u+2u' >= 1, 2u+u' >= 1, 5u+u' >= 2 all verified, each with
equality only at (1/3,1/3) and saved there by M_0's L^{-B}), the §3.2
resonance identity (re-derived exactly), F1-F5 (all re-proved), the term
zoo (all derivations reconstructed from #mu(J) <= 2mW g1/(|J|n) + 1
summed over the admissible-J AP of step s*g1 — coherent), Lemma R's
average structure, the n=0 and L^2 side-terms, the §3.3 diagonal
diagnostics and the retraction of the pair-cancellation cap, and the
machine ledger with its history — ALL CHECK. The difference-branch
E1-flat, which is the literal content of hyp:E1/lem:branch, stands at
PROVED-MODULO-write-up exactly as the report's §7 lists (items (i)-(iv)
confirmed as the genuine debts).

### E2 — side-findings and consumer audit

**SL2 side-finding: VERIFIED CORRECT.** Vinogradov's bound is
(P/sqrt(s) + P^{4/5} + sqrt(Ps)) log^{O(1)}P; the manuscript's lem:SL2
(12-e1e2.tex) wrongly has sqrt(s) for the third term. I recomputed
wp8-e2's claim at (1/3,1/2): worst truncated scale S = x^{1/6},
S(SQ/P+1) = x^{1/2}, max(sqrt(PS), P/sqrt(S), P^{4/5}) = x^{4/15} -> total
x^{23/30} > x^{2/3} = PQ/R. Confirmed: prop:E2's claimed sub-band
16u+10u' > 10 does NOT survive the corrected SL2 even at (1/3,1/2);
12-e1e2's prop:E2 should be retired (it is superseded by wp8-e2 anyway).
[Pre-existing manuscript error, GAP in 12-e1e2, no longer load-bearing.]

**Consumers of prop:familyB / hyp:E2 (grep, full manuscript):**
- prop:digit-assembly (08-major): tolerates the modified count — verified
  above (§5 of wp8-e2 is correct, including the honest extra 1/pi(Q) L).
- prop:C-cov(2) (14-lemmaC-reduction): uses prop:familyB "verbatim for
  p_2/p_1"; wp8-e2's Theorem is band-free (any P,Q with G_0 >= 8), so it
  applies verbatim there too; the extra L is absorbed by that section's
  B >= 2C+c+4 slack. OK.
- 07-minor rem:M2-strengthening still asserts parenthetically "the band
  average of D_R is O(L^2); Proposition familyB" — but familyB's own
  proof WITHDREW the band-average clause (for u > u' it is power-large).
  Pre-existing inconsistency to clean when familyB is restated
  unconditionally [COSMETIC, manuscript hygiene].
- 10-remaining.tex status tables: to be updated as wp8-e2 §5 suggests.

**E2 edge cases probed:** G_0 >= 8 needed and supplied (corner trim makes
G_0 >= L^{c+...}); if 2P/G_0 < 1 there are no witnesses and the bound is
trivial; structural-gap saturation (all q < p/G_0 failing) is consistent:
P > Q G_0/2 forces P^2 L^{B+2}/R > PQ L^2 — the P^2 term absorbs it. The
claim "valid at and through (1/3,1/3)" stands; trims enter only
downstream, as stated.

## Verdicts

### wp8-e2.md (E2): **UPHELD**
The Theorem (unconditional Family-B count, N_fail << PQ L^{B+1}/R +
P^2 L^{B+2}/R for all P,Q,R,B with G_0 >= 8) is correct; every step of
the proof checks (witness truncation, ordering of truncation vs
integer-relaxation, R1, R2, the modulus-p reciprocal sums, assembly).
prop:familyB becomes unconditional; hyp:E2 is discharged;
prop:digit-assembly tolerates the modified count with the same B and
trims, and so does the 14-lemmaC consumer. Repairs needed are trivial and
non-mathematical: E2-1 (log_2 x <= 2L, constant), E2-2 (say "non-final
convergent denominator" in the statement; fix CF-representation
convention), E2-3 (alpha in (0,1) hygiene — pre-existing). The "PROVED,
confidence ~0.9" self-assessment is justified.

### wp8-e1.md (E1): **UPHELD-WITH-REPAIRS** (one GAP-class, three minor)
For the literal Hypothesis E1 (= the difference-branch E_q of lem:branch,
signed/absolute form, integer-q relaxed): the report's route VERIFIES —
exact identities re-derived, F1-F5 re-proved, term zoo reconstructed and
coherent, Lemma R sketch sound, exponent ledger reproduced and robust
under adversarial re-scans (deeper t-grids, exact bottom shells, Lemma-G
ablation), Lemma R confirmed uniquely load-bearing. PROVED-MODULO-write-up
is a fair verdict FOR THAT STATEMENT, with the four self-declared debts
real but write-up-grade.
REQUIRED REPAIRS:
1. [GAP — mandatory before the headline claim stands] The sum branch
   (upper-half mu), claimed "cognate ... verbatim" in §1, is NOT: the
   q-independent tangency g_+(p*) = 2 sqrt(lambda mutilde) creates
   Pythagorean strips of (M1)-majors of width ~ Q L^{-B/2}/lambda for
   every q (verified analytically and numerically), so the
   downstream-consumed form (prop:familyA over ALL (M1)-failures) is NOT
   yet covered, and an E1-shaped bound P L^{1-B} is FALSE for that
   branch. Repair route (recorded above): monotone-split + new
   elementary tangency-strip count (~P L^{-B/2+O(C)} per q, u >= u'
   half-band only) + retune B to max(C+c+4, 2C+2c+10); manuscript fixes
   to eq:conic / lem:branch / hyp:E1. Until done, the report's verdict
   must be read as "difference branch proved-modulo-write-up; sum branch
   open with identified route" and confidence for the headline scope is
   materially below the stated 0.7.
2. [CONSTANT] A = O(C), not absolute (E1-2).
3. [CONSTANT/COSMETIC] Scanner hygiene: delete the dead, mis-encoded
   Lemma-G SING branch; fix the stale Vaaler docstring (E1 scanner items
   1-3 above).
4. [COSMETIC] Lemma R rho_0/s case; psi endpoint convention (E1-3/4).

### Cross-cutting note for the program ledger
The manuscript itself (not the prover reports) carries two errors
surfaced here: eq:conic's "exactly" (missing sum branch — the source of
E1's GAP) and lem:SL2's sqrt(s) (should be sqrt(Ps), killing prop:E2's
claimed sub-band — moot once wp8-e2 lands). Both should be fixed in the
same edit that restates prop:familyB unconditionally.

