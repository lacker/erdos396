# WP9: Theorem 1′ — the complete conditional chain


> **UPDATE (June 11, WP12b):** link 7 (E3-lb) — the elementary ladder is complete and bottomed out (`wp11-e3lb.md` STATUS header); the remaining input for links 7 AND 9 is the single external Kuznetsov/DI-class estimate (roadmap WP12b). G1 (the sum-branch count) is CLOSED and verified (wp10). E2 is discharged (wp8-e2, verified).

STATUS: COMPLETE (assembly document; no new analytic claims). Date: 2026-06-10.

Target: **Theorem 1′** (manuscript `01-intro.tex`, thm:lower, "Target 1′; rung
i-minus"): W₁ = {n ≥ 2 : n(n−1) | C(2n,n)} has **positive lower logarithmic
density** — hence W₁ is **infinite** (the headline result).

Sources: wp9-b0-audit.md (THE SPEC: minimal lb hypothesis list), wp9-verify-e1e2.md,
wp9-verify-e3cd.md, manuscript/sections/{01,03,04,06,07,08,09,10,13,14,15}.tex,
wp8-e3.md (§3 T1, §5 E3-lb), wp8-e2.md (via its verification), wp8-cdagger.md
(lb section), main.tex (status macros: [PROVED]=statusP, [PROVED, machine-
verified]=statusPM, [CITABLE]=statusC, [KNOWN-ADAPT]=statusKA, [STANDARD
TOOLBOX, to write]=statusN, [OPEN]=statusO).

Status vocabulary of this document:
- **PROVED** — proved in the manuscript (statusP/statusPM), proof present.
- **VERIFIED-DRAFT** — proved in a wp8 report AND upheld by the wp9
  adversarial verification; not yet transcribed into the manuscript.
- **CITATION** — pinned classical input, cited not proved.
- **OPEN-HYP** — one of the two named residual hypotheses (and nothing else).
- **WRITE-UP** — neither proved nor a named hypothesis: goes to the gap list (§4).

Standing parameters: L = log x; η > 0 the cell width parameter (reference
η = 0.05, see §6(c) for the corner caveat); δ > 0 the small-prime cutoff,
FIXED (reference δ = 0.01; the lb-track never sends δ → 0); c > 0 the saving
exponent, C the harmonic-cutoff exponent, B the level parameter with
**B = max(C+c+4, 2C+2c+10)** (the retuned value; see §4 G1); δ₀ > 0 the
exceptional-density budget (δ₀ ≤ 1% of the main coefficient). Top cell
U = (1/2−2η, 1/2−η); P = x^u, Q = x^{u'}, R = x/(pq) = x^{1−u−u'} ∈
[x^{2η}, x^{4η}] on the cell — so every polylog trim (corner trim in the
strengthened form √R ≥ L^{B/2+2c+8}, R ≥ L^{B+c+4}, etc.) holds with power
room, for free.

---

## 1. Statement, with the explicit constant chain

**Theorem 1′ (conditional form assembled here).** Assume the two residual
hypotheses **E3-lb (two-sided, λ-uniform)** and **C†-single-lb(g₀)** stated
verbatim in §2, links 7 and 9. Then there is an explicit κ_lb > 0 such that

  liminf-type lower log-density of W₁ ≥ κ_lb > 0 along a scale sequence,

in fact (1/log x) Σ_{n≤x, n∈W₁} 1/n ≥ κ_lb for all x in an unbounded scale
set. In particular W₁ is infinite.

**The constant chain** (audit ledger, wp9-b0-audit.md §6; reference values
η = 0.05, δ = 0.01; per side unless noted):

  κ_lb = [ (cell Mertens) × (friable cofactor) × (imposed coins) ]² × (1 − discards)
       ≈ [ 0.1 × 0.41 × 0.09 ]² × (1 − small)
       ≈ 1.4·10⁻⁵ ,

where per side:
- cell Mertens ≈ log((1/2−η)/(1/2−2η)) ≈ 2η ≈ 0.1 — exactly one band prime,
  in the top cell U;
- friable cofactor ≈ ρ((1/2+2η)/(3/10)) ≈ ρ(1.8) ≈ 1 − log 1.8 ≈ 0.41
  (Dickman; cell-edge reference value — the class average is ≈ 0.33–0.41,
  and only positivity matters);
- imposed coins ≈ (1/2) × E[2^{−ω}] ≈ 0.5 × 0.18 ≈ 0.09 — the slot-2 band
  coin (measure 1/2) times the slot-2 coins at the ω cofactor primes in
  (x^δ, x^{3/10}], class-average E[2^{−ω}] ≈ (δ/0.3)^{1/2} ≈ 0.18 at δ = 0.01;
- discards (subtracted, each calibrated < 1% of the product): Lemma-A set
  O(e^{−c_A/δ}), square-discard O(x^{−δ'}), the two δ₀-exceptional sets
  (E3-lb bad q; C†-lb bad p), Family-A/B major discards O(L^{−pos}),
  slot-boundary slivers O(ε′), harmonic-truncation tails O(L^{−pos}).

All factors are fixed positive constants (x-independent); κ_lb is small but
positive. The lower bound is needed only at one unbounded scale sequence
(almost-all-scales statements of the inputs make this free).

---

## 2. The proof skeleton: the numbered conditional chain

Cascade order follows prop:cascade (15-spine-bookkeeping.tex, lines 148–174):
sandwich → margins → Lemma A → class restriction → D-step → C-step → B-step
→ exceptional assembly → conclusion. Every link carries its status tag and
exact source; §6 records the adversarial self-check of each link.

### Link 1 — The exact sandwich. [PROVED (machine-verified)]
W₁ ⊇ D₀ ∩ (D₀⁽⁺⁾ + 1) (lower inclusion; exact, no exceptional set).
Source: lem:sandwich, `03-sandwich.tex` lines 6–35 (statusPM; zero
exceptions to 6·10⁴ and samples near 10⁹). The lb-track uses ONLY the lower
inclusion: it suffices to produce a positive-log-density set of n with
n ∈ D₀ and n−1 ∈ D₀⁽⁺⁾.

### Link 2 — Margins are free. [PROVED]
dens(D₀⁽±⁾) = dens(D₀) = c₁, log-density included. Source: lem:margins,
`03-sandwich.tex` lines 44–65, full proof in `15-spine-bookkeeping.tex`
(§"Lemma 0′", lines 50–74, via lem:fewcarries + lem:marginwins, both
statusP; status upgraded to statusP at line 73). Role in the lb chain:
minor — the construction imposes margin-strict slot-2 windows
[1/2, 1−q^{−2}) directly, so D₀⁽⁺⁾-membership at the designated primes is
by construction; Lemma 0′ guarantees the imposed windows lose only O(q^{−2})
measure against the plain windows.

### Link 3 — Small primes (Lemma A) + square-discard. [PROVED]
#{n ≤ x : v_p(A_n) > κ_p(n) for some p ≤ x^δ} ≪ x e^{−c/δ}, and discarding
p² | n(n−1) for p > x^δ costs ≪ x^{1−δ}. Source: lem:A, `04-architecture.tex`
lines 22–55 (statusKA as stated), proof executed in
`15-spine-bookkeeping.tex` lines 78–102 (status upgraded to statusP at line
100). lb-mode: δ stays FIXED; the loss e^{−c_A/δ} is subtracted once and
calibrated < 1% of κ_lb (audit ledger item 5). Off this set, every prime
≤ x^δ meets its carry budget automatically, on both sides (the shifted-side
digit pattern (1,0^{v−1}) is handled in the proof, lines 93–96).

### Link 4 — Restriction to the audit's anatomy cell. [PROVED modulo pinned citations + WRITE-UP scope items]
**The class (per side):** exactly one prime in the top cell U = (1/2−2η,
1/2−η) of the band, cofactor x^{3/10}-friable (audit §2/§5a). This kills:
the two-band-prime population (C†-pair, DMV debt), the major-pair absorption
((Hal) debt), AND the conductor gap window — primes of size v ∈ (3/10, 1/3)
would carry binding coins at conductors x^{2v} ∈ (x^{3/5}, x^{2/3}), beyond
DGS but below hyp:Cdagger's stated band floor 1/3; the 3/10 cutoff excises
them (the audit's **3/10-floor scope fix**, wp9-b0-audit §2 item 3).
Trim compliance: top trim u, u' ≤ 1/2−η ✓ by cell choice; corner trim
✓ with power room (u+u' ≤ 1−2η so R ≥ x^{2η}); auto-carry sliver: NOT used
as a class (density ≍ 1/log x, audit §3 correction of wp8-cdagger's
framing) — only excised from the C†-variance set, cost 0.

**The anatomy-pair lower bound (Lemma B at the cell-boxes):** the joint
count of n with A(n), A(n−1) both in the class is ≥ (1−o(1)) PD(box)² ×
log-mass. Two routes:
- TT-route: prop:B-assembled, `13-lemmaB-closure.tex` lines 123–149 —
  statusP **modulo (TT) = TT25 Thm 3.1 (statement PINNED against v2 source)
  and SL2′**, assembled from lem:interp (statusP), **lem:B0** (statusP,
  lines 48–94: the equidistribution axiom for g_z, proved unconditionally),
  lem:SW (statusP modulo SL2′). Outstanding fine print: (W4)
  Dickman–Billingsley identification; (W6) bounded-multiplicity general-band
  interpolation — needed here because the cell-box involves bands down to
  x^{3/10} (multiplicity ≤ 3 above x^{3/10}, so a mild extension of
  lem:interp's four-node Lagrange argument); (W6′) scale-drift average
  conversion (`10-remaining.tex` ledger, line 55; `13-lemmaB-closure.tex`
  preamble correction).
- Fallback (lb-sufficient, TT-free): Hildebrand's elementary stable-set
  method [Hil85], registered at `04-architecture.tex` lines 96–98; gives a
  positive-density LOWER bound for the anatomy layer, which is all link 4
  needs. Scope-check that it covers "one cell prime × friable cofactor"
  boxes is a WRITE-UP item (audit §6 closing paragraph; the box is
  anatomy-only, so the TT dilation-blocker does not apply). → Gap G4.
Density collected: [2η × ρ(≈1.8)]² ≈ [0.1 × 0.41]².

### Link 5 — Within-cell digit imposition (positivity set-up). [PROVED pieces + WRITE-UP assembly]
Per side, impose ONLY slot-2 successes (lower-bound mode: 1[κ_ℓ ≥ 1] ≥
1[slot-2 success], the cheap direction; deep digits j ≥ 3 are never
imposed — they exit the lb-track entirely, audit §2 item 3):
- at the designated cell prime p: the window fr{n/p²} ∈ [1/2, 1−p^{−2}),
  measure ≈ 1/2 — the "single near-fair coin" of `04-architecture.tex`
  lines 12–16 (j = 1 never carries for p‖n, j ≥ 3 deterministic at band
  size);
- at each cofactor prime ℓ ∈ (x^δ, x^{3/10}]: the slot-2 window mod ℓ²,
  class-average factor E[2^{−ω}] ≈ 0.18.
Sufficiency (elementary): imposed successes + link-3 non-exceptionality +
the cell-box anatomy imply n ∈ D₀ and n−1 ∈ D₀⁽⁺⁾ — every prime of n(n−1)
is either ≤ x^δ (link 3), a cofactor prime (imposed coin), or the cell
prime (imposed coin); square-discard makes all exponents 1.
Fourier detection of the imposed windows: exact finite expansions with
⟨λ⟩^{−1} coefficient decay — prop:depth(i), `15-spine-bookkeeping.tex`
lines 106–126 (statusP); truncation at ⟨λ⟩ ≤ L^C in MINORANT form
(Vaaler/Selberg minorants, to preserve positivity) is standard but unwritten
→ part of Gap G3. Slot-boundary slivers: prop:depth(iii), cost O(ε′), in
the trim budget.

### Link 6 — D-step: cross-side digit removal at the cell (Estimate D†, lb-form). [PROVED + VERIFIED-DRAFT + OPEN-HYP 1 + WRITE-UP]
Replace the (n−1)-side digit indicator by its class mean, for all q outside
a δ₀-density exceptional set, with the class-restricted population (the
n-side decoration w = centered digit weight × anatomy-class indicator, and
the (n−1)-side population restricted to the cell class). Per fixed harmonic
0 < |λ| ≤ L^C, decomposed exactly as `04-architecture.tex`'s D†-table
(lines 176–191), in lb-mode:

**6a. Opening and deep harmonics. [PROVED]** lem:beta (AP-opening),
lem:linearization, prop:two-freq: `06-reduction.tex` lines 12, 54, 153, all
statusPM; deep harmonics |λ| ≥ Λ₀ covered by prop:largelambda,
`06-reduction.tex` line 93, statusP.

**6b. Digit layer, minor p. [PROVED]** thm:minor (functional form,
`07-minor.tex` lines 88–197, statusP) + cor:minor (lines 97–108):
|V_p(λ)| ≪ √R L^{B/2+4} + R L^{2−B} ≤ R L^{−c−1} for minor p, POINTWISE in
(p,q,λ) — no average needed. Inputs: lem:cf (statusP).

**6c. Digit layer, major p: worst-case-per-q discard — what exactly replaces E1/E2.**
The lb-track discards major p at trivial cost R each, against the per-q
budget π(P) R L^{−c}; so it needs per-q COUNTS of (M1)/(M2*)-failures, not
the q-averaged boundary estimates E1/E2 (`08-major.tex` preamble, lines
9–12: "For the lower-bound track the worst-case-per-q versions suffice and
neither hypothesis is needed"). Verified precisely, the replacements are:

- **(M1)-failures, difference branch (μ in the lower half): lem:branch.
  [PROVED]** `08-major.tex` lines 24–51 (statusP, unconditional, per fixed
  (q,λ,μ), integer-p relaxed). Summed trivially over μ ≤ RL^{−B} and
  λ ≤ L^C using the unconditional pieces isolated in rem:E1-signed (lines
  69–85): per-q major count ≪ P L^{C+1−B} + R L^{C−B} + (PR/Q) L^{2C−B}
  + (R²Q/P) L^{C−2B}. At the cell: R ≤ x^{4η} and R/Q ≤ x^{−(1/2−6η)} make
  the middle terms power-small; the last term is power-small on the open
  cell and polylog-saved at the u = u' = 1/2−2η corner (see self-check
  §6(c)). Damage ≤ count × R ≪ π(P) R L^{−c−1} for B ≥ C+c+4. **No
  q-average used anywhere.** E1 itself (hyp:E1, lines 53–67, statusO) is
  consumed ONLY by the asymptotic track.
- **(M1)-failures, sum branch (μ near p): NOT covered by lem:branch.**
  eq:conic (line 17) says "exactly" but silently drops the branch
  ||μ̃q/p + λp/q|| ≤ δ_μ̃ (wp9-verify-e1e2, Finding E1-1 [GAP]). The
  lb-track needs the per-q worst-case count of this branch too. Per the
  verified repair route: for μ̃ ≥ C·m₀ the count is verbatim-cognate
  (monotone phase); for μ̃ ≤ C·m₀ split at the critical point p* =
  q√(μ̃/λ) plus an elementary tangency-strip count, total NEW per-q major
  mass ~ P L^{−B/2+O(C)} — affordable (damage ≪ π(P) R L^{−c−1}) once
  **B ≥ 2C+2c+10** (the standing retune). The strips live only on the
  u ≥ u' half of the cell (need integer k ≍ 2λP/Q ≥ 1). STATUS: route
  identified and feasibility-checked (wp9-verify-e1e2, repair (i)–(iii));
  the count itself is UNWRITTEN → **Gap G1** (the one genuinely missing
  lemma in the digit layer).
- **(M2*)-failures (Family B): wp8-e2's unconditional theorem + Markov.
  [VERIFIED-DRAFT + half-page glue]** wp8-e2 proves, unconditionally for
  all P,Q,R,B with G₀ = RL^{−B} ≥ 8: #{(p,q) failing (M2*)} ≪
  PQ L^{B+1}/R + P² L^{B+2}/R (verdict UPHELD, wp9-verify-e1e2; honest
  per-q conversion adds one L). Markov over q: off a (δ₀/4)-fraction of q,
  the per-q failure count is ≤ (4/δ₀)(P L^{B+2}/R + P² L^{B+3}/(QR));
  damage × R ≪ π(P) R L^{−c−1} needs R ≥ δ₀^{−1} L^{B+c+4} and
  x^{u−u'} ≤ δ₀ R L^{−B−c−4} — both hold on the cell with power room
  (R ≥ x^{2η}, u−u' ≤ η < 2η). Bad q join the δ₀ budget. E2 is thus
  DISCHARGED, not merely unneeded (hyp:E2, `08-major.tex` lines 128–136,
  becomes moot once wp8-e2 is transcribed). Alternative without wp8-e2: a
  per-q swap-roles adaptation of prop:familyB's lattice count — unwritten,
  unnecessary given the verified draft.

**6d. Anatomy layer, μ-tail and main terms: Theorem T1. [VERIFIED-DRAFT]**
T1 (wp8-e3.md §3; verdict UPHELD, wp9-verify-e3cd §B): pointwise in
(p,q,λ) with p minor, Σ_{0<μ<p} |Σ(θ_μ)|/⟨μ⟩ ≤ Σ_{⟨μ⟩≤μ₀} |E(θ_μ)|/⟨μ⟩
+ O(R L^{−c−2}), μ₀ = L^{2c+6}, under B ≥ 2c+8 and the strengthened corner
trim √R ≥ L^{B/2+2c+8} (free on the cell). Inputs: Prop S (root-sum
reduction, machine-verified, with the ℓ ≠ q exclusion), lem:cf(1), exact
λ-cancellation in θ_μ-differences, Montgomery–Vaughan spaced large sieve,
V ≤ R+1. T1's only arithmetic inputs are coefficient boundedness and the CF
spacing — it is **coefficient-agnostic**, which link 6e uses.

**6e. Anatomy layer, core frequencies + class-restricted population:
Hypothesis E3-lb (two-sided, λ-uniform). [OPEN-HYP 1]** Stated verbatim in
link 7. What feeds it: (i) the a-side rough sums E(θ_μ) at core ⟨μ⟩ ≤ μ₀
(wp8-e3 §5); (ii) the b-side rough terms 1[ℓ | pt+b₀] injected into the
λ ≠ 0 harmonics when the (n−1)-class friability 1[P⁺(b) ≤ x^{3/10}] is
unwound on b = pt+b₀ (audit §5b: prop:cascade's D-step centers the
(n−1)-digit WITH the class indicator present, so the m-population is
class-restricted — the §06/§15 population-gluing point, resolved by
statement inside E3-lb). The unwinding is exact at the cell by the
3/10-variant of prop:one-large (`09-anatomy.tex` lines 11–31, statusPM;
needs u' ≥ 2/5 ✓ on the cell: b ≤ x^{1−u'} ≤ x^{3/5} = (x^{3/10})², the
boundary case handled as in the original). The b-side hard mass is O(η) at
the cell (all window primes sub-one against length R — large-Λ Type-II
species of prop:species, `09-anatomy.tex` lines 41–76, statusPM, whose
remark's caveat (iii) extends to it). The a-side hard sub-range
Λ ∈ (Q, Q^{3/2}] ∩ (x^{u'}, x^{1−u}] has mass ≈ 4η at the cell — the
burden shrinks linearly with the trim (audit §5a). The μ-tail of the
b-side decoration is covered by T1 verbatim (coefficient-agnostic; the
centered b-side coefficients are bounded since ≤ 3 primes > x^{3/10}
divide b). The composite re-derivation of the D-step with the class
indicator present is bookkeeping → **Gap G2**.

**6f. Gluing (P3, repaired). [VERIFIED-DRAFT with mandated repair]** On the
good q-set (density ≥ 1−δ₀), the full D†-bound holds POINTWISE in q: core
μ-sum ≤ 5 log μ₀ · π(P) R L^{−c−4} ≪ π(P) R L^{−c−2}, T1 covers the rest
(wp8-e3 §5, Prop P3). Repair baked in (wp9-verify-e3cd, Finding E3-4
[GAP]): the λ-quantifier must sit INSIDE the bad-set event — the form in
link 7 below does this; the per-λ form of wp8-e3 §5 does NOT suffice (union
over L^C harmonics would inflate δ₀ to δ₀L^C).

### Link 7 — Residual hypothesis 1, stated verbatim. [OPEN-HYP 1]

> **Hypothesis E3-lb (two-sided population form, λ-uniform).** There is an
> absolute δ₀ > 0 such that, in the notation of wp8-e3 §3 (E(θ) the
> centered rough sum, θ_μ = μq/p − λp/q, μ₀ = L^{2c+6}),
>
>   #{ q ∼ Q : ∃ λ, 0 < |λ| ≤ L^C, with
>        Σ_{p∼P minor} max_{⟨μ⟩≤μ₀} |E_{p,q}(θ_μ)| > π(P) R L^{−c−4} }
>   ≤ δ₀ π(Q),
>
> **and** the mirror statement for the b-side rough sums: the centered
> contributions of the rough terms 1[ℓ | pt+b₀] (ℓ > x^{3/10}, from
> unwinding the (n−1)-class friability inside the λ ≠ 0 harmonics of the
> D-step), band-average over q, δ₀-exceptional q-set, λ-quantifier inside
> the event, core μ only — T1 covers the μ-tail of both sides pointwise.

(= audit §5b's statement with wp9-verify-e3cd's E3-4 repair made explicit.
The variance route to it, if used, must carry the strengthened exponent
δ₀² R² L^{−(4c+18+C)} per Finding E3-5; the plain exceptional-set form above
needs no such care.) Hard-mass accounting at the cell: a-side ≈ 4η, b-side
O(η) — both shrink with the trim. Same species both sides: dilated-phase /
sub-complete-sum Kloosterman-root equidistribution beyond per-ℓ Weil — the
program's named frontier.

### Link 8 — C-step: within-side digit removal against the fixed weight g₀. [CITATION + OPEN-HYP 2; everything else void or proved]
Replace the n-side digit indicator by its class mean, against the remaining
(n−1)-side data — which after the D-step is the ANATOMY-only class
indicator, the single fixed plain function

  g₀(m) = Σ_{q = m^{u'}, u' ∈ U} 1[q | m] · 1[P⁺(m/q) ≤ x^{3/10}]

(0/1-valued; the representation is exact since two cell primes would
violate friability — audit §3 b1; lem:interp is a tool, not part of the
demand, so **no SW-family uniformity is needed**: hyp:Cdagger as printed in
`14-lemmaC-reduction.tex` lines 156–164 is strictly over-engineered for
this track). The consumers of Lemma C's weighted layer at the class
(exhaustive, audit §2):
1. C†-pair / weighted minor pairs (prop:C-weighted): **VOID** — no n in
   the class has two band primes. The (DMV) citation debt exits.
2. Major-pair absorption ((Hal), `14-lemmaC-reduction.tex` lines 120–134,
   statusO): **VOID** — no pairs, and majors are discarded into the
   trim/δ₀ budget, not absorbed.
3. Cofactor-prime coins, ℓ ∈ (x^δ, x^{3/10}]: **CLASSICAL [CITATION]** —
   detection conductor ℓ² = x^{2v} ≤ x^{3/5}: inside
   Drappeau–Granville–Shao (x^{3/5}); inside Granville–Shao (x^{20/39}) if
   v ≤ 10/39 — prop:C-single's classical clause (`14-lemmaC-reduction.tex`
   lines 138–154), valid BELOW the band (the demotion was only for band
   conductors). SW admissibility of the g_z-components of g₀: lem:SW
   (`13-lemmaB-closure.tex` lines 96–121, statusP modulo SL2′). The gap
   window v ∈ (3/10, 1/3) (conductors (x^{3/5}, x^{2/3}), beyond DGS,
   below the band) is EMPTY by the friability cutoff — the **3/10-floor
   scope fix** again.
4. Deep digits j ≥ 3: **VOID in lb-mode** (never imposed).
5. The band coin at the designated p, conductor p² = x^{2u} ∈ (x^{2/3},
   x^{1−2η}): **the single irreducible C†-consumer** → OPEN-HYP 2, link 9.
Majors among p (Family-A/B exceptional structure, roles p↔q swapped via
prop:C-cov's change of variables, `14-lemmaC-reduction.tex` line 31,
statusP): worst-case-counted and discarded exactly as in link 6c — same
counts, same Gap G1 dependency on the u ≥ u' orientation (wp9-verify-e3cd
note CD-3 flags precisely this inheritance).

### Link 9 — Residual hypothesis 2, stated verbatim. [OPEN-HYP 2]

> **Hypothesis C†-single-lb(g₀)** (audit §4c2, verbatim). Let
> U = (1/2−2η, 1/2−η) (top cell; any positive-measure cell works, top is
> optimal), and let g₀(m) = Σ_{q = m^{u'}, u' ∈ U} 1[q|m] ·
> 1[P⁺(m/q) ≤ x^{3/10}] be the fixed plain (n−1)-class indicator. There
> are δ₀ > 0 and c > 0 such that for each fixed 0 < |h| ≤ (log x)^C, the
> centered sums
>   V_p(h) = Σ_{m ≤ x/p} g₀(pm − 1) e(hm/p) − (main term, FK law)
> satisfy the single second-moment bound over minor band primes p = x^u,
> u ∈ U (auto-carry slivers may be excised):
>   avg_{p minor} |V_p(h)|² ≪ δ₀ (x/p)² (log x)^{−2c−2C−10}.

Differences from hyp:Cdagger as printed (all weakenings, audit §4c2):
single-prime case only; ONE fixed 0/1 weight (no SW-family uniformity);
minor p only; no asymptotic, no main-term evaluation; second-moment /
exceptional-set form; one positive-measure cell; the 3/10-floor scope fix
embedded in g₀. What does NOT weaken: the conductor is still p² > x^{2/3}
(the binding digit is a mod-p² datum; the intrinsic-conductor argument of
wp8-cdagger §1 applies verbatim to g₀), so it is open for the same analytic
reason as C† — the BFI-dispersion route dies in the distinct-moduli sector
(deficit x^{3u₂+3u₁/2−1} ≥ x^{1/2} band-wide; wp8-cdagger, verdict UPHELD).
The B = 0 escape hatch is CLOSED (audit §4c1: smooth-cofactor no-go
ρ(t) = t^{−t(1+o(1))} vs the 2^{−1/c} floor, plus sub-band major-geometry
inversion), and every positivity/sieve-opening rearrangement to avoid the
weighted layer fails quantitatively (audit §3 b2) — so this hypothesis is
irreducible in the cascade architecture.

### Link 10 — Chebyshev / exceptional-set assembly. [VERIFIED-DRAFT + WRITE-UP]
- **C†-side closure. [VERIFIED-DRAFT]** Chebyshev at threshold
  T = R L^{−c−3} per harmonic: per-harmonic exceptional p-fraction
  σ²/T² = δ₀ L^{−2C−4}; union over the O(L^{2C}) harmonics ≤ δ₀ L^{−4} ≤
  δ₀; on good p the assembled weighted sum is ≪ (C log L)² R L^{−c−3} ≪
  R L^{−c−2}. The exponent −2c−2C−10 is CORRECTLY CALIBRATED to absorb
  both the harmonic union and the L² weight mass (wp9-verify-e3cd §F0,
  recomputed; contrast E3-5, which is why E3-lb is taken in exceptional-set
  rather than variance form).
- **E3-side closure. [VERIFIED-DRAFT, with E3-4 repair]** P3 as in link 6f.
- **Discard accounting.** Bad q (E3-lb): ≤ δ₀ π(Q); bad p (C†-lb): ≤ δ₀
  density; Family-B bad q (Markov): ≤ δ₀/4; Family-A majors and the
  remaining major damage: inside the per-q L^{−c} budgets (links 6c, 8);
  Lemma-A set and square-discard: link 3; sliver and truncation losses:
  link 5. Every discard is subtracted from a main term that is a fixed
  positive constant times the log-mass; total calibrated < 50% of κ_lb
  (the audit ledger's "1% each" allocation has large slack). The composed
  lb-variant of prop:cascade (restriction to one class pair, minorants,
  fixed δ, one good scale sequence) is the blueprint of audit §6 but is
  NOT yet a written proposition → **Gap G3**.

### Link 11 — Conclusion.
On the good set (positive log-density ≥ κ_lb ≈ 1.4·10⁻⁵ at the reference
parameters), n ∈ D₀ and n−1 ∈ D₀⁽⁺⁾ (link 5 sufficiency), hence n ∈ W₁
(link 1). Therefore W₁ has lower logarithmic density ≥ κ_lb > 0 along an
unbounded scale sequence; in particular **W₁ is infinite**. ∎ (conditional
on E3-lb two-sided + C†-single-lb(g₀) and the write-up items of §4).

---

## 3. Status table (every link, one line)

| # | Link | Status | Source |
|---|------|--------|--------|
| 1 | Sandwich (lower inclusion) | PROVED (machine-verified) | lem:sandwich, 03-sandwich.tex |
| 2 | Margins free | PROVED | lem:margins, 03 + 15-spine (full proof) |
| 3 | Lemma A + square-discard | PROVED | lem:A, 04 + 15-spine (proof) |
| 4 | Cell restriction / anatomy pair | PROVED modulo (TT pinned, SL2′, W4, W6, W6′); Hildebrand fallback CITATION + scope WRITE-UP (G4) | lem:B/prop:B-assembled, 04 + 13; [Hil85] |
| 5 | Digit imposition + Fourier set-up | PROVED (prop:depth) + WRITE-UP minorants (G3) | 15-spine prop:depth; 04 band-coin law |
| 6a | D-step opening, deep harmonics | PROVED | lem:beta, lem:linearization, prop:two-freq, prop:largelambda, 06 |
| 6b | Digit minor arcs | PROVED | thm:minor, cor:minor, lem:cf, 07 |
| 6c-i | Family A worst-case, difference branch | PROVED | lem:branch + rem:E1-signed, 08 |
| 6c-ii | Family A worst-case, sum branch | OPEN write-up, route verified feasible (G1) | wp9-verify-e1e2 E1-1 repair |
| 6c-iii | Family B worst-case | VERIFIED-DRAFT (+ Markov glue) | wp8-e2 Thm (UPHELD); 08 prop:familyB |
| 6d | Anatomy μ-tail (T1) | VERIFIED-DRAFT | wp8-e3 §3 (UPHELD, wp9-verify-e3cd §B) |
| 6e | Class-restricted population / b-side | inside OPEN-HYP 1 + WRITE-UP (G2) | audit §5b; prop:one-large/prop:species (PROVED-PM), 09 |
| 7 | **E3-lb two-sided, λ-uniform** | **OPEN-HYP** | audit §5b + E3-4 repair |
| 8 | C-step consumer triage | VOID/CITATION/PROVED per item | audit §2; prop:C-single classical clause, 14; lem:SW, 13 |
| 9 | **C†-single-lb(g₀)** | **OPEN-HYP** | audit §4c2 (verbatim) |
| 10 | Chebyshev/exceptional assembly | VERIFIED-DRAFT closures + WRITE-UP (G3) | wp8-cdagger lb (UPHELD); wp8-e3 P3 (repaired) |
| 11 | Conclusion, κ_lb > 0 | follows | audit §6 ledger |

Classical/citation inputs consumed: GS, DGS (cofactor coins; k = 0
anatomy-in-AP), SL2′ (for lem:SW), TT25 Thm 3.1 (pinned) OR [Hil85]
fallback, FK21 (counting framework + c₁), Khinchin CF facts (lem:cf),
Montgomery–Vaughan large sieve (inside T1). NOT needed on this track: E1,
E2 (discharged/replaced as in 6c), C†-pair, DMV, (Hal), E3† full variance.

---

## 4. Honest gap list (neither proved nor one of the two hypotheses)

| ID | Gap | Why it is needed | Effort |
|----|-----|------------------|--------|
| G1 | **Sum-branch worst-case-per-q Family-A count** (sibling of lem:branch: monotone split at p* + elementary tangency-strip count, ~P L^{−B/2+O(C)} majors per q; retune B = max(C+c+4, 2C+2c+10); fix eq:conic's "exactly") | The (M1)-failure set genuinely contains the Pythagorean strips (wp9-verify-e1e2 E1-1, numerically confirmed); without this count the major discard of links 6c and 8 silently undercounts on the u ≥ u' half of the cell | 1–2 pages, elementary; route feasibility already checked |
| G2 | **Two-sided population gluing write-up**: re-derive the D-step with the (n−1)-class indicator present; exact 3/10-variant of prop:one-large (needs u' ≥ 2/5 — holds on the cell); boundedness of the centered b-side coefficients; T1 restated coefficient-agnostically | Routes the class-restricted population into E3-lb's b-side clause instead of leaving an unstated assumption in prop:cascade's D-step | 2–3 pages bookkeeping (audit §5b is the blueprint); no new species |
| G3 | **lb-assembly proposition ("prop:cascade-lb")**: one class pair, Vaaler/Selberg MINORANTS for the imposed slot-2 windows, harmonic truncation at L^C with tail control, fixed δ, all discards subtracted, FK per-class probability lower bounds, one good scale sequence | prop:cascade (15-spine) is the asymptotic cascade; the lb-variant with positivity and exceptional discards exists only as the audit §6 ledger, not as a written proposition | 3–5 pages; standard, but it is where all constants are finally composed |
| G4 | **Lemma B lb-scope**: W6 generalized interpolation for boxes with bands down to x^{3/10} (multiplicity ≤ 3) and the cell box; or scope-check the Hildebrand [Hil85] stable-set fallback for "one cell prime × friable cofactor" boxes; (TT) transcription + (W4) + (W6′) if the TT route is used | Link 4's lower bound for the anatomy pair must cover exactly the audit's class | 1–2 pages (fallback route is the cheaper of the two for the lb) |
| G5 | **Family-B per-q glue**: transcribe wp8-e2's unconditional theorem into the manuscript (restate prop:familyB unconditionally, with the honest extra L) + the half-page Markov-over-q discard | Replaces E2 on this track; currently lives only in a draft report | 2–3 pages transcription (proof verified line-by-line) + half page |
| G6 | **T1 transcription** (wp8-e3 §3 → manuscript) with the cosmetic repairs E3-1/E3-3 (state the corollary of thm:minor's proof; correct the "(M2*) once" claim) | Link 6d currently cites a draft report | ~3 pages transcription (proof verified) |
| G7 | **Manuscript hygiene blocking correctness**: eq:conic "exactly" (G1); lem:SL2's third term √s → √(Ps) and retirement of 12-e1e2's prop:E2 (pre-existing errors found in verification — SL2′, which lem:SW cites, is "same family", so the corrected form must be the one pinned); restate hyp:Cdagger in the minimal C†-single-lb(g₀) form with the 3/10 floor; register E3-lb (two-sided, λ-uniform) in 11-typeII | Prevents the chain from citing statements that are false as printed | 1–2 days of editing; no mathematics |
| G8 | **Citation pinning**: GS, DGS exact statements/ranges for the cofactor-coin conductors ℓ² ≤ x^{3/5}; SL2′; [Hil85]; FK21 §7 constant | Links 4, 8 consume them quantitatively | citations.md work, small |

Items NOT on this list because they are inside the named hypotheses by
design: the a-side core frequencies (E3-lb), the b-side rough sums (E3-lb
two-sided), the band-coin variance (C†-single-lb(g₀)).

---

## 5. Minimal TODO to a complete Theorem 1′ manuscript

Ordered; (1)–(2) are the mathematics, (3)–(8) are writing.

1. **Prove E3-lb (two-sided, λ-uniform)** — exceptional-set form, hard mass
   O(η) per side at the cell. (THE open problem, frontier species.)
2. **Prove C†-single-lb(g₀)** — single second moment, fixed plain weight,
   conductor p²; the audit's recommended attack: exploit g₀'s
   q-AP × friable structure (far more rigid than a general SW weight) and
   the empirically observed variance collapse (z: 13.1 → 0.78). (THE other
   open problem; same Kloosterman frontier.)
3. G1: write the sum-branch per-q count; retune B; fix eq:conic.
4. G5 + G6: transcribe wp8-e2 (Family B unconditional) and T1 into the
   manuscript.
5. G2: write the two-sided gluing bookkeeping (D-step with class
   population; 3/10 one-large variant).
6. G4: close Lemma B's lb-scope (Hildebrand fallback recommended).
7. G3: write prop:cascade-lb and compose the ledger into the final κ_lb.
8. G7 + G8: hygiene edits and citation pinning; final pass re-verifying the
   composed error budget (ledger W5).

Nothing else stands between the two hypotheses and Theorem 1′.

---

## 6. Adversarial self-check of the chain (no link assumes more than its source proves)

(a) **"E1/E2 not needed" — verified, with one repair.** The 08-major
preamble's claim was checked against what the lb-track actually consumes:
E1's q-average is replaced by lem:branch + the unconditional pieces of
rem:E1-signed (per-q, no average) — TRUE for the difference branch; but the
preamble's implicit premise that lem:branch counts ALL (M1)-failures is
FALSE (eq:conic drops the sum branch, wp9-verify-e1e2 E1-1). The audit's
"E1 NOT needed (worst-case-per-q suffices; power room at the top cell)"
silently inherits this. The chain above does NOT: link 6c-ii names the
missing per-q sum-branch count as Gap G1, affordable at worst case with the
retuned B — so the conclusion ("no q-average equidistribution hypothesis
needed") survives, the silent assumption does not. E2 is genuinely
discharged (unconditional theorem, verified), not just bypassed.

(b) **E3-lb as stated by the audit needed one repair.** Audit §5b's
parenthetical "fixed λ" repeats wp8-e3 §5's per-λ form, which P3 cannot
consume (E3-4: union over L^C harmonics breaks constant density). Link 7
states the λ-uniform form. The C†-side needs no analogous repair: its
exponent −2c−2C−10 already pays for the harmonic union (verified
recomputation, wp9-verify-e3cd §F0).

(c) **Audit's "power room at the top cell" exponent slip (harmless).** The
audit writes R²Q/P = x^{4η+u'−u}; over the full cell R²Q/P = x^{2(1−u−u')+u'−u}
≤ x^{9η}, and at the corner u = u' = 1/2−2η the comparison against P = x^u
needs 2−3u−u' < u, i.e. η < 1/20 — equality at the reference η = 0.05. The
chain does not rely on power room there: the trivial-piece sum carries the
factor L^{C−2B} from δ_μ (Σ_μ μ ≤ (RL^{−B})²), which saves the corner by
polylog for B ≥ C+c+4. Alternatively shave the cell (η = 0.04 gives
κ_lb ≈ 6·10⁻⁶, still positive). Recorded so the write-up (G3) does not
inherit the slip.

(d) **Cell symmetry vs the sum branch.** An asymmetric cell (u' − u ≥
(C+1) log log x / log x) would empty the tangency regime on the D-step, but
the C-step consumes the same Family-A structure with p↔q swapped (link 8),
re-creating it in the other orientation; so G1 cannot be dodged by cell
geometry and is kept as a genuine (elementary) debt.

(e) **g₀'s exactness.** The plain representation of the class indicator
(link 8) was checked: two cell primes q₁q₂ > x^{1−4η} > x^{3/10}·x^{1/2}
force a non-friable cofactor structure violating the class, so the q-sum
has ≤ 1 nonzero term — no inclusion–exclusion correction, no
interpolation in the DEMAND (only in Lemma B's and lem:SW's proofs).

(f) **3/10-variant of prop:one-large.** Needs cofactor ≤ (x^{3/10})²: on
the cell 1−u ≤ 1/2+2η ≤ 3/5 with equality only at u = 2/5 = 1/2−2η at
η = 0.05 — exactly the original proposition's boundary situation (handled
trivially there); for η < 0.05 strict inequality holds. Fine, but G2's
write-up must say it.

(g) **What the imposed coins prove.** Link 5's sufficiency claim was
re-derived from the carry laws: for the cell prime, j = 1 gives fr = 0
(p | n), j ≥ 3 gives fr < 1/2 (p³ > 2x ≥ 2n on the cell since 3u ≥ 1.2);
for cofactor primes ℓ‖n, one slot-2 success meets the budget e = 1; the
(n−1)-side mirror uses the margin windows of D₀⁽⁺⁾ — all inside
proved/elementary territory (FK law, 04-architecture lines 12–16,
lem:sandwich's no-wrap branch).

(h) **No hidden upper-bound-track debt.** Grep of the chain against the
10-remaining ledger: (DMV), (Hal), (Vin), E1, E2, E3†-full, hyp:Cdagger-as-
printed, W1 (uniformity across the averaged assembly), W3 (FK gluing for
full Lemma C) are consumed NOWHERE above — they are asymptotic-track items.
W2 (fine-class bookkeeping) survives only in its lb-restricted form inside
G2/G4 (the single class "one cell prime × friable cofactor"), not as the
general fine-class program.

(i) **Ledger arithmetic.** [0.1 × 0.41 × 0.09]² = (3.69·10⁻³)² ≈ 1.36·10⁻⁵
≈ 1.4·10⁻⁵ ✓ (audit §6); all nine ledger rows re-checked as fixed positive
constants or subtracted small terms; item 6 (auto-carry) correctly enters
at cost 0, not as a class.
