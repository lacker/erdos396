# DRAFT — UNVERIFIED AGENT ATTACK REPORT

## WP8: Hypothesis E3 (anatomy dispersion)

Date: 2026-06-10 (agent attack, WP8/E3).

**VERDICT: PARTIAL (major reduction proved).** (1) The structural reduction
to root sums is proved and machine-verified (§1). (2) **Theorem T1 (§3,
new, unconditional):** for every minor $p$, *pointwise* in $(q,\lambda)$,
the E3 aggregate over all $\langle\mu\rangle>L^{2c+6}$ plus all main terms
is $\ll RL^{-c-2}$ — via exact CF-spacing of $\{\theta_\mu\}$ + spaced large
sieve + the one-large-prime variance bound; no equidistribution, no
$q$-average, no Weil. (3) E3 is thereby reduced to **E3† (§4)**: a variance
(pair-correlation-of-roots) bound for *polylog-many* fixed small
frequencies with *polylog* target saving — the minimal irreducible core, at
the DFI/BFI frontier, confirmed numerically with square-root cancellation.
(4) The lower-bound track needs only a constant-density exceptional-set
form E3-lb (§5). Confidence: T1 ~0.85; reductions ~0.9; E3† open.

## 0. Setup and notation

Date: 2026-06-10. Sources read: `manuscript/sections/11-typeII.tex` (hyp:E3),
`09-anatomy.tex` (prop:one-large, prop:species), `06-reduction.tex`
(lem:linearization, prop:two-freq, theta_mu), `07-minor.tex` ((M1),(M2*),
thm:minor), `08-major.tex` (prop:digit-assembly budget), `04-architecture.tex`
(lower-bound track/trims), `wp8-e2.md` (house style).

Notation: $L=\log x$, $P=x^u$, $Q=x^{u'}$, $u,u'\in(1/3,1/2)$, $R=x^{1-u-u'}$,
$y=(2x)^{1/3}$, $A=x^{1-u}$, $a_0=(p^{-1}\bmod q)$ (least positive),
$a=a_0+qt$, $0\le t\le R$, $\theta_\mu=\mu q/p-\lambda p/q \pmod 1$,
$\langle\mu\rangle=\min(\mu,p-\mu)$. In-band facts: $u+u'>2/3$ so $R<x^{1/3}<y$;
$u+2u'>1$ so $q>\sqrt{x/p}$ (beyond-sqrt regime). E3 (hyp:E3, 11-typeII.tex):
uniformly in $0<|\lambda|\le L^C$,
$$\frac1{\pi(Q)}\sum_{q\sim Q}\sum_{p\sim P\,\mathrm{minor}}\sum_{0<\mu<p}
\frac1{\langle\mu\rangle}\Big|\sum_{t\le R}\mathbf 1[P^+(a_0+qt)>y]\,e(t\theta_\mu)\Big|
\ll \pi(P)\,R\,L^{-c-1}.$$

## 1. Verified structural reduction (inner sum = sum over roots nu_ell(q))

**Proposition S (reduction to root sums).** Fix band primes $p\ne q$,
$a_0=(p^{-1}\bmod q)\in[1,q)$. For every real $\theta$,
$$\Sigma(\theta):=\sum_{0\le t\le R}\mathbf 1\big[P^+(a_0+qt)>y\big]\,e(t\theta)
\;=\;\sum_{\substack{\ell\ \mathrm{prime},\ y<\ell\le A_{\max}\\ \nu_\ell\le R}}
e(\nu_\ell\,\theta),\qquad
\nu_\ell:=(-a_0\,\bar q)\bmod \ell\in[0,\ell),$$
where $\bar q q\equiv1\ (\ell)$ and $A_{\max}=a_0+qR\le x/p+q$. Each prime
$\ell\in(y,A_{\max}]$ contributes **at most one** $t$, namely $t=\nu_\ell$ when
$\nu_\ell\le R$, else nothing; distinct $t$ come from distinct $\ell$
(injectively: $t\mapsto$ its unique large prime factor).

*Proof.* (i) Every value $a=a_0+qt\le x/p+q<y^2$ for large $x$: indeed
$x/p\le x^{1-u}\le x^{2/3}<2^{2/3}x^{2/3}=y^2$, and $q=x^{u'}=o(y^2-x/p)$
when $u<1/3+$... — more carefully, $x/p+q\le x^{1-u}(1+o(1))$ and
$1-u<2/3$ strictly for $u>1/3$, so $a<y^2$ with room (at the corner $u=1/3$,
$a\le x^{2/3}+x^{1/2}<(2x)^{2/3}=y^2$ since $2^{2/3}>1+x^{-1/6}$). By
prop:one-large's argument, $a$ has at most one prime factor $>y$ counted with
multiplicity ($\ell_1\ell_2>y^2>a$). Hence
$\mathbf 1[P^+(a)>y]=\sum_{\ell>y,\ \ell\mid a}1$ exactly (the sum is 0 or 1).
(ii) Exchange sums: for fixed prime $\ell>y$, $\ell\ne q$: $\ell\mid a_0+qt$
iff $t\equiv-a_0\bar q\ (\ell)$. **Correction found by the probe:** in-band
$q=x^{u'}>x^{1/3}\sim y$, so $\ell=q$ *is* in the range $(y,A_{\max}]$; but
$(a_0,q)=1$ means $q\nmid a_0+qt$ always — the $\ell=q$ term is empty and the
RHS sum carries the (harmless, must-be-stated) restriction $\ell\ne q$.
The solutions $t\in[0,R]$ form
$t=\nu_\ell+s\ell$; but $\ell>y>R\ge t$ forces $s=0$: **at most one hit**,
present iff $\nu_\ell\le R$. (iii) Range of $\ell$: $\ell\mid a\le A_{\max}$
and $\ell>y$ requires $\ell\le A_{\max}$. $\square$

This is sharper than prop:species restricted to the band: the "small/medium
$\Lambda$" species of 09-anatomy.tex is **empty** in-band ($R<y$ kills all
$s\ge1$ terms), confirming the 11-typeII.tex diagnosis. E3 is exactly an
equidistribution statement for the Kloosterman-type roots
$\nu_\ell(q)\equiv-a_0(q)\,\bar q\ (\bmod\ \ell)$, $a_0(q)\equiv\bar p\ (q)$,
in the window $[0,R]$, $R/\ell\asymp x^{1-u-u'}/\Lambda$ — DFI territory,
**but with the q-average available**.

Counting note: $\#\{\ell: \nu_\ell\le R\}\approx\sum_{y<\ell\le x/p}
(R+1)/\ell\asymp R\log\frac{1-u}{1/3}/\log... \asymp R$ (Mertens over
$(y,x/p]$, $\log\log$-range $\log(3(1-u))\in(\log 1.5,\log 2)$): the root sum
has $\asymp R$ terms — same trivial size as $\Sigma$, nothing lost.

**Machine verification (probe A, `e3_probe.py`):** $x=2\cdot10^6$, corners
$(u,u')\in\{(0.34,0.34),(0.4,0.4),(0.34,0.48),(0.48,0.34)\}$, 15 random
$(p,q,\theta)$ each: LHS$=$RHS to $10^{-8}$, **0 mismatches / 60 trials**
(after adding the $\ell\ne q$ exclusion, which the probe itself caught via a
non-invertible $\bar q\bmod q$).

## 2. Attack log

1. **Prop S (structural reduction)**: proved + machine-checked (§1); found and
   fixed the $\ell\ne q$ subtlety ($q>y$ in-band, so $q$ lies in the
   $\ell$-range but never divides $a_0+qt$).
2. **Abel-summation route** ($\Sigma(\theta)=e(R\theta)N(R)-2\pi i\theta\int
   e(v\theta)N(v)dv$, then discrepancy of $N(v)$): FAILS structurally — it
   converts phase-weighted equidistribution into sup-norm discrepancy and
   loses a factor $1+\|\theta\|R$; since $\sup_v|N(v)-\mathrm{main}|\ge 1/2$
   whenever the window contains a root, the loss is fatal for
   $\|\theta_\mu\|\gg L^{O(1)}/R$. Abandoned.
3. **Phase discretization** (blocks of length $\Delta$ with
   $\Delta\|\theta\|$ small): fails for the same reason at
   $\|\theta\|\asymp1$ ($\Delta<1$). Abandoned.
4. **Cauchy–Schwarz in $t$** (drop the $t$-phase): gives
   $\sqrt{R\cdot V}\asymp R/\sqrt L$ per dyadic $\Lambda$-block — *worse than
   trivial* after recombining blocks; confirms the 11-typeII warning that a
   pure $L^2$ in $t$ fails (anatomy weight has variance $\asymp R$). Abandoned.
5. **WINNER for the $\mu$-aggregation (kills most of E3 unconditionally):**
   the $\mu$-dependence of $\theta_\mu=\mu q/p-\lambda p/q$ is a pure shift:
   $\theta_{\mu_1}-\theta_{\mu_2}=(\mu_1-\mu_2)q/p$ exactly (the $\lambda$-term
   cancels). So for $\mu$ in a block of consecutive integers the evaluation
   points are well-spaced by continued-fraction best approximation
   (lem:cf(1)), and the **spaced large sieve** (Montgomery–Vaughan) applies to
   the trig polynomial $E(\theta)=\sum_{t\le R}\epsilon_t e(t\theta)$,
   $\epsilon_t:=\mathbf 1[P^+(a_0+qt)>y]-\kappa'$, whose coefficient mass
   $V=\sum\epsilon_t^2\le R+1$ is controlled by the **one-large-prime
   injection** ($t\mapsto$ its unique $\ell$, so $\#\{t:\omega=1\}\le R+1$;
   in fact $V\approx\kappa'(1-\kappa')R$). (M2*) enters exactly once: to bound
   the spacing via $s^+\le sRL^{-B}$ at scales $M\le R$. Result: the whole
   range $\langle\mu\rangle>\mu_0:=L^{2c+6}$ is bounded **pointwise in
   $(p,q,\lambda)$** by $RL^{-c-2}$, for every minor $p$. Full proof in §3.
   No root equidistribution, no $q$-average, no Weil input needed.
6. **$h=0$/main term** (Angle 2): in the completion the $h=0$ coefficient is
   *exactly* $G(\theta)/\ell$, so the main term is $\kappa'G(\theta_\mu)$ with
   $\kappa'=\sum_\ell 1/\ell$ exact — its weighted $\mu$-aggregate is
   $\kappa'\times$(eq:minor-start object) and is consumed by cor:minor
   verbatim (minor $p$). No separate equidistribution estimate needed:
   Angle (2) is absorbed exactly. For small $\mu$, (M1) gives
   $\kappa'|G(\theta_\mu)|\le\langle\mu\rangle L^B$ — negligible.
7. **Residual core** = small frequencies only: $\langle\mu\rangle\le L^{2c+6}$
   (polylog many!), where the weight $1/\langle\mu\rangle$ defeats any
   $\mu$-average. Second moment in $q$ (dispersion): diagonal $=V\approx0.2R
   \ll(RL^{-c-3})^2$-compatible under the corner trim; everything reduces to
   the **off-diagonal pair correlation of roots** (§4). Attempted full
   dispersion: Fourier completion + reciprocity turns the phases into
   $e(h\,\overline{p\ell}_{(q)}/q)$ (Kloosterman fractions, modulus $q$,
   numerator $p\ell$) or, after C-S in $\ell$ and opening the $q$-square,
   into sums over primes $\ell$ of $e(n\overline{q_1q_2}/\ell)$ with
   pair-dependent numerators — pointwise Weil/Fouvry–Michel covers only
   $\Lambda\ge Q^{3/2+\varepsilon}$, which misses $[y,Q^{3/2}]$; the
   pair-dependent numerator blocks a clean DFI bilinear-fraction citation.
   The core is genuinely at the BFI/DFI frontier — but it is now *minimal*:
   polylog-many $\mu$, polylog target saving, all aggregations stripped.
   Precise statement E3† in §4; numerics in §6 confirm it holds with
   square-root cancellation at model scale.
8. Structural observation worth recording: the band condition $u+2u'>1$
   (the *beyond-sqrt obstruction* on the AP side) is **exactly** the
   condition $A=x^{1-u}<Q^2$ — on the root side it says every modulus
   $\ell$ is below $q^2$, i.e. the $q$-aspect completion is sub-quadratic.
   The same inequality that kills AP-side Cauchy–Schwarz makes the root-side
   dispersion geometry favorable.

## 3. Theorem T1: the $\mu$-tail of E3 is unconditional (pointwise, no
$q$-average) — complete proof

Fix band primes $p\ne q$, $0<|\lambda|\le L^C$, and suppose $p$ is **minor
for $(q,\lambda)$ at level $B$** ((M1)+(M2*), def:minor-conditions). Let
$\omega(a):=\mathbf 1[P^+(a)>y]$, $\kappa':=\sum_{y<\ell\le A_{\max},\,
\ell\ne q}1/\ell$ ($\le\log 2+o(1)<1$), $\epsilon_t:=\omega(a_0+qt)-\kappa'$,
$$E(\theta):=\sum_{0\le t\le R}\epsilon_t\,e(t\theta),\qquad
\Sigma(\theta)=E(\theta)+\kappa'G(\theta),\quad G(\theta)=\sum_{t\le R}e(t\theta).$$

**Theorem T1.** Let $\mu_0:=L^{2c+6}$ and assume $B\ge 2c+8$ and the corner
trim in the strengthened form $\sqrt R\ge L^{B/2+2c+8}$. Then, pointwise in
$(p,q,\lambda)$ with $p$ minor,
$$\sum_{0<\mu<p}\frac{|\Sigma(\theta_\mu)|}{\langle\mu\rangle}
\;\le\;\sum_{\langle\mu\rangle\le\mu_0}\frac{|E(\theta_\mu)|}{\langle\mu\rangle}
\;+\;O\!\big(R\,L^{-c-2}\big).$$
That is: **E3 holds unconditionally except for the polylog-many frequencies
$\langle\mu\rangle\le L^{2c+6}$.**

*Proof.*

(0) *Coefficient mass.* $\omega\in\{0,1\}$ and $0<\kappa'<1$ give
$|\epsilon_t|\le1$, so $V:=\sum_{t\le R}\epsilon_t^2\le R+1$. (Sharper,
unused: $\#\{t:\omega(a_0+qt)=1\}\le R+1$ by the injection $t\mapsto\ell$ of
Prop S, and $V\approx\kappa'(1-\kappa')R$.)

(1) *Main term.* $\sum_{0<\mu<p}\frac{\kappa'|G(\theta_\mu)|}{\langle\mu\rangle}
\le\kappa'\cdot\tfrac12\sum_\mu\frac{X_\mu}{\langle\mu\rangle}\cdot 2$ with
$X_\mu=\min(R,\tfrac1{2\|\theta_\mu\|})$ — exactly eq:minor-start. By
thm:minor + cor:minor (minor $p$): $\ll\sqrt R L^{B/2+4}+RL^{2-B}\ll
RL^{-c-2}$ under the trim and $B\ge c+4$. [Consumes the proved minor-arc
machinery verbatim; nothing new.]

(2) *Spacing of the evaluation points.* $\theta_{\mu_1}-\theta_{\mu_2}
=(\mu_1-\mu_2)\,q/p \pmod 1$ — the $\lambda p/q$ part cancels identically.
Write $\alpha=q/p$ (lowest terms, $(p,q)=1$), convergent denominators $s$
with successors $s^+$. Best approximation (lem:cf(1), proved in 07-minor):
for $0<k<s^+$, $\|k\alpha\|\ge\|s\alpha\|\ge\frac1{s+s^+}\ge\frac1{2s^+}$.
Hence: **any set of at most $W$ consecutive $\mu$, $W\le s^+$, has its
$\theta_\mu$ pairwise $\frac1{2s^+}$-spaced mod 1.**

(3) *Large sieve.* (Montgomery–Vaughan) For $\delta$-spaced points $x_j$ and
$S(x)=\sum_{t=0}^{R}\epsilon_te(tx)$:
$\sum_j|S(x_j)|^2\le(R+\delta^{-1})\,V$.

(4) *Regime I: dyadic $M$ with $\mu_0\le M\le R$.* The $\mu$ with
$\langle\mu\rangle\in(M,2M]$ form two intervals $I$ of $\le M$ consecutive
integers; weight $\le1/M$. Let $s$ = largest convergent denominator $\le M$;
maximality gives $s^+>M$, so $I$ is one window in the sense of (2) with
$\delta=\frac1{2s^+}$. By (M2*) ($s\le M\le R$): $s^+\le sRL^{-B}\le MRL^{-B}$.
Cauchy–Schwarz + (3):
$$\sum_{\mu\in I}\frac{|E(\theta_\mu)|}{\langle\mu\rangle}
\le\frac{\sqrt{|I|}}{M}\Big(\sum_{\mu\in I}|E|^2\Big)^{1/2}
\le M^{-1/2}\big[(R+1+2MRL^{-B})V\big]^{1/2}
\le\sqrt{\tfrac{2RV}{M}}+\sqrt{2RVL^{-B}}.$$
Summing dyadic $M\in[\mu_0,R]$ (the first piece is geometric, dominated by
$M=\mu_0$; the second occurs $\le 3L$ times, $\times2$ intervals):
$$\mathrm{(Regime\ I)}\;\ll\;\sqrt{\frac{RV}{\mu_0}}+L\sqrt{RVL^{-B}}
\;\le\;R\sqrt{\tfrac{2}{\mu_0}}+\sqrt2\,R\,L^{1-B/2}
\;\ll\;R\big(L^{-c-3}+L^{-c-3}\big)$$
using $V\le R+1$, $\mu_0=L^{2c+6}$, $B\ge2c+8$.

(5) *Regime II: dyadic $M$ with $R<M<p$.* Let $s_0$ = largest convergent
denominator $\le R$; maximality forces $s_0^+>R$ (so $s_0^+\ge R+1$), and
(M2*) gives $s_0^+\le s_0RL^{-B}\le R^2L^{-B}$. Split each interval $I$
($|I|\le M$) into $\le M/W+1\le 2M/W$ windows of $W:=\min(M,s_0^+)$
consecutive $\mu$; each window is $\frac1{2s_0^+}$-spaced by (2). Large sieve
per window + Cauchy–Schwarz:
$$\sum_{\mu\in I}\frac{|E|}{\langle\mu\rangle}
\le M^{-1/2}\Big[\tfrac{2M}{W}(R+1+2s_0^+)V\Big]^{1/2}
=\Big[\tfrac{2}{W}(R+1+2s_0^+)V\Big]^{1/2}.$$
If $s_0^+\ge M$: $W=M>R$ and $\frac{2}{M}(R+1+2s_0^+)\le 2+\tfrac2M
+4RL^{-B}\le 4+4RL^{-B}$ (using $s_0^+\le R^2L^{-B}$, $M>R$); bound
$\le 2\sqrt{V}+2\sqrt{RVL^{-B}}\le 2\sqrt{2R}+2\sqrt2 RL^{-B/2}$.
If $s_0^+<M$: $W=s_0^+\ge R+1$ and $\frac{2}{s_0^+}(R+1+2s_0^+)\le2+4=6$;
bound $\le\sqrt{6V}\le\sqrt{12 R}$.
Either way each dyadic block contributes $O(\sqrt R+RL^{-B/2})$; over
$\le 3L$ blocks: $\mathrm{(Regime\ II)}\ll L\sqrt R+RL^{1-B/2}\ll RL^{-c-3}$
under the corner trim ($\sqrt R\ge L^{B/2+2c+8}\ge L^{c+5}$) and $B\ge2c+8$.

(6) Collecting (1)+(4)+(5) proves T1. $\square$

**Inputs audit (adversarial).** (M1): only in step (1) via cor:minor and in
§4 below for the small-$\mu$ main term. (M2*): only in steps (4),(5) via
$s^+\le sRL^{-B}$ for $s\le R$. Corner trim: strengthened to
$\sqrt R\ge L^{B/2+2c+8}$ (still polylog, same $O(\eta'')$ density cost;
needed again in §4). Band geometry: none — no use of $R<p$, no use of
$u+2u'>1$; T1 degrades gracefully at all corners. Primality of $\ell$, roots
$\nu_\ell$, Weil, DFI: **not used**. The only arithmetic inputs are the
one-large-prime structure (via $|\epsilon_t|\le1$ — even that is just
boundedness) and the CF spacing of $\{\mu q/p\}$.

**Remark (why this works where AP-side Cauchy–Schwarz could not).** The
beyond-sqrt diagnosis concerned recovery of the $1/q$ density inside a
length-$R$ progression with modulus $q>\sqrt{A}$. T1 never touches that: it
compares the decorated sum to $\kappa'\times$(geometric sum) and pays only
the *variance* of the decoration, $V\asymp R$, against the large-sieve
spacing $\asymp$ the (M2*)-certified CF geometry of $q/p$. The saving comes
from the $1/\langle\mu\rangle$ weight (mass $\log$) meeting square-root
cancellation on $\mu$-average (Parseval), not from progression densities.

## 4. The residual core E3† (small frequencies), and its dispersion shape

**Small-$\mu$ main term.** For $\langle\mu\rangle\le\mu_0$, (M1) gives
$\|\theta_\mu\|\ge\frac{1}{2\langle\mu\rangle L^B}$, so
$\kappa'|G(\theta_\mu)|\le\langle\mu\rangle L^B$ and
$\sum_{\langle\mu\rangle\le\mu_0}\frac{\kappa'|G|}{\langle\mu\rangle}
\le2\mu_0L^B=2L^{B+2c+6}\ll RL^{-c-2}$ under the strengthened corner trim
($R\ge L^{B+4c+16}$). Hence on the core range $|E(\theta_\mu)|$ may be
replaced by $|\Sigma(\theta_\mu)|=|\sum_{\ell:\nu_\ell\le R}e(\nu_\ell
\theta_\mu)|$ and vice versa, freely.

**Definition (Hypothesis E3†).** For each fixed $0<|\lambda|\le L^C$ and each
fixed $\mu$ with $0<\langle\mu\rangle\le L^{2c+6}$:
$$\frac{1}{\pi(P)\pi(Q)}\sum_{q\sim Q}\sum_{\substack{p\sim P\\ p\ \mathrm{minor}}}
\Big|\sum_{\substack{y<\ell\le A_{\max},\ \ell\ne q\\ \nu_\ell(p,q)\le R}}
e\big(\nu_\ell(p,q)\,\theta_\mu\big)\Big|^2\;\ll\;R^2\,L^{-2c-8}.$$

**Proposition P2 (reduction).** T1 + E3† $\Rightarrow$ E3 (with the
strengthened corner trim and $B\ge2c+8$). *Proof.* By T1 it remains to bound
$\mathbb E_{p,q}\sum_{\langle\mu\rangle\le\mu_0}\frac{|E(\theta_\mu)|}
{\langle\mu\rangle}$. Swap sums; for each fixed $\mu$, Cauchy–Schwarz over
$(p,q)$ and E3† (plus the main-term swap above) give
$\mathbb E_{p,q}|E(\theta_\mu)|\le(\mathbb E_{p,q}|E|^2)^{1/2}\ll RL^{-c-4}$;
then $\sum_{\langle\mu\rangle\le\mu_0}\frac1{\langle\mu\rangle}\cdot RL^{-c-4}
\le 5\log\mu_0\cdot RL^{-c-4}\ll RL^{-c-2}$. $\square$
(Note: only the $L^2$-in-$(p,q)$ version is needed; an $L^1$ version with the
same saving also suffices.)

**Diagonal accounting (why E3† is exactly the off-diagonal).** Expanding
$|E|^2=\sum_{t_1,t_2}$: the diagonal $t_1=t_2$ contributes
$\mathbb E_{p,q}V\le R+1\ll R^2L^{-2c-8}$ under the corner trim. In the root
form $|\sum_\ell e(\nu_\ell\theta)|^2$: the diagonal $\ell_1=\ell_2$ is the
count $\approx\kappa'R$, same conclusion. So E3† asserts precisely: **the
pair correlation of distinct roots, with phase, saves $L^{2c+8}$ over
trivial on $(p,q)$-average**; square-root cancellation (what the WP1.5/2.4
empirics show, and §6 confirms for these exact objects) would give
$\mathbb E|E|^2\approx V\approx0.2R$ — beating the requirement by a power
of $x$ (margin $R/L^{O(1)}$ vs needed $R^2L^{-2c-8}$: requirement is
**$R\,L^{2c+8}\ll R^2$**, pure polylog).

**Arithmetic shape of the off-diagonal.** With $pa_0=1+bq$, $b=b(q)=
(-\bar q\bmod p)$, and $\ell\ne p$ (the $\ell=p$ terms: $\le1$ value of $t$,
contribute $O(1)$, negligible):
$$\nu_{\ell}\le R\ \text{with}\ t=\nu_\ell\iff q\,(b(q)+pt)\equiv-1\ (\mathrm{mod}\ \ell),\ t\le R.$$
The off-diagonal of E3† is therefore (after expanding the two windows by
additive characters mod $\ell_1,\ell_2$ and pulling out $h_i=0$):
correlation sums over primes $q\sim Q$ of
$$e\Big(\Delta t\big(\tfrac{\mu q}{p}-\tfrac{\lambda p}{q}\big)\Big)\,
e\Big(\tfrac{h_1\,\overline{q(b+pt_1)}}{\ell_1}+\tfrac{h_2\,\overline{q(b+pt_2)}}{\ell_2}\Big)
\quad(\ell_1\ne\ell_2\sim\Lambda,\ t_i\le R),$$
i.e. joint equidistribution of $\big(q,\ \bar q\bmod p\big)$ against moduli
$\ell_1\ell_2\le A^2<Q^4$ — Kloosterman-fraction species with **three**
inverse layers ($\bar q\bmod p$ inside inverses mod $\ell_i$). Pointwise in
$(\ell_1,\ell_2)$ this is hopeless (effective modulus $p\ell_1\ell_2\ge
x^{u+2/3}\gg Q$); the $(\ell_1,\ell_2,t_1,t_2)$-averages must be kept.
Routes, with the obstruction each hits:
- *C-S in $\ell$, open the $q$-square* (prompt Angle 1): inner object
  $\sum_{\ell\sim\Lambda\ \mathrm{prime}}e(n(q_1,q_2,h)\,\overline{q_1q_2}/\ell)$
  — prime-variable Kloosterman fractions, numerator depending on the
  $(q_1,q_2)$ pair. Reciprocity converts to $e(-n\bar\ell_{(q_1q_2)}/q_1q_2)$
  + smooth; Weil-completion handles an *integer* $\ell$-variable for
  $\Lambda\ge(Q^2)^{1/2+\varepsilon}$, and Fouvry–Michel-type prime-variable
  bounds need $\Lambda\ge Q^{3/2+\varepsilon}$: the sub-range
  $\Lambda\in(y,Q^{3/2}]$ (nonempty everywhere in-band) survives. The
  pair-dependent numerator blocks DFI/Bettin–Chandee bilinear-fraction
  theorems as black boxes. **Partial coverage only.**
- *Dispersion à la BFI with the $p$-average kept* (the core has both $p$- and
  $q$-averages): in the reparametrization $n=pa$, the condition set is
  $n\equiv1\ (q)$, $p\mid n$, $\ell_1\mid n/p$, $\ell_2\mid n/p+q\Delta t$ —
  a shifted-divisor correlation to moduli $q\sim x^{u'}\le x^{1/2}$ on
  average: Titchmarsh-divisor/BFI homeland, plausibly provable with current
  technology (the needed saving is polylog, the moduli are below $x^{1/2}$,
  and the weight at $\ell_2$ is a genuine average), but it is a paper-scale
  dispersion computation, not completed here.
- In-band geometry helps: $u+2u'>1\iff A<Q^2$ — every root modulus is below
  $q^2$ (§2 item 8), so the $q$-aspect completions are sub-quadratic
  everywhere; and $\Lambda\le Q$ (true for $\Lambda\le x^{u'}$, a nonempty
  initial segment of the range since $u'>1/3$) makes the $q$-interval longer
  than the modulus — complete-sum regime, where Weil per $\ell$ does give
  power saving. **The hard sub-range is $\Lambda\in(Q,\,Q^{3/2}]$.**

## 5. Weakest E3-variant sufficient for the lower-bound track (Theorem 1')

The lower-bound track tolerates (04-architecture trim registry; 08-major:
"worst-case-per-$q$ versions suffice"): (i) discarding any set of $q\sim Q$
of small *constant* density $\delta_0$ (main-term loss $O(\delta_0)$ inside
the Buchstab/positivity sandwich — lemma-0-sandwich); (ii) restricting to a
positive-measure sub-band of $(u,u')$; (iii) restricting to one
positive-proportion anatomy subclass.

Since **T1 is pointwise in $(p,q)$** — for minor $p$ the entire
$\langle\mu\rangle>\mu_0$ range and the main terms are unconditional — the
only $q$-sensitive object left is the small-$\mu$ core. Chebyshev then
yields the weakest sufficient variant:

**Hypothesis E3-lb (exceptional-set form).** There is $\delta_0>0$ (a small
absolute constant) such that for each $0<|\lambda|\le L^C$,
$$\#\Big\{q\sim Q:\ \sum_{\substack{p\sim P\ \mathrm{minor}}}\
\max_{\langle\mu\rangle\le L^{2c+6}}\big|E_{p,q}(\theta_\mu)\big|
\;>\;\pi(P)\,R\,L^{-c-4}\Big\}\;\le\;\delta_0\,\pi(Q).$$

**Proposition P3.** T1 + E3-lb suffice for the anatomy layer of the
lower-bound track: on the good $q$-set (density $\ge1-\delta_0$), the full
E3 bound holds *pointwise in $q$* — the core $\mu$-sum is bounded by
$\sum_{\langle\mu\rangle\le\mu_0}\frac1{\langle\mu\rangle}\cdot
\max_{\mathrm{core}}|E|\le5\log\mu_0\cdot\pi(P)RL^{-c-4}\ll\pi(P)RL^{-c-2}$,
and T1 covers the rest; the bad $q$ are discarded into the
sandwich's $O(\delta_0)$ main-term loss, exactly as the Family-A/B major-$q$
exceptional sets are. No $q$-average of errors is ever needed — only the
**measure** of the bad set.

Two strictly weaker sufficient inputs, in decreasing strength:
1. **Variance form** (implies E3-lb by Chebyshev + Markov over $p$):
   $\mathbb E_{p,q}|E(\theta_\mu)|^2\le\delta_0^2L^{-2c-10}R^2/L^{2}$ per
   core $\mu$ — i.e. E3† with constants; still off-diagonal pair
   correlation, but **only an upper bound on a variance**, no asymptotic,
   no main-term evaluation.
2. **Positive-proportion form**: it even suffices that a *fixed positive
   proportion* $1-\delta_0$ of pairs $(p,q)$ (jointly) satisfy
   $\max_{\mathrm{core}\ \mu}|E(\theta_\mu)|\le RL^{-c-4}$, restricting if
   necessary to a sub-band of $(u,u')$ where this holds: the sandwich only
   needs one positive-measure cell. This is far below what any
   equidistribution heuristic predicts (truth $\approx\sqrt R$ for *all but
   power-few* pairs).

Diagnosis: the upper-bound track (Theorem 1) needs E3† (full polylog-saving
variance); the lower-bound track needs only E3-lb / its variance form —
**a constant-density exceptional-set bound for polylog-many fixed
frequencies**. This is the precise gap left open by this WP.

## 6. Numerics (`.venv/bin/python e3_probe.py`, `e3_probe2.py`)

**(N1) Prop S exact identity.** $x=2\cdot10^6$, four band corners, 15 random
$(p,q,\theta)$ each: **0 mismatches / 60** to $10^{-8}$ (§1). The probe
caught the $\ell\ne q$ exclusion.

**(N2) Full $\mu$-aggregate decomposition** (FFT over all $0<\mu<p$;
$x=2\cdot10^6$ at $(0.36,0.36)$ and $x=2\cdot10^7$ at $(0.34,0.45)$,
$(0.45,0.34)$; $\lambda=1$): writing total $=$ main($\kappa'G$) $+$
core($\langle\mu\rangle\le12$) $+$ tail, observed (13 pairs):
- tail $\approx(0.12\text{–}0.27)\cdot\sqrt R\,\log x$ — square-root scale
  with small constant, uniformly across geometries (vs trivial
  $\approx 2R\log p$: the tail mechanism saves the predicted factor);
- main and core are each comparable to the tail at toy scale (where
  $L^{-c}$ separations are meaningless) — the split is structural, not yet
  asymptotic, at $R\le40$.

**(N3) Core variance E3† at model scale** ($x=2\cdot10^6$ and $2\cdot10^7$,
three geometries, $\lambda\in\{1,3\}$, $\mu\in\{1,2,3,5,10\}$, 30–60 $q$ per
cell, 10 $p$): the dispersion ratio
$\mathbb E_q|E(\theta_\mu)|^2\,/\,V$ (off-diagonal-to-diagonal; $1.0$ =
perfect square-root cancellation) came out
**$0.71$–$1.40$, median-of-medians $\approx0.75$**, with per-$q$ maxima
$\le6.4$ — no off-diagonal accumulation at any small $\mu$, any geometry,
either $\lambda$. E3† needs ratio $\ll R/L^{2c+8}$; observed $O(1)$.
Also $V\approx\kappa'(1-\kappa')R$ as predicted ($V/R\approx0.21$–$0.26$).

**(N4) Corner exponent arithmetic.** Verified numerically at
$(1/3,1/3),(0.4,0.4),(1/3,1/2),(1/2,1/3)$: in-band facts $u+u'>2/3$ ($R<y$),
$u+2u'>1$ ($A<Q^2$), $2u+u'>1$ ($R<P$), $u+u'<1$, $1-u>1/3$
($\Lambda$-range nonempty) — all strict except at $(1/3,1/3)$ where the
first three are exact equalities (margins $0.0$): consistent with the open
band; T1 itself uses none of them (only the corner trim on $R$), so nothing
in this WP degrades at that corner. Prop S's $a<y^2$ at $u=1/3$ holds via
the explicit constant $2^{2/3}$ ($a\le x^{2/3}+2Q<2^{2/3}x^{2/3}$).

## 7. Obstructions (and how each was resolved or localized)

1. *$\ell=q$ in the root range* (since $q>y$ in-band): resolved — the term is
   empty by $(a_0,q)=1$; must be stated in Prop S.
2. *Phase-vs-discrepancy loss* ($1+\|\theta\|R$ factor in Abel/discretization
   routes): unresolvable head-on; routed around by keeping the phase inside
   the large sieve (T1).
3. *Pure $L^2$ in $t$* loses (variance $\asymp R$): confirmed; routed around
   — the $L^2$ is taken over $\mu$ (where Parseval is exact) instead.
4. *Cauchy–Schwarz $\mu$-tail with flat Parseval fails* ($p\gg R$ makes the
   full-range $L^2$ mass $pV$ too big): resolved by the **spaced** large
   sieve per dyadic block + (M2*) — this is where minor-ness earns its keep
   a second time.
5. *Large-$M$ spacing beyond $R$* (no (M2*) control of $s_0^{++}$ etc.):
   resolved by windows of length $\min(M,s_0^+)$ and the automatic
   $s_0^+>R$ (maximality), giving $O(\sqrt R)$ per block with no hypothesis.
6. *The small-$\mu$ core*: NOT resolved — reduced to E3† (§4): pair
   correlation of roots $\nu_{\ell_1},\nu_{\ell_2}$ on $(p,q)$-average,
   needing only $L^{2c+8}$ saving. Completion+reciprocity produces
   Kloosterman fractions with pair-dependent numerators (blocks DFI/BC
   citation); pointwise Weil/Fouvry–Michel covers only
   $\Lambda\gtrsim Q^{3/2}$; the BFI-style dispersion with the $p$-average
   (shifted-divisor form, moduli $q\le x^{1/2}$) is the plausible route but
   is a paper-scale computation. The four burned-accounting traps were
   checked: no per-pair rare-event counting is attempted anywhere; all
   trivial-bound comparisons are done per dyadic block with explicit
   constants.
7. *Bookkeeping deltas vs the manuscript*: T1 needs $B\ge2c+8$ (vs
   prop:digit-assembly's $B=C+c+4$; take $B=\max(C+c+4,2c+8)$ — all
   downstream uses want $B$ large, Family counts improve with $B$) and the
   corner trim strengthened to $\sqrt R\ge L^{B/2+2c+8}$ (same $O(\eta'')$
   cost). Boundary $\ell$-range wobble ($A_{\max}$ depends on $q$): immaterial
   for T1 (full range used); for E3†'s dispersion, fix $\ell\le x/p-2Q$ and
   count the boundary by $q\mid p\ell m-1$ divisor-bounds — $O(1)$ per
   $(p,\mu)$ on $q$-average.

## 8. Verdict + confidence

**PARTIAL — major unconditional reduction, core isolated, not closed.**

Proved here (modulo independent re-derivation of constants):
- **Prop S** (machine-checked): the E3 inner sum is exactly a sum over
  roots $\nu_\ell=-a_0\bar q\bmod\ell$ of primes $\ell\in(y,A_{\max}]$,
  $\ell\ne q$, in the window $[0,R]$.
- **Theorem T1**: for every minor $p$, pointwise in $(q,\lambda)$, the whole
  of E3 except the frequencies $\langle\mu\rangle\le L^{2c+6}$ —
  unconditionally (spaced large sieve + (M2*) + one-large-prime variance;
  no equidistribution, no Weil, no $q$-average). Confidence in T1: ~0.85
  (the CF-spacing/large-sieve steps are standard; the dyadic bookkeeping
  was self-checked twice; constants should be re-derived).
- **P2/P3**: E3 $\Leftarrow$ T1 + E3† (variance of polylog-many fixed small
  frequencies); lower-bound track $\Leftarrow$ T1 + E3-lb
  (constant-density exceptional-set form). Confidence: ~0.9.
- Angle (2) (h=0 main term) closes exactly; no separate estimate needed.

Open: **E3†** — off-diagonal pair correlation of roots at polylog-many
small $\mu$, polylog saving, on $(p,q)$-average. DFI/BFI frontier; numerics
show it holds with square-root cancellation (ratio $\approx1$) at model
scale. This is now the *entire* content of Hypothesis E3.

Suggested manuscript edits: restate hyp:E3 as E3† (small-$\mu$ variance
form) + cite T1; record the structural remark $u+2u'>1\iff A<Q^2$; bump
$B$ and the corner trim as in §7.7.
