# Proof skeleton: positive logarithmic density for the $k=1$ window

**Target.** $W_1 := \{n\ge 2 : n(n-1) \mid \binom{2n}{n}\}$.

**Theorem 1 (main target).** $W_1$ has logarithmic density $c_1^2$, where
$c_1 = 0.11424\ldots$ is the Ford–Konyagin constant (density of the governor
set $D_0=\{m: m\mid\binom{2m}{m}\}$).

**Theorem 1′ (acceptable weakening).** $W_1$ has positive lower logarithmic
density. (Suffices for infinitude.)

**Theorem 1″ (fallback).** Positive density at almost all scales
(Tao–Teräväinen sense). (Still gives infinitude.)

*Context.* The $k=1$ instance of Erdős 396 ("exists $n$") is trivial ($n=2$).
The value here is (i) the first result on the hard side of 396 beyond single
shifts (Pomerance's $\,n-k\mid\binom{2n}{n}$, $\gg x/\log^2x$ witnesses), and
(ii) the template for $k\ge2$, where each new factor adds one more point to
the correlation.

Status tags: **[K]** known/citable, **[KA]** known-adapt (low risk),
**[N]** new but standard-toolbox (medium risk), **[HC]** hard core
(make-or-break).

---

## §0. Notation and exact criterion

For prime $p$ and $m\ge1$: $\kappa_p(m) := \#\{j\ge1 : \{m/p^j\}\ge 1/2\}$
(= carries in $m+m$ base $p$ = $v_p\binom{2m}{m}$, Kummer). Then
$$n\in W_1 \iff \forall p:\ v_p\big(n(n-1)\big)\le \kappa_p(n).$$
Every prime divides at most one of $n,n-1$, so the conditions split by side:
for $p^e\,\|\,n$ we need $e$ carries of $n$ at $p$; for $q^e\,\|\,n-1$ we need
$e$ carries **of $n$** at $q$.

Margin variants of the governor set: for $\sigma\in\{+,0,-\}$ let
$$\kappa^{(\sigma)}_p(m) := \#\Big\{j\ge1: \{m/p^j\}\in I^{(\sigma)}_j\Big\},\quad
I^{(+)}_j=[\tfrac12,\,1-p^{-j}),\ I^{(0)}_j=[\tfrac12,1),\ I^{(-)}_j=[\tfrac12-p^{-j},\,1),$$
and $D_0^{(\sigma)} := \{m : \forall p^e\|m,\ \kappa^{(\sigma)}_p(m)\ge e\}$,
so $D_0^{(0)}=D_0$.

## §1. Lemma 0 — exact reduction to a two-set correlation **[verified]**

**Lemma 0 (sandwich).**
$$D_0\cap\big(D_0^{(+)}+1\big)\ \subseteq\ W_1\ \subseteq\ D_0\cap\big(D_0^{(-)}+1\big).$$

*Proof.* If $q\mid n-1$ then $n/q^j=(n-1)/q^j+q^{-j}$, so
$\{n/q^j\}=\{(n-1)/q^j\}+q^{-j}$ unless $\{(n-1)/q^j\}\ge 1-q^{-j}$ (wrap).
Hence $\{(n-1)/q^j\}\in[\tfrac12,1-q^{-j})\Rightarrow\{n/q^j\}\ge\tfrac12$,
giving the left inclusion (the $p\mid n$ conditions are verbatim $n\in D_0$).
Conversely $\{n/q^j\}\ge\tfrac12\Rightarrow\{(n-1)/q^j\}\ge\tfrac12-q^{-j}$,
giving the right inclusion. $\square$

**Lemma 0′ (margins are free).** $d(D_0^{(\pm)})=d(D_0)=c_1$.
*Sketch:* the symmetric difference forces some $\{m/p^j\}$ within $p^{-j}$ of
$\tfrac12$ or $1$ at a prime power relevant to $m$'s factorization; summing
$p^{-j}\cdot p^{-1}$-type costs over the FK decomposition gives density $0$.
**[KA]** — routine within FK's framework.

**Empirical verification.** Both inclusions hold with **zero exceptions** for
all $n\le 60{,}000$; $|D_0^{(+)}|=|D_0|$ exactly on this range and
$|D_0^{(-)}|$ is $2\%$ larger; the lower set captures $98.7\%$ of $W_1$
(`lemma0_test.py`).

**Consequence.** Theorem 1 is *equivalent* to:
$$\boxed{\ \delta^{\log}\Big(D_0\cap(D_0^{(\pm)}+1)\Big)=c_1^2\ }$$
— a pure binary correlation of two fixed, density-$c_1$ sets, each defined by
(anatomy, digit) data of a single integer. All windowing/shift bookkeeping is
now gone, exactly (not just up to density-0 sets as in Pomerance's
$D_0+k\simeq D_{-k}$).

## §2. Architecture

Write $\mathbf 1_{D_0}(m) = \Phi(\mathcal A(m), \mathcal R(m))$ where
$\mathcal A(m)$ = anatomy data (the sizes $u_i=\log p_i/\log m$ of the prime
factors $>m^{\delta}$, with multiplicity) and $\mathcal R(m)$ = digit data
(residues $m \bmod p_i^{j}$). The proof is a conditional-independence cascade:

$$\Pr^{\log}\big[n\in D_0,\ n-1\in D_0^{(+)}\big]
= \underbrace{\Pr[\mathcal A(n)\in\cdot\,]\Pr[\mathcal A(n-1)\in\cdot\,]}_{\text{Lemma B}}
\times \underbrace{\Pr[\mathcal R(n)\ \text{good}\mid \mathcal A]}_{\text{Lemma C}}
\times \underbrace{\Pr[\mathcal R(n-1)\ \text{good}\mid \text{rest}]}_{\text{Lemma D}}
+ o(1),$$
preceded by Lemma A removing small primes. Lemmas A–C are [KA]/[N];
Lemma D is the hard core [HC].

## §3. Lemma A — small primes ignorable, two-sided **[KA]**

**Statement.** For $0<\delta\le1$, write $n(n-1)=A_nB_n$ with
$P^+(A_n)\le x^\delta<P^-(B_n)$. Then
$\#\{n\le x: v_p(A_n)>\kappa_p(n)\ \text{for some }p\}\ll x\,e^{-c/\delta}$.

*Proof sketch.* FK Lemma 2.1 verbatim for $p^v\mid n$ (low base-$p$ digits of
$n$ are $0^v$; failure forces $<v$ of the remaining $D-v$ digits to be
$\ge p/2$; binomial digit-count). For $p^v\mid n-1$: low digits of $n$ are
$(1,0^{v-1})$, contributing no carries, and the identical counting applies to
the top $D-v$ digits. Union over the two sides and over $p\le x^\delta$, $v$,
as in FK Prop. 1. Also discard $n$ with $p^2\mid n(n-1)$ for some
$p>x^\delta$ (cost $\ll x^{1-\delta}$). After Lemma A: only squarefree
large parts; each large prime needs $\ge1$ carry.

*Note (important negative result, §8):* the loss $e^{-c/\delta}$ is a fixed
positive density for fixed $\delta$ — fine for asymptotics with
$\delta\to0$ *after* $x\to\infty$, but it **forbids** any design that demands
smooth cofactors (smoothness probabilities $\rho(1/\delta)$-type always lose
to $e^{-c/\delta}$).

## §4. Lemma B — binary independence of anatomies **[KA⁻ — citable via TT (arXiv:2512.01739) Thm 1.7/Thm 3.1; named verifications in HYPOTHESES_CHECK.md]**

**Statement.** For finite unions of anatomy boxes
$A,B\subseteq\{(u_1\ge u_2\ge\cdots): \sum u_i\le 1\}$,
$$\sum^{\log}_{n\le x}\mathbf 1_{\mathcal A(n)\in A}\,\mathbf 1_{\mathcal A(n-1)\in B}
= \mathrm{PD}(A)\,\mathrm{PD}(B)+o(1).$$

**Reduction to citable form (the $z$-trick).** Anatomy-box indicators are not
multiplicative, but: (i) the number of prime factors $>x^{1/3}$ is $\le3$, so
"exactly $r$ primes in band $\beta$, none in band $\beta'$" is recovered from
finitely many values of $z\mapsto g_z(n):=\prod_{p^a\|n} z^{\#\{\text{band-}\beta\ p\}}\mathbf 1_{p\notin\beta'}$
by polynomial interpolation; each $g_z$ ($z\in[0,1]$) is bounded, real,
non-negative, **multiplicative**, and equidistributed in APs to fixed moduli.
(ii) Teräväinen's main discorrelation theorem [T18, Forum Math. Sigma 2018]
gives each pairwise correlation $\to$ product of mean values (qualitative
backstop). **Quantitative upgrade (Dec 2025):** Tao–Teräväinen
arXiv:2512.01739. Their Theorem 1.7 is the anatomy prototype verbatim —
$\frac1x\sum 1_{n\,x^{1/u}\text{-sm}}1_{n+1\,x^{1/v}\text{-sm}}
=\rho(u)\rho(v)+O(\log^{-c}x)$ at a log-density-1 set of scales, *uniformly*
in $u,v\le c\log_2x/\log_3x$ — and their general Theorem 3.1 (shape: $g_1$
centred against uncentred $g_2$, both 1-bounded multiplicative, conditions on
$g_1$ only: real + equidistributed in small-modulus classes) is the citable
engine, since each $g_z$ is literally in its class and the $x$-dependent band
edges are the same feature as the $x^{1/u}$ threshold in Thm 1.7. Work needed
(all verification-grade; see HYPOTHESES_CHECK.md §2): (B0) half-page
equidistribution lemma for $g_z$ ($g_z\equiv1$ below $x^\delta$ ⇒ equal class
means mod tiny $W$); (C1–C3) Thm 3.1 fine print (quantified equidistribution
definition, asymmetry of hypotheses, uniformity scope); fallback: mimic their
§3.7 derivation directly. (b) bookkeeping for the $\le3$ band-prime
constraint. The natural conclusion mode is almost-all-scales with
$\log^{-c}$ savings — exactly Theorem 1″'s mode, and by §4 of
HYPOTHESES_CHECK.md that also yields Theorem 1's log-density asymptotic.
Risk: low.

## §5. Lemma C — digit conditions on the $n$-side, twisted **[N]**

**Statement (FK twisted by a multiplicative weight).** For $g$ bounded
multiplicative (a Lemma-B-type weight carrying the $(n-1)$-anatomy condition),
the FK count of $n$ with prescribed large-prime data and digit successes,
weighted by $g(n-1)$, factors as (FK main term)$\times$(mean of $g$)$+o(1)$.

**Where the new sums live.** FK detect, for $p\,\|\,n$, $n=pm$, the conditions
$\{m/p^{a-1}\}\ge\frac12$ by Fourier: $e(h\,m/p^{a-1})$, then oscillate over
$m$ and over the primes (their §§3–5; Lemma 3.2 handles phases
$\sum_a \beta_a u^{-(a-1)}$ over $u=p$). Inserting $g(n-1)=g(pm-1)$ turns the
$m$-sums into
$$\sum_{m\sim x/p} g(pm-1)\,e\!\big(h\,m/p^{a-1}\big),$$
i.e. **mean values of bounded multiplicative functions in APs to modulus
$p^{a-1}$** (the character is $m$-periodic mod $p^{a-1}$), needed *on average
over $p\sim x^{u}$*. Individual moduli of size up to $x^{1-u}$ are far beyond
unconditional reach, but only the average over $p$ is needed —
Bombieri–Vinogradov-type theorems for multiplicative functions
(e.g. Granville–Shao and successors) and/or large-sieve dispersion are the
candidate inputs. For Theorem 1′ (lower bound), one may also restrict the
$a=2$ digit range so only $O(1)$ harmonics $h$ matter. Risk: medium; this is
real work but inside the standard toolbox.

## §6. Lemma D — digit conditions on both sides **[HC]**

**Statement.** With all anatomy fixed (Lemma B classes) and $n$-side digits
detected (Lemma C), the $(n-1)$-side digit conditions — by Lemma 0,
*the carry conditions of $n-1$ at its own primes $q$* — equidistribute
jointly, i.e.
$$\sum^{\log}_{n}\Big[\text{anat}\Big]\,
e\!\Big(\textstyle\sum_{i,a}\alpha_{i,a}\frac{n}{p_i^a}\Big)\,
e\!\Big(\textstyle\sum_{j,b}\beta_{j,b}\frac{n-1}{q_j^b}\Big) = o(\text{trivial}),
\qquad p_i\mid n,\ q_j\mid n-1,$$
for nonzero frequency vectors.

**Why it's the crux.** The two phase families live on coprime prime-power
moduli, so there is no *algebraic* obstruction — but there is a severe
*counting* obstruction: for fixed primes the cofactor ranges are far shorter
than the products of the moduli, so joint uniformity is false pointwise and
holds only at the ensemble level, after averaging over the primes. (This is
already true *within* one side — it is exactly the content of FK §4 — and our
data shows it: a persistent $\approx4\%$ within-side finite-scale deficit,
$\sim5\sigma$ combined over three samples, while FK's theorem guarantees it
vanishes asymptotically.) The summation variable moreover parametrizes only one
side multiplicatively at a time: writing $n=p m$ makes the $p$-phases nice
($e(hm/p^{a-1})$) but turns the $q$-phases into
$e(\beta(pm-1)/q^b)$ — additive characters of modulus $q^b$ where $q$ is a
prime factor of $pm-1$, **not a free variable**. This is the genuine binary
entanglement.

**Candidate attack D-i (dispersion).** Open the $q$-side via the divisor
switch: $n-1=q m'$, sum over the pairs of parametrizations subject to
$pm - qm' = 1$, Cauchy–Schwarz in the smooth variables, and bound the
off-diagonal bilinear sums
$\sum e\big(n(\beta/q^b-\beta'/q'^b)\big)$ by the curvature of
$q\mapsto q^{-b}$ (FK Lemma 3.2 is exactly a $j$-th-derivative-test engine for
such phases). Classical dispersion à la Linnik/Motohashi/BFI; the required
ranges should be checked symbolically before any writing.

**Candidate attack D-ii (quantitative correlations — now with a concrete
template).** Tao–Teräväinen, *"Quantitative correlations and some problems on
prime factors of consecutive integers"* (arXiv:2512.01739), prove joint
statements about $(n,n+1)$ — including an Erdős–Pomerance–Sárközy asymptotic
for $\#\{n\le x:\omega(n)=\omega(n{+}1)\}$ at almost all scales — via exactly
the pipeline Lemma D wants: encode the joint condition by the circle method,
bound minor arcs with **Pilatte's recent quantitative correlation estimates for
bounded multiplicative functions** (power-of-log savings), and treat major arcs
by sieve methods in physical space. Their stated frontier ("current pairwise
correlation technology either requires logarithmic averaging, or is restricted
to almost all scales") coincides with our Theorem 1/1″ dichotomy. **Reading
verdict (see HYPOTHESES_CHECK.md §3): black-box NO.** Three independent
blockers, each with a mechanism: (1) Tao's dilation needs $F(dn)=F(n)$, but
digit residues transform by $r\mapsto(d\bmod p^j)r$ — a bijection, so
distributions survive but the pointwise identity dies, and $d$-averaging
randomizes the digits away; (2) the centring step consumes an MRT-type
multiplicative-functions input; (3) their frequency objects $e(\alpha\Omega(n))$
are multiplicative *because $\Omega$ is additive* — our digit functionals are
not additive. What survives: Pilatte's spectral engine is 1-bounded-only
(a general bilinear tool, shape-mismatched but available), and — the key
conceptual gain — **the parity barrier does not apply to Lemma D**: our
indicators are non-negative, positive-mean, local conditions, so D's hardness
class is large-moduli equidistribution on average (dispersion/BV type, moduli
$q^a\le x^{2/3+}$ correlated with $n-1$), not parity. D-i is the lead attack;
D-ii is reframed as proving "Estimate D\*" (Pilatte-strength bounds with
divisor-correlated prime-power frequencies), stated in HYPOTHESES_CHECK.md.

**Mitigations that shrink D's burden** (use freely for Theorem 1′):
- *Automatic band:* if $q^2\in(n,2n]$ (i.e. $q\in(\sqrt n,\sqrt{2n}\,)$), the
  $j{=}2$ carry is free — top-prime-near-$\sqrt n$ configurations need no
  digit analysis at all.
- *Deep digits:* primes with $u<1/3$ have $\ge2$ chances; only an upper bound
  on joint failure is needed, weakening the required equidistribution.
- The truly unavoidable case is $u\in(1/3,1/2)$ with its single coin flip —
  Lemma D can be first proven for *one* such prime per side ($r=s=1$), which
  already yields Theorem 1′ with a smaller constant.

## §7. Assembly

Lemma A (with $\delta\to0$ last) + Lemma B (anatomy product) + Lemmas C, D
(conditional digit products, FK §5 bookkeeping) + FK §7 (numerics of $c_1$)
$\Rightarrow$ Theorem 1. The PD computation of the limit constant is FK's
verbatim, squared. Consistency data already in hand: measured pair density
$=0.90$–$0.94\times$(FK finite-scale density)$^2$ across $10^5$–$10^9$, drift
direction matching FK's own slow convergence.

## §8. Failed approaches (recorded so effort isn't repeated)

1. **Pure union bound / digit counting.** FK Lemma 2.1-type counting gives
   unconditional per-prime failure bounds $\ll(x/p)e^{-c/u}$, but the total
   failure mass is $\Theta(1)\approx 0.99$ (the true density of $W_1$ is
   $\approx0.013$), so no union-bound design can reach positivity; the events
   must be handled multiplicatively (inclusion–exclusion/independence). No
   elementary proof by this route.
2. **Smooth-cofactor designs.** Any event requiring a cofactor to be
   $x^\delta$-smooth costs $\rho(c/\delta)$-type probability, which always
   loses to Lemma A's $e^{-c/\delta}$ exceptional set. (This also retro-explains
   why the Tier-B $n=m^2$ family underperformed.)
3. **Semiprime trick (Pomerance Thm 3) on both sides.** Needs $n-1$ to be a
   balanced semiprime along the sequence $\{2pq-1\}$; sieves give $P_2$ but
   cannot unconditionally exclude the prime case, which is fatal
   ($n-1$ prime $\Rightarrow$ non-smooth $\Rightarrow n\notin W_1$).
4. **Stable-set softness.** Even if $D_0$ were stable (unclear), Hildebrand '85
   would give pairs — but McNamara's counterexample caps this route at pairs,
   and $D_0$'s digit component likely breaks stability anyway. Worth a
   10-minute check (is $D_0$ empirically stable under small dilations?), not
   worth a proof attempt.

## §9. Falsification tests — **EXECUTED**; see `SKELETON_TESTS_ADDENDUM.md`

Summary: Lemma B and Lemma D independence pass cleanly at the $10^9$ scale
(cross-side digit ratios $0.984,\,1.003,\,0.995$ over three independent
samples; digit success indifferent to the other side's anatomy to within
$1\sigma$); margins are numerically free; the within-side measurements exhibit
the *expected* FK finite-scale structure (top-digit determinism + ensemble-only
equidistribution), which forced two corrections now incorporated above.
**Drafting note from the tests:** for band primes ($1/3<u<1/2$) the $j{=}2$
digit is the *top* digit and its law is the explicit piecewise function of the
size ratio ($p^2\in(n,2n]$: forced success; $p^2\in(2n/3,n]$: forced failure;
etc.) — Lemmas C/D should be stated as: top digit handled deterministically by
this law (it is what FK's $\lfloor 1/u\rfloor$ integrates), equidistribution
claimed only for interior digits. Original test list:

1. **Lemma B test:** measure $\Pr[\mathcal A(n)\in A,\ \mathcal A(n-1)\in B]$
   vs product, for the specific band-boxes the proof uses, at $10^6$–$10^9$.
2. **Lemma C/D test:** within fixed anatomy classes, measure the joint
   distribution of the digit variables $(\{n/p^2\})_{p\|n}$,
   $(\{(n-1)/q^2\})_{q\|n-1}$ — uniformity and cross-side independence,
   with quantitative discrepancy estimates vs $x$.
3. **Stability probe of $D_0$** (§8.4).
4. **Margin robustness:** densities of $D_0^{(\pm)}$ at $10^8$–$10^9$
   (Lemma 0′ numerics).

## §10. Beyond $k=1$

The same skeleton for general $k$ replaces Lemma B/D by $(k{+}1)$-point
correlations: anatomy independence at order $\ge3$ is open in natural density
(and stable-set-impossible by McNamara), but the Tao–Teräväinen
almost-all-scales framework is the live route for $k=2$ (Theorem 1″-type
conclusions still give infinitude, i.e. genuine cases of 396). Every lemma
proven here is a module reused there.

---

### Citations needed in a formal write-up
Kummer 1852; Pomerance, Amer. Math. Monthly 122 (2015) 636–644;
Ford–Konyagin, Trans. AMS 374 (2021) (arXiv:1909.03903);
Sanna (upper density of $D_0$); Teräväinen, Forum Math. Sigma 6 (2018) e10
(arXiv:1710.01195); Tao–Teräväinen, ANT 13 (2019);
Tao–Teräväinen, arXiv:2512.01739 (quantitative correlations; the D-ii
template); Pilatte, arXiv:2310.19357 (two-point logarithmic Chowla
$\ll(\log x)^{1-c}$; almost-all-scales Rmk 2.8; the spectral engine —
multiplicativity used only in the dilation and centring steps, the rest
1-bounded-only); Hildebrand PAMS 95 (1985); McNamara arXiv:2312.08544
(context); Balog–Wooley JAMS 64 (1998) (context for $k\ge2$).

