# WP10 Verification: Gap G1 closure (wp10-g1.md)

**Verifier:** adversarial referee pass, 2026-06-10.
**Target:** wp10-g1.md claims G1 CLOSED-MODULO-write-up.
**Status:** COMPLETE. **Verdict: UPHELD** (one CONSTANT-class statement
repair mandatory at transcription; rest cosmetic).

## Checklist
- [x] (0) Rerun probe wp10_g1_probe.py with .venv/bin/python — REPRODUCED
- [x] (1) Exact identity behind Lemma B+ ((T-exp)); tangency-term exponents — CORRECT
- [x] (2) Lemma T (≍ sqrt(m) perfect-square saturation); S5 <= c5 P L^{-B/2} per (q,lambda); dyadic bookkeeping — CORRECT
- [x] (3) Cognate-identity transfer (sign-free) — VERIFIED, incl. scanner read + rerun (full pass)
- [x] (4) Corner emptiness at (1/2-,1/3) and (1/3,1/2-) — VERIFIED, incl. the wrong-reason correction of wp9's 6c-ii
- [x] (5) Downstream deltas / lb-track per-q worst case with no average — VERIFIED

## Findings

### (0) Probe reruns — REPRODUCED EXACTLY
`.venv/bin/python wp10_g1_probe.py` (log /tmp/wp10_verify_probe_rerun.log):
- Part 2: max obs/(main+four+T+5) = 1.678; without T = 10.280 at
  (lam,nu) = (2,2), obs 518 vs ~45 — matches §5.2's "1.68 / 10.3"; 36
  exact-tangency cells; (1,1) cells obs/T in [1.07, 2.01]. MATCH.
- Part 3: (0.40,0.36) strips at nu=1,4 (exact t*), graded nu=2,6;
  obs/T <= ~2.0 throughout; clipping at p* < P behaves as claimed. MATCH.
- Part 4: (0.48,0.34) m_*=631.4 > 16 M_0, 0 tangency hits, obs 3143 vs
  pred 3270; (0.34,0.48) 0 hits, obs 128 vs 205. MATCH.
- Part 5: 0/0 grid violations (41x41 closed band); budget slack
  min B/2-(C+c+3) = 2.0. MATCH.
- Part 7: resonance identity max rel. error 1.10e-38 at 50 digits. MATCH.
- Verifier's original /tmp/sum_branch_probe.py rerun: per-q sum-branch
  failures {66,...,129}, diff 19-32, ratio 4.0, predicted half-width
  278.1 — verbatim the wp9-verify-e1e2 E1-1 numbers. MATCH.

### (1) Lemma B+ / (T-exp) identity and tangency exponents — RE-DERIVED, CORRECT
- t* = g_+(p*) = 2 sqrt(lambda nu): direct computation. EXACT.
- (T-exp): g_+(p*(1+v)) - t* = sqrt(lambda nu)[(1+v) + 1/(1+v) - 2]
  = sqrt(lambda nu) v^2/(1+v). EXACT (algebra checked).
- Lemma S1: g_+' = (lambda/q)(1-(p*/p)^2) and -g_+' = (nu q/p^2)
  (1-(p/p*)^2); the [3/4,1]-comparabilities for p outside [p*/2,2p*] and
  both parenthetical slope-scale equivalences (p* < P/2 => nu q/P^2 <=
  lambda/(4q); p* > 4P => lambda/Q <= nu q^2/(16P^2 Q)) all re-derived
  from p*^2 = nu q^2/lambda. CORRECT.
- Lemma S2: F(v) = sqrt(lambda nu) v^2/(1+v) on [-1/2,1]; F >= v^2
  sqrt(lambda nu)/2 (needs 1+v <= 2: true); |F'| = sqrt(lambda nu)
  |v|(2+v)/(1+v)^2 with (2+v)/(1+v)^2 decreasing, min 3/4 at v=1 >= 1/2;
  on the D >= 2delta window |v| >= (1/2)sqrt(D/sqrt(lambda nu)) from the
  one-sided bounds F <= sqrt(lambda nu)v^2 (v>0) / <= 2 sqrt(lambda nu)v^2
  (v<0); hence |F'| >= (1/4)(lambda nu)^{1/4} sqrt(D); window v-length
  <= 8 delta (lambda nu)^{-1/4} D^{-1/2}. All steps CORRECT.
- T-term exponents: p* (lambda nu)^{-1/4} = q nu^{1/4} lambda^{-3/4}
  identically, so T = q delta nu^{1/4} lambda^{-3/4}
  max(||2 sqrt(lambda nu)||, delta)^{-1/2} is RIGHT; necessity confirmed
  by probe (10.3x violation without T).
- Height bookkeeping above t*: nearest k above outside the delta-window
  has height >= max(||t*||, delta) (either ||t*|| or 1-||t*|| >= 1/2);
  J <= F(1)+delta+1 <= sqrt(lambda nu)+1 (F(±1/2 resp. 1) =
  sqrt(lambda nu)/2); sum_j (D_0'+j)^{-1/2} <= 2 sqrt(J); AM-GM
  sqrt(lambda nu) <= (nu Q/P + lambda P/Q)/2. All CORRECT.

**Finding G1-V1 [CONSTANT].** Lemma B+ as STATED (N_q^+ = 2 delta P +
E_q^+, |E_q^+| ≪ four-terms + T) is stronger than what the recorded
proof establishes in the case p* in [P/2,4P]: the band∩Z accounting
upper-bounds the non-tangent Z-windows by 16 p* delta <= 64 delta P,
which is NOT ≪ four+T when lambda nu is large (T can be as small as
~delta P (lambda nu)^{-1/4}); and no lower bound on the Z-zone count is
proved at all. What IS proved: N_q^+ <= 2 delta P + O(delta P)·
1_{p* in [P/2,4P]} + O(four + T), plus the two-sided form off the
tangency zone. Probe data shows the slack is real (e.g. (0.40,0.36),
q=6533, nu=5: obs=0 vs main 66.7 with four+T = 60). Minimal fix: add
the term delta P · 1_{p* in [P/2,4P]} to |E_q^+| (or state the
tangency-zone case as a one-sided ≪ bound). Downstream impact: NONE —
every consumer (lb-track §4.4, S5, hyp:E1+) only uses upper bounds and
already sums sum_nu delta_nu P ≪ P L^{1-B}; the extra O(delta_nu P) over
the single dyadic block nu ≍ m_* adds ≪ P L^{-B} per q. Checked each use.
(Also factor-2 slips: two v-sign intervals per k counted once in the
B+ proof display; <=2 integers possible in [t*-delta, t*+delta] when
delta = 1/2 exactly — both absorbed by implied constants.)

### (2) Lemma T + S5 assembly — RE-DERIVED, CORRECT (one statement nit)
- Lemma T: image length 7.5 sqrt(lambda m) <= 8 sqrt(lambda m); per-k
  nu-length <= 8 Delta sqrt(m/lambda); product expansion 64 Delta m +
  8 sqrt(lambda m) + 8 Delta sqrt(m/lambda) + 1 with third term <= 8
  Delta m; trivial cap 16m. Case split (lambda <= 4m vs > 4m) gives the
  min(m, sqrt(lambda m)) form with c0 <= 72. CORRECT.
- Sharpness: lambda=1, nu=j^2, j in [sqrt(m)/4, 4 sqrt(m)]: ≍ sqrt(m)
  EXACT tangencies — so wp9-verify-e1e2's repair-sketch phrase "O(1)
  exact tangencies per lambda" was indeed WRONG, as wp10-g1 claims; the
  wp10 critique and its min-form repair are correct.
- S5 dyadic bookkeeping: delta_nu in [1/(32 m_* L^B), 8/(m_* L^B)] on
  nu ≍_16 m_* (checked); shells Delta dyadic: Delta^{1/2} m_* sums
  geometrically UP to Delta = 1/2 (≪ m_*), (min+1)Delta^{-1/2} sums
  geometrically DOWN to delta_min (≪ (min+1) delta_min^{-1/2}); bottom
  shell included. CORRECT (standard cumulative-count-per-shell upper
  bound; valid for upper bounds).
- Exponent algebra, all three pieces re-derived independently:
  (a) q lambda^{-1/2}(P/Q)^{1/2} L^{-B} <= 4P lambda^{-1/4} L^{-B}
  via sqrt(Q/P) < 2 lambda^{1/4} (from p* >= q/sqrt(lambda) <= 4P when
  S5 != 0); (b) Q<=P: min = sqrt(lambda m_*) = lambda P/Q, term =
  q (P/Q)^{1/2} L^{-B/2} <= 2 sqrt(PQ) L^{-B/2} — LAMBDA-FREE; Q>P:
  min = m_*, term = q (P/Q)^{3/2} L^{-B/2} <= 2P (P/Q)^{1/2} L^{-B/2}
  — LAMBDA-FREE; (c) q lambda^{-1}(Q/P)^{1/2} L^{-B/2} <= 16 P
  lambda^{-1/4} L^{-B/2} (doc says 8 — constant nit, absorbed).
  Hence S5(lambda) <= c5 P L^{-B/2} per q, S5_tot <= c5 P L^{C-B/2}:
  CORRECT, per-q worst case, no average anywhere.
- The L^{C/4}-loss claim for the naive sqrt(lambda m_*)-only Lemma T:
  re-derived (Q>P case would give q(P/Q)^{1/2} <= 4P lambda^{1/4},
  lambda-sum ~ L^{5C/4}): CORRECT — the min refinement is load-bearing
  exactly as claimed.
- m_* < 1/16 => no integer nu in M_T => S5 = 0; Lemma T's m >= 1
  hypothesis is never violated in use (the +1 covers m_* ≍ 1). OK.

### (3) Cognate-identity transfer to wp8-e1 — VERIFIED sign-free
- Exact identity re-derived from scratch: with lambda c^2 - tc + nu = 0
  (small root, 2 lambda c - t = -sqrt(t^2-4 lambda nu)), n = sc - y:
  lambda n^2 - tsn + nu s^2 = y(s(t - 2 lambda c) + lambda y)
  = y(s sqrt(t^2-4 lambda nu) + lambda y); with t = k ± delta this is
  J ∓ sigma, J = nu s^2 - ksn + lambda n^2, sigma = delta sn. EXACT;
  probe Part 7 confirms to 1e-38.
- Scan-regime geometry: nu > 6400 m_0 >= 6400 m_* gives p* =
  q sqrt(nu/lambda) > 80P (re-derived); band entirely on the decreasing
  small-root side; the large root c^{(+)} q > p* > 80P sits outside the
  band — only ONE interval per (q,nu,k), mirroring lem:branch. CORRECT.
  (§2's root-labeling: small root on p < p* — checked, the §6 item-1
  self-correction is right.)
- Two-sided factor ≍ s Kbar: 4 lambda nu/t^2 <= 16 m_*/nu <= 1/400;
  lambda|y| <= lambda/s <= lambda n <= ts/50 (ratio lambda c/Kbar =
  m_*/nu modulo constants <= 1/800). CORRECT.
- F1-F5, AP structure, Lemma R sign-freeness re-checked individually:
  F1 divisibility s(s,n)|lambda n^2 identical (sign of RHS irrelevant);
  F2 g1^2|(s^2, sn, n^2); F3 |J| >= 1 quantization sign-free; F4/F5
  properties of c and of sigma(nu) only; the nu-AP nu s^2 ≡ J - lambda
  n^2 (mod sn) has the same step and count; Lemma R needs rho_a for
  a = +lambda n^2 instead of -lambda n^2 — the 4^omega sqrt((a,s)) bound
  is sign-symmetric since (a,s) = (-a,s). ALL SIGN-FREE as claimed.
- e1_exponents.py read in full: encodes m, K = mQ/P, h, Nbar =
  max(h x^{u-u'},1), sigma, W-shells, weight K/W, terms A/J0/JA/JB/J2/
  SING/B2/CAPC — magnitudes only; no sign of the lambda n^2 term enters
  any formula. Scanner rerun: see (0)/(5.6) below. The transfer claim
  "ledger applies literally" is SOUND, and correctly inherits (not
  improves) wp8-e1's write-up debts (D1) — the report is honest that
  E1+ is only at E1-flat's grade.
- The flagged wp8-e1 §2.1 patch (add Q/P to the max in the trivial
  regime) re-checked: mu Q/P <= max(1, lambda P/Q) indeed FAILS when
  m_0 = 1 < Q/P; the conclusion survives since M_0 Q/P = P x^{1-3u}
  L^{-B} <= P L^{-B} on the closed band (u >= 1/3). COSMETIC, correctly
  classified.

### (4) Corner emptiness — VERIFIED, including the wrong-reason correction
- (1/2-,1/3)-type: m_*/16 > M_0 ⟺ lambda x^{3u-u'-1} > 16 L^{-B};
  3u-u'-1 = 1/6 > 0 at (1/2,1/3) (0.10 at the probe point (0.48,0.34)),
  power-large vs polylog for every lambda >= 1: M_T ∩ [1,M_0] EMPTY.
  Probe: 0 tangency hits, totals at pure main-term level. CORRECT.
- (1/3,1/2-)-type: existence needs Q/P = x^{u'-u} <= 4 sqrt(lambda)
  (from p* >= q/sqrt(lambda) <= 4P with nu >= 1); x^{1/6}-power-large
  vs 4L^{C/2}: EMPTY. Probe: 0 hits. CORRECT.
- The correction of wp9-theorem1prime 6c-ii's parenthetical is RIGHT:
  "need integer k ≍ 2 lambda P/Q >= 1" is a bogus reason (t* =
  2 sqrt(lambda nu) >= 2 always, so a nearby integer always exists; and
  2 lambda P/Q >= 1 is weaker than Q <= 4P sqrt(lambda) for lambda > 4).
  The binding constraints are integer nu >= 1 in M_T (p*-in-band) and
  m_* <= 16 M_0; wp9's reason also misses the second entirely — which is
  the one that empties the (1/2-,1/3) corner. wp10's restatement should
  replace 6c's parenthetical, as its downstream-deltas section says.
- Cell relevance double-checked: at u = u' = 1/2 - 2eta, 3u-u'-1 =
  -4eta < 0 and u' - u = 0, so strips DO exist on the lb-cell — S5 is
  genuinely needed there; G1 could not have been dodged by emptiness.

### (5) Downstream deltas / lb-track per-q claim — VERIFIED
- Per-q worst case, fixed (q,lambda): lem:branch (per-q, unconditional)
  + Lemma B+ (per-q, unconditional) + S5(lambda) <= c5 P L^{-B/2}
  (per-q, unconditional). NO q-average is used anywhere in the lb-track
  chain; hyp:E1/E1+ enter only the asymptotic track. The quoted per-q
  list P L^{1-B} + (R^2Q/P)L^{-2B} + lambda(PR/Q)L^{-B} + R L^{-B} +
  P L^{-B/2} matches 6c's ledger doubled plus the new term; edge term
  sums ≪ P L^{-B} unconditionally via AM-GM (nu Q/P^2 + lambda/Q >=
  2 sqrt(nu lambda)/P). CORRECT.
- Budget: damage R x P L^{C+1-B/2} <= pi(P) R L^{-c-1} needs B >=
  2C+2c+6+O(1); B = max(C+c+4, 2C+2c+10) gives uniform slack L^2 (probe
  Part 5, min slack exactly 2.0). The headline B in wp9-theorem1prime
  (line 28) already carries this value — no downstream statement changes.
- B-monotonicity sweep re-checked: cor:minor (B >= c+4), T1 (B >= 2c+8),
  familyB consumer (R >= L^{B+c+4}, implied by the tightened corner trim
  sqrt R >= L^{C+2c+10}), M_0 and delta_mu shrink (failures rarer),
  (M2*) threshold monotone. The one paying consumer is the corner trim
  — polylog, O(eta'')-registered, as stated. CORRECT.
- prop:familyA sparsity threshold B >= 2C+2c'+4 and the eq:conic'
  bijection mu <-> (nu,eps) (valid since nu <= RL^{-B} <= P L^{-B} <
  p/2): both check. eq:conic' uses <= where failure is strict-< — D5
  flags it; harmless for upper bounds [COSMETIC, already flagged].
- Minor nit: 08-major's "damage control" remark (B >= c+C+2) must be
  retuned in the same edit batch; wp10-g1's delta list does not name it
  explicitly (it is subsumed by the prop:digit-assembly delta)
  [COSMETIC].

## Findings summary (classification, minimal fixes)

| # | Class | Finding | Minimal fix | Downstream |
|---|-------|---------|-------------|------------|
| G1-V1 | CONSTANT | Lemma B+ as stated (N = 2 delta P + E, \|E\| ≪ four+T) overclaims vs the recorded proof in the tangency-zone case: the non-tangent Z-window total is only bounded by 64 delta P (not ≪ four+T when lambda nu large), and no lower bound on the Z-zone count is proved | Add delta P · 1_{p* in [P/2,4P]} to the stated \|E_q^+\| bound, or state the tangency-zone case one-sided (N ≪ delta P + four + T) | NONE — all consumers use upper bounds and already sum sum_nu delta_nu P; extra mass ≪ P L^{-B} per q |
| G1-V2 | COSMETIC | Constant slips in B+ proof/S5: two v-sign intervals per k counted as one (factor 2); two integers possible in [t*-delta, t*+delta] at delta = 1/2; term (c) constant is 16 not 8 | absorb in implied constants at write-up | none |
| G1-V3 | COSMETIC | 08-major "damage control" remark (B >= c+C+2) needs the retune too; wp10-g1's delta list subsumes but does not name it | add to the §4 edit batch | none |
| G1-V4 | COSMETIC | eq:conic' boundary (<= vs strict <) — already self-flagged as D5 | one line | none |

Positive verifications (all load-bearing items): (T-exp) exact; S1/S2
slope and width bounds correct; T-term exponents q delta nu^{1/4}
lambda^{-3/4} max(||2 sqrt(lambda nu)||, delta)^{-1/2} right and NECESSARY
(probe: 10.3x violation without T); Lemma T correct with c0 <= 72 and
SATURATED by the perfect-square family — wp10-g1's claim that the prior
verifier's "O(1) exact tangencies" was wrong is itself CORRECT, and the
min(m, sqrt(lambda m)) refinement is genuinely load-bearing (avoids
L^{C/4} on the u' > u sliver — re-derived); S5(lambda) <= c5 P L^{-B/2}
per q with all three exponent splits re-derived; sum-branch resonance
identity exact (re-derived + 1e-38 numerics); F1-F5/AP/Lemma-R transfer
sign-free (each fact re-checked); scanner read in full (magnitudes only)
and rerun FULL PASS; corner emptiness at both off-diagonal corners with
the CORRECTED reasons; strips present on the lb-cell (3u-u'-1 = -4eta <
0) so S5 is genuinely needed there; lb-track per-q count uses NO average
anywhere; B = max(C+c+4, 2C+2c+10) gives uniform slack L^2 and all other
B-consumers are monotone-safe (re-swept: cor:minor, T1, familyB, trims).

The report's own adversarial discipline checks out: its §6 items 1-3
(root labeling, sigma sign, the (1/2,1/3) trivial-regime save via M_0
rather than 3(u-u') < u) are all correctly resolved in the final text.

## Verdict

**UPHELD.**

wp10-g1.md's headline — Gap G1 CLOSED-MODULO-write-up, with the lb-track
per-q worst-case piece at statusP-grade (Lemma B+ + Lemma T + S5 <=
c5 P L^{C-B/2} per q, B retuned to max(C+c+4, 2C+2c+10)) and the
asymptotic piece at exactly wp8-e1's PROVED-MODULO-write-up grade via the
sign-free transfer — is correct as stated. Every exact identity was
re-derived independently; every exponent split was re-derived; all
numerics reproduced bit-for-bit; the scanner was read for sign-dependence
and rerun (full pass). The single mandatory repair (G1-V1) is a one-line
statement weakening of Lemma B+ in the tangency zone with zero downstream
impact; the report's stated confidences (0.85 lb-track / 0.7 asymptotic)
are reasonable, the latter correctly capped by wp8-e1's base. Gap table
G1 may move to CLOSED-DRAFT (verified) with G1-V1 folded into the
lem:branch-plus transcription.

Logs: /tmp/wp10_verify_probe_rerun.log, /tmp/wp10_verify_scanner.log.
