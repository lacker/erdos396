# Reading session: Pilatte + Tao–Teräväinen vs. Lemmas B and D

Sources read: Pilatte, *Improved bounds for the two-point logarithmic Chowla
conjecture*, arXiv:2310.19357 (v2, Dec 2025) — §§1–3 in full detail, proof
architecture of the rest; Tao–Teräväinen, *Quantitative correlations and some
problems on prime factors of consecutive integers*, arXiv:2512.01739 — §1
complete (including the displayed shape of the general estimate and Theorem
1.7 verbatim), §2 partially, §3 (the precise Theorem 3.1) **not yet retrieved**;
Tao's blog exposition (Dec 1, 2025). Items below are tagged **[V]** verified
from the text or **[I]** inferred from §1, to be confirmed against §3.

---

## 1. The two engines, precisely

### 1.1 Pilatte (arXiv:2310.19357) **[V throughout]**

**Theorem 1.1.** $\sum_{n\le x}\frac1n\lambda(n)\lambda(n+1)\ll(\log x)^{1-c}$
for an absolute $c>0$ (trivial bound $\log x$; author: "appears to be best
possible with current methods").

**Setup.** $\varepsilon_1$ small; $H$ large; $H_0=\exp((\log H)^{1-\varepsilon_1})$;
$J\le\varepsilon_1^2\log\log H$; disjoint prime sets
$\mathcal P_1,\dots,\mathcal P_J\subset(H_0,H)$ in geometric bands;
$V_j=\sum_{p\in\mathcal P_j}1/p\asymp\varepsilon_1\log\log H/(2J)$;
$\mathcal D=\{p_1\cdots p_J\}$; $x=\exp((\log H)^6)$.

**Theorem 2.4 (core estimate).** For $\log N\ge(\log H)^{2.001}$:
$$\sum_{(p_1,\dots,p_J)\in\mathcal P_1\times\cdots\times\mathcal P_J}\ \ 
\sum_{\substack{n\in(N,2N]\\ p_1\cdots p_J\mid n}}\lambda(n)\lambda(n+p_1\cdots p_J)
\ \le\ e^{O(J)}(V_1\cdots V_J)^{1/2}N,$$
an exponential improvement over the trivial $V^JN$ once $J\asymp\log\log H$.
**Remark 2.6:** the version with absolute values (arbitrary signs
$c_{p_1,\dots,p_J}\in\{\pm1\}$) holds by the same proof.

**Where multiplicativity lives (author's own localization).** *"The complete
multiplicativity of $\lambda$ is only used in Proposition 3.1 and in the proof
that Theorem 2.4 implies Theorem 1.1. The only other property of $\lambda$ we
use is that it is 1-bounded."* Concretely:
- **Tao's dilation** (2.4 ⟹ 1.1): $\lambda(n)\lambda(n+1)=\lambda(dn)\lambda(dn+d)$
  for every $d\in\mathcal D$ — this *manufactures* the divisibility structure
  $d\mid m$ inside the shift-1 correlation. Needs exact multiplicative
  covariance.
- **Centring** (Prop 3.1, $\mathbf 1_{p\mid n}\to\mathbf 1_{p\mid n}-\tfrac1p$):
  proved in Appendix C by the circle method, *crucially relying on an
  exponential-sum estimate of Matomäki–Radziwiłł–Tao* — a multiplicative-
  functions input.
- **Spectral engine** (Prop 3.4 and §§4–13): for the matrix $A$ with entries
  $\prod_{p\mid d}(\mathbf 1_{p\mid n}-\tfrac1p)$ at $|m-n|=d\in\mathcal D$,
  there is $X\subseteq I_N$ with $|I_N\setminus X|\ll e^{-JV/3}N$ such that
  every eigenvalue of $A|_X$ is $\le e^{O(J)}V^{J/2}$ in absolute value
  (non-backtracking operators, Ihara–Bass, high-trace). **Uses only
  1-boundedness** — i.e. $f^\top (A|_X)\,g\le e^{O(J)}V^{J/2}N$ for *arbitrary*
  1-bounded vectors $f,g$, multiplicative or not.

**Remark 2.8.** Almost-all-scales corollary:
$\frac1x\sum_{n\le x}\lambda(n)\lambda(n+1)\ll(\log X)^{-c/2}$ for all
$x\in[1,X]$ outside a set of logarithmic density $O((\log X)^{-c/2})$.

### 1.2 Tao–Teräväinen (arXiv:2512.01739)

**General estimate — displayed shape (§1.3) [V as a display; precise Thm 3.1 unread]:**
$$\frac WN\sum_{N<n\le2N}\bigl(g_1(n+h_1)-\delta_N\bigr)\,g_2(n+h_2)\,
\mathbf 1_{n\equiv b\ (W)}\ \ll\ \mathcal L^{-c}$$
for **all scales $N$ outside a small exceptional set**, where: $g_1,g_2$ are
1-bounded multiplicative; $h_1\ne h_2$ are integer shifts; $\delta_N$ is an
approximation to the mean of $g_1$ on $[N,2N]$; $W,b\le\mathcal L^{c}$;
$1\le\mathcal L\ll\log N$; and **the hypothesis falls on $g_1$ only**: $g_1$
is either *real-valued and "equidistributed"* (roughly the same mean on all
residue classes of small modulus) or *complex-valued and "non-pretentious"*
(far from every $\chi(n)n^{it}$ in the distance $M(g;X,Q)$ of (1.16)–(1.17)),
with $\mathcal L$ quantifying "roughly"/"close". Derived "by using Pilatte's
method in Section 3"; per the blog, Pilatte's $O(\log^{-c})$ strength is
essential (earlier estimates "too weak").

**Theorem 1.7 (Consecutive smooth numbers) [V verbatim]:** there is
$\mathcal X\subset\mathbb N$ with
$\frac1{\log X}\sum_{n\in[1,X]\setminus\mathcal X}\frac1n\ll\log^{-c}X$
(so $\mathcal X$ has logarithmic density 1) such that for every
$x\in\mathcal X$ and **all** $u,v\ge1$:
$$\frac1x\sum_{n\le x}\mathbf 1_{n\ x^{1/u}\text{-smooth}}\,
\mathbf 1_{n+1\ x^{1/v}\text{-smooth}}=\rho(u)\rho(v)+O(\log^{-c}x),$$
uniformly for $u,v\in[1,\,c\log_2x/\log_3x]$ — strengthening [T18, Thm 1.14]
(fixed $u,v$) to a *uniform, quantitative, almost-all-scales asymptotic*.

**Theorem 1.6 pipeline [V]:** the EPS asymptotic for
$\#\{n\le x:\omega(n)=\omega(n+1)\}$ at almost all scales is proved by circle
method on $\frac1x\sum e(\alpha\omega(n+1))e(-\alpha\omega(n))$ — the frequency
objects $e(\alpha\omega(n))$ are **multiplicative because $\omega$ is
additive** — with Pilatte handling minor arcs and major arcs converted back to
physical space and estimated by sieves. Stated frontier: *"pairwise
correlation technology either requires logarithmic averaging, or is restricted
to almost all scales rather than all scales."*

---

## 2. Lemma B: hypotheses checklist — VERDICT: citable-in-principle

Our objects: the $z$-trick functions
$g_z(n)=\prod_{p^a\|n}z^{\#\{\text{band-}\beta\text{ prime}\}}
\mathbf 1_{p\notin\beta'}$, with $g_z\equiv1$ on all prime powers with
$p\le x^\delta$; band-anatomy box indicators are finite $\pm$-combinations of
finitely many $g_z$.

| Theorem-3.1 hypothesis (shape from §1) | our $g_z$ | status |
|---|---|---|
| 1-bounded | values in $[0,1]$ | ✓ |
| multiplicative | by construction (defined on prime powers) | ✓ |
| real-valued (⇒ equidistributed branch) | yes | ✓ |
| "equidistributed": same mean on classes mod $W\le\mathcal L^c$ | $g_z\equiv1$ below $x^\delta$, $W$ supported on tiny primes ⇒ class means agree up to negligible error | **Lemma B0 to write** (half page, standard) |
| $x$-dependent parameters (band edges $x^a$) | identical feature to the threshold $x^{1/u}$ in Thm 1.7, where uniformity up to $u\le c\log_2x/\log_3x$ is *part of the statement*; we need a fixed compact $u$-range only | ✓ by analogy; **[C3]** confirm scope in §3 |
| shifts | we need $(h_1,h_2)\in\{(0,-1),(1,0)\}$: "distinct integer shifts" | ✓ |
| $W$-trick | take $W=1$ (or small $W$ as a wheel, harmless) | ✓ |
| conclusion form | $g_1$ centred against $g_2$ *uncentred* ⇒ $\sum g_1(n)g_2(n-1)=\delta_N\sum g_2(n-1)+O(N\mathcal L^{-c})$; combine with a one-variable mean-value computation for $g_2$ (classical; FK-style) ⇒ product-of-means asymptotic | ✓ structurally; **[C2]** confirm asymmetry ($g_2$ unconditioned beyond 1-bdd mult) |
| error budget | $\mathcal L^{-c}$ savings, $\mathcal L$ up to $\log N$; we apply it $O(1)$ times ($z$-interpolation) and take $\delta\to0$ after $x\to\infty$ | ✓ ample |
| averaging mode | almost all scales, exceptional log-density $\ll\log^{-c}$ | ✓ — exactly Theorem 1″'s mode |

**Two structural points that make this nearly mechanical.**
1. Smoothness/band indicators **are** multiplicative functions — our $g_z$ are
   literally in the theorem's class, not a generalization of it. Thm 1.7 *is*
   the anatomy prototype, and its proof (§3.7, "Application to smooth numbers")
   is the template to mimic if citing 3.1 directly ever pinches.
2. Equivalently, in Pilatte's own decomposition: Tao's dilation step **works**
   for the anatomy layer — for $d\in\mathcal D$ (primes $\le H=x^{o(1)}\ll
   x^\delta$), the multiset of prime factors $>x^\delta$ of $dn$ equals that of
   $n$, so $A(dn)=A(n)$ and $A(d(n+1))=A(n+1)$ *exactly*. The anatomy layer
   sits wholly inside the multiplicative world.

**Status change: Lemma B [N, plausible via T18] → [KA⁻]** — citable modulo the
named verification items **B0** (equidistribution lemma for $g_z$, to write),
**C1** (exact quantified definition of "equidistributed" in Thm 3.1), **C2**
(asymmetry), **C3** (uniformity scope). All verification-grade, none
research-grade. Quantitative backstop if any item fails: mimic §3.7 directly.

---

## 3. Lemma D: verdict — black-box NO, with mechanisms; hardness reclassified

**The technology boundary passes exactly between Lemma B and Lemma D.** What
breaks, blocker by blocker:

**(D-block-1) Tao's dilation.** Need $F(dn)=F(n)$ for the digit-decorated
indicator $F$. For $p\mid n$, $p>x^\delta$, level $j$: the residue
$r=n\bmod p^j$ maps to $dn\bmod p^j=(d\bmod p^j)\cdot r$. This is a *bijection*
of residues — distributions are preserved — but the pointwise identity is
destroyed, and the repair of averaging over $d$ makes it worse:
$\mathbb E_{d\in\mathcal D}F(dn)\approx(\text{anatomical part})\times
\prod(\text{base rates})$, i.e. the $d$-average *randomizes away* exactly the
digit information Lemma D is about. No rescue inside the identity.

**(D-block-2) Centring.** Prop 3.1 consumes MRT's averaged exponential-sum
estimate — a multiplicative-functions theorem. Our $F$'s would need a new
"averaged-shift correlation" estimate (sub-question **D-0**; plausibly easier
than Lemma D itself, since averaging over long shift ranges defeats
sign-sensitive obstructions, but it is new mathematics either way).

**(D-block-3) Frequency multiplicativity.** TT's circle-method encoding yields
multiplicative frequency objects $e(\alpha\Omega(n))$ *because $\Omega$ is
additive*. Our digit functionals $n\mapsto\{n/p^a\}$ at $p\mid n$ are not
additive in $n$; the encoding does not produce objects in the Pilatte/TT class.

**What survives.**

- **(S1) The spectral engine as a general bilinear tool.** Since §§4–13 use
  only 1-boundedness, one extracts: for arbitrary 1-bounded $f,g$ and signs
  $c_d$,
  $$\Bigl|\sum_{d\in\mathcal D}c_d\sum_{\substack{n\in I_N\\ d\mid n}}
  f(n)\,g(n+d)\prod_{p\mid d}\bigl(\mathbf 1_{p\mid n}-\tfrac1p\bigr)\Bigr|
  \le e^{O(J)}V^{J/2}N+(\text{exceptional rows}),$$
  with the exceptional set of rows of size $e^{-JV/3}N$ (their contribution
  needs the crude row bound — flag **P1** if this is ever used). Shape
  mismatch with our problem is real: their moduli sit on $n$ with shift $=d$;
  ours sit on $n-1$ with shift $1$. So: a *possible hammer and a method*
  (non-backtracking/high-trace for bespoke divisibility matrices), not a
  plug-in.

- **(S2) Hardness reclassification — the conceptual payoff of the session.**
  $\lambda$'s two-point problem is hard because $\lambda$ is *parity-sensitive*
  (sign-valued, minor-arc); the entire entropy/dilation/spectral apparatus
  exists to break parity under logarithmic averaging. Our digit indicators are
  **non-negative, positive-mean, local conditions at prime-power moduli
  $q^a\mid n-1$**. The parity barrier does **not** apply to Lemma D. Its true
  hardness class is *large-moduli equidistribution on average*
  (Bombieri–Vinogradov/dispersion type), with moduli $q^a$ reaching
  $x^{2/3+}$ — beyond BV's $x^{1/2}$, hence dispersion/well-factorable
  territory — and with the extra twist that the moduli are *divisors of*
  $n-1$ (divisor-correlated). Target statement to aim at (**Estimate D\***):
  for a bounded multiplicative anatomy weight $v$,
  $$\sum_{q\ \text{band}}\ \Bigl|\sum_{\substack{n\sim x\\ n\equiv1\ (q^a)}}
  v(n)\,e\bigl(h\,n/q^a\bigr)-\text{(main)}\Bigr|\ \ll\ x\,\mathcal L^{-c}$$
  on average over the band, uniformly in the relevant $h$ — i.e. a
  Pilatte-strength estimate with divisor-correlated prime-power frequencies.
  This re-ranks the attacks: **D-i (dispersion + multiplicative-functions-in-
  APs-on-average for the weights + FK exponential sums for the digit phases)
  is the lead**; D-ii is reframed as "prove Estimate D\*" — research-grade,
  but now named and shaped.

**Status: Lemma D stays [HC]**, with three gains: the black-box question is
settled (no), the parity barrier is off the table (epistemically significant —
no known *wall* stands in front of D, "only" hard standard technology), and
the needed new estimate is explicitly formulated.

---

## 4. Structural bonus: Theorem 1″ implies Theorem 1 (log-density form)

Let $d(t)=|W_1\cap[1,t]|/t$. Partial summation gives
$\sum_{n\le X}\mathbf 1_{W_1}(n)/n=d(X)+\int_1^X d(t)\,\frac{dt}t$. If
$d(t)=c_1^2+O(\log^{-c}t)$ for $t$ in a set of logarithmic density 1 (Theorem
1″'s conclusion) and $|d|\le1$ elsewhere, then
$\frac1{\log X}\sum_{n\le X}\mathbf 1_{W_1}(n)/n=c_1^2+o(1)$.

**Consequence for the program:** proving Lemmas A, B, C, D *at almost all
scales* — the native mode of every engine on the table — yields simultaneously
Theorem 1″ (natural density $c_1^2+O(\log^{-c}x)$ at almost all scales, hence
infinitude) **and** the logarithmic-density asymptotic of Theorem 1. The
all-scales natural-density statement is beyond the current frontier *for
everyone* (TT's own Theorem 1.6 carries the same limitation), so
almost-all-scales is the correct target, not a concession.

---

## 5. Reading-debt ledger and next actions

Open verification items (none blocks starting the manuscript):
**B0** equidistribution lemma for $g_z$ (to write, ~½ page);
**C1–C3** TT §3 fine print (read when drafting Lemma B's proof);
**P1** exceptional-row bound for the extracted spectral tool (only if S1 used);
**D-0** averaged-shift correlations for digit-decorated $F$ (only if a
dilation-style route is reattempted).

Fork: **(a)** start the manuscript — Lemma 0/0′ + Lemma A + Lemma B0 formally
(~3–4 pages, zero research risk; the reading makes the B-layer nearly
mechanical and will force C1–C3 at the right moment); or **(b)** the $k\ge2$
track — Balog–Wooley witness construction and carry-profile measurement.
Recommendation: (a).

