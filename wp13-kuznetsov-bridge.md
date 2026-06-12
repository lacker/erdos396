# WP13: Kuznetsov / Deshouillers–Iwaniec Bridge for the W4.6 Closing Estimate

**Status: COMPLETE (2026-06-11). VERDICT: DOES-NOT-COVER — see §4. All sources fetched and quoted
verbatim from PDFs except DI82 original (quoted via Drappeau's published superset, flagged §2.1).**

**Deciding question.** Does Kuznetsov/DI-class technology (spectral theory of Kloosterman sums,
as packaged for dispersion by Drappeau 2017 and relatives) cover the W4.6 closing estimate of
wp11-e3lb.md §4.7.4 — signed cancellation on the cross-denominator coincidence graph, deficit
x^{2λ−0.725}, λ = log_x Λ ∈ [0.425, 0.575], top cell P = Q = x^{0.425}, R = x^{0.15}?

## Findings log

1. (§1.2 K3) NEW: prime-moduli restriction on W4.6 is REMOVABLE by positivity (|D_Λ(p,c)|² ≥ 0
   defined for all c ~ Q; diagonal re-closes at polylog cost). The W4.6 obstruction is NOT
   "Kuznetsov can't do prime moduli"; it is conductor/range.
2. (§1.2 K3) The all-moduli W4.6 main term is a SIGNED DIVISOR CORRELATION
   Σ_{c~C} Σ ĉĉ'·1[c | hℓ'−h'ℓ] — no Kloosterman oscillation survives the full-period a-sum;
   per-pair it is a nonnegative count (mass real & attained): per-pair c-sum tech can never help.
3. (§2.2) Drappeau Thm 2.1 / DI Thm 12: arbitrary b_{n,r,s} DISSOLVES the wp9 §2c numerator
   pair-dependence blocker — but every allocation leaves coefficient mass x^{1.125..1.575} ≫
   spectral conductor C² = x^{0.85}; best bound x^{0.2875} above the divisor floor (machine-checked).
4. (§2.5) Sarnak–Tsimerman/Steiner: our aggregate sits deep in the Selberg range (C ≤ √(mn) by
   x^{0.1375..0.2875}), where verbatim "the trivial bound is still the best known bound."
5. (§2.3) Prime-argument dressings range-dead (FKM p^{3/4+ε}; Bourgain–Garaev p^{1/2+ε}
   prime-modulus only; savings x^{0.02}-class vs needed x^{0.125+}). Spectral access to restricted
   moduli stops at P₆ almost-primes (Xi 2024); pure primes open — but mooted by finding 1.
6. (§2.4) KMS/BFKMM: range (MN < q^{5/4}), savings (q^{−1/64}), and category (PSD Gram form, not
   trace-function bilinear) all mismatch.
7. (§2.6) Bettin–Chandee trilinear: closest shape (arbitrary weights incl. modulus); fails on
   arity (quadrilinear with coupled ν(q,a) = self-similarity) and on M ≍ N ranges; at/above
   trivial here.
8. (§3) Dual check: cor:crude's pointwise form is Wieferich-hard (non-Wieferich infinitude open
   unconditionally — verified against source; a contrary web claim was an artifact); count-level
   literature (BFKS 2010) is fixed-q only; W4.6 needs SIGNS, counts provably cannot close it.
9. (§4) DOES-NOT-COVER; the missing estimate stated exactly in two equivalent forms; plausibly
   provable but research-grade; three positive deliverables for the program recorded.

## 1. The W4.6 object in Kloosterman-average language

Sources read verbatim this session: wp11-e3lb.md §§4.7–4.7.4 (W1.1, W2.1, W3.0–W3.4, W4.0–W4.8),
manuscript/sections/05-deep-large-sieve.tex (thm:dls, cor:rms, cor:crude), main.tex macros.

### 1.1 Verbatim W4.6 (kernel form, prime q)

Top cell P = Q = x^{0.425}, A = x^{0.575}, R = x^{0.15}, η = 0.05; λ := log_x Λ ∈ [0.425, 0.575].
Tuples t = (ℓ, h): ℓ ~ Λ prime (≠ q), 0 < |h| ≤ H_ℓ = ⌈ℓ/(R+1)⌉; Vaaler weights ĉ_h^±(ℓ),
|ĉ_h| ≤ 1/(H_ℓ+1) + min((R+1)/ℓ, 1/(π|h|)), per-ℓ ℓ¹-mass ≤ m₁ = 4.1, ℓ²-mass ≤ 7(R+1)/Λ (W3.4).
Phases θ_t(q) := −h q̄_ℓ/ℓ mod 1. Needed (W4.6): for all but δ₀N_Q/L of primes q ~ Q,

    | Σ_{t ≠ t', ℓ ≠ ℓ'} ĉ_t ĉ_{t'} F_q(θ_t(q) − θ_{t'}(q)) | ≤ 0.01 δ₀ (ηR)²/L³ = x^{0.3−o(1)},
    F_q(β) := q^{−1} Σ_{a=1}^{q} e(aβ)   (normalized Dirichlet kernel).

Divisor-counting floor (W4.2–W4.4, PROVED, tight up to L³): the |·|-version of the LHS is
x^{2λ−0.425+o(1)}. **Required saving below the absolute-value floor: x^{2λ−0.725+ε}, uniformly
in λ ∈ [0.425, 0.575].** Numerically: x^{0.125} (λ=0.425), x^{0.275} (λ=0.5), x^{0.425} (λ=0.575).

### 1.2 The same object as a Kloosterman-fraction average — three equivalent dressings

CRT + 3-term reciprocity (the W2(ii)–(iii) identities, exact): with m := ℓℓ' ~ Λ² and
w₀ := hℓ' − h'ℓ (≠ 0, |w₀| ≤ 9Λ²/R = x^{2λ−0.15}; w₀ correlated with m — the wp9-frontier §2c
pair-dependence), θ_t(q) − θ_{t'}(q) ≡ −w₀ q̄_m/m ≡ w₀ m̄_q/q − w₀/(qm) (mod 1). So the W4.6
LHS is exactly

    Σ_{ℓ≠ℓ'~Λ} Σ_{h,h'} ĉ_h(ℓ) ĉ_{h'}(ℓ') · q^{−1} Σ_{a=1}^{q} e( a·w₀·m̄_q/q ) e( −a·w₀/(qm) ),

and the smooth factor exits by partial summation at cost (1 + 19/R) against sup_T of the
a-truncated sum (the §4.7.2(iii) move). Three readings:

(K1) PRIME-MODULUS READING. Modulus = q ~ Q = x^{0.425} PRIME; numerators w₀m̄_q vary with the
m-side; need, for a.e. prime q, square-root-plus cancellation in the (ℓ,ℓ',h,h')-aggregate.
Sum over q with the prime constraint = "sums of Kloosterman-type sums over PRIME moduli" — the
known hard part (spectral/Kuznetsov sees ALL levels, not prime levels).

(K2) FLIPPED READING (modulus m). Same object with modulus m = ℓℓ' ~ Λ² = x^{0.85..1.15},
argument q prime ~ x^{0.425} ≤ m^{1/2}: a prime-ARGUMENT Kloosterman fraction of length
≤ modulus^{1/2}, below every known prime-input threshold (Fouvry–Michel needs length ≥ mod^{3/4+ε},
Korolev/Bourgain ≥ mod^{1/2+ε} for prime modulus only — here m has two prime factors AND length
= mod^{0.37..0.5}). Matches W3a's range-dead finding; dead.

(K3) ALL-MODULI RELAXATION [NEW observation, this session — changes the pricing]. The summand
|D_Λ(p,c)|² ≥ 0, and D_Λ(p,c) is defined by the same formula for ANY c ~ Q coprime to p and to
the ℓ's (excluded terms: c = p, ℓ = c — O(1) each). Hence

    Σ_{q~Q prime} Σ_p |D_Λ(p,q)|² ≤ Σ_{c~Q, all c} Σ_p |D_Λ(p,c)|²,

at polylog cost (L from the prime density) — IMMATERIAL against a power deficit. The W4.4
diagonal + same-ℓ terms re-close on every block with x^{0.15−o(1)} room (they cost only L more).
So a SUFFICIENT form of W4.6 is the all-moduli cross term: with full a-period mod c,
q^{-1}Σ_{a≤q} → c^{-1}Σ_{a≤c}, and the complete part of the a-sum collapses
(Σ_{a mod c} e(aw₀m̄_c/c) = c·1[c | w₀]):

    W4.6′:  | Σ_{c~C} Σ_{ℓ≠ℓ'~Λ} Σ_{h,h'} ĉ_h(ℓ)ĉ_{h'}(ℓ') 1[c | hℓ'−h'ℓ] |
            + (1+o(1))·(incomplete remainder)  ≤  x^{0.725−o(1)},   C = x^{0.425},

a SIGNED DIVISOR-CORRELATION sum (no exponentials in the main part!) plus a genuine
sums-of-Kloosterman-sums remainder. Absolute mass of the main part: Σ_pairs |ĉĉ'|·E#{c~C: c|w₀}
~ 0.7·(m₁N_Λ)² = x^{2λ−o(1)} — same deficit x^{2λ−0.725}, but now over ALL moduli c ~ C:
**the prime-moduli obstruction is REMOVABLE by positivity; what remains is a DI-shaped object.**
Equivalently, completing the n' = pℓ₁ℓ₂-variable mod c in the (W2.1) form turns the cross term
into Σ_{c~C} c^{−1} Σ_{a,ν} b_{a,ν} S(a, ν; c) with a = h* ≤ 3Λ²/R = x^{2λ−0.15} (h* = h₁ℓ₂+h₂ℓ₁),
ν ≤ c, and b encoding the (unknown) weights — the exact DI-Theorem-12 / dispersion habitat,
EXCEPT that ||b|| cannot be treated as arbitrary without re-paying the open distribution (see
pricing in §2).

### 1.3 The required inequality, exact, in each dressing (self-checked at λ = 0.425/0.5/0.575)

Per good prime q (kernel form): LHS ≤ x^{0.3−o(1)}; floor x^{2λ−0.425} = x^{0.425}/x^{0.575}/x^{0.725}.
Summed over q ~ Q (or relaxed to all c ~ C): need ≤ N_Q·x^{0.3−o(1)} = x^{0.725−o(1)}; floor
x^{2λ+o(1)} = x^{0.85}/x^{1.0}/x^{1.15}. Deficit in both normalizations: x^{2λ−0.725} =
x^{0.125}/x^{0.275}/x^{0.425}. Ranges for the literature comparison:
  C = x^{0.425} (moduli);  m = ℓℓ' ~ x^{0.85}/x^{1.0}/x^{1.15};  |w₀| ≤ x^{0.7}/x^{0.85}/x^{1.0};
  h* ≤ x^{0.7}/x^{0.85}/x^{1.0};  n' = pℓ₁ℓ₂ ~ x^{1.275}/x^{1.425}/x^{1.575};  #T_lin = x^{0.7}/x^{0.85}/x^{1.0}.
Note mn-type products (h*·ν up to x^{2λ−0.15}·x^{0.425} = x^{1.125}/x^{1.275}/x^{1.425}) vs
C² = x^{0.85}: ABOVE C² on every block — the Linnik-range condition mn ≪ C² FAILS; uniformity
beyond it (Sarnak–Tsimerman territory) is load-bearing.

## 2. Candidate technology pricing

### 2.1 Deshouillers–Iwaniec 1982 (Invent. Math. 70, 219–288, "Kloosterman sums and Fourier coefficients of cusp forms")

PROVENANCE FLAG (fine-print honesty): the original is paywalled (Springer; GDZ digitization caps
downloads at 2 pages — attempted). DI Theorem 12 is quoted here through Drappeau 2017, whose
Theorem 2.1 (fetched verbatim from the PDF, §2.2 below) carries the attribution, verbatim: "The
main result, which extends [DI82b, Theorem 12] ... is the following." At q = 1 (no congruence)
Drappeau's display IS the DI Theorem 12 shape:

    Σ_{c,d,n,r,s, (rd,sc)=1} b_{n,r,s} g(c,d,n,r,s) e( n·\overline{rd}/(sc) )
      ≪_ε (CDNRS)^ε K(C,D,N,R,S) ||b_{N,R,S}||₂,
    K(C,D,N,R,S)² = CS(RS+N)(C+RD) + C²DS·sqrt((RS+N)R) + D²NRS^{−1},

g smooth, dyadically supported in c ~ C, d ~ D; b arbitrary on (n,r,s). Any transcription into the
manuscript must re-verify against the original (or quote Drappeau Thm 2.1 with q = 1, which is a
published superset and is what we price). Mechanism: completion of the smooth c,d-sums →
Kloosterman sums S(±n, r·\bar{s}...; scq-type moduli) → Kuznetsov on Γ₀ levels → spectral large
sieve; gain lives at spectral conductor ~ C² relative to the smooth-modulus variable.
MODULI CLASS: smooth dyadic c (times arbitrary s | level structure) — all integers, NOT primes.
NUMERATOR UNIFORMITY: arbitrary b_{n,r,s} (n is the Kloosterman numerator): pair-correlated
numerators ADMISSIBLE. RANGES vs ours and savings: priced in §2.2 (identical formula at q = 1):
every allocation of our (c, a; q or m; h, h*, w₀) into (c,d,n,r,s) leaves arbitrary-coefficient
variables of total size x^{0.85+2λ−0.15} ≥ x^{1.275} ≫ C² = x^{0.85}, where K² exceeds the trivial
bound squared. PRECISE GAP: at the best allocation the DI bound exceeds even the divisor-counting
floor by x^{0.2875+}; the needed x^{2λ−0.725} below that floor is not approached.

### 2.2 Drappeau 2017 (Proc. LMS 114, 684–732; arXiv:1504.05549, dispersion-packaged DI)

FETCHED (ar5iv, first pass — exact statement, cross-check of constants below in 2.2b). Theorem 2.1
(sums of Kloosterman sums in arithmetic progressions, quintilinear form): parameters
C, D, N, R, S ≥ 1; q, c₀, d₀ ∈ N, (c₀d₀, q) = 1; coefficients (b_{n,r,s}) ARBITRARY, supported in
(0,N] × (R,2R] × (S,2S]; g: R₊⁵ → C smooth, compactly supported in (C,2C] × (D,2D] × (R₊*)³ with
∂^ν g ≪ {c^{−ν₁}d^{−ν₂}n^{−ν₃}r^{−ν₄}s^{−ν₅}}^{1−ε₀}. Then

    Σ_{c ≡ c₀, d ≡ d₀ (mod q), (qrd, sc) = 1} b_{n,r,s} g(c,d,n,r,s) e( n·\overline{rd}/(sc) )
      ≪_{ε,ε₀} (qCDNRS)^{ε+O(ε₀)} q^{3/2} K(C,D,N,R,S) ||b_{N,R,S}||₂,
    K(C,D,N,R,S)² = qCS(RS+N)(C+RD) + C²DS·sqrt((RS+N)R) + D²NRS^{−1}.

(q = 1, no congruence: this is exactly Deshouillers–Iwaniec 1982 Theorem 12's shape — see 2.1.)

MODULI CLASS: c, d are the SMOOTH variables (modulus sc contains the smooth factor c summed over a
dyadic range with smooth weight; d a smooth factor of the argument rd). Moduli in arithmetic
progressions mod q — NOT prime moduli; primality of the modulus variable is not admissible input.
NUMERATOR UNIFORMITY: n carries arbitrary coefficients JOINTLY with (r,s) — b_{n,r,s} arbitrary.
**This DISSOLVES the wp9-frontier §2c "numerator pair-dependence" blocker (W3b's structural
blocker): h* correlated with the m-side is admissible as b_{n,r,s}.** The blocker was never
structural for DI-class technology — only for the fixed-numerator DFI 1997 form.

PRICING vs W4.6 (all allocations; using the K3 positivity relaxation so the modulus variable IS a
smooth dyadic c ~ x^{0.425} — prime-moduli obstruction removed, see §1.2):
(a) c-modulus dressing, e(h*·\overline{pℓ₁ℓ₂}/c): c_DI = c = x^{0.425} (smooth ✓), but the argument
    rd = pℓ₁ℓ₂ = x^{0.425+2λ} has NO smooth factor (all three prime) unless p is Vaughan-decomposed;
    with d = 1, r = pℓ₁ℓ₂ ~ x^{1.275..1.575}, s = 1, n = h* ≤ x^{2λ−0.15}:
    K² = C(R+N)(C+R) = x^{4λ+1.275} dominant → K = x^{2λ+0.6375}, ||b||₂ = x^{0.3625}: bound
    x^{2λ+1.0} vs trivial x^{2λ+0.85} (ABOVE trivial by x^{0.15}) vs demand x^{1.15}: FAIL by
    x^{2λ−0.15} = x^{0.7}/x^{0.85}/x^{1.0} at λ = 0.425/0.5/0.575 (machine-checked).
(b) m-modulus dressing, e(a·w₀·m̄_c/c) (kernel form flipped): c smooth ✓, r = ℓℓ' = x^{2λ}, d = s = 1,
    n = a·w₀ ≤ x^{2λ+0.275}: K² ≈ CNR = x^{4λ+0.7} (terms a/b/c = x^{4λ+0.7}/x^{4λ+0.275}/
    x^{2λ+0.9875}, machine-checked), bound (1/C)K||b||₂ = x^{2λ+0.2875}: BELOW raw trivial
    x^{2λ+0.425} by x^{0.1375} — DI does produce spectral cancellation here — but x^{0.2875}
    ABOVE the elementary divisor floor x^{2λ} (W4.2-counting beats it), and x^{2λ−0.4375} =
    x^{0.4125}/x^{0.5625}/x^{0.7125} above the demand x^{0.725}. FAIL.
(c) Vaughan-decomposing p to create a smooth d ~ D ≤ x^{0.2825} (S = 1, R = x^{0.425+2λ}/D ≥
    x^{0.9925}): K² ≥ C(R+N)(C+RD) ≥ C·R·RD = CR²D = x^{4λ+1.275}/D ≥ x^{4λ+0.9925}, so
    K ≥ x^{2λ+0.496} and the bound ≥ x^{2λ+0.85}-grade vs demand x^{1.15}: FAIL by ≥ x^{2λ−0.3}
    = x^{0.55}/x^{0.7}/x^{0.85}. Root cause in every allocation: total argument rd·s = x^{0.425+2λ}
    ≫ C² = x^{0.85}.
ROOT CAUSE: DI/Drappeau leverage lives at spectral conductor C² = x^{0.85}; the W4.6 family has
arbitrary-coefficient mass at argument/numerator scale x^{1.125..1.575} ≫ C² on every block —
the same overcrowding that W4.5(ii) measured (thm:dls threshold transferred). The q^{3/2} loss and
θ-dependence never even get tested; ranges kill it first.
GAP: not a subrange issue — NO allocation of (c,d,n,r,s) puts the W4.6 mass inside K²'s paying
regime; deficit ≥ x^{2λ−0.4375} in the best allocation (b), i.e. worse than the x^{2λ−0.725}
target gap by x^{0.2875+}.

### 2.3 Fouvry–Michel and successors: the two prime restrictions, priced separately

(a) PRIME ARGUMENT (the K2 dressing: Σ_{q~Q prime} e(c q̄_m/m), modulus m = ℓℓ'). Fetched
verbatim: Fouvry–Michel 1998 (Ann. Sci. ENS 31, Théorème 1.1, as restated in FKM arXiv:1211.6043
p.1): "Let f = P/Q, with P, Q ∈ Z[X] coprime unitary polynomials. For every prime p such that the
reduction of f modulo p is not a polynomial of degree ⩽ 1, for every X ⩽ p and every η < 1/32:
Σ_{q⩽X prime, (Q(q),p)=1} e(P(q)·\overline{Q(q)}/p) ≪ X (p/X)^{7/32} p^{−η}" — nontrivial only for
X ≳ p^{6/7}. Successor, FKM 2014 (Duke 163; arXiv:1211.6043 Theorem 1.5, verbatim): "Let K be an
isotypic trace weight on F_p associated to some sheaf F, and assume that F is not exceptional...
Σ_{q prime} K(q)V(q/X) ≪_Q X(1+p/X)^{1/6} p^{−η}, Σ_{q prime, q⩽X} K(q) ≪ X(1+p/X)^{1/12} p^{−η/2},
for any η < 1/24" — Remark 1.6 verbatim: "these bounds are non-trivial as long as the conductor of
F remains bounded and the range X is greater that p^{3/4+ε}"; for special K = e((an+b·n̄^k)/p),
Bourgain / Bourgain–Garaev reach X ⩾ p^{1/2+ε} (PRIME modulus p only). PRICING: our argument range
is Q = x^{0.425} = m^{1/2} (λ = 0.425) down to m^{0.37} (λ = 0.575): at or below the p^{1/2+ε}
threshold of the strongest special-phase results, far below FKM's p^{3/4+ε} and FM98's p^{6/7} —
AND m = ℓℓ' is composite with two large prime factors while the entire FM/FKM/Bourgain corpus is
prime-modulus (ℓ-adic sheaves over F_p). Savings class, even in range: p^{−1/48}..p^{−1/32}-grade
= x^{−0.02}-grade vs needed x^{0.125..0.425}. DEAD on range, modulus class, AND savings size —
confirms W3a.

(b) PRIME MODULI (the K1 dressing: Σ_{q~Q prime} of Kloosterman-type data at level q). State of
the art for spectral access to restricted moduli (sign-change literature, where this exact problem
is the bottleneck): Fouvry–Michel 2003/2007 reached moduli c with ≤ 23 prime factors via
Selberg-sieve weights + Kuznetsov on Γ₀(d)-levels (divisibility conditions c ≡ 0 (mod d) ARE
spectrally admissible; primality is NOT); successively Sivak-Fischler 18, Matomäki 15, Xi 10
(arXiv:1310.8623), Xi 2024 ≤ 6 prime factors (arXiv:2411.13170); Drappeau–Maynard: 2, but only
assuming a Landau–Siegel zero. PURE PRIME MODULI: open in the entire literature; combinatorial
identities (Vaughan/Heath-Brown) do not apply to a modulus variable (it is not a convolution
variable), and sieve decompositions deliver only upper/lower-bound sieve MAJORANTS — usable for
nonnegative integrands, not for an arbitrary signed restriction. COST: a genuine prime-moduli
restriction of a DI-class bound is not available at any power saving.
**MOOTED FOR US by the K3 positivity relaxation (§1.2): our integrand at fixed modulus is
|D_Λ(p,c)|² ≥ 0, so prime moduli embed in all moduli at cost L — the prime-moduli restriction is
NOT the binding obstruction for W4.6. The binding obstruction is conductor/range (§§2.2, 2.5).**

### 2.4 KMS (Kowalski–Michel–Sawin, Ann. of Math. 186 (2017)) and BFKMM — bilinear forms at a single prime modulus

FETCHED verbatim (arXiv:1511.01636v5). Theorem 1.1 (General bilinear forms): "Let q be a prime.
Let c be an integer coprime to q. Let M and N be real numbers such that 1 ⩽ M ⩽ Nq^{1/4},
q^{1/4} < MN < q^{5/4}. Let N ⊂ [1, q−1] be an interval of length ⌊N⌋ ... For any ε > 0:
B([×c]*Kl_k, α, β) ≪ q^ε ||α||₂||β||₂ (MN)^{1/2} ( M^{−1/2} + (MN)^{−3/16} q^{11/64} )."
Remark 1.2: nontrivial for M = N ⩾ q^{11/24}; "in the special case M = N = q^{1/2}, the saving
factor is q^{−1/64+ε}". Theorem 1.3 (type I): hypotheses 1 ⩽ M ⩽ N², N < q, MN < q^{3/2}; bound
≪ q^ε ||α||₁^{1/2}||α||₂^{1/2} M^{1/4} N · ((M²N⁵)/q³)^{−1/12}; at M = N = q^{1/2} saving
q^{−1/24+ε}. BFKMM: per KMS Remark 1.4(2) verbatim: "For k = 2, a slightly stronger result is
proved by Blomer, Fouvry, Kowalski, Michel and Milićević [BFK+a, Prop. 3.1]. This builds on a
method of Fouvry and Michel [FM98, §VII]" — same class (single prime modulus, bilinear, savings
q^{−δ} with δ of 1/64..1/16 grade).

PRICING vs W4.6: three independent mismatches.
(i) MODULI CLASS: single prime modulus q with all variables inside [1, q−1]-scale and MN < q^{5/4}
    = x^{0.53}; our per-q tuple mass is #T_lin = x^{0.7..1.0} with numerator scale h* ≤ x^{0.7..1.0}
    ≫ q — out of the hypothesis window on every block.
(ii) SAVINGS SIZE: q^{−1/64+ε} = x^{−0.0066} (best, balanced case) vs needed x^{0.125..0.425}:
    short by x^{0.118..0.418} even if ranges matched.
(iii) CATEGORY: at fixed q the W4.6 form is a PSD Gram form, F_q(θ_t−θ_{t'}) = ⟨v_t, v_{t'}⟩ with
    v_t = q^{−1/2}(e(aθ_t(q)))_{a⩽q} — the needed statement is quasi-orthogonality of #T_lin ≫ q
    exponential vectors (an overcrowded large-sieve claim, W4.5(ii)), not a bilinear form OF
    hyper-Kloosterman trace functions; Fourier-expanding the kernel to manufacture Kl-structure
    lands back on the divisibility count (§1.2 K3), one ladder generation down (self-similarity).
GAP: not a subrange — the technology class addresses per-prime-modulus signed bilinear
cancellation at q^{−1/64}-grade in sub-q ranges; W4.6 needs x^{2λ−0.725} on a super-q² family.

### 2.5 Sarnak–Tsimerman 2009 / Steiner 2017 (ranges; Kuznetsov in the (m,n)-aspect)

FETCHED verbatim (Steiner, arXiv:1707.02113, pp. 1–4, which quotes/generalizes Sarnak–Tsimerman
[Manin volume, Progr. Math. 270, 2009, 619–635]). Kuznetsov 1979: Σ_{c≤C} S(m,n;c)/c
≪_{m,n} C^{1/6} log^{1/3}(2C) — "still the best known bound to date" in C-aspect. Steiner
Corollary 2 (at s = 1, α = 0; θ ≤ 7/64 Kim–Sarnak; ≲ hides (Cmns)^ε):

    Σ_{c≤C} S(m,n;c)/c ≲ C^{1/6} + C^{2θ} + (mn)^{1/6} + m^{1/4} + n^{1/4}
                          + min{ (mn)^{1/8+θ/2}, (mn)^{1/4} },
    hypotheses: mn > 0, s ≪ min{(mn)^{1/4}, C^{1/2}}, (m,n,s) = 1.

RANGES: nontrivial (vs Weil's C^{1/2}) only for mn ≪ C^{4−δ}-grade with the C ≥ √(mn) "Linnik
range" the comfortable one; Steiner pp. 3–4, VERBATIM: "in the application one is very deep in
the Selberg range [C ≤ √(mn)], for which the trivial bound is still the best known bound."
PRICING vs W4.6 — TWO independent kills:
(i) CATEGORY MISMATCH (decisive, new observation): per tuple-pair (t,t') the W4.6 c-object is
    Σ_{c~C} F_c(−w₀c̄_m/m), whose complete part is the DIVISOR COUNT #{c ~ C: c | w₀} ≥ 0 — the
    full-period a-sum has already collapsed the Kloosterman structure; there is NO oscillation
    in c left for Kuznetsov to detect per pair (contrast Σ_c S(m,n;c)/c, where the cancellation
    lives in the sign changes of S in the c-aspect). Per-pair c-sum technology of ANY strength
    cannot go below the divisor floor because the per-pair object is genuinely nonnegative-plus-
    kernel-tails; the needed cancellation is only in the signed (t,t')-aggregate.
(ii) RANGE: where Kuznetsov does get re-introduced (Fourier-detecting the pair aggregate, §1.2
    K3 / §2.2), the coefficient mass sits at mn ~ x^{2λ+0.275} = x^{1.125}/x^{1.275}/x^{1.425}
    (λ = 0.425/0.5/0.575) vs C² = x^{0.85}: C ≤ (mn)^{1/2} by x^{0.1375}/x^{0.2125}/x^{0.2875}
    on every block — deep Selberg range, verbatim the regime where "the trivial bound is still
    the best known bound."

### 2.6 Bettin–Chandee (Adv. Math.; trilinear Kloosterman fractions) — the closest-fitting shape

FETCHED verbatim via Fouvry–Radziwiłł, arXiv:1811.08672, Lemma 2.4 (= Bettin–Chandee, Theorem 1):
"Let ε > 0 ... for every non-zero integer ϑ, and for every sequence of complex numbers α = (α_m),
β = (β_n), ν = (ν_a), and for every A, M, N ≥ 1:
    | Σ_{a~A} Σ_{m~M} Σ_{n~N} α(m)β(n)ν(a) e( ϑ a m̄/n ) |
      ≤ C(ε) ||α||₂ ||β||₂ ||ν||₂ (1 + |ϑ|A/(MN))^{1/2}
        × ( (AMN)^{7/20+ε}(M+N)^{1/4} + (AMN)^{3/8+ε}(AN+AM)^{1/8} )."
UNIQUE STRENGTH: arbitrary ℓ²-coefficients on ALL THREE variables, including the MODULUS n — no
smoothness, no primality restriction anywhere: of all fetched technology this is the only shape
that tolerates our prime q's and two-prime moduli m = ℓℓ' as-is, and it averages over the
NUMERATOR (the dispersion feature). Fouvry–Radziwiłł run dispersion on it and get level
1/2 + 1/66 for unbalanced convolutions — savings class x^{1/66} ~ x^{0.015}.
TWO GAPS vs W4.6:
(i) ARITY: our object is QUADRIlinear — phase e(−(a·h)·q̄_ℓ/ℓ) (linear level) or
    e(−(a·w₀)·q̄_m/m) (pair level) with numerator a PRODUCT of two weighted variables, and the
    dispersion linearization forces ν to depend on (q,a) JOINTLY (ν = φ·conj(U(q,a)) — the
    self-similarity rider in trilinear clothing). No published trilinear statement covers either
    coupling; BC's ϑ is a FIXED integer.
(ii) RANGES, even granting (i) (indicative allocation ϑ = ±1, BC-(a,m,n) = (a·w₀, q, ℓℓ'),
    A = x^{2λ+0.275}, M = x^{0.425}, N = x^{2λ}; AMN = x^{4λ+0.7}; (1+|ϑ|A/MN)^{1/2} = O(1) since
    A/MN = x^{−0.15}): term 2 dominates: (AMN)^{3/8}(AN+AM)^{1/8} = x^{2λ+0.297}; with the actual
    ℓ²-mass x^{0.15−o(1)} the bound is x^{2λ+0.447} vs trivial x^{2λ+0.425−o(1)}: AT/ABOVE trivial
    on every block (BC's savings need M ≍ N; ours is M = x^{0.425} vs N ≥ x^{0.85}). Self-check at
    λ = 0.425/0.5/0.575: BC x^{1.297}/x^{1.447}/x^{1.597} vs demand x^{0.725}: short
    x^{0.572}/x^{0.722}/x^{0.872}.

## 3. Dual check: cor:crude cross-moduli Wieferich-pair counts vs literature

cor:crude (05-deep-large-sieve.tex, verbatim): "The genuine strengthening (the program's flagged
main theoretical question) is a tailored (q,λ)-averaged sieve exploiting cross-moduli
Wieferich-pair counting: for fixed n₁ ≠ n₂ the primes q with q² | n₁^{q−1} − n₂^{q−1} should be
far sparser than fixed-q counting sees." Literature audit:

(a) Bourgain–Ford–Konyagin–Shparlinski, "On the divisibility of Fermat quotients" (Michigan Math.
J. 59 (2010) 313–328): bounds the smallest a with a^{p−1} ≢ 1 (mod p²): a ≤ (log p)^{463/252+o(1)},
and (log p)^{5/3+o(1)} for almost all p; tools: smooth numbers, multiplicative-subgroup
equidistribution, Heilbronn exponential sums (Heath-Brown, Heath-Brown–Konyagin; since improved
by Shkredov), and a large sieve with SQUARE MODULI (Baier–Zhao). Every statement is FIXED-q,
n-aggregated — the transpose of what cor:crude needs. The square-moduli large sieve is the
nearest cross-moduli tool (conductors {q²} sparse-averaged) but is an ℓ²-mean statement with the
classical (N + Q³)-type constant: at our parameters it reproduces overcrowding, no divisor-beating
gain. NO MATCH.

(b) Fixed pair, q varies (the literal cor:crude question): setting b ≡ n₁n̄₂, the condition is
"q is a Wieferich prime to base b". State of the art (verified 2026-06, arXiv:2508.08472v2,
verbatim): "There is currently no unconditional result in this direction" — even the INFINITUDE
of non-Wieferich primes (fixed base, over Q) is open; Silverman 1988 gives ≫ log x non-Wieferich
only under abc; expected Wieferich count O(log log x) is heuristic; NO unconditional o(π(x)) upper
bound for the Wieferich count exists. (A web summary claiming unconditional density-1
non-Wieferich was checked against the source and is an artifact — the source says the opposite.)
So the pointwise-in-pair form of cor:crude is at least as hard as a famous open problem. NO MATCH.

(c) Logical direction for W4.6, important: W4.6's coincidence condition is the DEPTH-ZERO
analogue (q | jℓℓ' − (hℓ'−h'ℓ), e(·/q)-world), and there the COUNT-level version of the needed
improvement is provably FALSE — the coincidence mass is real (wp11 §4.7.4 truth-grade analysis;
W4.7/E3 numerics: kernel q-average ≈ 6/Q attained). Only SIGN-sensitive input can close W4.6.
The Fermat-quotient/Wieferich literature is entirely count-level. DUAL CHECK VERDICT: no direct
literature match in either direction; cor:crude's day-one question remains the program's own;
its depth-one (q²) form is Wieferich-hard pointwise, and its depth-zero (W4.6) form needs signs,
which no counting result — existing or hoped-for — supplies.

## 4. Verdict

**DOES-NOT-COVER** — [the precise new spectral estimate that must be proved: a signed
cross-moduli coincidence bound at spectral conductor beyond C². Exact statement (either form
suffices for (W1.1) via the proved W4.0–W4.4 chain):

  (Form A, per prime q — W4.6 verbatim) for all but δ₀N_Q/L primes q ~ Q = x^{0.425}:
    |Σ_{ℓ≠ℓ'~Λ prime} Σ_{0<|h|≤H_ℓ, 0<|h'|≤H_{ℓ'}} ĉ_h(ℓ)ĉ_{h'}(ℓ')
        F_q( (hℓ'−h'ℓ)·\overline{q}_{ℓℓ'} / (ℓℓ') )| ≤ x^{0.3−o(1)},  uniformly λ ∈ [0.425, 0.575];
  (Form B, all-moduli sufficient version, §1.2 K3) Σ_{c~x^{0.425}} of the same with the complete
    part the signed divisor-correlation Σ ĉĉ'·1[c | hℓ'−h'ℓ]: total ≤ x^{0.725−o(1)} vs real mass
    x^{2λ}; i.e. signed saving x^{2λ−0.725+ε} = x^{0.125}/x^{0.275}/x^{0.425} at λ = 0.425/0.5/0.575
    below a TRUE (attained) absolute mass.

WHY NO FETCHED TECHNOLOGY COVERS IT (each priced verbatim above): (1) DI 1982 Thm 12 / Drappeau
2017 Thm 2.1 — the only technology whose coefficient generality (b_{n,r,s} arbitrary) swallows our
numerator-modulus correlation, and the K3 relaxation removes their smooth/progression moduli-class
mismatch; but their gain lives at spectral conductor C² = x^{0.85} while our arbitrary-coefficient
mass sits at x^{1.125..1.575}: best allocation lands x^{0.2875} ABOVE the elementary divisor floor
(machine-checked, §2.2); (2) per-pair c-sum technology (Kuznetsov 1/6, Sarnak–Tsimerman, Steiner)
is category-mismatched: our per-pair c-object is a nonnegative divisor count — no c-oscillation
exists to detect (§2.5(i)) — and where Kuznetsov re-enters via the aggregate, the family is deep
in the Selberg range, where verbatim "the trivial bound is still the best known bound"; (3) prime
restrictions: prime ARGUMENT dressing is range-dead (length ≤ mod^{1/2} vs FKM p^{3/4+ε},
Bourgain–Garaev p^{1/2+ε} prime-modulus-only; savings class x^{0.02} vs needed x^{0.125+}); prime
MODULI restriction is mooted by K3 positivity (genuinely new simplification: the missing estimate
need NOT be proved for prime moduli — all moduli c ~ x^{0.425} suffices, at polylog cost);
(4) KMS/BFKMM bilinear (single prime modulus, MN < q^{5/4}, savings q^{−1/64}): out of range by
powers, savings 20–60× too small in exponent, and the W4.6 per-q form is a PSD Gram form, not a
trace-function bilinear; (5) Bettin–Chandee trilinear — closest shape (arbitrary weights on all
variables incl. modulus), but our object is quadrilinear with coupled ν(q,a) (the self-similarity
in trilinear clothing) and even granting the coupling the bound sits at/above trivial (M ≍ N
required; ours M = x^{0.425}, N ≥ x^{0.85}).

IS IT PLAUSIBLY PROVABLE? Genuinely open, not absurd: (i) TRUE in the random model with room
x^{0.18+} (W4.7 numerics, signed-rms x^{−0.0625} vs demand); (ii) the family is explicit and
algebraic (Farey differences h/ℓ − h'/ℓ', prime denominators ~ Λ, Vaaler weights); (iii) but it
requires beating the large-sieve constant on an overcrowded family by the full overcrowding ratio
#T_lin/Q · x^{−0.15} = x^{2λ−0.725}, i.e. a large-sieve-beyond-conductor mechanism for a specific
sparse Farey family WITH SIGNS — no instance of such a mechanism exists in the corpus (square-
moduli large sieve, the nearest, improves constants for sparse MODULI sets, not overcrowded
frequency families); and the self-similarity rider (machine-confirmed: Fourier-detecting Form B's
divisor correlation regenerates the same congruence c | kℓ'+k'ℓ one level down with NO
contraction) rules out assembling it from the fetched estimates by iteration. This is
research-problem-grade, not transcription-grade: no reduction-outline-plus-transcription list can
be written from the 1982–2026 Kuznetsov corpus.

CONFIDENCE: high (≥ 0.9) that the fetched sources do not cover W4.6 — every pricing is a
computable exponent gap ≥ x^{0.2875} (DI/Drappeau, best case), with statements quoted verbatim
from PDFs (Drappeau Thm 2.1; KMS Thm 1.1/1.3; FKM Thm 1.5 + Rem. 1.6; FM98 Thm 1.1; BC via FR
Lemma 2.4; Steiner Thm 1/Cor. 2) — only the DI82 original is quoted through Drappeau's published
superset (flagged, §2.1). Moderate-high (≈ 0.75) that nothing else published covers it: the K3
reformulation shows the obstruction is conductor-structural (mass ≫ C² with arbitrary weights),
which is invariant across the entire Kuznetsov-class literature searched (DI descendants,
dispersion packages, trace-function bilinear/trilinear forms, prime/almost-prime moduli lines,
twisted Linnik–Selberg).

POSITIVE DELIVERABLES OF THIS DIAGNOSIS (usable regardless): (1) the K3 all-moduli relaxation —
prime-moduli restriction removable by positivity at polylog cost; W4.6 may henceforth be attacked
over ALL moduli c ~ x^{0.425} (Form B), a strictly easier-looking object (signed divisor
correlation, no exponentials in the main part); (2) the wp9-frontier §2c numerator-pair-dependence
blocker is NOT structural for DI-class technology (b_{n,r,s} arbitrary absorbs it) — that blocker
should be deprioritized in future audits; (3) the exact conductor accounting: any future candidate
technology can be pre-screened by one number — does its gain survive arbitrary-coefficient mass at
x^{2λ+0.275} against smooth-modulus conductor x^{0.85}?]

ESTIMATED SESSIONS: not applicable for a COVERS execution (none exists). If the program chooses to
attack Form B as new mathematics: unbounded / research-grade; the file's §1–§3 give the exact
starting object and the three dead perimeters.
