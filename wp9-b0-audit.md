# WP9: B=0 consumer audit — can C† exit the lower-bound track?

STATUS: COMPLETE (bookkeeping audit; no new analytic claims). Date: 2026-06-10.

VERDICT (one line): **C† PARTIALLY removable — NOT removable as a species
(the B=0 escape hatch is CLOSED), but reducible to a sharply minimal
residual C†-single-lb(g₀): one fixed plain weight, one coin per side,
fixed harmonics, exceptional-set form.** Minimal lb-track list:
{E3-lb (two-sided), C†-single-lb(g₀)}; E1 NOT needed, E2 NOT needed,
C†-pair NOT needed, DMV NOT needed, (Hal) NOT needed.

Question (from wp8-cdagger.md, lb-section flag): for Theorem 1′ (positive
lower density of W₁ = {n : n(n−1) | C(2n,n)}), trim registry permits
restriction to any positive-proportion anatomy subclass. If the cofactor
side carries no band primes beyond designated ones (B(n)=1, B(n−1)=1 with
friable cofactors, or B=0), do any consumers of Lemma C's weighted layer
survive? Can the weight g(n−1) be replaced by a plain indicator via a
positivity/sandwich (inclusion–exclusion) argument? What is the minimal
residual hypothesis list for the lb-track (E1? E2? E3-lb? C†-lb?), and
the density cost of each restriction?

Sources read: manuscript/sections/04-architecture.tex,
14-lemmaC-reduction.tex, 15-spine-bookkeeping.tex (prop:cascade),
lemma-C-within-side.md, wp8-cdagger.md (lb section).

Additional sources consulted beyond the assignment list: 06-reduction.tex
(est:Ddagger, lem:beta, prop:two-freq), 08-major.tex (lem:branch, E1, E2,
prop:digit-assembly, and the lb-exemption sentence), 09-anatomy.tex
(prop:one-large, prop:species), 10-remaining.tex (ledger, trims),
11-typeII.tex (hyp:E3), 12-e1e2.tex, 01-intro.tex (thm:lower),
lemma-D-cross-side.md (auto-carry slivers), wp8-e3.md §5 (E3-lb).

## 1. Inventory: consumers of Lemma C's weighted layer (from sources)

Read so far: 04-architecture.tex, 14-lemmaC-reduction.tex,
15-spine-bookkeeping.tex (prop:cascade), lemma-C-within-side.md,
wp8-cdagger.md (lb section), 11-typeII.tex (hyp:E3), wp8-e3.md §5.

**Where C's weighted layer is invoked (exhaustive list from prop:cascade
proof, 15-spine-bookkeeping.tex lines 148-174):**

The cascade factors, within each anatomy-class pair at resolution rho:

  joint = (anatomy-pair indicator) x (digit indicator of n | class)
          x (digit indicator of n-1 | rest)

Step order: (D-step) replace third factor by class mean via Lemma D
[cost L^{-c_D}]; (C-step) replace second factor by its class mean via
Lemma C, "the remaining (n-1)-side data (anatomy only, after the D-step)
being rendered 1-bounded multiplicative by the generalized interpolation
of Lemma interp" [cost L^{-c_C}]; (B-step) factor the anatomy pair via
Lemma B [cost L^{-c_B}].

So the ONLY consumer of C's *weighted* layer (g != 1) in the entire
cascade is the C-step, and the only weight ever fed to C is:

  g(n-1) = z-interpolation combination of band-count indicators of the
           (n-1)-side ANATOMY BOX (1-bounded multiplicative via
           lem:interp; the (n-1)-side DIGIT data has already been
           removed by the D-step and never reaches C).

This is decisive for the audit: the weight g in Lemma C's application is
never an arbitrary SW-multiplicative function in the assembly — it is
precisely the (n-1)-anatomy-box indicator, interpolated. (hyp:Cdagger as
stated in 14-lemmaC-reduction.tex is uniform over SW-multiplicative g,
i.e. strictly stronger than what prop:cascade consumes.)

**C's internal structure (14-lemmaC-reduction.tex):**
- prop:C-cov (PROVED): unweighted (g=1) two-band-prime core = the
  two-frequency minor/major machinery; minor pairs give sqrt(R) saving,
  major pairs counted by Family-A/B at density O(L^{2-B}).
- prop:C-weighted (DEMOTED, open): weighted minor pairs; rests on C-dagger.
- prop:C-single (DEMOTED, open): single-band-prime weighted core,
  conductor p^2 = x^{2u} > x^{2/3} beyond GS/DGS; rests on C-dagger.
- Major-pair absorption remark (statusO): Halasz/MRT cannot control means
  of g along APs of modulus > length; asymptotic track debt only.
- prop:C-assembled: Lemma C := [unweighted core (proved)] +
  [weighted layer (= C-dagger)] + [FK gluing (ledger)].

**Population cases of C by band count B(n) of the n-side:**
- B(n)=0: no band prime on n. NO binding band-digit condition exists on
  the n-side band layer; Lemma C's band-digit equidistribution claim is
  VACUOUS for this class (the only digit data are deep slots j>=3 of
  smaller primes, handled in upper-bound mode via chooseable position
  p^{j-1} <= x^{1/2}, prop:C-single last sentence, and the top-slot
  deterministic FK law). [To verify below: whether deep slots need g.]
- B(n)=1: single binding digit at conductor p^2 — prop:C-single, the
  C-dagger-single case. Auto-carry sub-band q^2 in (n,2n] (log-measure
  0.288 of slot-2 successes) is deterministic-success: C void there
  (trim registry item 4, 04-architecture.tex line 229-231).
- B(n)=2: pair case V^C(g), conductor p1p2 — C-dagger-pair. Removed
  already by the B<=1 subclass (wp8-cdagger.md lb section).

## 2. (a) Consumers remaining under B(n)=1, B(n−1)=1 + friable cofactors

Fix the lb-class (per side): exactly one band prime in a positive-measure
cell of the band, cofactor friable at x^{3/10} (the DGS boundary: see
below; x^{10/39} if only GS is cited). Walk the C-consumer list:

1. **prop:C-weighted / C†-pair (two-band-prime weighted minor pairs):
   VOID.** No n in the class has two band primes; V^C(g) never forms.
   Consequently the **(DMV) citation debt exits the lb-track** (it feeds
   only weighted minor *pairs*, ledger 10-remaining (DMV) item).
2. **Major-pair absorption clause ((Hal) debt): VOID** for the lb-track
   twice over: no pairs, and majors are discarded into the trim/δ₀
   budget rather than absorbed (wp8-cdagger lb §(a); consistent with
   08-major lines 10-12).
3. **Cofactor-prime coins (primes x^δ < ℓ ≤ x^{3/10} of the cofactor):
   REMAIN in C's weighted layer but are CLASSICAL, not C†.** For the
   lower bound, positivity lets us impose only the *slot-2* carry at
   each cofactor prime (1[≥1 carry] ≥ 1[slot-2 carry]) — lower-bound
   mode, the cheap direction. Detection conductor ℓ² = x^{2v} ≤ x^{3/5}:
   inside Drappeau–Granville–Shao (x^{3/5}); inside Granville–Shao
   (x^{20/39}) if v ≤ 10/39. So this consumer is discharged by the
   pinned GS/DGS citations (prop:C-single's classical clause — which is
   valid *below* the band; it was demoted only for band conductors).
   Deep digits (j ≥ 3) exit entirely in lb-mode (we never impose them).
   **Boundary caution:** primes with v ∈ (3/10, 1/3) have minimal
   conductor x^{2v} ∈ (x^{3/5}, x^{2/3}) — beyond DGS but below the band
   as §14 states C†. This gap window must be EXCLUDED from the cofactor
   (the friable cutoff at x^{3/10} does exactly this). Without the
   exclusion, an unregistered C†-like species at conductors
   (x^{3/5}, x^{2/3}) would survive — flagged as a statement-scope bug
   in hyp:Cdagger (its "band" floor 1/3 is not the classical-range
   boundary; 3/10 is).
4. **The band coin (slot-2 at the designated p, conductor
   p² = x^{2u} ∈ (x^{2/3}, x^{1−2η})): REMAINS, and is irreducible in
   the cascade architecture.** This is the single surviving consumer of
   C†: the C-step of prop:cascade with weight g₀ = the (n−1)-side class
   indicator (after the D-step has removed the (n−1)-digit data). One
   coin per side, single-prime case only.

**Net (a):** exactly one C†-consumer remains — C†-single at the band
conductor, with the one fixed weight g₀; everything else in C's weighted
layer is void or classical (GS/DGS) in this class.

## 3. (b) Replacing g(n−1) by a plain indicator (sandwich/positivity)

Split the question in two.

**(b1) Is the weight already plain? YES.** The cascade (prop:cascade,
15-spine lines 158-164) only ever feeds Lemma C the (n−1)-side
ANATOMY-box indicator (the digit data is gone after the D-step); the
interpolation lem:interp is a *tool*, not part of the demand. So the
lb-track may state its C-input for the single fixed function
  g₀(m) = Σ_{q ∈ cell} 1[q | m]·1[P^+(m/q) ≤ x^{3/10}]
(plain, 0/1-valued; ≤ 1 nonzero q-term since two cell-primes would
violate the friability — the representation is exact). **No uniformity
over SW-multiplicative g is needed** — hyp:Cdagger as stated in §14 is
strictly over-engineered for the lb-track. This is a genuine weakening
(family → single function) and should be recorded.

**(b2) Can weighted-C then be avoided altogether — joint count
lower-bounded by inclusion–exclusion through Lemma B alone? NO.** Lemma
B is anatomy×anatomy; the surviving object is digit×anatomy
(slot2_p against g₀). Every positivity rearrangement was checked and
fails quantitatively:

- *Drop g₀ and compensate (Bonferroni at the class level):*
  Σ 1[A]f_p·1[B] ≥ Σ 1[A]f_p − Σ 1[A]f_p·1[¬B] needs the subtracted
  term < main; but P(¬B) ≈ 1 ≫ P(B)/4. Dead. (Variant with 1[¬B]
  retained reproduces weighted-C with weight 1−g₀ — same species.)
- *Make the n-side coin deterministic (auto-carry sliver):* the
  deterministic slivers q² ∈ (n/2, 2n/3] ∪ (n, 2n] force the slot-2
  digit, but as a class of integers n the sliver has density
  ≍ 1/log x, NOT positive proportion: n must have a prime in a
  constant-multiplicative-width window around √n
  (Σ_{q ≤ √x} q/2 ≈ x/(2 log x) such n ≤ x). **Correction to
  wp8-cdagger's framing:** "log-measure 0.288" is the measure of the
  sliver in the log(n/q²)-variable per configuration (per
  lemma-D-cross-side item 1), useful for the constructive route and for
  shaving C†'s variance set — it is NOT a positive-proportion anatomy
  subclass and cannot carry Theorem 1′.
- *Union-bound the coin away:* impossible — its complement has mass 1/2
  (the registered dead end "union bounds across the digit layer,
  failure mass Θ(1)", 10-remaining).
- *Sieve-open g₀ into congruences* (expand 1[friable cofactor] by exact
  bounded-depth inclusion–exclusion over window primes ℓ, so the C-step
  becomes decorated counts along APs mod qℓ₁⋯ℓ_k, D†-species, no
  multiplicative weight): the k=0 term works beautifully — its μ=0 part
  is anatomy-in-AP mod q ~ x^{u'} < x^{20/39}, inside GS, and its μ≠0
  part is the proved two-frequency layer + E3-species. But the k ≥ 1
  terms carry Θ(1) relative mass (Σ 1/ℓ ≈ log(0.55/c) ≈ 0.5–1.2) at
  moduli qℓ > x^{0.6} and must be EVALUATED (they enter with signs; the
  alternating sum reconstitutes ρ — an upper bound with constant-factor
  loss destroys positivity). At every cell geometry these progressions
  are sub-one-per-class (qℓ > x ≥ length regimes) or beyond-√: the same
  wall in counting coordinates. Checked at top cell (u=u'=1/2−η:
  ℓ > R = x^{2η} always) and bottom cell (u=u'=0.34: hard mass
  log(0.66/0.32) ≈ 0.72 survives). **The wall is intrinsic: g₀'s
  divisor structure has unavoidable Θ(1) mass beyond every classical
  modulus range** — the same diagnosis as §14's unifying remark, seen
  in sieve coordinates. C† and this wall are one object.

Side finding (medium primes can't rescue B=0 either, see §5a): handling
cofactor coins by *subtraction* instead of imposition fails for every
friability cutoff c: the needed majorant-retention inequality
4·C_loss·η(c) < 1 fails for all c (η(c) ≈ Σ_{J≥1/c} (1/J)2^{−(J−2)}
against C_loss ≈ Mertens(window)/ρ(0.55/c); the product exceeds 1 on
(0, 1/3], minimized ≈ 1.3 near c ≈ 0.2). This independently confirms
that the cofactor coins must be imposed inside the weighted layer —
which is fine, since there they are GS/DGS-classical (§2 item 3).

## 4. (c) Minimal residual C†-statement, and the closed B=0 hatch

**(c1) The B(n)=B(n−1)=0 escape hatch is CLOSED.** Two independent
mechanisms, both decisive:

- *Smooth-cofactor no-go, sharpened.* B=0 does not make Lemma C's
  weighted layer empty: the digit data R(n) lives at ALL primes
  > x^δ (04-architecture, definition of A,R), and a B=0 integer still
  carries genuine coins at primes in (x^δ, x^{1/3}] — those of size
  v ∈ (1/4, 1/3) fail with probability ≈ 1/2 (one random slot), i.e.
  band-like coins one octave down. They cannot be union-bounded
  (failure mass Θ(1)); forbidding them extends the forbidden window
  down to x^c and forces P^+(n) ≤ x^c on the WHOLE integer, paying
  Dickman ρ(Θ(1/c))² against a subtraction floor ≈ 2^{−1/c}:
  ρ(t) = t^{−t(1+o(1))} loses for every c
  (2^{−(2/c)log₂ c⁻¹} ≪ 2^{−1/c}) — exactly the recorded no-go
  (04-architecture remark; 10-remaining dead-end list), now verified to
  bite this hatch.
- *Geometry inversion below the band.* Imposing the (1/4, 1/3)-coins
  jointly instead would rerun the D†/two-frequency machinery at
  sub-band sizes, where the in-band facts flip: R = x/(pq) ≥ x^{0.4}
  ≫ P, the worst-case Family-A branch count R²Q/(PL^{2B}) ≫ P is
  vacuous, and E1-type *averaged* major counts re-enter — a regression,
  since the in-band lb-track needs no E1/E2 (08-major lines 10-12).
  (Partial compensation — R > y un-voids the small-Λ damping in the
  E3-objects — does not pay for this.)

So: hyp:Cdagger's flagged hope (wp8-cdagger lines 235-239, "if the
assembly permits it, C† exits Theorem 1′ entirely") does NOT validate.

**(c2) Minimal residual statement (the exact surviving hypothesis).**

> **Hypothesis C†-single-lb(g₀).** Let U = (1/2−2η, 1/2−η) (top cell;
> any positive-measure cell works, top is optimal — §5), and let
> g₀(m) = Σ_{q = m^{u'}, u' ∈ U} 1[q|m] · 1[P^+(m/q) ≤ x^{3/10}] be the
> fixed plain (n−1)-class indicator. There are δ₀ > 0 and c > 0 such
> that for each fixed 0 < |h| ≤ (log x)^C, the centered sums
>   V_p(h) = Σ_{m ≤ x/p} g₀(pm − 1) e(hm/p) − (main term, FK law)
> satisfy the single second-moment bound over minor band primes
> p = x^u, u ∈ U (auto-carry slivers may be excised):
>   avg_{p minor} |V_p(h)|² ≪ δ₀ (x/p)² (log x)^{−2c−2C−10}.

By Chebyshev + union over the O(L^C) harmonics this gives the per-prime
C-bound pointwise off a δ₀-density exceptional set of p, discarded into
the sandwich at cost O(δ₀). Differences from hyp:Cdagger as stated in
§14: single-prime case only (no pair, no bifactorable moduli); ONE fixed
0/1 weight g₀ (no SW-family uniformity); minor p only (majors
worst-case-counted and discarded); no asymptotic, no main-term
evaluation; second-moment/exceptional-set form; one positive-measure
cell. **What does not weaken:** the conductor is still p² = x^{2u} >
x^{2/3} (the binding digit is a mod-p² datum of n — intrinsic-conductor
argument of wp8-cdagger §1 applies verbatim to g₀, whose q-AP × friable
structure does not reduce it), so C†-single-lb(g₀) is open for the same
analytic reason as C† (Lemma-α/Route-2′ shortfalls stand).

## 5. E3-lb: anatomy subclass minimizing its burden

**(5a) Which subclass.** Same class as for C†: B=1 per side with
x^{3/10}-friable cofactors, cell at the TOP of the band,
u, u' ∈ (1/2−2η, 1/2−η) with corner trim satisfied (u+u' = 1−O(η),
R = x^{Θ(η)} ≥ polylog ✓). Reasons, quantified:

- The friable indicator unwinds exactly (prop:one-large: cofactor
  a ≤ x^{1−u} < y², at most one prime > y): 1[friable] = 1 − Σ_{ℓ>y,ℓ|a},
  so E3's object appears with ℓ-mass Σ_{y<ℓ≤A} 1/ℓ = log(3(1−u)),
  minimized at the top: log(1.5+O(η)) ≈ 0.405. (A B=2-style class makes
  σ the rough indicator directly AND needs C†-pair: strictly worse.)
- The HARD sub-range identified by wp8-e3 §4 is Λ ∈ (Q, Q^{3/2}]
  (sub-complete-sum, beyond per-ℓ Weil); intersected with the ℓ-support
  (y, A] it is (x^{u'}, x^{1−u}], of mass log((1−u)/u') ≈ **4η at the
  top cell** — the burden shrinks linearly with the trim. Below Q the
  q-interval exceeds the modulus (complete-sum regime, Weil power
  saving); above A the support is empty.
- Bonus consistency: at the top cell the worst-case (per-q) Family-A/B
  counts are power-small (R²Q/P = x^{4η+u'−u} ≪ P), so the lb-track's
  E1/E2-exemption (08-major) holds with power room; and E2's proved
  sub-band 16u+10u′ > 10 contains the cell (11.7 > 10 at (0.45,0.45)) —
  moot but reassuring.

**(5b) E3-lb must be stated TWO-SIDED (the §06/§15 gluing gap, now
resolved as a ledger item).** est:Ddagger carries only the n-side
decoration w(1+qm) over the FULL m-range, but prop:cascade's D-step
centers the (n−1)-digit with 1[anat(n−1) ∈ B] present: the m-population
is class-restricted. Unwinding 1[P^+(b) ≤ x^{3/10}] on b = pt + b₀
(linear in the t-parameter; prop:one-large applies on the b-side too
since u' > 1/3) injects rough terms 1[ℓ | pt+b₀] into the λ≠0
harmonics: dilated-frequency geometric sums / ℓ-resonance counts /
Type-II at large ℓ — the SAME species as §09, at modulus p instead of
q. These are error-mode (upper bounds with L^{−c} saving, exceptional-set
form admissible), so they belong in E3-lb, not in a new hypothesis:

> **E3-lb (two-sided population form).** The exceptional-set statement
> of wp8-e3 §5 for the a-side rough sums, PLUS its mirror for the
> b-side rough sums inside the λ-harmonics (band-average over q,
> δ₀-exceptional q-set, fixed λ, core μ only; T1 covers the rest
> pointwise).

This addition is a bookkeeping completion, not a strengthening of
species: both sides sit on the identical dilated-phase/Type-II
frontier, and the b-side hard mass is also O(η) at the top cell
(window primes vs length R: all sub-one at the top cell — large-Λ
Type-II species of prop:species, claimed standard-toolbox there; the
genuine-check caveat (iii) of §09 extends to it).

## 6. Density ledger (every restriction, positive-proportion check)

All factors below are fixed positive constants (x-independent); their
product is the lb main-term coefficient. Reference values at η = 0.05,
δ = 0.01, log-density at almost-all scales (lb needs one good scale
sequence — free).

| Restriction | Cost factor (per side unless noted) | Positive? |
|---|---|---|
| 1. Top-of-band + corner trims (registry 1-2) | absorbed into cell choice | ✓ |
| 2. Cell u ∈ (1/2−2η, 1/2−η), one band prime | Mertens ≈ log((1/2−η)/(1/2−2η)) ≈ 2η ≈ 0.1 | ✓ |
| 3. Cofactor x^{3/10}-friable (kills C†-gap window (x^{3/10},x^{1/3}) and second band primes) | ρ((1/2+2η)/(3/10)) ≈ ρ(1.8) = 1−log 1.8 ≈ 0.41 (GS-only variant: ρ(1.95) ≈ 0.33) | ✓ |
| 4. Imposed slot-2 coins: band prime (1/2) × cofactor primes (≥ 2^{−ω}, ω = #primes in (x^δ, x^{3/10}); class-average ≈ (δ/0.3)^{1/2}-type ≈ 0.18 at δ=0.01) | ≈ 0.09 | ✓ (fixed δ; lb does NOT need δ→0) |
| 5. Lemma A exceptional set + square-discard (subtracted) | −O(e^{−c_A/δ}) − O(x^{−δ}); choose δ with e^{−c_A/δ} < 1% of product | ✓ |
| 6. Auto-carry sliver | NOT used as a class (density ≍ 1/log x — §3); excised from C†-variance set only, cost 0 | ✓ |
| 7. δ₀-exceptional sets (E3-lb, C†-single-lb) | −O(δ₀), δ₀ ≤ 1% of product | ✓ |
| 8. Major (p,q) discards (worst-case counts, top cell) | −O(L^{−pos}) | ✓ |
| 9. Slot-boundary slivers (registry/D5) | −O(ε′) | ✓ |

Joint pair coefficient ≈ [0.1 × 0.41 × 0.09]² × (1−small) ≈ 1.4·10⁻⁵ —
small but a fixed positive proportion. The joint anatomy-pair lower
bound (after both digit removals) is Lemma B's job: TT-route, or the
registered elementary Hildebrand stable-set fallback (04-architecture);
scope-check that the fallback covers "one cell prime × friable
cofactor" boxes is a write-up item (it is anatomy-only — no digit data
— so the TT dilation-blocker does not apply).

## 7. Verdict

**C†: PARTIALLY REMOVABLE.**

- REMOVED from the lb-track: the pair case (and with it the DMV debt),
  the major-pair absorption ((Hal) debt), g-family uniformity, deep
  digits, all asymptotics, all sub-x^{3/5}-conductor weighted content
  (→ GS/DGS classical).
- NOT removable: one irreducible consumer — the single band coin per
  side against the fixed plain class weight g₀, conductor p² > x^{2/3}.
  The flagged B=0 hatch is CLOSED (smooth-cofactor no-go + sub-band
  major-geometry inversion, §4c1); the sieve-opening restructure
  relocates but does not lower the wall (§3 b2).

**Exact minimal lb-track hypothesis list for Theorem 1′:**

1. **E3-lb, two-sided population form** (§5b) — open, exceptional-set;
   hard mass O(η) at the top cell.
2. **C†-single-lb(g₀)** (§4c2) — open, exceptional-set second moment,
   single fixed weight, single-prime case.
3. NOT needed: **E1** (08-major: worst-case-per-q suffices; power room
   at the top cell), **E2** (same; cell also inside its proved
   sub-band), C†-pair, DMV, (Hal).
4. Classical/citation inputs: GS + DGS (cofactor coins, anatomy-in-AP
   mod q at the k=0 layer), SL2′/lem:SW (Siegel–Walfisz for g_z), FK21
   counting, TT25-or-Hildebrand for the anatomy pair (lb: Hildebrand
   fallback suffices, scope-check pending).
5. Proved layers consumed as-is: Lemma 0/margins, Lemma A, deep large
   sieve + prop:largelambda, thm:minor (T1), lem:branch worst-case,
   prop:one-large/prop:species, depth packaging, prop:cascade
   bookkeeping (with the D-step population clause now routed per §5b).

Highest-value next actions: (i) restate hyp:Cdagger in the manuscript
with the C†-single-lb(g₀) minimal form and the 3/10-boundary fix (§2
item 3); (ii) add the b-side clause to E3-lb and register the §06/§15
population gluing as resolved-by-statement; (iii) attack
C†-single-lb(g₀) directly — its g₀ is q-AP-times-friable, far more
structured than a general SW weight, and the empirical collapse
(z: 13.1 → 0.78) lives exactly in its variance.
