# WP9: The Unified Frontier Object (E3† / C†-D3 / D†-core) — Diagnosis

**STATUS: COMPLETE (research diagnosis, web-assisted). VERDICT:
CITATION-ADJACENT for E3† — the 2005–2020 Kloosterman-sums-over-primes
literature (Bourgain 05 / Baker 12 / Korolev 18 / Korolev–Changa 20) covers
the hard sub-range $\Lambda\in(Q^{1+\varepsilon},Q^{3/2}]$ of the inner
object with POWER savings vs our polylog need; remaining work = a
paper-scale dispersion reduction + an $x^\varepsilon$-thin seam at
$\Lambda\approx Q$ (§4). Hard-sub-range pair correlation numerically shows
square-root cancellation (§3, new stratified probe). The C† twin does NOT
inherit the coverage and stays open (§4). Citations NOT yet merged into
`citations.md`.**

Date: 2026-06-10. Sources: `wp8-e3.md` (Prop S, T1, E3†), `wp8-cdagger.md`
(D3 sector, obstruction 2 = unification finding), `lemma-alpha-beta.md` §5
(D† second-moment core), `manuscript/sections/11-typeII.tex` (hyp:E3).
Findings here are NOT yet merged into `citations.md` (per scope).

Notation (program-standard): $L=\log x$, $P=x^u$, $Q=x^{u'}$,
$u,u'\in(1/3,1/2)$, $R=x^{1-u-u'}$, $y=(2x)^{1/3}$, $A=x^{1-u}$,
$a_0=(p^{-1}\bmod q)\in[1,q)$, $\theta_\mu=\mu q/p-\lambda p/q$,
$\langle\mu\rangle=\min(\mu,p-\mu)$. In-band: $u+u'>2/3$ (so $R<y$),
$u+2u'>1$ (so $A<Q^2$).

---

## 1. The unified object: one statement, two incarnations

### 1a. Incarnation R (root pair correlation) — Hypothesis E3† verbatim

For each fixed $0<|\lambda|\le L^C$ and each fixed $\mu$ with
$0<\langle\mu\rangle\le L^{2c+6}$ (polylog-many frequencies):
$$\frac{1}{\pi(P)\pi(Q)}\sum_{q\sim Q\ \mathrm{prime}}
\sum_{\substack{p\sim P\ \mathrm{prime}\\ p\ \mathrm{minor}}}
\Big|\sum_{\substack{\ell\ \mathrm{prime},\ y<\ell\le A_{\max},\ \ell\ne q\\
\nu_\ell(p,q)\le R}} e\big(\nu_\ell(p,q)\,\theta_\mu\big)\Big|^2
\;\ll\; R^2\,L^{-2c-8},$$
where $\nu_\ell(p,q)=(-a_0\bar q)\bmod\ell\in[0,\ell)$ is the root of the
linear congruence $a_0+qt\equiv0\ (\mathrm{mod}\ \ell)$, i.e. the unique
$t$-location where $\ell$ divides the progression $a_0+qt$. The diagonal
$\ell_1=\ell_2$ is $\approx\kappa'R\ll R^2L^{-2c-8}$ (corner trim), so the
content is exactly the **off-diagonal pair correlation of the roots with
phase $\theta_\mu$, on $(p,q)$-average, with polylog target saving**:
$$\mathbb{E}_{p,q}\ \sum_{\substack{\ell_1\ne\ell_2\ \mathrm{prime}\in(y,A]\\
\nu_{\ell_1},\nu_{\ell_2}\le R}}
e\big((\nu_{\ell_1}-\nu_{\ell_2})\,\theta_\mu\big)\;\ll\;R^2L^{-2c-8}
\qquad(\text{trivial} = R^2\cdot O(1);\ \text{need saving } L^{2c+8}).$$
Per T1 (`wp8-e3.md` §3) this single statement is the *entire* remaining
content of Hypothesis E3, hence of the full-density Theorem 1 anatomy layer.
Lower-bound track needs only the constant-density exceptional-set form E3-lb.

### 1b. Incarnation K (bilinear Kloosterman-type sums over primes)

Completing the window condition $\nu_{\ell_i}\le R$ by additive characters
mod $\ell_i$ and writing $\nu_\ell=-a_0\bar q\bmod\ell$, the nonzero
harmonics of the off-diagonal are (with $b=b(q)=(-\bar q\bmod p)$, so
$pa_0=1+bq$):
$$\sum_{q\sim Q\ \mathrm{prime}}
e\Big(\tfrac{h_1\,\overline{q(b+pt_1)}}{\ell_1}
+\tfrac{h_2\,\overline{q(b+pt_2)}}{\ell_2}\Big)
\,e\big(\Delta t\,\theta_\mu\big),
\qquad \ell_1\ne\ell_2\sim\Lambda\in(y,A],\ t_i\le R,$$
i.e. **Kloosterman fractions with a prime numerator variable $q$, nested
inverses ($\bar q\bmod p$ inside the mod-$\ell_i$ inverse), composite
completion modulus $\ell_1\ell_2\le A^2<Q^4$**. After Cauchy–Schwarz in
$\ell$ and opening the $q$-square (route K1), the inner object is
$$\sum_{\ell\sim\Lambda\ \mathrm{prime}} e\big(n(q_1,q_2,h)\,
\overline{q_1q_2}\,/\,\ell\big)
\ \xrightarrow{\ \text{reciprocity}\ }\
\sum_{\ell\sim\Lambda\ \mathrm{prime}} e\big(-n\,\bar\ell\,/\,q_1q_2\big)
+\ \text{smooth},$$
a **Kloosterman sum over primes $\ell\sim\Lambda$ to the modulus
$q'=q_1q_2\sim Q^2$, with numerator $n$ depending on the pair $(q_1,q_2)$**.
The same species appears verbatim as the D†-second-moment core
(`lemma-alpha-beta.md` §5): $\sum_{p_2\sim P}\sum_{p_1\equiv p_2(q)}
e(-\lambda s\bar p_2/q)$ (prime inverse in the frequency, modulus $q\sim Q$),
and as the C†-pair D3 sector (`wp8-cdagger.md` §2): bilinear Kloosterman
fractions $\bar m\bmod p_2,\ \bar m'\bmod p_2'$ at completion modulus
$p_1p_2p_2'>x$. The program's dispersion debts all converge here.

### 1c. The dictionary

| Incarnation R (roots) | Incarnation K (Kloosterman) |
|---|---|
| root $\nu_\ell=-a_0\bar q\bmod\ell$ | fraction $e(h\,\overline{q\cdot}\,/\ell)$, then reciprocity $e(-n\bar\ell/q_1q_2)$ |
| window $\nu_\ell\le R$, $R/\ell\asymp R/\Lambda$ | harmonics $h$ up to $\approx\ell/R$ per modulus |
| modulus of roots: primes $\ell\sim\Lambda\in(y,A]$ | prime *argument* variable $\ell\sim\Lambda$; modulus $q_1q_2\sim Q^2$ |
| $q\sim Q$ prime, average available | numerator/modulus built from $q$; $q$-average = bilinear structure |
| pair correlation $\ell_1\ne\ell_2$ | pair-dependent numerator $n(q_1,q_2,h)$ |
| target: save $L^{2c+8}$ over $R^2$ | target: any $L^{-\mathrm{big}}$ saving over trivial, uniform in $n$ |
| hard sub-range $\Lambda\in(Q,Q^{3/2}]$ | prime-variable length $\Lambda\in(q'^{1/2},q'^{3/4}]$, $q'=Q^2$ |

**Why $(Q,Q^{3/2}]$ is the hard sub-range** (from `wp8-e3.md` §4):
$\Lambda\le Q$ = complete-sum regime ($q$-interval longer than modulus
$\ell$): Weil per $\ell$ gives power saving. $\Lambda\ge Q^{3/2+\varepsilon}$
= Fouvry–Michel prime-variable territory ($\Lambda\ge(Q^2)^{3/4+\varepsilon}$).
In between, the prime variable $\ell$ has length between the square root and
the 3/4 power of the modulus $q'\sim Q^2$ — exactly the
sums-over-primes-below-$q^{3/4}$ frontier. In-band geometry guarantees
$y<Q^{3/2}<A$ can all occur, and $A<Q^2$ ($u+2u'>1$) caps everything below
the modulus: the whole range is sub-complete in the $q'$-aspect.

**Our specific advantages over the literature's standard setting** (the
adaptation levers): (i) only LOG-power saving needed, not power saving;
(ii) the average over $q\sim Q$ (and over $p\sim P$) is available — the
statement is a variance, not a pointwise bound; (iii) the moduli $\ell$ are
averaged over a dyadic range (and over pairs); (iv) lower-bound track needs
only a positive-proportion/exceptional-set form (E3-lb).

---

## 2. Adjacent literature (web-pinned this session)

Recall the two reference shapes. **Shape K-single** (route K1 inner sum,
pointwise in $(q_1,q_2,h)$, uniform in numerator): $W_{q'}(N)=
\sum_{\ell\le N\ \mathrm{prime}}e(n\bar\ell/q')$, modulus $q'=q_1q_2\sim Q^2$
(squarefree, two prime factors), $N=\Lambda$, hard range
$N\in(q'^{1/2},q'^{3/4}]$, need: any $L^{-\mathrm{big}}$ saving uniform in
$n$, $(n,q')=1$. **Shape K-bilinear** (the full off-diagonal kept):
$\sum_m\sum_n\alpha_m\beta_n e(a\bar m/n)$-type with one variable prime and
pair-dependent numerators. **Shape R** (roots): pair correlation of
$\nu_\ell/\ell$-type points at scale $R/\Lambda$, moduli = primes.

### 2a. Duke–Friedlander–Iwaniec 1995 (roots of quadratic congruences)

*Equidistribution of roots of a quadratic congruence to prime moduli*,
Ann. of Math. 141 (1995) 423–441. Statement shape: for fixed $f(x)=ax^2+bx+c$
with negative discriminant, the normalized roots $\nu/p$ of
$f(\nu)\equiv0\ (\mathrm{mod}\ p)$ equidistribute as $p\le X$ runs over
primes; engine = a nontrivial bound on the Weyl linear form
$\sum_{p\le X}\sum_{f(\nu)\equiv0(p)}e(h\nu/p)$ with power saving, proved by
expanding $\nu/p$ via the theory of binary quadratic forms into Salié/
Kloosterman fractions and applying Iwaniec's spectral bounds for sums of
Kloosterman sums — i.e. the *average over the moduli* $p\le X$ is the
load-bearing average. **Coverage of our object:** method-adjacent, not
range-adjacent. We do have the analogous modulus average (over $\ell$), but:
(i) our congruence is linear with the coefficient $q$ varying (the Weyl sum
in our case *is* a Kloosterman fraction, see dictionary §1c — DFI's
quadratic-form expansion has no analogue and is not needed); (ii) our test
scale is the power-small window $R/\Lambda$, not a fixed interval; (iii) we
need the second moment (pair correlation), not the first. Gap: DFI95 gives
the $h$-th Weyl sum on $\ell$-average — formally the $q$-less, first-moment
shadow of E3†.

### 2b. Marklof–Welsh 2022+ (pair correlation of roots — exact analogue, wrong category)

*Fine-scale distribution of roots of quadratic congruences* (Bristol
preprint, July 2022; J. Marklof, M. Welsh). For $\mu^2\equiv D\ (m)$, $D>0$
squarefree, $D\not\equiv1\ (4)$, **all moduli $m$ in order**: the pair
correlation measure $R_{2,N}(I)\to\int_I w_D$ exists with explicit density
$w_D$ (not Poissonian), via convergence of geodesic random line processes
in the hyperbolic plane (homogeneous dynamics; unconditional but **no
rate**). Restriction to prime moduli: NOT handled (they note prime-moduli
fine-scale statistics as open; equidistribution-with-rate for prime moduli
is exactly DFI95's harder regime). **Coverage:** this is the closest
statement *in kind* to Incarnation R (pair correlation of congruence
roots), and it shows such pair correlations are genuinely computable
objects; but: no rate, no prime moduli, no varying coefficient $q$, no
exponential-sum saving — useless as a citation, valuable as a sanity model
(its $w_D$ is $O(1)$: pair correlation does not blow up — consistent with
our square-root-cancellation numerics).

### 2c. DFI 1997 / Bettin–Chandee 2018 / 2026 successors (bilinear Kloosterman fractions)

- **DFI97**, *Bilinear forms with Kloosterman fractions*, Invent. Math. 128
  (1997) 23–43: $\sum_{m\sim M}\sum_{n\sim N}\alpha_m\beta_n e(a\bar m/n)
  \ll\|\alpha\\|\|\beta\|\,(\dots)$ with saving $(MN)^{-1/48}$-grade at
  $M\approx N$; arbitrary coefficients on both sides; *the* origin result.
- **Bettin–Chandee**, *Trilinear forms with Kloosterman fractions*, Adv.
  Math. 328 (2018) 1234–1262 (arXiv:1502.00769): adds a third arbitrary
  coefficient $\nu_a$ on the numerator, saving $N^{1/20}$ at $M\approx N$,
  $a\ll MN$; nontrivial in wider unbalanced ranges.
- **Dong–Robles–Zeindler 2026** (arXiv:2601.00292): bilinear bound
  $\ll\|\alpha\|\|\beta\|(a+bMN)^{1/4}(M+N)^{1/6}N^{1/3}M^{-1/12+\varepsilon}$
  — saving up to $1/12$ at balanced ranges, arbitrary coefficients.
- **Wright 2026** (arXiv:2604.25177, *Trilinear Kloosterman fractions I:
  partially fixed moduli and unbalanced convolutions*): Bettin–Chandee with
  a fixed factor $R$ in the modulus treated losslessly; application:
  equidistribution of unbalanced convolutions $\alpha*\beta$ in APs to
  moduli $Q\le X^{1/2+1/66-\delta}$ with $N$ as short as
  $\exp((\log X)^\varepsilon)$ — log-saving culture, BV-type conclusions.

**Coverage of our object:** these are the right *species* (after completion
our off-diagonal is exactly a trilinear Kloosterman-fraction form), and the
2026 activity shows the area is alive. Two blockers, both already visible in
`wp8-e3.md` §4: (i) **pair-dependent numerators** — in our form the
numerator $n(q_1,q_2,h)$ is a function of the two outer variables, so the
form is not a product of free coefficient sequences; DFI/BC/DRZ/Wright all
need $\nu_a$ free of $(m,n)$. (ii) Even granting structure, at our scales
($M\sim Q^2$ from the $q$-pair, $N\sim\Lambda\le Q^{3/2}$, plus the nested
$\bar q\bmod p$ layer riding along) the balanced-range savings
$(MN)^{-1/12}$-grade are power savings in the *completed* variables, but
the completion of the $t_i\le R$ windows costs $(\Lambda/R)^2$ harmonics —
the bookkeeping that `wp8-cdagger.md` found saturating in the C† twin. Gap:
no black-box theorem applies; the *techniques* (Cauchy + count solutions of
$\bar m_1/n_1-\bar m_2/n_2$-equations à la DFI Lemma 1) are the right
toolkit for a bespoke proof.

### 2d. Kloosterman sums over primes — the decisive sub-literature (Shape K-single)

For $W_q(N)=\sum_{p\le N,\ p\nmid q}e_q(a\bar p+bp)$, $(a,q)=1$
(Vinogradov–Vaughan decomposition + bilinear Kloosterman technology;
sources: Korolev's 2018 HKU survey slides [extracted in full this session],
the cited originals):

| Result | modulus $q$ | range of $N$ | saving | notes |
|---|---|---|---|---|
| Fouvry–Michel, Ann. Sci. ENS 31 (1998) 93–130 | prime | $q^{3/4+\varepsilon}\le N\le q$ | power $q^{-\delta(\varepsilon)}$ | full $a\bar p+bp$ phase |
| Garaev 2010 | prime, $b=0$ | $N\ge q^{3/4+\varepsilon}$ | $N^{15/16}+N^{2/3}q^{1/4}$ | |
| Fouvry–Shparlinski, Acta Arith. 2011 | **composite**, $b=0$ | $q^{3/4+\varepsilon}\le N\le q^{4/3-\varepsilon}$ | power | Garaev-type bound |
| **Bourgain 2005** | prime | $\mathbf{q^{1/2+\varepsilon}\le N\le q}$ | power $q^{-\eta(\varepsilon)}$ | sum-product era |
| **Baker 2012** | squarefull part $\le q^{1/4}$ (so: **squarefree composite OK**) | $\mathbf{q^{1/2+\varepsilon}\le N\le q}$ | power, $\eta=\varepsilon^4/2000$ | explicit |
| Korolev 2018 (Thm 1) | prime, $b=0$ | $q^{1/2+\varepsilon}\le N\le q$ | power, $\eta=\varepsilon^2/20$ | via Karatsuba–Bourgain–Garaev mean values |
| Korolev 2017/2018 (Thm 3) | **arbitrary composite**, $b=0$ | $q^{5/8+\varepsilon}\le N\le q^{7/4-\varepsilon}$ | power, explicit 3-regime $\Delta$ | e.g. $(q^{5/8}N^{-1})^{1/5}$ |
| Korolev, arXiv:1911.09981 / RNT 2020 | composite, full phase | $q^{3/4+\varepsilon}\le N\ll q^{3/2}$ | power | |
| **Korolev–Changa, Math. Notes 108 (2020) 87–93** | **arbitrary** | $\mathbf{q^{1/2+\varepsilon}\le N\ll q^{3/2}}$ | refines FSh11 + K18/19 (saving at the bottom of the range is weaker — log-grade per the surrounding literature; exact $\Delta$ to be pulled from the paper) | the closest single statement to Shape K-single |

**Coverage of our object — the key finding of this session.** Shape
K-single is $W_{q'}(\Lambda)$ with $q'=q_1q_2$ squarefree composite and
$\Lambda\in(q'^{1/2},q'^{3/4}]$ — i.e. exactly the range that this
sub-literature conquered between 2005 and 2020, *including composite
moduli*: Baker 2012 (squarefull part $1\le q'^{1/4}$ ✓) gives a **power
saving** $q'^{-\eta}$ on the whole hard sub-range
$\Lambda\in(Q^{1+\varepsilon},Q^{3/2}]$ provided $\Lambda\le q'$ ✓
($\Lambda\le A<Q^2$ in-band), and Korolev 2018 Thm 3 independently covers
$\Lambda\ge Q^{5/4+\varepsilon}$, Korolev–Changa the full
$\Lambda\ge Q^{1+\varepsilon}$. The `wp8-e3.md` §4 assessment
("Fouvry–Michel-type prime-variable bounds need
$\Lambda\ge Q^{3/2+\varepsilon}$") **understates the literature**: it
priced only FM98. The residual sliver $\Lambda\in(Q,Q^{1+\varepsilon}]$ is
covered from the other side: there $\ell\le Q^{1+\varepsilon}\ll Q^{2-\delta}$
and the *$q$-aspect* sum over primes $q\sim Q$ to prime modulus $\ell$ is in
the Bourgain-2005 range $Q\ge\ell^{1/2+\varepsilon}$ (prime modulus ✓) —
power saving again. So **at the level of Shape K-single, the entire hard
sub-range carries known power-saving bounds, far more than the polylog we
need.** What is NOT covered by citation: the reduction of E3† *to* Shape
K-single (the C-S/dispersion bookkeeping: window completion costs, the
$b(q)=-\bar q\bmod p$ nested-inverse layer, the diagonal $q_1=q_2$ terms,
keeping the saving through Cauchy–Schwarz) — paper-scale but elementary-
shaped work, no new technology evidently required. See §4 verdict.

### 2e. Bourgain–Garaev (bilinear/multilinear Kloosterman, prime modulus)

*Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*
(2014): additive properties of $I^{-1}$ for intervals $I\subset\mathbb F_p$
+ multilinear exponential-sum estimates ⇒ incomplete multilinear Kloosterman
bounds below the Weil range; with Karatsuba's mean-value theorem
($I_k(X)\ll$ for $X^{2k-1}\ll q$) this is the engine inside the
$q^{1/2+\varepsilon}$-range results of §2d. **Coverage:** technology
substrate, prime modulus only; cite as the method behind Bourgain
2005/Korolev 2018; not directly applicable to composite $q'$ (that is
Baker's/Korolev–Changa's contribution).

### 2f. Irving / Khan (divisor function in APs to special large moduli)

- **Irving**, *The divisor function in arithmetic progressions to smooth
  moduli* (IMRN 2015; arXiv:1403.8031): $\tau(n)$ in APs beyond the Weil
  $x^{2/3}$ barrier for $x^\rho$-smooth squarefree moduli ($q$-van der
  Corput factorization of the modulus).
- **Khan**, *The divisor function in arithmetic progressions modulo prime
  powers* (Mathematika 2016; arXiv:1510.03377): moduli $q=p^k$, $k\ge7$
  fixed, $q$ in a window around $x^{2/3}$ (past the barrier by $x^{\rho_k}$)
  — Postnikov/p-adic explicit-phase methods. (Adjacent: Milićević's
  sub-Weyl subconvexity at powerful moduli; Liu–Shparlinski–Zhang-type
  variants at $p^k$, $k$ small, remain at/below $2/3$.)

**Coverage:** relevant to the C†/D† incarnation (our conductor $q^2$, $k=2$:
Postnikov machinery exists at $k=2$ but the $k\ge7$/smoothness factorization
tricks do not apply; and our modulus $p_1^2\sim x^{2u_1}>x^{2/3}$ exceeds
all these ranges anyway, as `wp8-cdagger.md` priced). For E3† proper:
factorable-modulus $q$-vdC is a possible *substitute* technology in the
$\ell$-completion (our completed modulus $\ell_1\ell_2$ IS factored — two
prime factors of equal size — which is precisely the $q$-vdC-friendly
shape; Irving's mechanism, not his theorem). Gap: no statement to cite;
shape-compatible technique.

### 2g. What the program needs vs. what exists — summary table

| need | closest theorem | covers? | precise gap |
|---|---|---|---|
| pair correlation of roots, prime moduli, power-small scale, $q$-average, polylog saving (E3† as stated) | Marklof–Welsh 2022 (kind); DFI95 (method) | NO | no rate / no prime moduli / first moment only |
| Shape K-single: prime-variable Kloosterman, composite modulus $q'\sim Q^2$, $N=\Lambda\in(q'^{1/2},q'^{3/4}]$ | **Baker 2012 + Korolev–Changa 2020** (+ Bourgain 2005 for the $q$-aspect sliver) | **YES — with power saving** | none in the range; need uniformity-in-$a$ audit (standard) |
| the reduction E3† $\to$ Shape K-single | BFI-style dispersion (BFI 1986); `wp8-e3.md` §4 sketch | NO (not in print) | paper-scale dispersion bookkeeping: window completion, $b(q)$ layer, diagonal, C-S loss budget |
| Shape K-bilinear as black box (skip the reduction) | DFI97 / Bettin–Chandee / DRZ26 / Wright26 | NO | pair-dependent numerator violates free-coefficient hypothesis |
| C†/D† twin (conductor $p^2$, binding digit twist) | Irving/Khan special-moduli τ-in-APs | NO | modulus $x^{2u}>x^{2/3}$ beyond all known special-moduli ranges |

---

## 3. Numerical probe (hard sub-range pair correlation)

Script: `wp9_frontier_probe.py` (`.venv/bin/python wp9_frontier_probe.py`,
runs in ~5 s; seed 396). New beyond `e3_probe2.py`: the $\Lambda$-range is
**stratified**, isolating the hard sub-range $(Q,Q^{3/2}]$ that no prior
probe had separated, plus a direct Shape K-single measurement.

**(P1) Root pair correlation, stratified.** $x=2\cdot10^7$,
$(u,u')=(0.34,0.36)$, $\lambda=1$, $\mu\in\{1,2,3,5\}$, 6 random $p\sim P$,
160 random $q\sim Q$. Diagnostic: $\mathbb E_q|S|^2/\mathbb E_q n$
($S$ = root sum, $n$ = #terms = diagonal; $1.0$ = exact square-root
cancellation, E3† needs $\ll R/L^{2c+8}$):

| range | #primes $\ell$ | mean $n$ | ratio over $(\mu,p)$ cells |
|---|---|---|---|
| easy $(y,2Q]$ | 78 | 11.5 | 0.91–1.13 (means), all cells 0.74–1.67 |
| **HARD $(2Q,Q^{3/2}]$** | 947 | 23.2 | **0.79–1.28 (means)**, cells 0.60–2.17 |
| top $(Q^{3/2},A]$ | 5487 | 12.0 | 0.91–1.05 (means) |

**(P2) Larger scale, hard range only.** $x=2\cdot10^8$, same geometry,
200 $q$, mean $n\approx51$: per-$\mu$ mean ratios $0.84,0.98,0.99,1.05$
($\mu=1,2,3,5$); off-diagonal/diagonal within $\pm0.16$ at every $\mu$.
**Square-root cancellation holds in the hard sub-range with no off-diagonal
accumulation as the population grows** ($n$ 23→51 leaves ratios at $O(1)$).

**(P3) Shape K-single directly.** $W(\Lambda)=\sum_{\ell\le\Lambda\
\mathrm{prime}}e(n\bar\ell/q')$, $q'=q_1q_2\sim2Q^2\approx3.6\cdot10^5$,
40 random pairs $(q_1,q_2)$, random unit numerators $n$:
$|W|/\sqrt{\pi(\Lambda)}$ has mean $0.84/0.89/0.86$ at
$\Lambda=q'^{0.55}/q'^{0.65}/q'^{0.75}$ (max over samples $\le2.1$) —
square-root cancellation throughout the literature's
$(q'^{1/2},q'^{3/4}]$ window, comfortably stronger than the cited
power-saving bounds require.

Caveats: model scale compresses $\Lambda/Q$ ratios; no minor-$p$ filtering
(minor-ness is generic and T1 consumes the majors); $\lambda=1$ only
(wp8 probes covered $\lambda=3$ with identical behavior).

---

## 4. Verdict

**CITATION-ADJACENT** (confidence ~0.6 that the gap closes with known
technology; ~0.9 that no *new* hard-analysis input beyond a paper-scale
dispersion computation is needed for E3† specifically).

**Closest theorems (the citation chain).** The Kloosterman-sums-over-primes
family: **Bourgain 2005** (prime modulus, $N\ge q^{1/2+\varepsilon}$, power
saving), **R. C. Baker, *Kloosterman sums with prime variable*, Acta Arith.
156 (2012) 351–372** (modulus with squarefull part $\le q^{1/4}$ — includes
our squarefree $q_1q_2$ — $q^{1/2+\varepsilon}\le N\le q$, explicit power
saving $\eta=\varepsilon^4/2000$), **Korolev 2018/Thm 3** (arbitrary
composite, $N\ge q^{5/8+\varepsilon}$), **Korolev–Changa, Math. Notes 108
(2020)** (arbitrary modulus, $q^{1/2+\varepsilon}\le N\ll q^{3/2}$). These
cover Shape K-single — the inner sum of the completed off-diagonal — on the
**entire hard sub-range $\Lambda\in(Q^{1+\varepsilon},Q^{3/2}]$ with power
savings**, against a polylog need. The `wp8-e3.md` frontier placement
("Fouvry–Michel needs $\Lambda\ge Q^{3/2+\varepsilon}$") was priced against
the 1998 literature; the 2005–2020 prime-variable literature moves the
covered threshold from $q'^{3/4}$ down to $q'^{1/2+\varepsilon}$, i.e.
from $Q^{3/2}$ down to $Q^{1+\varepsilon}$.

**The adaptation needed (the actual remaining work).**
1. *The dispersion reduction* E3† → Shape K-single: carry out the
   `wp8-e3.md` §4 route-1 sketch in full (complete the $\nu_{\ell_i}\le R$
   windows mod $\ell_i$; Cauchy–Schwarz in $\ell$; open the $q$-square;
   absorb the $b(q)=-\bar q\bmod p$ nested layer into the pair-dependent
   numerator $n(q_1,q_2,h)$ — pointwise uniformity in $n$ is exactly what
   the cited theorems provide; control the $q_1=q_2$ diagonal and the
   completion-harmonic budget). Power room is available: inner savings are
   $q'^{-\eta}$, the need is $L^{2c+8}$, and C-S halves a power into a
   power. This is BFI-grade bookkeeping, not new mathematics — but the C†
   twin (`wp8-cdagger.md`) is the cautionary tale that bookkeeping can
   saturate; the structural difference here is that E3†'s budget has
   power-sized slack where C†-D3's was saturated *exactly*.
2. *The seam $\Lambda\in(Q,Q^{1+\varepsilon}]$*: below the
   $q'^{1/2+\varepsilon}$ threshold of the prime-variable theorems, above
   the complete-sum regime ($\Lambda\le Q$) where Weil per $\ell$ works.
   Options: (i) Korolev–Changa's bottom-of-range form (their range formally
   starts at $q'^{1/2+\varepsilon}$ — check the exact $\Delta$ in the
   paper: if the saving at $N=q'^{1/2}L^{O(1)}$ is
   $\exp(-c\sqrt{\log})$-type it beats any polylog and closes the seam from
   above); (ii) stretch the complete-sum/$q$-aspect treatment to
   $\Lambda\le Q^{1+\varepsilon}$ (completion loss $\ell^{1/2}/Q\le
   Q^{-1/2+\varepsilon'}$ — power room — but must verify the $b(q)$ layer
   admits the mod-$p\ell_1\ell_2$ completion there); (iii) note the seam is
   one dyadic block of $x^{\varepsilon}$-width needing only polylog saving.
   This seam is the *weakest link* of the chain and the first thing a
   future session should resolve.
3. *Uniformity audit*: the cited bounds are uniform in $(a,q')=1$ — needed
   because our numerators are pair-dependent; verify no hidden
   numerator-size restrictions (Korolev's statements are for all
   $(a,q)=1$; Baker's likewise per the survey).

**What remains NEW-MATHEMATICS (flagged, out of E3†'s scope).** The C†-pair
D3 sector and the C†-single deep-twist object (`wp8-cdagger.md`) do NOT
inherit this coverage: their inner variables carry *arbitrary*
divisor-bounded coefficients (no prime-variable structure), their budgets
are power-saturated (deficit $\ge x^{1/2}$), and their completion conductor
exceeds $x$. For the lower-bound track this is mooted if the $B=0$
subclass audit (`wp8-cdagger.md` lb-section) validates; for the
full-density theorem C† remains the genuinely open second front — bilinear
Kloosterman with arbitrary coefficients at super-$x$ conductors, for which
the missing technology is fairly named: a dispersion estimate beyond the
known $x^{3/5}$ moduli range for unbalanced convolutions (Wright 2026's
direction, but his $Q\le x^{1/2+1/66}$ is far below our $x^{2/3+}$).

**Recommended attack (next session, in order).**
1. Pull Korolev–Changa (Math. Notes 108:1 (2020) 87–93 / Mat. Zametki
   108:1, 39–48) and Baker (Acta Arith. 156 (2012)) PDFs; transcribe exact
   $\Delta$'s into `citations.md` (PINNED grade); decide seam option
   (i)/(ii)/(iii).
2. Write the dispersion-reduction lemma (E3† ⟸ K-single + complete-sum
   range) as a standalone manuscript section with explicit harmonic budget;
   adversarially audit against the four burned-accounting traps
   (`wp8-e3.md` §7).
3. If the budget closes: restate hyp:E3 in `11-typeII.tex` as PROVED-modulo
   -citations; if it saturates: fall back to E3-lb (variance form needs only
   the same inputs at constant density — Chebyshev room is free).
4. Independently: run the $B=0$ subclass audit to try to moot C† on the
   lower-bound track.

**Confidence summary.** Unified statement (§1): 0.9 (machine-checked
reductions upstream). Literature table (§2): 0.85 on ranges/shapes (slides
+ abstracts; two exact $\Delta$'s still to transcribe from paywalled PDFs).
Numerics (§3): high (clean, reproducible). Verdict CITATION-ADJACENT for
E3†: 0.6. C†-twin remains NEW-MATHEMATICS: 0.8.

---

## Sources (web, this session)

- DFI95: annals.math.princeton.edu/1995/141-2/p08 (Ann. Math. 141 (1995) 423–441)
- DFI97: link.springer.com/article/10.1007/s002220050135 (Invent. Math. 128 (1997) 23–43); preprint math.ucla.edu/~wdduke/preprints/bilinear.pdf
- Bettin–Chandee: arxiv.org/abs/1502.00769 (Adv. Math. 328 (2018) 1234–1262)
- Dong–Robles–Zeindler 2026: arxiv.org/abs/2601.00292
- Wright 2026: arxiv.org/abs/2604.25177
- Marklof–Welsh: people.maths.bris.ac.uk/~majm/bib/roots_pair_correlation.pdf
- Korolev survey slides (HKU 2018, full text extracted): hkumath.hku.hk/~imr/event/SRC/files/slides_Maxim_Korolev.pdf
- Fouvry–Michel: Ann. Sci. ENS 31 (1998) 93–130
- Baker: eudml.org/doc/278899 (Acta Arith. 156 (2012) 351–372)
- Korolev–Changa: link.springer.com/article/10.1134/S0001434620070081 (Math. Notes 108 (2020) 87–93)
- Korolev composite-moduli: arxiv.org/abs/1911.09981; RNT version link.springer.com/article/10.1007/s40993-020-00201-5
- Bourgain–Garaev: arxiv.org/abs/1211.4184
- Irving: arxiv.org/abs/1403.8031; Khan: arxiv.org/abs/1510.03377
