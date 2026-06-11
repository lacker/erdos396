# WP12: Diagnosis of C†-single-lb(g₀) — the weighted coin-flip estimate

STATUS: DIAGNOSIS COMPLETE (no proof attempts beyond sketches). Date: 2026-06-11.
Sources: wp9-b0-audit.md (§4c2 minimal statement, §2 item 3 scope fix),
wp8-cdagger.md (lb Chebyshev closure + dead angles), wp9-verify-e3cd.md
(CD-section: closure verified, exponent −2c−2C−10 calibrated),
lemma-alpha-beta.md (Lemma α/β, Routes 1/2/2′ shortfalls),
manuscript/sections/05-deep-large-sieve.tex (thm:dls, cor:ap),
06-reduction.tex (lem:beta, lem:linearization, prop:largelambda),
14-lemmaC-reduction.tex (hyp:Cdagger, prop:C-single), main.tex;
wp11-e3lb.md verdict section (for the SHARES-E3-CORE comparison).

Notation: L = log x; η fixed (reference 0.05); top cell U = (1/2−2η, 1/2−η);
p ~ P = x^u, u ∈ U, minor; M = x/p ∈ (x^{1/2+η}, x^{1/2+2η});
B_lb := 2c+2C+10 (the lb-calibrated polylog, wp9-verify CD); δ₀ = exceptional
density budget; κ := density of g₀ ≈ log(0.45/0.40)·ρ(0.55/0.30) ≈ 0.118×0.35
≈ 0.04 (fixed positive constant — NOT 1/L; the cell has constant Mertens mass).

## 1. The precise minimal object

**Hypothesis C†-single-lb(g₀)** [= wp9-b0-audit §4c2, restated cleanly with
the 3/10-floor scope fix]. Let

  g₀(n) = Σ_{q′ prime, q′ ∈ (x^{1/2−2η}, x^{1/2−η}]} 1[q′ | n] · 1[P⁺(n/q′) ≤ x^{3/10}]

— the single FIXED plain 0/1 weight (the (n−1)-side anatomy-class indicator;
at most one q′-term survives since two cell primes violate the friability; the
3/10 floor — not hyp:Cdagger's 1/3 — excises the gap window (x^{3/5}, x^{2/3})
of conductors so that ALL sub-band weighted content is GS/DGS-classical).
For m ≤ M put n = pm−1 (so n ≡ −1 (p), n ≤ x clean) and, for each fixed
0 < |h| ≤ L^C,

  V_p(h) = Σ_{m ≤ x/p} g₀(pm−1) e(hm/p)  −  (FK main term; for h ≠ 0 this is
           the geometric edge term κ_p Σ_m e(hm/p), |·| ≤ κp/(2|h|) — a factor
           x^{2η} below target, absorbable but present).

Demand (second-moment / exceptional-set form): there are δ₀, c > 0 with

  (1/#{p minor}) Σ_{p∼P minor} |V_p(h)|² ≪ δ₀ (x/p)² L^{−2c−2C−10},

minor p only (majors worst-case-counted and discarded into δ₀; auto-carry
slivers excisable), for one positive-measure cell (top cell optimal for the
sibling brick E3-lb). Consumer closure: Chebyshev per h + union over the
O(L^C) harmonics → pointwise C-bound off a δ₀-density p-set → sandwich
discards at O(δ₀). VERIFIED to close with room (wp9-verify-e3cd, CD section:
the exponent −2c−2C−10 absorbs both the harmonic union (L^{C} in the single
case) and the weight mass; contrast E3-lb's E3-5 miscalibration, repaired
separately).

**Why it is open (intrinsic conductor).** m mod p ↔ n mod p² on n ≡ −1 (p):
the binding datum is a mod-p² datum of n. Equivalently (machine-proved chain):
e(hm/p) = χ_h(−n) — a depth-one Fermat-quotient character of conductor
exactly p² (def:fq + lem:beta primitivity). Conductor p² = x^{2u} ∈
(x^{1−4η}, x^{1−2η}) at the top cell — beyond GS (x^{20/39}), DGS (x^{3/5}),
and every known dispersion range, while the modulus p = x^{1/2−η} itself is
INSIDE GS. The twist is what is open; the AP alone is classical.

**Scale card (top cell, η = 0.05, u = 0.45):** modulus p = x^{0.45};
conductor p² = x^{0.90}; length M = x^{0.55}; periods M/p = x^{0.10};
fiber per class mod p²: x/p² = x^{0.10} (sparse); fiber mass
G_p := #{m: g₀(pm−1)=1} ≈ κx/p = κx^{0.55}.
Trivial: |V_p|² ≤ G_p² = κ²x^{1.10}. Target: δ₀x^{1.10}L^{−B_lb} — a PURE
POLYLOG below trivial. Truth (square-root cancellation, §3 numerics):
|V_p|² ≈ G_p = κx^{0.55} — a factor x^{0.55} below trivial. The statement has
x^{1/2}-grade truth-room; the demand has only polylog slack vs trivial. All
three routes below live in that wedge.

## 2. Three candidate routes, priced at the top cell

Budget for the p-averaged form: Σ_{p minor}|V_p(h)|² ≪ δ₀ (P/L)(x/P)² L^{−B_lb}
= δ₀ x^{3/2+η} L^{−B_lb−1}  (= x^{1.55−} at η = 0.05).

### Route 1: α-second-moment (Lemma β opening + Garaev completion + Baier–Zhao)

The task's question: Lemma α bounds the average over moduli p of the MAX over
primitive χ mod p²; the lb-form needs only a SECOND MOMENT over p of ONE
character sum. Does α's machinery give the second-moment version with a
better exponent? **Answer: yes, by x^{1/2−η}-grade — and it then stalls at
exact budget saturation, polylog-short, for a structural reason.**

Chain. lem:beta (PROVED): V_p(h) = χ_h(−1)/φ(p) · Σ_{χ₁ mod p} S(χ̃₁χ_h),
S(χ) = Σ_{n≤x} g₀(n)χ(n), every χ̃₁χ_h primitive mod p². Coset Cauchy–Schwarz
is an EXACT identity, not just a bound:
  (1/φ(p)) Σ_{χ₁} |S(χ̃₁χ_h)|² = Σ_{c mod p} |V_p^{(c)}(h)|²,
the same object summed over ALL residue classes n ≡ c (p) — a positivity
extension from the one class c = −1 to p classes. Affordability check: the
extension multiplies the truth by p but the per-p target (x/p)²L^{−B} sits a
factor x^{2η}L^{−B} above the extended truth κx — affordable for any fixed
η > 0 (this is Route 2′ of lemma-alpha-beta §3, which "discards the deep
twist": the discard is exactly affordable in lb-mode at the top cell, which
the asymptotic track could not afford).

Pricing (N = x, Q = P = x^{1/2−η}, ‖g₀‖₂² = κx; exponents at η = 0.05):
- (1a) Lemma α verbatim (max-form, ν = 1): Σ_p max_χ |S|² ≪
  (Q³ + N + min(NQ^{1/2}, N^{1/2}Q²)) N x^{o(1)} = x^{1.35}·x = x^{2.35}.
  Deficit vs x^{1.55}: **x^{0.80} = x^{1−4η}**. (Route-1-of-α rediscovered.)
- (1b) Second-moment version (coset identity + 1/φ(p) weight + full-family
  BZ mean square — extend the p-element coset to all ≈ p² primitive χ mod p²,
  Hölder-free): bound = (1/P)(P³ + N + min(NP^{1/2}, N^{1/2}P²))·κx:
  terms x^{1.90} / x^{1.55} / x^{1.775}. Leading: (1/P)P³N = P²N = x^{2−2η}.
  Deficit: **x^{1/2−3η} = x^{0.35}**. The binding term is now the BZ family
  count P³ — paid only because the coset (P² characters total) was extended
  to the full family (P³). The max-device and Hölder are NOT the binding
  loss; the family extension is.
- (1c) Thin-family repair (NEW spacing lemma needed): after Gauss/Garaev
  completion the coset corresponds to deep-shifted Farey points
  {b/p + c_h(p)/p²: b mod p, p ∼ P}: within-modulus spacing 1/p exact;
  cross-moduli spacing 1/(pp′) MINUS deep shifts of the SAME order 1/P² —
  near-collisions exactly on |bp′ − b′p| ≤ 1 lines (O(1) per (b,p,p′), but
  ~P/L potential partners per point). IF a spacing/excision lemma controls
  these (elementary-looking, unproven, alignment needs an arithmetic input
  on h(p̄′² − p̄²)-type quantities), the best conceivable constant is
  Δ = N + O(P²) = x(1+o(1)), giving bound (1/P)·x·κx = κx^{3/2+η}:
  **EXACT BUDGET SATURATION** — short of target by precisely δ₀^{-1}L^{B_lb+1},
  a pure polylog.
- Why it stops there: the large sieve is sharp for coefficient sequences
  concentrating on one character's Bohr set; beating saturation requires the
  g₀-specific non-concentration (non-pretentiousness per character) to be
  converted into the family average — which is the original problem. Duality
  is constitutionally unable to supply the last L^{−B}. Same endpoint as the
  D3 sector of wp8-cdagger (budget saturated; aggregate cancellation real —
  numerics — but unextractable by these tools).

What it gives: power deficit x^{0.80} → x^{0.35} (citable) → 0 (conditional
on a new spacing lemma). What it needs to finish: a non-duality input worth
L^{B_lb+1} at saturation. Net: **deficit L^{B_lb+1} at best; route cannot
close alone** — useful only as the frame into which a g₀-specific input lands.

### Route 2: deep-large-sieve / family average over the digit harmonics

Does averaging over the digit harmonics help the lb-form? **Yes — it is the
strongest structural simplification available: it removes the oscillatory
phase entirely**, at the price of a positivity extension that consumes most
of the x-room.

The consumer needs Σ_{0<|h|≤L^C}(1/⟨h⟩)|V_p(h)| ≪ (x/p)L^{−c−2} per good p.
Cauchy–Schwarz in h and positivity-extend the harmonic box to ALL h mod p
(legal: adding nonneg terms; requires L^C < p/2 ✓), then EXACT orthogonality
(the mechanism of cor:ap = classical additive large sieve in the progression
coordinate, here an identity):
  Σ_{h≠0 (p)} |Ṽ_p(h)|² = p · Var_p,
  Var_p := Σ_{m₀ mod p} |A_p(m₀) − (G_p/M)·cnt(m₀)|²,
A_p(m₀) = #{m ≤ M: m ≡ m₀ (p), g₀(pm−1) = 1} — the class-count variance of
the g₀-fiber over the p classes mod p² inside n ≡ −1 (p). Sufficient
replacement statement (harmonic-free!):

  **C†-single-lb-BDH:** for p ∼ P minor off a δ₀-density set,
  Var_p ≪ (x²/p³) L^{−2c−4}   [equivalently p·Var_p ≪ (x/p)² L^{−2c−4}];
  second-moment/Chebyshev form over p admissible as usual.

Pricing: truth (Poisson/BDH-grade) Var_p ≈ G_p = κx/p; target (x²/p³)L^{−2c−4}
= (x/p)·x^{1−2u}·L^{−2c−4}. Room: **x^{1−2u}L^{−2c−4}κ^{−1} = x^{2η−o(1)}
SURPLUS** (= x^{0.10} at η = 0.05) — positive power room for any fixed η, the
only route with one. (The full-h extension is what eats x^{1−2u} down to
x^{2η}; note the room GROWS to x^{1/3} at the band bottom u = 1/3+, a
cell-geometry tension against E3-lb, which prefers the top cell — recorded,
not resolved.)

What it needs: Var_p expands into lag correlations
  C_{p,k} = Σ_{n ≡ −1 (p)} g₀(n) g₀(n+kp²),  0 < |k| ≤ x/p² = x^{2η}
(only x^{2η} lags; diagonal k=0 is absorbed with x^{2η}-room), each needing
evaluation to RELATIVE precision L^{−B′} (log-precision, not power) with
mean-square-over-p and k-averaging available. This is a shifted convolution
of the (cell-prime)∗(friable) sequence at lag kp², restricted to the fiber
n ≡ −1 (p). Opening the shifted copy by its q″-divisor: g₀-sequence counted
in APs to joint modulus pq″ = x^{1−2η} — beyond everything; the mod-p fiber
is the crux (without it, modulus q″ = x^{1/2−η} < x^{20/39} is INSIDE GS,
margin x^{0.0128+η}). Fourier-expanding the fiber costs bilinear sums
Σ α_{q″}β_{s′} e(a q″s′/p) with the friable s′ flexibly factorable; the
optimized bilinear/large-sieve bound saves x^{0.225} per term vs the x^{0.45+}
needed pointwise — **per-term deficit ≈ x^{0.225}**; only an ensemble
dispersion over (p, k, q′) in second-moment form can close. Sub-one-per-class
checks: fixing (q′,q″,p,k), the s-variable lives in an AP mod pq″ = x^{0.95−}
against length x^{0.55} — 0/1-detector regime, no per-tuple bound exists;
cancellation must come from aggregates (the D3 phenomenology, one floor down).

What it gives: phase-free pure-counting form, x^{2η} statement surplus,
friable-flexible factorization (the DGS lever, unavailable to E3's
prime-only variables), log-precision-per-lag sufficiency, δ₀-exceptional
sets. What remains: a NEW bespoke variance-dispersion ("BDH at one square
modulus p² ∈ (x^{1−4η}, x^{1−2η}) for a prime×friable convolution") — the
modulus-average lever of classical BDH is structurally EMPTY here (each lag
kp² determines its p: no cross-p sharing of differences), so it stands or
falls on the bilinear structure of g₀ alone.

### Route 3: direct dispersion in p

Open Σ_p |V_p(h)|² (the second moment IS the dispersion quantity; the average
runs over the modulus — the genuine BFI orientation, unavailable to wp8's
pair case where p₁ was pinned). Structure: |V_p(h)|² = Σ_j e(hj/p) C̃_{p,j},
C̃_{p,j} = Σ_m g₀(pm−1)g₀(p(m−j)−1) — lag correlations along the fiber at
lags pj, |j| ≤ x/p, with the phase depending on j mod p only.
- No distinct-moduli sector forms: the second moment is p-diagonal by
  construction. The D3 sector of wp8-cdagger — completion conductor
  p₁p₂p₂′ > x, deficit ≥ x^{1/2} — is STRUCTURALLY ABSENT. This is the
  decisive bookkeeping advantage of single+second-moment over pair.
- Diagonal (j = 0): Σ_p G_p ≈ κ·0.12·x ≪ budget x^{3/2+η}L^{−B−1}:
  **x^{1/2}-grade room** (vs the pair case's exact-saturation diagonal).
- Everything else: quadruple count Σ_p G_p² = κ²x^{3/2+η}/L = budget·L^{B}:
  saturation at polylog distance; cancellation needed in
  Σ_{j≡δ(p)}-aggregates of C̃_{p,j} against e(hδ/p) — the Fourier-dual of
  Route 2's Var_p (pairs grouped by m−m′ mod p instead of m mod p). Routes
  2 and 3 are ONE route in two coordinates; 3 keeps the phase and per-h form
  (weaker demand), 2 trades the phase for the ℓ²-identity (cleaner object).
  Completion of the lag/AP conditions on the (q′,s,q″,s′)-opening produces
  Kloosterman-fraction-type sums with prime/friable-restricted variables at
  moduli pq″ ≈ x^{0.9} ≫ √(variable lengths): the named frontier of wp8
  obstruction 2 / wp9-frontier, with friable (not prime) long variables.

Deficit/surplus summary table (top cell, η = 0.05):

| route | citable machinery | best conceivable in-route | residual to close |
|---|---|---|---|
| 1 α-2nd-moment | deficit x^{0.80} (max-form) / x^{0.35} (coset+BZ) | saturation (needs NEW deep-Farey spacing lemma) | L^{B_lb+1}, no in-route mechanism |
| 2 h-average/BDH | n/a (no citation covers square-moduli BDH for sequences) | statement carries x^{2η} SURPLUS over Poisson truth | bespoke variance-dispersion; per-term bilinear deficit x^{0.225}, must be averaged away |
| 3 direct dispersion in p | diagonal closes with x^{1/2} room; off-diagonal saturates at L^{B} | same as 2 (Fourier-dual) | same bespoke dispersion, phase kept |

## 3. Numerics (model scale): is square-root cancellation there with margin?

Probe: `wp12_probe.py` (.venv/bin/python; run 2026-06-11, seed 396). The
LITERAL object: g₀ = (cell-prime in (x^{0.40}, x^{0.45}]) × (x^{0.30}-friable
cofactor), V_p(h) over m ≤ (x+1)/p, empirical-mean-centered (removes the
geometric edge term, which at model scale is comparable to the noise for
h ≤ 2 — at real scale it is x^{−2η}-absorbable). Normalization: Bernoulli
unit G(1−κ), so square-root cancellation ⟺ Z ≈ 1. Z1(p,h) per harmonic
(h = 1..8); Z2(p) = full-h mean = p·Var_p/((p−1)G(1−κ)) — the Route-2 object,
computed by class counts and machine-checked against the DFT identity.

| x | cell | #p | κ | Z1 mean/med/max | Z2 mean/med/max | Z2-tail >1.5 / >3 | perm control |
|---|---|---|---|---|---|---|---|
| 1e6 | top | 40 | .048 | 0.97/0.68/5.7 | 0.966/0.971/1.08 | 0 / 0 | 1.010 |
| 4e6 | top | 40 | .047 | 1.05/0.73/5.7 | 0.961/0.964/1.05 | 0 / 0 | 0.999 |
| 1.6e7 | top | 40 | .047 | 1.02/0.62/7.5 | 0.970/0.965/1.09 | 0 / 0 | 0.987 |
| 1.6e7 | low(0.34,0.36) | 17 | .048 | 0.75/0.52/6.2 | 0.886/0.893/1.05 | 0 / 0 | 0.986 |

Findings. (i) **Square-root cancellation is there with margin**: Z2 ≈ 0.97,
flat in x over a factor 16 (L: 13.8 → 16.6), statistically indistinguishable
from the permuted-fiber control — the arithmetic structure of g₀ adds NO
excess variance at this resolution, even in the sparse-fiber regime
(x/p² ≈ 5 elements per class mod p², the model analogue of x^{2η}).
(ii) The Route-2 aggregate Z2 is dramatically cleaner than per-h Z1
(max 1.09 vs 7.5 — Z1's spread is ordinary Exp(1) tails over 320 samples,
max ≈ log 320 ≈ 5.8, consistent): the exceptional p-set for the BDH form is
EMPTY at model scale, while the per-h form genuinely needs its δ₀/Chebyshev
slack. The h-averaged statement is the empirically natural one.
(iii) Limitation: model L ≈ 16 cannot distinguish L^{−B} demands from
constants; this is a truth-check of the power-scale claim and of
exceptional-set thinness, not of the polylog calibration.
(iv) All §2 exponent claims recomputed numerically (printout in probe):
route-1a deficit 1−4η, 1b deficit 1/2−3η, 1c exact saturation; route-2 room
2η and per-(p,k) bilinear deficit x^{0.225}; route-3 diagonal room x^{0.55},
quadruple saturation at target+0.000. All match.

## 4. Verdict

**SHARES-E3-CORE-GENUS (shallow end) — HARD, but measurably easier than
E3-core; TRACTABLE only conditional on one new bespoke dispersion.**

- It does NOT reduce to the literal E3-core sum: E3-core is bilinear
  Kloosterman over prime pairs in APs (phase e(−λsp̄₂/q)), currently
  OBSTRUCTED at every priced aggregation order (wp11: x^{0.41} citation-grade
  deficit, x^{1/4−2.25η} absolute CS floor). C†-single-lb(g₀)'s residual —
  after the Route-2 reduction, which is exact and elementary — is a
  PHASE-FREE variance: BDH at a single square modulus p² ≈ x^{1−2η} for a
  prime×friable convolution, with x^{2η} statement surplus. Both objects sit
  on the same named frontier (wp8-cdagger obstruction 2: aggregate
  cancellation at super-√ conductor where budgets saturate and classes are
  sub-one-per-tuple), so closing one does not close the other for free —
  but the technology would transfer, and every lever points the same way
  here and none is available to E3: (a) no distinct-moduli/D3 sector at all
  (second moment is p-diagonal); (b) flexible friable factorization of the
  long variables (DGS lever; E3's variables are rigid primes); (c) only x^{2η}
  lags, each needing only LOG-precision relative error; (d) power room x^{2η}
  in the statement (E3-lb's budget is constant-factor tight at 0.95ηR);
  (e) empirically empty exceptional set in the strongest (BDH) form.
- Routes priced out: Route 1 cannot finish even idealized (saturation =
  duality cap; the answer to the α-question is "yes, x^{0.80}→x^{0.35}
  citable, →saturation with a new deep-Farey spacing lemma — and there it
  is structurally stuck"). Routes 2/3 are one route; the genuine fight is
  the lag-correlation dispersion with per-term bilinear deficit x^{0.225}
  to be averaged away over (p, k, q′) in second-moment form.
- Estimated cost if attacked: 4–8 focused sessions to close-or-floor the
  Route-2 dispersion (design + pricing ladder like wp11's, with the friable
  lever); P(close with current technology) ≈ 0.3–0.4 — better odds than
  E3-core in its current state, and the right order is C† AFTER any E3
  progress, since transfer flows E3→C† more than conversely.
- Immediate cheap upgrade (bookkeeping, ~½ session): register
  **C†-single-lb-BDH** (the Var_p form, §2 Route 2) as the canonical minimal
  brick in place of the per-h form — weaker to consume, harmonic-free,
  empirically cleanest; seam note: its h=0/mean calibration consumes GS at
  modulus p < x^{20/39} (inside range, on average over p), which should be
  pinned when restating. Flag the cell-geometry tension: Route 2's room
  x^{1−2u} grows DOWN-band while E3-lb's hard mass shrinks UP-band; the
  joint cell for Theorem 1′ may want to sit slightly below the top.

Confidence in this diagnosis: ~0.8 (route arithmetic machine-checked at two
η values; the Route-2 reduction is an exact identity machine-checked in the
probe; numerics clean and scale-stable; residual uncertainty is whether a
cleverer-than-priced formulation evades the bilinear deficit, and the usual
model-scale/polylog blindness).
