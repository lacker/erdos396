# Roadmap — $n(n-1)\mid\binom{2n}{n}$ Program

**v0.4, June 9, 2026.** This file holds strategy, sequencing, risk, and everything without a home. Mathematical content lives in the per-lemma documents; sources live in `citations.md`. Supersedes the single-file v0.3.

## Document map

| File | Status at a glance |
|---|---|
| `lemma-0-sandwich.md` | PROVED + written; 0′ margins PROVED (manuscript §§3,15) |
| `lemma-A-small-primes.md` | PROVED — written (manuscript §15) |
| `lemma-B-anatomy-independence.md` | ASSEMBLED (manuscript §13) mod TT+SL2′ (~97%) |
| `lemma-C-within-side.md` | DIAGNOSED (WP3): core = two-frequency machinery; lit pinned (~85–88%) |
| `lemma-D-cross-side.md` | OPEN — the hard core (~25–30% full / ~60% lower-bound after weakened pass) |
| `prop-deep-large-sieve.md` | PROVED June 9, numerically verified |
| `numerology-D.md` | WP1.4 ANALYSIS COMPLETE |
| `empirics-D.md` | WP1.5 COMPLETE — **G1: PASS** |
| `lemma-alpha-beta.md` | WP2.0: $\alpha,\beta$ PROVED; assembly NEGATIVE; D† defined |
| `wp21-reduction.md` | WP2.1: two-frequency reduction, validated |
| `wp22-minor-major.md` | WP2.2: D†-digit closed modulo write-up |
| `wp23-anatomy.md` | WP2.3: anatomy layer PASS — elementary unwinding; **no structural obstruction left on D** |
| `wp24-e1-e2-fineclass.md` | WP2.4: E1/E2 diagnosed LOW-RISK (signed form suffices, true in data); fine-class check PASS |
| `wp5-diagnosis.md` | WP5: constructive-route diagnosis — FQ convergence, entropy obstruction, $k=2$ rung viable |
| `wp3-lemma-C-diagnosis.md` | WP3: C's core = D's machinery; GS/DGS pinned; FI retired; major arcs absorb into main term |
| `citations.md` | ledger; verification statuses inside |

## Targets

- **Theorem 1″ (rung i, realistic form):** density of $W_1=\{n:n(n-1)\mid\binom{2n}{n}\}$ equals $c_1^2+O(\log^{-c}x)$ at almost all scales $\Rightarrow$ infinitude + log-density $c_1^2$ ($c_1=0.11424$, Ford–Konyagin). As far as our review found, even infinitude of $W_1$ is not in the literature.
- **Theorem 1′ (rung i-minus):** positive log-density lower bound, via Lemma D's mitigations.
- **Rung ii:** conditional paper — "pair density $=c_1^2$ modulo Estimate D\*" with everything else proved. Locked in barring surprises.
- **Rung iii:** machinery feeds the constructive (Balog–Wooley-style) track for literal Erdős 396, general $k$.

Assembly: Lemma 0 (sandwich) reduces Theorem 1 to independence of $D_0$ and its shift; A×B×C×D with error bookkeeping gives Theorem 1″.

## Dead-ends registry (program-wide; proofs of death recovered — do not repay)

Union bounds across the digit layer (failure mass $\Theta(1)$). Smooth-cofactor designs ($\rho(c/\delta)$ vs $e^{-c/\delta}$ — also explains the Tier-B $m^2$ disappointment). Semiprime trick (dies on the prime case). D-specific dead ends: see `lemma-D-cross-side.md` §8.

## Work packages (hardest first; de-risk before prove)

**WP1 — Lemma D de-risk (in progress).**
- WP1.1 Formal Estimate D\* — **DONE in reduced form** (`lemma-D` §2); formal LaTeX pending.
- WP1.2 TT/Pilatte verdict — **DONE** (`lemma-D` §4).
- WP1.3 Deep large sieve writeup — **DONE June 9** (`prop-deep-large-sieve.md`).
- WP1.4 Numerology table — **DONE June 9** (`numerology-D.md`). Headline: required savings are only logarithmic; no exponent gap on average over the band; gap = three adaptation lemmas ($\alpha,\beta,\gamma$) + the bilinear assembly ($\delta$). G1: leaning PASS pending WP1.5.
- WP1.5 Band empirics — **DONE June 9** (`empirics-D.md`): square-root cancellation on real coupled populations at five strata; conditional structure of D confirmed; one flag at smallest harmonics / top of band. Original design (kept for re-runs at larger $x$): $T_q(\lambda)$ over real band populations ($\sim$5 primes $q\in[10^3,10^4]$, inner populations $10^4$–$10^5$), $|T|/\sqrt{N_{\text{class}}}$ vs benchmark, stratified by $\gamma$ (top stratum = diagnostic), phase-aligned $\sum_qS(q,h)$ per stratum, $E_q$ validation near $10^9$. ~1 day compute.
- WP1.6 **Gate G1: PASS (June 9; basis revised same day).** Original numerology basis partially withdrawn (Erratum, `numerology-D.md` §9); pass retained on: empirics directly on D†'s object + log-target, parity-free residual with a named second-moment core. → **WP2 is live.**

**WP2 — Prove D** (post-pass): toolkit (a) deep large sieve + bilinearity + $q$-averaged Wieferich counting; (b) tailored $(q,\lambda)$-averaged mean-value theorem (the flagged main question); (c) re-weighted Pilatte engine.

**WP2′ — Lower-bound theorem** via the four mitigations (`lemma-D` §7).

**WP3 — Lemma C: DIAGNOSIS DONE (June 10; `wp3-lemma-C-diagnosis.md`).** The thin-progression core ≡ the two-frequency machinery (change of variables; the λ-free case, strictly simpler than D†); major arcs are absorbed into the main term (empirically: resonant ensemble z 13.1 → 0.78 under Liouville); weighted layer on GS ($x^{20/39}$) + DGS smooth-supported ($x^{3/5}$) + Daboussi–MV. FI dependency retired. Remaining: the formal reduction, S–W check for $g_z$ (shareable with B0), Daboussi–MV quantitative form, FK gluing, pretentious main-term bookkeeping. C: ~85–88%.

**WP3b — Close Lemma B: CHECKS DONE (June 9 late evening).** TT Thm 3.1 fetched from the v2 TeX source and verified: all three fine-print checks pass (uniformity in $x$-dependent functions YES — constants absolute, hypotheses quantitative; conclusion shape YES — centered correlation + their $\delta_N$ remark gives product of means; verbatim statement retrieved, now in `lemma-B-anatomy-independence.md` with the technical condition checked trivially for our $g_z$). Lemma B0 (the equidistribution axiom for $g_z$) proof-sketched with defect $O(\sqrt N\,\mathrm{polylog})$ — ample. Remaining: write B0 formally + the $\le3$-band-prime bookkeeping. Lemma B: ~85% → **~95%**.

**WP4 — Manuscript spine: SPRINT DONE (June 9 evening).** `manuscript/main.tex` (+ 12 section files, compiles via `tectonic main.tex`) now holds, with full proofs: Kummer prelims, **Lemma 0** (exact sandwich, precise margin sets fixed), the **deep large sieve** (Props 1–2, Thm, Cors incl. the generalized AP version), **lemma β**, **linearization**, **large-λ coverage**, the **two-frequency reduction**, the **D†-minor bound (corrected — see below)**, the **anatomy unwinding**; plus precise statements with status tags for Lemmas A/B/C/D, Estimate D†, the major-arc counts modulo **Hypotheses E1/E2** (now precisely stated), lemma α (appendix), the numerics record (appendix), and the exhaustive remaining-gaps ledger (§10). *(The "lost" originals were also recovered from the chat export into `archive/original-session/`; full transcripts in `archive/transcripts/`.)*

**WP4 finding (erratum-grade, recorded in `wp22-minor-major.md` §0):** writing the D†-minor proof showed the WP2.2 statement was wrong twice over — single-scale (M2) misses small-scale convergent-gap "grazes," and the polylog conclusion is structurally false for $u>u'$ (the $s{=}1$ gap). Corrected form: a Diophantine-functional bound $|V_p|\ll L^{B+3}(1+\mathcal D_R)+L^2R/s_0$, minor set by all-scale gap-ratio threshold $RL^{-B}$ (structural gap auto-exempt under the top trim), minor-set worst case $\sqrt R\,L^{O(1)}$ — **within budget with room**; Family B recounted, still sparse. Conclusion-level WP2.2 claims survive. The draft-the-proof discipline has now caught an overcount twice (WP2.0, WP4).

**WP11 — E3-lb session (June 10/11, overnight): NOT CLOSED — reduced to one bespoke estimate; six sub-results, two errata.** The ladder: range table → (ii-a) pointwise OBSTRUCTED (Pólya–Vinogradov barrier; Korolev 2018 pinned as the right citation) → (b1)/(b2) citation bridges DEAD (frontier "power room" withdrawn = **erratum 5**) → (b3) absorption VIABLE conditional on a first-moment count → first-moment Steps A–C: reduction + bound (*) PROVED via an exact reciprocity flip + Korolev (DFI killed on normalization); **erratum 6** (mine): the §4.2 budget line refuted → Step D (ℓ-average): OBSTRUCTED — **absolute values close at NO single-variable level, band-structurally** (deficit $x^{1/4-2.25\eta}$ ∀η<1/9). **Unique survivor: a bespoke bilinear dispersion estimate for the first moment (the §3 ladder), feasibility floor verified (room $x^{0.15}$), all single-variable routes carry proofs-of-death.** E3†-proper demoted to fallback behind it. Calibration: Theorem 1′ ~70% → **~60%** (the "weakest demand" was not weak; truth-evidence unchanged, route now unique and bespoke). Next options: the bespoke dispersion (dedicated session), or C†-single-lb first (the other open item).

**WP10 — Gap G1: CLOSED (June 11; attack `wp10-g1.md` UPHELD by `wp10-verify-g1.md`, one one-line CONSTANT repair owed).** Corrected eq:conic (± branch); Lemma B+ with tangency term (verified necessary, 10× violation without); spacing Lemma T (and the prior verifier's own O(1)-tangency claim was confirmed wrong — errors get caught in both directions); per-q worst-case count, **no average needed** — the lb-track keeps E1/E2-freedom. B = max(C+c+4, 2C+2c+10) with L² slack. **Theorem 1′ now needs exactly two mathematical items: E3-lb (citation-adjacent) and C†-single-lb(g₀), plus writing.** Calibration: Theorem 1′ ~65% → **~70%**.

**WP9 — Verification + audit + assembly + frontier: DONE (June 10/11, overnight). Five-item session, all reports in repo.**
1. **Verification:** E2 **UPHELD** (now proved, full band); E1 **UPHELD-WITH-REPAIRS** (difference branch verified; sum-branch tangency gap found = G1, repair route named); E3's T1 **UPHELD** (two polylog-cheap lb-restatements); C† report **UPHELD** end-to-end.
2. **B=0 audit (`wp9-b0-audit.md`):** minimal lower-bound hypothesis list = **{E3-lb two-sided, C†-single-lb(g₀)}** — E1/E2 not needed on the lb-track (modulo the named per-q sum-branch count G1); scope bug fixed (C† floor 3/10); all restrictions positive-proportion (κ_lb ≈ 1.4e-5).
3. **Theorem 1′ chain (`wp9-theorem1prime.md`):** 11 links, each tagged; minimal TODO = 2 mathematical items (the two lb-hypotheses) + G1 + 6 writing items. **The infinitude theorem is now a two-problem program.**
4. **Frontier (`wp9-frontier.md`):** E3† is **CITATION-ADJACENT** (~0.6) — Bourgain/Baker/Korolev prime-variable Kloosterman covers the hard sub-range with power savings; remaining: BFI-grade reduction + one thin seam at Λ≈Q. C†'s D3-twin stays NEW-MATHEMATICS.
5. **Consolidation:** empirics re-run at x=10⁹ (`empirics-1e9-output.txt`): cross-band aggregate z=1.23 clean; top-of-band λ=1 reading is the known μ/λ=1 major arc.
Calibration: **Theorem 1′ (infinitude): ~65%** (two named second-moment objects + G1, one citation-adjacent) · rung i full: **~45%** (E3† citation-adjacent; C†-core still new-math) · rung ii: ~90% (hypotheses now sharply stated and verified-sharp).

**WP8 — Parallel attack on the four hypotheses: DONE (June 10, night). Reports `wp8-*.md`, all DRAFT pending verification (WP9).**
- **E2: PROVED unconditionally, full band** (~0.9): witness truncation $s<p/G_0$ empties all large scales; prop:familyB closes elementarily. Hypothesis discharged by bypass.
- **E1: PROVED-MODULO-write-up** (~0.7): the prime aspect was never needed (upper bound on the excluded set suffices); pure lattice counting via CF convergents; sole input = Lemma R (averaged root counts of quadratic congruences, elementary, sketched); exponent ledger machine-verified on the closed band; the diagonal sits exactly at budget — E1 is sharp.
- **E3: PARTIAL, major reduction**: new unconditional Theorem T1 (everything except polylog-many small frequencies, pointwise, no q-average, no Weil); machine-checked root-sum reduction; residual = **E3†** (pair correlation of congruence roots at fixed μ — DFI/BFI frontier); $u+2u'>1$ is FAVORABLE on the root side ($A<Q^2$). Lower-bound variant E3-lb: Chebyshev on T1.
- **C†: BFI-dispersion angle NEGATIVE** (proof-of-death, deficits quantified): residual core **unifies with D†'s second-moment core** (bilinear Kloosterman over primes, `lemma-alpha-beta.md` §5) — the program's two hardest objects are one problem. Lower-bound track: a single Chebyshev-grade second moment suffices; majors discarded; flagged audit (B=0 consumers) may remove C† from the lb-track entirely.
**Net: if WP9 verification upholds E1/E2, the digit layer is unconditional; the lower-bound theorem (infinitude!) needs only E3-lb + the C†-lb second moment (or its removal). Full rung i still gated by E3†/C†-core (one unified frontier object). Next: WP9 = verify wp8 reports; then the B=0 consumer audit; then E3†.**

**WP7 — Adversarial verification pass: DONE (June 10, late). ERRATUM #3 — the largest.** Four independent verifier agents refereed the fast-written manuscript. Findings: (i) §7 minor theorem SURVIVES (one rigor gap repaired, constants only); (ii) §15's elementary proofs had three fatal defects — all repaired in place (Chernoff/conditioning; Lemma 0′ and Lemma A now genuinely proved); (iii) §12's E1 proof was fatally flawed and E2's holds only on the upper sub-band — **both revert to open hypotheses** (partial results + named routes retained); (iv) **the big one**: the "classical toolbox" classification of D†-anatomy and weighted-C was wrong at the band-arithmetic level — $u+2u'>1$ and $u+u'>2/3$ ALWAYS, so every *weighted* object lives beyond the square-root barrier (BFI/dispersion frontier), and the small-Λ regime never existed. New structural hypotheses: **E3** (anatomy dispersion, manuscript §11) and **C†** (twisted dispersion at conductor $p^2$/bifactorable moduli, §14). The unweighted digit layer is untouched (its exact geometric sums are the wall's one exception). Both E3 and C† are empirically true with square-root room, parity-free, and adjacent to the deep-large-sieve toolkit. Calibration: rung i **65% → ~40%** (the draft-then-verify discipline has now caught major overcounts four times; the truth-evidence is unchanged, the proof distance was underestimated). Rung ii ~93% → ~85% (the conditional paper now carries four hypotheses, but they are sharply stated and well-evidenced).

**WP6 — Consolidation II: DONE (June 10).** The five-item execution list landed in the manuscript: §11 anatomy ranges glued (Type-II computation written; no range gap; extreme range = cited Vinogradov input); §12 E1/E2 PROVED modulo classical SL1/SL2; §13 Lemma B assembled (interpolation + B0 full proof + S–W modulo SL2′); §14 Lemma C formally reduced (two-frequency change of variables proved; DMV/Halász/GS inputs named); §15 Lemma 0′ PROVED in full, Lemma A PROVED, depth packaging (D5) stated-with-isomorphic-proofs, assembly cascade PROVED given A–D. The ledger (§10) now contains only citation debts and mechanical write-ups — zero structural items.

**WP5 — Constructive route, literal 396: DIAGNOSIS DONE (June 10; `wp5-diagnosis.md`).** Findings: (i) witness densities are geometric $\approx c_1^{k+1}$ — independence true at every order in data; (ii) the naive band-coin model is wrong — top-of-band carries are automatic by size (FK law), so constructions should *select* band primes into auto-carry slivers; (iii) absolute-counting comparisons are dead at every smoothness level (unifies two old dead-ends, quantitatively: needs $u<2^{1/(k+1)}$ vs the forced $u\ge2$); (iv) **route convergence**: in Balog–Wooley families the slot-2 digits at window primes are Fermat quotients of the explicit bases — Lemma D's deep-large-sieve species, and linear in the construction's exponents (CRT-forcible); (v) **entropy obstruction**: pure B–W families carry $O(t\log\log X)$ entropy vs the $\gtrsim\log x$ needed — insufficient, proof-of-death recorded. Reduction: literal 396 $\Leftarrow$ entropy-rich $\sqrt{2n}$-smooth window families (exist for $k\le2$ only: Hildebrand/Balog–Ruzsa) + family-FQ equidistribution (our wheelhouse, upper-bound mode). **WP5a ($k=2$ rung, after the $k=1$ paper): genuinely approachable, ~35–40%.** General $k$: blocked on window technology or $(k{+}1)$-point correlations. P(literal 396 via this program): **~10%**.

## Decision tree & calibration

```
WP1.4–1.5 ─► G1 ─┬─ PASS ────► WP2 ─┬─ success + WP3/3b ─► Theorem 1″
                 │                  └─ stall ─► weakened handling
                 ├─ WEAKENED ► WP2′ ─► Theorem 1′ + rung-ii paper
                 └─ KILL ────► exact obstruction ─► rung-ii paper + WP5
                       (WP4 runs in parallel throughout)
```

Rung i full: **~40%** (post-WP7 verification: unweighted digit layer solid; 0′/A/B-support proved; residue = four open hypotheses E1/E2/E3/C†, all dispersion-species, all empirically true; the next real work is dispersion proofs, not write-ups) — the one-day-swing humility warning still applies · Route-B lower bound: **+~25%** · rung ii: **~85%** · $k{=}2$ rung (WP5a): **~35–40%** · **literal 396 via this program: ~10%** (post-WP5-diagnosis: half on entropy-rich windows, half on the long-horizon analytic route).

## Immediate next actions

1. WP2.0 — **DONE** (`lemma-alpha-beta.md`): $\alpha,\beta$ proved; assembly accounting NEGATIVE; numerology erratum issued; residual = **Estimate D†** + its second-moment core.
2. WP2.1 — **MAJOR PROGRESS** (`wp21-reduction.md`): D†'s digit layer reduced exactly to a two-frequency minor/major-arc dichotomy; minor arcs cancel to polylog (validated), major arcs localized on $p\approx q\sqrt{\mu/\lambda}$ and reduced to a Diophantine count. Kloosterman core bypassed on this route. WP2.2 — **DONE June 9** (`wp22-minor-major.md`): D†-minor stated (standard toolbox); both major-arc families counted out (A: polylog-sparse on q-average; B: sparse + power-small); **D†-digit closed modulo write-up**. WP2.3 — **DONE June 9** (`wp23-anatomy.md`): **PASS, elementary** — $u_f=3(1-u)<2$ gives an exact unwinding of the friable indicator into Type-I/II sums and primes-in-APs; friable literature demoted to fallback. **No identified structural obstruction remains on Lemma D.** Next: **consolidation sprint (WP4)** — the pile of closed-modulo-write-up items is now the binding constraint; then the fine-anatomy-class check and the two equidistribution rigorizations.
3. **WP3b — DONE June 9 late evening** (see above; `lemma-B-anatomy-independence.md` has the verbatim theorem + resolved checks; TT row in `citations.md` now PINNED).
4. **WP4 — DONE June 9 evening** (see above): manuscript spine drafted and compiling; D†-minor proved in corrected form; E1/E2 isolated as the precise open hypotheses of the digit layer. Remaining manuscript debts are exactly manuscript §10's ledger: E1, E2, the anatomy Type-I/II ranges + ℓ-resonance count, the fine-class check, the Vaaler/completion packaging (D5), Lemma 0′ margins, Lemma A write-up, assembly bookkeeping.
5. **WP2.4 — DONE June 9 late evening** (`wp24-e1-e2-fineclass.md`): E1/E2 diagnosed — both LOW RISK (E1: only the *signed* average is needed, true in data with 10–300× margin, two of three boundary pieces unconditional; E2: tail law and moments confirmed, elementary + one BV corner); fine-class check (D4) **PASS** (bounded-depth exact I–E, same species; class-restricted probes all at $z=O(1)$). **Next binding items:** (a) write-ups: E1/E2 proofs, B0, D†-anatomy Type-I/II ranges (the one remaining named risk); (b) Lemma C (WP3) — now the largest open surface; (c) re-read FK with our notation (citations.md row A3).
6. **WP5 — DIAGNOSIS DONE June 10** (`wp5-diagnosis.md`); future sub-items: WP5a ($k=2$ via Hildebrand windows + family-D machinery), entropy-rich B–W variants (reading/derivation session), pin Hildebrand strings + Balog–Ruzsa exact statements.
7. (When convenient) re-run `empirics_d.py` at $x=10^9$ to check the §4 flag shrinks like a boundary term.

## Method note

Hardest-first governs risk-resolution order, not all effort; the first unit of work on a risky item is diagnosis; dead ends are recorded with proofs of death; and anything derived must be written immediately — a derivation that lives only in a session's working memory is one context limit away from oblivion.
