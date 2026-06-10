# Erdős Problem 396 — Literature report (Tier C/D item (a))

**Scope.** (1) Exact statements on strings of consecutive smooth integers and
whether the constructions admit congruence control; (2) state of the art on
divisibility of $\binom{2n}{n}$ by shifted/windowed factors; (3) gap analysis:
what exactly is missing for each $k$; (4) the revised program. Forum/community
check: nothing beyond the results below is recorded for #396.

---

## Part 1 — Consecutive smooth integers

**[H85] Hildebrand, "On a conjecture of Balog", PAMS 95 (1985).**
If $S$ is *stable* (membership essentially invariant under multiplication by
any fixed integer, up to density-0 exceptions) and has positive lower density,
then $\underline d\big(S\cap(S+1)\big)>0$. Since $n^\varepsilon$-smooth numbers
are stable with density $\rho(1/\varepsilon)>0$: **for every
$\varepsilon>0$, the set of $n$ with $n$ and $n+1$ both $n^\varepsilon$-smooth
has positive lower density.** (Solves Erdős's 1976 twin-smooth question, with
density to spare.) Balog–Ruzsa (1997) extend to pairs $(n, an+c)$.

**[H89] Hildebrand, Mathematika 36 (1989).**
A stable set with lower density $>(k-2)/(k-1)$ contains $k$-strings of
consecutive members, at positive density. For smooth numbers this needs
$\rho(1/\alpha)>(k-2)/(k-1)$, i.e. smoothness exponent
$\alpha>e^{-1/(k-1)}$: for **triples** that is $\alpha>e^{-1/2}\approx 0.607$ —
*strictly above our needed $1/2$*. So Hildebrand's positive-density strings are
not smooth enough for window size $\ge 3$.

**[McN23] McNamara, arXiv:2312.08544.**
**Counterexample** to Hildebrand's conjecture that stability + positive density
suffices for triples: there are stable sets of positive density with
$S\cap(S+1)\cap(S+2)=\emptyset$, and stable sets of density $1-\tfrac1{q-1}$
with empty $q$-fold intersection (matching [H89]'s threshold). **Consequence
for us: any proof of sqrt-smooth (or governor-set) triples must use structure
beyond stability and density.** The soft route is provably closed for $k\ge2$.

**[T18] Teräväinen, "On binary correlations of multiplicative functions",
Forum Math. Sigma 6 (2018).**
For real multiplicative functions equidistributed in APs, the logarithmically
averaged binary correlation equals the product of mean values. Applications:
the numbers of large prime factors of n and n+1 are independent of each other with respect to logarithmic density, and a logarithmic version of the Erdős–Pomerance conjecture on two consecutive smooth numbers.
I.e. in **logarithmic density**, $\Pr[P^+(n)\le n^\alpha,\ P^+(n+1)\le
n^\beta]=\rho(1/\alpha)\rho(1/\beta)$: pair anatomies are exactly independent.
Follow-ups: Tao–Teräväinen (ANT 2019: correlations at almost all scales,
incl. largest prime factors of consecutive integers) and a recent
**Tao–Teräväinen "Quantitative correlations and some problems on prime factors
of consecutive integers"** — the quantitative toolbox is actively improving.
This is the theoretical counterpart of our empirical ×1.14-only
consecutiveness correction (which is exactly a finite-scale effect).

**[BW98] Balog–Wooley, J. Austral. Math. Soc. 64 (1998) — full construction
extracted.**
Theorem 1: infinitely many strings of consecutive integers of size about n, free of prime factors exceeding n^ε, with string length growing like log log log log n.
Mechanism: the witness is an explicit product of powers of small integers; each
window element takes the form $b_j(z_j^{\gamma_j}-1)$ with $\gamma_j$ a product
of an equitable class of primes (their Lemma 2.1 partition), and smoothness
comes from the cyclotomic factorization of $z^d-1$ (largest prime factor
$\lesssim z^{\phi(d)}e^{...}$). The exponents are fixed by CRT congruences
mod the $\gamma_j$.
*Congruence-control assessment (for our R1):* the defining congruences are
preserved under shifting exponents by multiples of $\gamma_j$, so the witness
$x \bmod Q$ ranges over a **coset of a multiplicative subgroup** of
$(\mathbb Z/Q)^*$ — partial, not full, CRT control. More importantly the
digits of $x$ are highly structured (not heuristically random), so carry counts
must be proven directly; the saving grace is that the window elements factor
cyclotomically, so $v_p$ of everything in sight is computable by
lifting-the-exponent. Witnesses are exponentially sparse
($x\in[\exp((\log n)^{1/11}),n]$) — fine for the literal existence statement,
useless for density. Predecessor: Eggleton–Selfridge 1976 (strings of length
$\le5$; [BW98] note and fix a half-density oversight there).

---

## Part 2 — Divisibility of the central binomial coefficient

**[Po14/15] Pomerance, "Divisors of the middle binomial coefficient", Amer.
Math. Monthly 122 (2015).** With $D_k=\{n: n+k\mid\binom{2n}{n}\}$:
- Thm 2 + remark: density of $D_k$ is 1 for $k\ge1$, and
  the set of n with (n+1)(n+2)...(n+k) dividing the central binomial coefficient has asymptotic density 1 (the easy side of 396, explained by the free units-digit carry when $n\equiv -i \bmod p$).
- Thm 3: $D_{-k}$ is infinite for $k\ge0$ with upper density $\le 1-\log 2$;
  the infinitude construction is n = pq + k with primes p, q satisfying k < p and (3/2)p < q < 2p, giving ≫ x/(log x)^2 witnesses — the balanced-semiprime trick: the digit pair $(k, q-p)$ base $p$ and $(k,p)$ base $q$ each force the needed carry.
- Thm 4 (the **governor set**): $D_0+k \simeq D_{-k}$ (symmetric difference of
  density 0); also $D^{(2)}_k+k\simeq D_0$. He conjectures $D_0$ has positive
  density.

**Reformulation this gives us (new, and clean).** Up to density-0 exceptional
sets, the 396 window condition $\prod_{i\le k}(n-i)\mid\binom{2n}{n}$ is
$n\in D_0\cap(D_0+1)\cap\cdots\cap(D_0+k)$: **Problem 396 is asymptotically the
statement that the governor set contains arbitrarily long strings of
consecutive integers** — precisely the [H85]/[H89]/[McN23] framework, with
$D_0$ in place of the smooth numbers. (For pure existence one uses the exact
local versions: for $p>2k$ the per-prime equivalences are exact; $p\le 2k$
contribute effective $O(x^{1-a})$ exceptional sets.)

**[Sa17] Sanna.** Upper density of $D_0$ $\le 1-\log2-0.0555$;
$\#\{n\le x:(n,\binom{2n}{n})=1\}\ll x/\sqrt{\log x}$.

**[FK21] Ford–Konyagin, Trans. AMS 374 (2021), arXiv:1909.03903.**
- Thm 1: for fixed ℓ the set of n with n^ℓ | C(2n,n) has positive asymptotic density c_ℓ, given by an explicit expectation over the Poisson–Dirichlet process; $c_1=0.11424$ (so Pomerance's conjecture is proven: the governor set has positive density).
- Thm 2: $c_\ell\sim\rho(2\ell+1-\log(2\ell\log 2\ell)-\cdots)$.
- Method, in our language: **Section 2 proves small primes are ignorable**
  (the number of n ≤ x for which the x^δ-smooth part A_n fails A_n^ℓ | C(2n,n) is ≪ x e^{-1/(300ℓδ)}) — the rigorous form of our Tier-A "asymptotic simplification"; the anatomy of $n$ is handled by Poisson–Dirichlet (Donnelly–Grimmett), and the digit conditions $\{n/p^s\}>1/2$ for the several large primes of $n$ are detected **jointly by Fourier analysis / van der Corput estimates** (their Sections 3–5, "a method to capture the effect of large prime factors of integers in general sequences").
  Their numerics confirm very slow convergence to $c_\ell$ — matching the slow
  drift in our measurements.

**Community check.** The #396 page lists only [Po14]; related recent activity
(Ford–Konyagin; Croot–Mousavi–Schmidt 2024 and Bloom–Croot 2025 on
*small* $P$-divisibility, relevant to #376 not #396; an information-theoretic
disproof of #397; AI-assisted solutions to #728/#729 on factorial divisibility)
does not touch 396. Our program duplicates nothing.

---

## Part 3 — Quantitative unification (new observation)

Under Pomerance's governor equivalence plus Teräväinen-style independence, the
limiting window density should be exactly
$$\boxed{\ \delta_k = c_1^{\,k+1},\qquad c_1=0.11424\ \text{(Ford–Konyagin)}.\ }$$
Checks against our Tier A/B measurements:
- $k=1$: prediction $c_1^2=0.01305$; our $1/\log$-extrapolation gave
  $\approx0.017$, but FK's own data shows $D_0$'s finite-scale density
  overshoots its limit (0.1240 at $10^{10}$ vs 0.11424) before descending — the
  same overshoot inflates our extrapolation. At matched scales, our measured
  pair density is a steady $0.90$–$0.94\times$ the square of FK's $D_0$ density
  ($10^5$: 0.896, $10^6$: 0.935, $10^9$: 0.921) — i.e. **asymptotic
  independence with a mild, stable finite-scale anti-correlation**, exactly
  what [T18] (log density) predicts.
- Geometric decay: $c_1=0.114$ vs our measured per-factor ratios 0.06–0.13. ✓
- First witnesses: $c_1^{-(k+1)}$ gives $3.4\times10^7$ at $k=7$ (OEIS:
  $1.0\times10^8$) ✓; refined predictions $a(8)\approx 3$–$7\times10^8$,
  $a(9)\approx 3$–$7\times10^9$.

---

## Part 4 — Gap analysis and revised program

**$k=1$ — "infinitely many $n$ with $n(n-1)\mid\binom{2n}{n}$" — now looks
genuinely attackable.** Target theorem: *the set of such $n$ has positive
logarithmic density* (log density suffices for infinitude, hence for this case
of 396). Assembly plan:
  1. Reduce to large primes via [FK21] §2 (verbatim — their bound is per-$n$
     and applies to the window with trivial modifications).
  2. Joint anatomy of $(n, n-1)$: binary-correlation input. [T18] gives exactly
     the needed PD$\times$PD independence in log density; the quantitative
     Tao–Teräväinen versions may upgrade this. **This is the one genuinely new
     analytic interface**: $1_{D_0}$ is not multiplicative (it couples anatomy
     with digits), so [T18] can't be cited black-box — the needed statement is
     a binary correlation for "anatomy events" (which are multiplicative-type:
     $P_j(n)\in[n^{a_j},n^{b_j}]$), conditioned on which the digit conditions
     decouple.
  3. Digit conditions: the large primes of $n$ and of $n-1$ are distinct, so
     all carry conditions live at distinct primes of the *same* $n$ —
     CRT-independent — and [FK21]'s Fourier machinery (their §4: simultaneous
     fractional parts $\{n/p^s\}$ for several primes $p\mid n$) needs extending
     only to allow some primes dividing $n-1$ instead of $n$; the exponential
     sum structure is unchanged in form.
  Risks: making step 2 quantitative enough to compose with step 3's error
  terms; logarithmic averaging propagating through FK's natural-density
  argument. Realistic outcome: a paper-scale theorem, possibly the first
  unconditional progress on the "hard side" of 396 beyond single shifts.
  *Elementary alternative (E1), flagged honestly:* Pomerance's balanced
  semiprime trick for the window would need e.g. $n=2pq$, $n-1=rs$
  simultaneously with ratio constraints; sieve methods give $n-1=P_2$ on the
  sequence $\{2pq-1\}$ but cannot unconditionally forbid the prime case, which
  is fatal here ($n-1$ prime $\Rightarrow$ non-smooth). Blocked at the last
  step; record and shelve.

**$k=2$.** Triples. Stable-set route closed [McN23]; positive-density
sqrt-smooth triples open. Two live options: (i) ternary correlations of the
relevant non-negative multiplicative-type functions **at almost all scales**
(Tao–Teräväinen ANT 2019 framework — their machinery already handles largest
prime factors of consecutive integers at almost all scales; an "almost all
scales" version of 396's $k=2$ would still prove infinitude!); (ii) the
[BW98] construction with explicit LTE-based carry analysis.

**All $k$ (the literal problem).** Only [BW98]-type constructions currently
produce windows smooth enough for arbitrary $k$. The R1 task is now precisely
scoped: for the BW witness $x$ (a product of powers of small integers), prove
$\text{carries}(x,p)\ge \sum_i v_p(x-i)$ for every $p$, using (a) LTE to compute
the needs exactly, (b) the multiplicative-coset freedom in the exponent
parameters to dodge bad primes, (c) possibly enlarging the BW prime classes so
each window element is a $\gamma$-th-power-minus-one with $\gamma$ enormous,
making carry room plentiful. High risk, but every object in it is explicit —
a good fit for machine-assisted experimentation: we can *compute* BW witnesses
for small parameters and measure their carry profiles before proving anything.

**Priority order:** (1) $k=1$ log-density theorem [FK ⊗ Teräväinen];
(2) computational probe of BW witnesses' carry profiles (cheap, informs R1);
(3) $k=2$ at almost all scales; (4) full R1.

