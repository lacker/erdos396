# The Open Problem: signed cancellation on a cross-denominator coincidence graph

**A self-contained statement of the one missing estimate in the Erdős-396 (k = 1) program.**

This document is written for an analytic number theorist with no prior contact with the
program. All notation is defined from scratch; nothing below requires any other document.
Internal labels ("W4.6", "E3-lb", "C†") are quoted only so that a reader who later opens the
working files can match objects; they carry no content here.

In one sentence: *we need square-root–type cancellation, with signs, in a weighted count of
coincidences $q \mid h\ell' - h'\ell$ among Farey fractions $h/\ell$ with prime denominators
$\ell \sim \Lambda$ and short numerators, on average over prime (or all) moduli
$q \sim x^{0.425}$, in a regime where the corresponding absolute-value count is provably of
the trivial order and where the spectral theory of Kloosterman sums is blocked by a
conductor mismatch.* Everything else in the proof of the theorem in §5 is either proved
(much of it machine-verified) or reduced, with verified bookkeeping, to this estimate and
one sibling estimate of the same genus (§5.2).

---

## 1. Context: what theorem this estimate feeds

Erdős and Graham (1980; Erdős problem 396) asked for which $k$ there are infinitely many
$n$ with $\prod_{i=0}^{k}(n-i) \mid \binom{2n}{n}$. The case $k = 0$ concerns the *governor
set* $\mathcal{D} = \{m \ge 1 : m \mid \binom{2m}{m}\}$, whose membership is, by Kummer's
theorem, a digit condition on $m$ in base $p$ at the primes $p \mid m$; Ford and Konyagin
(2021) proved $\mathcal{D}$ has asymptotic density $c_1 = 0.11424\ldots$. The first
genuinely *binary* case is $k = 1$:

$$\mathcal{W} \;=\; \Big\{\, n \ge 2 \;:\; n(n-1) \,\Big|\, \binom{2n}{n} \,\Big\}\;=\;\{2,\ 210,\ 460,\ \ldots\},$$

where two consecutive integers must divide the same central binomial coefficient. To our
knowledge even the infinitude of $\mathcal{W}$ is not in the literature. The program
reduces the statement "$\mathcal{W}$ has positive lower logarithmic density (in particular
$\mathcal{W}$ is infinite)" — Theorem 1′ of §5 — through an exact sandwich, a digit-anatomy
factorization, and a dispersion analysis, to exactly two open estimates: the one stated in
§2 below (the deep end), and a sibling variance estimate of the same genus (the shallow
end, §5.2). Every other link of the chain is proved, machine-verified, or pinned to
verified classical citations, with all constants tracked. The estimate of §2 is the
program's single missing analytic input; this document is the program's product if the
estimate stays open.

Where the object comes from (three sentences, for orientation only — the statement in §2
stands alone). The divisibility condition on the shifted side forces one to show that, for
typical pairs of primes $p, q \sim x^{0.425}$, the residues
$\nu_\ell = (-a_0\,\overline{q}_\ell) \bmod \ell$ — where $a_0 = a_0(p,q) \in [1, q)$ is
the representative of $p^{-1} \bmod q$ — equidistribute in the short
window $[0, R]$, $R = x^{0.15}$, on average over primes $\ell$ in dyadic blocks
$(\Lambda, 2\Lambda] \subseteq (x^{0.425}, x^{0.575}]$ — a variance statement for a triple
inverse-correlation. Completing the window by Vaaler polynomials, opening the square, and
running a proved chain of exact identities (CRT combination, reciprocity, a new
fiber-counting lemma — §3.2) closes every term *except* one: the signed cross-denominator
coincidence sum below. That one term is the estimate.

---

## 2. The estimate

### 2.1 Notation (complete)

Throughout, $e(x) = e^{2\pi i x}$, $\|\beta\|$ is the distance from $\beta$ to the nearest
integer, $\overline{q}_\ell$ denotes the multiplicative inverse of $q$ modulo $\ell$, and
$n \sim N$ means $N < n \le 2N$. Let $x$ be large and $L = \log x$.

**Fixed parameters** (the reference cell; $\eta = 0.05$):

* $Q = x^{0.425}$ (the modulus scale), $A = x^{0.575}$, $R = x^{0.15}$ (the window length;
  $A = QR$);
* $\Lambda = x^{\lambda}$, a dyadic block parameter with $\lambda \in [0.425,\, 0.575]$
  (i.e. $Q \le \Lambda \le A$); the estimate is needed **uniformly in $\lambda$** over this
  range (equivalently: for every dyadic block $\Lambda = 2^j Q \le A$);
* $\delta_0 \in (0,1)$ an exceptional-density budget: the program takes $\delta_0$ a small
  fixed power of $1/L$; since every gap in this problem is a power of $x$, all
  polylogarithmic factors below are immaterial, and the reader may treat the right sides as
  $x^{0.3 - o(1)}$, $x^{0.725 - o(1)}$ with $o(1)$ absorbing them;
* $N_Q = \#\{\text{primes } q \sim Q\}$.

**The weights.** For each prime $\ell \sim \Lambda$ set

$$H_\ell \;=\; \Big\lceil \frac{\ell}{R+1} \Big\rceil \qquad (\text{so } H_\ell \asymp \Lambda/R = x^{\lambda - 0.15}),$$

and let $S^{\pm}_\ell$ be the Vaaler majorant/minorant trigonometric polynomials of degree
$H_\ell$ for the indicator of the window $\{0, 1, \ldots, R\} \bmod \ell$:
$S^-_\ell \le \mathbf{1}_{[0,R] \bmod \ell} \le S^+_\ell$ pointwise, with Fourier expansion
$S^{\pm}_\ell(\nu/\ell) = \sum_{|h| \le H_\ell} \hat{c}^{\pm}_h(\ell)\, e(h\nu/\ell)$. The
coefficients are real ($\hat{c}_{-h} = \overline{\hat{c}_h}$) and satisfy, for
$0 < |h| \le H_\ell$,

$$|\hat{c}^{\pm}_h(\ell)| \;\le\; \frac{1}{H_\ell + 1} + \min\Big( \frac{R+1}{\ell},\, \frac{1}{\pi |h|} \Big), \tag{2.1}$$

with per-$\ell$ masses $\sum_{0<|h|\le H_\ell} |\hat{c}^{\pm}_h(\ell)| \le m_1 = 4.1$ and
$\sum_{0<|h|\le H_\ell} |\hat{c}^{\pm}_h(\ell)|^2 \le 7(R+1)/\Lambda$. Only the harmonics
$h \ne 0$ enter below. (Any construction with these properties would do; nothing in the
surrounding chain uses more than (2.1), reality, and the masses. A version of the estimate
uniform over all real coefficients obeying (2.1) is sufficient and is probably the natural
target.)

**The tuple family and phases.** For a prime $q \sim Q$ put

$$T_{\mathrm{lin}} \;=\; \{\, t = (\ell, h) \;:\; \ell \sim \Lambda \text{ prime},\ \ell \ne q,\ 0 < |h| \le H_\ell \,\},
\qquad \#T_{\mathrm{lin}} \asymp \frac{\Lambda^2}{R\,L} = x^{2\lambda - 0.15 - o(1)} \in [x^{0.7},\, x^{1.0}],$$

and the Farey-type phases

$$\theta_t(q) \;:=\; -\,\frac{h\, \overline{q}_\ell}{\ell} \ \bmod 1, \qquad t = (\ell, h) \in T_{\mathrm{lin}}.$$

Write $\hat{c}_t = \hat{c}^{\pm}_h(\ell)$ (one fixed choice of sign throughout a given
application; the majorant $+$ is the one needed). Finally, the normalized Dirichlet kernel:

$$F_q(\beta) \;:=\; \frac{1}{q} \sum_{a=1}^{q} e(a\beta), \qquad |F_q(\beta)| \le \min\Big( 1,\, \frac{1}{2q\|\beta\|} \Big).$$

Note the exact identity, for $t = (\ell, h) \ne t' = (\ell', h')$ with $\ell \ne \ell'$:

$$\theta_t(q) - \theta_{t'}(q) \;\equiv\; -\,\frac{w_0\, \overline{q}_{\ell\ell'}}{\ell\ell'} \pmod 1,
\qquad w_0 \;:=\; h\ell' - h'\ell \;\ne\; 0, \quad |w_0| \le \frac{9\Lambda^2}{R} = x^{2\lambda - 0.15}. \tag{2.2}$$

### 2.2 The statement, verbatim from the diagnosis file

The closing verdict of the program's literature diagnosis (`wp13-kuznetsov-bridge.md` §4)
states the missing estimate exactly, in two forms, either of which suffices:

> the precise new spectral estimate that must be proved: a signed cross-moduli coincidence
> bound at spectral conductor beyond C². Exact statement (either form suffices for (W1.1)
> via the proved W4.0–W4.4 chain):
>
>     (Form A, per prime q — W4.6 verbatim) for all but δ₀N_Q/L primes q ~ Q = x^{0.425}:
>       |Σ_{ℓ≠ℓ'~Λ prime} Σ_{0<|h|≤H_ℓ, 0<|h'|≤H_{ℓ'}} ĉ_h(ℓ)ĉ_{h'}(ℓ')
>           F_q( (hℓ'−h'ℓ)·\overline{q}_{ℓℓ'} / (ℓℓ') )| ≤ x^{0.3−o(1)},  uniformly λ ∈ [0.425, 0.575];
>     (Form B, all-moduli sufficient version, §1.2 K3) Σ_{c~x^{0.425}} of the same with the complete
>       part the signed divisor-correlation Σ ĉĉ'·1[c | hℓ'−h'ℓ]: total ≤ x^{0.725−o(1)} vs real mass
>       x^{2λ}; i.e. signed saving x^{2λ−0.725+ε} = x^{0.125}/x^{0.275}/x^{0.425} at λ = 0.425/0.5/0.575
>       below a TRUE (attained) absolute mass.

### 2.3 Form A, re-expounded

**Estimate (Form A; per prime modulus).** *With the notation of §2.1: for every dyadic
$\Lambda = x^{\lambda}$, $\lambda \in [0.425, 0.575]$, and for all primes $q \sim Q$
outside an exceptional set of at most $\delta_0 N_Q / L$ elements,*

$$\Bigg| \sum_{\substack{t = (\ell,h),\ t' = (\ell',h') \in T_{\mathrm{lin}} \\ \ell \ne \ell'}}
\hat{c}_t\, \hat{c}_{t'}\; F_q\big( \theta_t(q) - \theta_{t'}(q) \big) \Bigg|
\;\le\; 0.01\, \delta_0\, \frac{(\eta R)^2}{L^3} \;=\; x^{0.3 - o(1)}. \tag{A}$$

By (2.2) the kernel argument is the Farey difference
$\theta_t - \theta_{t'} = -w_0 \overline{q}_{\ell\ell'} / (\ell\ell') \bmod 1$: the left
side of (A) is a weighted, signed count of near-coincidences among the $\#T_{\mathrm{lin}}$
points $\{\theta_t(q)\}$ at scale $1/q$ (the kernel $F_q$ is essentially the indicator of
$\|\beta\| \lesssim 1/q$, with mild tails). The constant $0.01$ and the exact $L$-powers
are not delicate: any bound $x^{0.3-\varepsilon}$, or $x^{0.3}$ times a sufficiently large
negative power of $L$, suffices, and the exceptional $q$-set may have relative density up
to $\delta_0/L$ (the $1/L$ absorbs a union over the $\le 0.22\,L$ dyadic blocks $\Lambda$;
any polylog-small density is fine).

**The floor, and the required saving.** The corresponding *absolute-value* sum is a
theorem (§3.2): replacing the summand by
$|\hat{c}_t \hat{c}_{t'}|\,|F_q(\theta_t - \theta_{t'})|$ and averaging over $q \sim Q$
gives $x^{2\lambda - 0.425 + o(1)}$, and this is **attained** — the coincidence mass is
real, to truth grade (numerically: per-pair kernel $q$-average $\approx 6/Q$). Hence (A)
demands a saving of

$$x^{2\lambda - 0.725 + \varepsilon} \qquad \text{below the attained absolute mass, uniformly in } \lambda \in [0.425, 0.575],$$

i.e. numerically:

| $\lambda$ | absolute floor $x^{2\lambda - 0.425}$ | demand $x^{0.3}$ | required signed saving $x^{2\lambda - 0.725}$ |
|---|---|---|---|
| $0.425$ | $x^{0.425}$ | $x^{0.3}$ | $x^{0.125}$ |
| $0.500$ | $x^{0.575}$ | $x^{0.3}$ | $x^{0.275}$ |
| $0.575$ | $x^{0.725}$ | $x^{0.3}$ | $x^{0.425}$ |

The saving must come from the **signs**: of the products $\hat{c}_t \hat{c}_{t'}$ and of
the (essentially unimodular, non-oscillating in $a$) kernel values at the coincidence
pairs. No count-level improvement is possible (§3.2).

### 2.4 Form B, re-expounded: all moduli, and no exponentials in the main term

The left side of (A) arises, over the proved chain, from the nonnegative quantity
$\sum_p |D_\Lambda(p,q)|^2$, where $D_\Lambda(p,q)$ is the (Vaaler-completed, centered)
windowed sum of §1; the same expression defines $D_\Lambda(p, c)$ for *any* modulus
$c \sim Q$ coprime to $p$ and to the $\ell$'s. By positivity, the average over prime $q$ embeds in the
average over **all** integers $c \sim Q$ at the cost of one factor $L$ (the prime density)
— immaterial against a power deficit — and the diagonal and same-denominator terms re-close
over all moduli with $x^{0.15 - o(1)}$ to spare. Now split the kernel argument by exact
three-term reciprocity: with $m = \ell\ell'$,
$$\theta_t(c) - \theta_{t'}(c) \;\equiv\; -\,\frac{w_0 \overline{c}_m}{m} \;\equiv\; \frac{w_0 \overline{m}_c}{c} \;-\; \frac{w_0}{cm} \pmod 1.$$
The $a$-sum in $F_c$ is a full period mod $c$, so the first (period-$c$) part collapses
completely — $\sum_{a \bmod c} e(a w_0 \overline{m}_c / c) = c \cdot \mathbf{1}[c \mid w_0]$
— leaving the smooth factor $e(-a w_0/(cm))$ to generate an incomplete remainder. What
remains is:

**Estimate (Form B; all moduli — sufficient for Form A's role).** *With $C = x^{0.425}$,
uniformly in $\lambda \in [0.425, 0.575]$:*

$$\Bigg| \sum_{c \sim C} \ \sum_{\substack{\ell \ne \ell' \sim \Lambda \ \mathrm{prime} \\ 0<|h|\le H_\ell,\ 0<|h'|\le H_{\ell'}}}
\hat{c}_h(\ell)\, \hat{c}_{h'}(\ell')\; \mathbf{1}\big[\, c \mid h\ell' - h'\ell \,\big] \Bigg|
\;+\; \big|\text{(incomplete remainder)}\big|
\;\le\; x^{0.725 - o(1)}, \tag{B}$$

*where the incomplete remainder is the corresponding sum of incomplete (Kloosterman-type)
$a$-sums left over from the smooth factor $e(-a w_0/(cm))$ — a genuine sums-of-Kloosterman-sums
object of the same size budget.* The main term of (B) is a **signed divisor-correlation
sum: there are no exponentials in it.** Its absolute mass is again real and attained:
$\sum_{\text{pairs}} |\hat{c}\hat{c}'| \cdot \mathbb{E}\,\#\{c \sim C : c \mid w_0\}
\approx 0.7\, (m_1 N_\Lambda)^2 = x^{2\lambda - o(1)}$ (with
$N_\Lambda = \#\{\ell \sim \Lambda \text{ prime}\}$), so (B) demands the identical signed
saving $x^{2\lambda - 0.725 + \varepsilon}$, now with the primality of the modulus variable
**removed** (see §3.4: this relaxation is legitimate and changes the pricing of spectral
technology, not the deficit).

**Scale card** (for comparison with the literature; the three values are at
$\lambda = 0.425 / 0.5 / 0.575$):

* moduli: $c \sim C = x^{0.425}$ (all integers, or primes $q$ in Form A);
* inner modulus $m = \ell\ell' \sim \Lambda^2$: $x^{0.85} / x^{1.0} / x^{1.15}$;
* coincidence integer $w_0 = h\ell' - h'\ell$, $0 < |w_0| \le 9\Lambda^2/R$:
  up to $x^{0.7} / x^{0.85} / x^{1.0}$;
* family size $\#T_{\mathrm{lin}}$: $x^{0.7} / x^{0.85} / x^{1.0}$;
* after dispersion-style completion, arbitrary-coefficient (numerator $\times$ level) mass
  sits at $x^{1.125} / x^{1.275} / x^{1.425}$ — **above** the spectral conductor
  $C^2 = x^{0.85}$ on every block. The Linnik-range condition $mn \ll C^2$ of the
  Kuznetsov/Deshouillers–Iwaniec theory fails on every block; this is the structural
  obstruction (§3.3(e)).

---

## 3. What is known

### 3.1 Truth evidence: the cancellation is there, with room

**Random model.** At a fixed prime $q$, the coincidence graph
$\{(t, t') : \|\theta_t(q) - \theta_{t'}(q)\| \lesssim 1/q\}$ has
$\asymp \#T_{\mathrm{lin}}^2 / Q = x^{4\lambda - 0.725}$ edges. If the signed contributions
$\hat{c}_t \hat{c}_{t'}$ at the coincidences cancel like independent signs, the left side
of (A) has r.m.s. size
$\big( \sum_{\mathrm{coinc}} |\hat{c}_t \hat{c}_{t'}|^2 \big)^{1/2}
\asymp (R/\Lambda)^2\, x^{(4\lambda - 0.725)/2} = x^{-0.0625 - o(1)}$, *independently of
$\lambda$* — below the demand $x^{0.3 - o(1)}$ by $x^{0.3625}$, and still below the demand of
the tighter cell $\eta = 0.02$ (where the budget exponent is $0.12$) by $x^{0.18+}$. The
estimate is true in the random model **with at least $x^{0.18}$ of room at every block and
at both calibrations of the cell.**

**Numerics** (probe `wp11_w4_probe.py`; model of the top cell at $x = 10^8$:
$P = Q = 2512$, $R = 16$, $A = 39811$, $L = 18.42$; blocks $\Lambda = Q,\ 4Q,\ A/2$; 300
$(p,q)$-samples for the square, 48 for the linear aggregate, 1500 random cross-$\ell$ pairs
for the kernel averages; the Farey-structure computation exact in rationals):

* *Signed truth of the square*: the measured $\mathbb{E}\, D_\Lambda^2$ against the
  Bernoulli (independent-window) diagonal gives ratios $1.11 / 0.73 / 0.82$ on the three
  blocks — the signed off-diagonal is $O(\text{diagonal})$ and of both signs. On the
  $\Lambda = Q$ block the *absolute* coincidence mass is
  $(\sum |\hat c|)^2 \times (\text{measured kernel average}) = 236^2 \times 0.00246 \approx 137$
  (and $\approx 2.1 \cdot 10^3$ after the positivity step's $0.85L$), versus measured
  signed truth $1.50$: **the absolute-value step discards about three orders of magnitude
  already at toy scale, all of it sign cancellation.**
* *Linear aggregate vs. random model*: $\mathrm{rms}\,|U| / \|\hat c\|_2 = 1.01 / 0.87 / 0.68$
  on the three blocks ($\#T_{\mathrm{lin}}$ up to $6.8 \cdot 10^6$): square-root
  cancellation in the signed aggregate, on the nose, while any absolute-value chain pays
  the factor $\|\hat c\|_1 / \|\hat c\|_2 = 276 / 1017 / 1953 \approx \sqrt{\#T_{\mathrm{lin}}}$.
* *Floor truth-grading*: the per-pair kernel $q$-average measures $0.00246 \approx 6.2/Q$
  on the mean (max $0.0092$), i.e. the divisor-counting floor of §3.2 is attained at
  $L^0$ grade — it is not a polylog artifact of the proof.

### 3.2 The floor theorems: count-level improvement is provably impossible

The program *proved* the absolute-value side of the problem, by elementary divisor
counting, and proved that it cannot be improved. The key lemma (new; zero citation weight):

> **Fiber-count lemma.** Fix $t = (\ell, h) \ne t' = (\ell', h')$ as in §2.1 (cross- or
> same-denominator). Then for every $k \ge 0$,
> $$\#\{\, q \sim Q \ \mathrm{prime},\ q \ne \ell, \ell' \;:\; \|\theta_t(q) - \theta_{t'}(q)\| < 2^k/q \,\} \;\le\; 2^{k+4}.$$
> *Proof sketch.* With $m = \ell\ell'$, the difference is $n/m \bmod 1$ where
> $qn \equiv -w_0 \pmod m$, $w_0 = h\ell' - h'\ell \ne 0$ fixed. A near-coincidence gives an
> integer $r \equiv n \pmod m$ with $|r| \le 2^k m/q$; then $qr + w_0 = jm$ for some
> $|j| \le 2^k + 1$, so $q$ divides the fixed nonzero integer $jm - w_0$ of size $< Q^4$:
> at most $3$ prime divisors $q \sim Q$ per $j$, and summing over $j$ gives the bound. $\square$

Consequences, all proved: the per-pair $q$-average of the kernel is
$\le 4.4 L^2 / Q$ — *full square-root grade per pair, uniformly*, achieving unconditionally
what no Kloosterman-sum citation chain could (see §3.3(c)) — and the assembled bound is

$$\mathbb{E}_{p,q} |D^{\pm}_\Lambda|^2 \;\le\; 14.3\,(R+1) \;+\; 152\, \frac{\Lambda L^2}{Q} \;+\; 363\, \frac{L \Lambda^2}{Q}.$$

The first two terms (diagonal and same-denominator) close the variance target with
$x^{0.15 - o(1)}$ of room on every block; the third — the cross-denominator coincidence
mass $x^{2\lambda - 0.425 + o(1)}$ — is the floor of §2.3, over budget by exactly
$x^{2\lambda - 0.725}$. And the floor is **truth-grade, not an artifact**: for a typical
pair, the integers $jm - w_0$, $|j| \le 2$, have $\asymp 1/L$ expected prime divisors
$\sim Q$, so the per-pair average over the $\asymp Q/L$ primes is genuinely $\asymp 1/Q$-grade
(the proved bound $4.4 L^2/Q$ is tight up to $L^3$; the numerics of §3.1 show $\approx 6/Q$
on the nose). At any coincidence
$\|\theta_t - \theta_{t'}\| < 1/q$ the kernel value has modulus $\asymp 1$ with **no
oscillation in $a$** (the phase $e(a\Delta)$ moves by less than $2\pi$ over the whole
period). Hence the absolute mass is real and irreducible for *every* chain that takes
absolute values at the pair level, wherever in the argument it does so: the deficit
$x^{2\lambda - 0.725}$ is invariant across all aggregation orders audited. **Only
sign-sensitive input can close the estimate.** Two corollaries of the same analysis fix the
geometry: the pair-frequency family has multiplicity exactly $2$ (minimal additive energy),
lives in a single macro-cluster of length $\asymp 1/R$, and attains its minimal gap
$\asymp \Lambda^{-4}$ — it is cluster-heavy by $x^{0.15+o(1)}$ against its mean gap, so any
unweighted $(N + \delta^{-1})$ large sieve pays $\delta^{-1} = 16\Lambda^4 \ge x^{1.7}$ and
is dead on arrival.

### 3.3 The obstruction map: every priced approach, with its exact deficit

Each route below was executed (not merely sketched) and priced to an exact exponent at the
reference cell; "deficit $x^{\alpha}..x^{\beta}$" means the route falls short of the demand
by that factor as $\lambda$ runs over $[0.425, 0.575]$.

**(a) Pointwise completion at fixed $(q, h)$ — a Pólya–Vinogradov barrier.** Completing the
window sum at a fixed modulus and applying *any* bound for complete Kloosterman-type sums
fails structurally: the window $\nu_\ell \le R$ has relative density
$R/\Lambda \le x^{-0.275}$, far below the square-root scale $\Lambda^{-1/2}$, so a per-$(q,h)$
completion bound of strength $\Lambda q^{-\eta_0}$ *exceeds the trivial windowed count
itself*. Deficit at the strongest citation grade (Korolev 2018): $x^{0.2504}..x^{0.4081}$;
even at the absolute Weil ceiling $\eta_0 = 1/2$ (unattainable for sums over primes):
$x^{0.0625}..x^{0.2125}$. No single-modulus completion estimate, however strong, can see a
window this far below square-root density.

**(b) Dispersion with the harmonic outside the square — a Cauchy–Schwarz diagonal floor.**
Averaging over $(p,q)$ first and Cauchy–Schwarz-ing the $h$-sum afterwards is priced and
closed: deficit $x^{0.4127 + o(1)}$ at citation strength, and $\ge x^{1/4 - 2.25\eta - o(1)}
= x^{0.1375}$ **absolutely**, from the exact diagonal identity, even granting perfect
off-diagonal cancellation. The harmonics must go inside the square — which is what produces
the object of §2.

**(c) Per-tuple bounds after the square is opened — the citation-to-$\sqrt{}$ gap.** With
the square opened and the phases combined (an exact identity chain), the best per-tuple
input from the Kloosterman-sums-over-primes literature (Korolev 2018, via a verified
reciprocity flip) saves $x^{0.0245}$ per pair: deficit $x^{0.5254}..x^{0.8254}$. The
*unprovable* per-tuple square-root line ("god mode", $x^{-0.425}$ per pair) would still
leave deficit $x^{0.125}..x^{0.425}$. The fiber-count lemma of §3.2 then *proved* the
square-root line unconditionally — a gain of $x^{0.4005}$ over the citation chain, with
zero citation weight — and the deficit persists: it is the same $x^{2\lambda - 0.725}$.
This is the precise sense in which the absolute-value floor, not the quality of per-tuple
Kloosterman bounds, is the obstruction.

**(d) Duality / large-sieve arrangements — capped by overcrowding.** Every dual pairing was
priced. (i) Pair-level dual: the family has $\#T_{\mathrm{pair}} = x^{4\lambda - 0.3 - o(1)}
\in [x^{1.4}, x^{2.0}]$ unimodular columns against $N_Q = x^{0.425 - o(1)}$ samples, so the
large-sieve constant obeys $\Delta \ge \#T_{\mathrm{pair}}$: yield short by
$x^{0.675}..x^{1.275}$. (ii) Linear level, $q$-samples: $\#T_{\mathrm{lin}} =
x^{0.7}..x^{1.0}$ against $q = x^{0.425}$ — overcrowded by $x^{0.275}..x^{0.575}$;
equivalently the family's conductor (inverse minimal gap, $4\Lambda^2$ same-denominator,
$\Lambda^4$-grade cross) exceeds the sample range by $x^{0.425}..x^{0.725}$. (iii) Joint
$(p,q)$-samples ($x^{0.85}$ of them) are *not* overcrowded for $\lambda < 0.5$, but the
needed quasi-orthogonality of the Gram matrix requires per-pair
$|G| \le x^{1.0 - 2\lambda}$: Korolev-grade off-diagonal bounds miss by
$x^{0.675}..x^{0.975}$, and even a hypothetical double-square-root $|G| \asymp x^{0.425}$
misses by $x^{0.275}..x^{0.575}$ (and for $\lambda \ge 0.5$ overcrowding returns
regardless). Schur/Gram is an absolute-value chain: same wall, one level up. **Conclusion:
duality arrangements are capped at the absolute-value floor; the cap is the overcrowding
ratio, not a technique deficiency.**

**(e) The spectral corpus (sums of Kloosterman sums) — a conductor mismatch, priced
verbatim.** The full Kuznetsov-technology perimeter was fetched, quoted, and priced against
the scale card of §2.4.

* *Deshouillers–Iwaniec 1982 (Thm 12) / Drappeau 2017 (Thm 2.1).* The only technology
  whose coefficient generality ($b_{n,r,s}$ arbitrary) swallows the correlation between the
  numerator $w_0$ and the inner modulus $m = \ell\ell'$ (see §3.4). Its gain lives at
  spectral conductor $C^2 = x^{0.85}$; the family's arbitrary-coefficient mass sits at
  $x^{1.125}..x^{1.575}$ — beyond $C^2$ on every block and in every allocation of the
  variables into $(c, d, n, r, s)$ (machine-checked over all allocations). Best case (the
  flipped, modulus-$m$ dressing): the DI bound lands $x^{0.1375}$ *below* raw trivial —
  genuine spectral cancellation — but $x^{0.2875}$ *above* the elementary divisor floor of
  §3.2, hence $x^{0.4125}..x^{0.7125}$ above the demand. Elementary counting beats the
  spectral machine here.
* *Kuznetsov-aspect averages (Kuznetsov $C^{1/6}$; Sarnak–Tsimerman; Steiner).* Category
  mismatch, decisive: per tuple-pair the $c$-sum object is
  $\sum_{c \sim C} \mathbf{1}[c \mid w_0]$ — a **nonnegative divisor count**; the complete
  $a$-sum has already collapsed all Kloosterman oscillation in $c$, so per-pair $c$-sum
  technology of any strength cannot pass below the divisor floor. Where Kuznetsov re-enters
  through the pair *aggregate*, the coefficient mass sits at $mn \asymp x^{2\lambda + 0.275}$
  versus $C^2 = x^{0.85}$: $C \le \sqrt{mn}$ by $x^{0.1375}/x^{0.2125}/x^{0.2875}$ — deep in
  the **Selberg range**, of which Steiner writes, verbatim: "in the application one is very
  deep in the Selberg range, for which **the trivial bound is still the best known
  bound**."
* *Prime-variable dressings (Fouvry–Michel 1998/2014; Bourgain, Bourgain–Garaev).* Reading
  the object with modulus $m = \ell\ell'$ and prime argument $q$: the argument length is
  $m^{0.37}..m^{0.5}$, below every known threshold (Fouvry–Michel–Kowalski require length
  $\ge p^{3/4+\varepsilon}$; the Bourgain–Garaev $p^{1/2+\varepsilon}$ results are
  prime-modulus only, while $m$ has two prime factors); and the savings class there is
  $x^{0.02}$-grade versus the needed $x^{0.125+}$. Range-dead, modulus-class-dead, and
  size-dead independently. Spectral access to *restricted moduli* stops at $P_6$
  almost-primes (Xi 2024); pure prime moduli are open in the entire literature — but this
  obstruction is moot for us, by §3.4(i).
* *Trace-function bilinear forms at one prime modulus (Kowalski–Michel–Sawin;
  Blomer–Fouvry–Kowalski–Michel–Milićević).* Three independent mismatches: range
  (hypotheses cap $MN < q^{5/4} = x^{0.53}$, while the per-$q$ tuple mass is
  $x^{0.7}..x^{1.0}$ with numerator scale up to $x^{0.7}..x^{1.0} \gg q$); savings size
  (best $q^{-1/64+\varepsilon} = x^{-0.0066}$ versus needed $x^{0.125}..x^{0.425}$ — short
  by a factor of $20$–$60$ in the exponent); and category — at fixed $q$ the left side of
  (A) is a **positive-semidefinite Gram form**
  $F_q(\theta_t - \theta_{t'}) = \langle v_t, v_{t'} \rangle$,
  $v_t = q^{-1/2}(e(a\theta_t(q)))_{a \le q}$, not a bilinear form of trace functions.
* *Trilinear Kloosterman fractions (Bettin–Chandee; as run by Fouvry–Radziwiłł).* The
  closest shape in the corpus: arbitrary $\ell^2$-weights on all three variables
  *including the modulus* — the only fetched statement that tolerates prime $q$'s and
  two-prime $m$'s as they stand. It fails on arity (the object is quadrilinear, with the
  dispersion linearization forcing a weight $\nu(q,a)$ coupled across two variables — the
  self-similarity of §4 in trilinear clothing; Bettin–Chandee's $\vartheta$ is a fixed
  integer) and on ranges even granting the coupling: their saving needs $M \asymp N$, ours
  has $M = x^{0.425}$ against $N \ge x^{0.85}$, landing at/above trivial; short of the
  demand by $x^{0.572}..x^{0.872}$.

**(f) The dual (count-level) flank — Wieferich-hard.** The program's day-one formulation of
the same gap (manuscript, Cor. `cor:crude`) asks, after summing the single-modulus deep
large sieve trivially over moduli: "the genuine strengthening ... is a tailored
$(q,\lambda)$-averaged sieve exploiting cross-moduli Wieferich-pair counting: for fixed
$n_1 \ne n_2$ the primes $q$ with $q^2 \mid n_1^{q-1} - n_2^{q-1}$ should be far sparser
than fixed-$q$ counting sees." The literature audit returned: the pointwise-in-pair form is
at least as hard as the non-Wieferich-primes problem (unconditionally open; Silverman's
$\gg \log x$ requires abc); the count-level literature (Bourgain–Ford–Konyagin–Shparlinski
2010 and its line) is entirely fixed-$q$, the transpose direction. And decisively: the
estimate of §2 is the *depth-zero* analogue of that question, and there the count-level
version of the needed improvement is **provably false** — the coincidence mass is attained
(§3.2). Counting cannot close it in either depth; only signs can.

### 3.4 Simplifications already secured (an attacker starts here)

Two genuine simplifications, both established in the diagnosis, reshape the target:

**(i) Prime moduli are removable by positivity.** Since the underlying per-modulus quantity
is $|D_\Lambda(p, c)|^2 \ge 0$ and is defined for all $c \sim Q$, the prime-$q$ average
embeds in the all-moduli average at polylog cost, and the re-opened diagonal closes with
$x^{0.15 - o(1)}$ room. **The missing estimate need not be proved for prime moduli: Form B,
over all integers $c \sim x^{0.425}$, suffices.** The folklore hardness of "Kloosterman
sums over prime moduli" is *not* the binding obstruction; the binding obstruction is the
conductor/range mismatch of (e).

**(ii) The numerator–modulus correlation is not a structural blocker.** The coincidence
integer $w_0 = h\ell' - h'\ell$ is correlated with the inner modulus $m = \ell\ell'$ (the
program's earlier audits flagged this pair-dependence as potentially fatal for dispersion).
The Deshouillers–Iwaniec/Drappeau coefficient generality ($b_{n,r,s}$ arbitrary, jointly in
numerator and level variables) absorbs it entirely: the blocker dissolves, for the whole
DI class. What it cannot absorb is the mass-versus-conductor mismatch — which yields a
one-number pre-screen for any candidate technology: *does its gain survive
arbitrary-coefficient mass at $x^{2\lambda + 0.275}$ against smooth-modulus spectral
conductor $x^{0.85}$?*

---

## 4. Why it is plausibly hard — and plausibly true

**True.** The estimate holds in the random model with $x^{0.18+}$ of room at every block
(§3.1), and the model is corroborated by direct computation of the literal object at toy
scale, where the signed sum sits three orders of magnitude below the absolute mass. The
family is explicit and algebraic — Farey differences $h/\ell - h'/\ell'$ with prime
denominators $\sim \Lambda$ and short numerators, dilated by $\overline{q}_\ell$, weighted
by Vaaler coefficients — with no visible conspiracy mechanism: the coincidence pattern
$c \mid h\ell' - h'\ell$ is governed by divisor structure that the numerics show behaving
pseudorandomly against the signs.

**Hard, for an identified structural reason.** Form B places the problem squarely in the
divisor-correlation world: bound
$\sum_{c \sim C} \sum \hat{c}\hat{c}'\, \mathbf{1}[c \mid h\ell' - h'\ell]$ below its
attained absolute mass by a power. Every spectral detection of that congruence produces
sums of Kloosterman sums whose coefficient mass exceeds the available spectral conductor
$C^2 = x^{0.85}$ by $x^{0.275}..x^{0.575}$ — i.e. the dual object sits *deep in the Selberg
range* $C \le \sqrt{mn}$, the regime of the twisted Linnik–Selberg problem where, verbatim
from the current literature, "the trivial bound is still the best known bound." The
estimate is thus a **signed refinement of a problem family whose unsigned version already
marks the frontier**. In large-sieve terms, what is demanded is a gain over the sieve
constant on an overcrowded family equal to the *full* overcrowding ratio,
$(\#T_{\mathrm{lin}}/Q) \cdot x^{-0.15} = x^{2\lambda - 0.725}$, for a specific sparse
Farey family, with signs; no instance of such a mechanism exists in the corpus (the
square-moduli large sieve of Baier–Zhao, the nearest relative, sharpens constants for
sparse *moduli* sets, not for overcrowded *frequency* families). Finally, the problem is
**self-similar under its own elementary toolkit** (machine-confirmed): opening the square,
completing, and fiber-counting maps the demand-versus-floor gap to an identical gap one
generation down — Fourier-detecting the divisor correlation of Form B regenerates the same
congruence species $c \mid k\ell' + k'\ell$ with no contraction of the exponent. Iterating
the ladder converges to no proof; the missing input is genuinely external. The diagnosis
grades it research-problem-grade, not transcription-grade: no
reduction-outline-plus-transcription can be written from the 1982–2026 Kuznetsov-class
corpus (confidence $\ge 0.9$ against the fetched sources, $\approx 0.75$ against the
published literature at large, the obstruction being conductor-structural and hence
invariant across the class).

**What a solution would likely require.** One of:

1. *A sign-sensitive cross-moduli coincidence estimate*: beat divisor counting on
   $q$-average for the signed weights $\hat{c}_t \hat{c}_{t'}$ on the coincidence graph —
   the $e(\cdot/q)$-analogue of the cross-moduli Wieferich-pair question that the program
   flagged on day one (§3.3(f)), now with the exact exponent it must produce:
   $x^{2\lambda - 0.725 + \varepsilon}$ below trivial, uniformly in
   $\lambda \in [0.425, 0.575]$.
2. *Spectral uniformity beyond the Linnik range*: power-saving bounds for sums of
   Kloosterman sums with arbitrary coefficients in the regime $mn \gg C^2$ (equivalently,
   progress on the Selberg-range half of the twisted Linnik–Selberg problem strong enough
   to carry coefficient mass $x^{2\lambda + 0.275}$ at conductor $x^{0.85}$).
3. *A bespoke large-sieve mechanism* that converts the proved three-scale cluster geometry
   of this particular family (multiplicity exactly $2$, macro-cluster $1/R$,
   per-denominator lattice $1/\ell\ell'$, fine scale $\Lambda^{-4}$ attained; selected
   residues $h\overline{q}_\ell$ multiplicatively structured) into a beyond-conductor gain
   with signs.

Route 1 is the most concrete: Form B contains no exponentials at all, and the positivity
relaxation (§3.4(i)) has already discharged the moduli-class difficulties that historically
made such averages hard.

---

## 5. The payoff

### 5.1 The theorem that follows

> **Theorem 1′ (conditional; the program's headline).** *Assume the estimate of §2 (Form A
> or Form B), together with the sibling estimate of §5.2. Then there is an explicit
> $\kappa_{\mathrm{lb}} > 0$ such that*
> $$\frac{1}{\log x} \sum_{\substack{n \le x \\ n(n-1) \mid \binom{2n}{n}}} \frac{1}{n} \;\ge\; \kappa_{\mathrm{lb}}$$
> *for all $x$ in an unbounded set of scales. In particular $\mathcal{W}$ has positive
> lower logarithmic density, and there are infinitely many $n$ with
> $n(n-1) \mid \binom{2n}{n}$.*

At the reference parameters the audited constant chain gives
$\kappa_{\mathrm{lb}} \approx 1.4 \cdot 10^{-5}$. The deduction from the two estimates to
Theorem 1′ is complete: a sandwich $\mathcal{W} \supseteq \mathcal{D}_0 \cap
(\mathcal{D}_0^{(+)} + 1)$ that is exact (no exceptional set), a digit-anatomy
factorization, and a fully audited cascade with every link proved, machine-verified, or
pinned to verified citations and every constant tracked. The estimate of §2 enters as
follows: it implies, through the proved chain summarized in §3.2 (positivity, kernel bound,
fiber counting — each step an inequality already in place), the variance statement
$\mathbb{E}_{p,q} |D^{+}_\Lambda|^2 \le 20\, \delta_0 (\eta R)^2 L^{-2}$ on every dyadic
block, which in turn closes — by a proved absorption and exceptional-set layer — the first
of the two residual hypotheses (internally "E3-lb"; the
polylog-short near-diagonal sliver is bundled inside the same cross-denominator sum, so (A)
closes it too). Nothing else is missing on that branch.

### 5.2 The second brick — same genus, shallow end

The other residual hypothesis (internally "C†-single-lb($g_0$)") is stated here in full,
both because Theorem 1′ needs it and because it shares its genus with §2 — a solution of
one is expected to teach the solution of the other, with the transfer flowing from §2's
estimate downhill. Let $\eta = 0.05$, and let

$$g_0(n) \;=\; \mathbf{1}\big[\, \exists\, q' \mid n,\ q' \text{ prime},\ q' \in (x^{0.40}, x^{0.45}],\ P^{+}(n/q') \le x^{3/10} \,\big]$$

(a fixed $0/1$ weight: one prime factor in the band, the cofactor $x^{3/10}$-friable; the
band prime is then unique). For primes $p \in (x^{0.40}, x^{0.45}]$ (restricted to a
"minor-arc" subset; the complement is discarded into the exceptional budget) and a fixed
harmonic $0 < |h| \le L^{C}$, set

$$V_p(h) \;=\; \sum_{m \le x/p} g_0(pm - 1)\, e\big( hm/p \big) \;-\; (\text{main term})$$

(the main term is explicit; for $h \ne 0$ it is a geometric edge term of size
$\le \kappa p / (2|h|)$, where $\kappa \approx 0.04$ is the density of $g_0$ — a factor
$x^{0.10}$ below the target, absorbable).

**Estimate (C†-single-lb).** *There are $\delta_0, c > 0$ such that, for each fixed $h$,*

$$\frac{1}{\#\{p\}} \sum_{p} |V_p(h)|^2 \;\ll\; \delta_0 \Big( \frac{x}{p} \Big)^2 L^{-2c - 2C - 10}.$$

An exact orthogonality identity converts this (in sufficient, harmonic-free form) into a
Barban–Davenport–Halberstam-type variance at a *single square modulus*: with $M = x/p$,
$A_p(m_0) = \#\{m \le M : m \equiv m_0 \ (p),\ g_0(pm-1) = 1\}$,
$G_p = \#\{m \le M : g_0(pm-1) = 1\}$, and $\mathrm{cnt}(m_0) = \#\{m \le M : m \equiv m_0\ (p)\}$,
it suffices that, for $p$ off a $\delta_0$-density set,

$$\mathrm{Var}_p \;:=\; \sum_{m_0 \bmod p} \Big| A_p(m_0) - \frac{G_p}{M}\,\mathrm{cnt}(m_0) \Big|^2 \;\ll\; \frac{x^2}{p^3}\, L^{-2c-4}.$$

The genus is the same as §2's: on the fiber $n \equiv -1 \ (p)$ the binding datum
$m \bmod p$ is a datum mod $p^2$ of $n$ — the phase $e(hm/p)$ is exactly a depth-one
Fermat-quotient character of conductor $p^2 = x^{0.90}$, beyond every known
Bombieri–Vinogradov-type range for the relevant weights (Granville–Shao $x^{20/39}$;
Drappeau–Granville–Shao, smooth-supported, $x^{3/5}$) — while the *untwisted* modulus
$p = x^{0.45}$ itself is inside the classical range: the twist is the whole problem —
and the
demanded cancellation is sign-sensitive aggregate cancellation at a super-square-root
conductor with fewer than one element per residue class ($x/p^2 = x^{0.10}$) — precisely
the frontier on which §2 sits. The differences all point the easier way: the demand is only
*polylog* below trivial (the truth, square-root cancellation, has $x^{0.55}$ of room;
model-scale numerics show the normalized variance at $0.97$, flat over a factor $16$ in
$x$, with an *empty* exceptional set); the long variables are friable, hence flexibly
factorable (a lever the rigid prime family of §2 lacks); there are only $x^{0.10}$ lag
correlations, each needed to log-precision; and the variance form carries an $x^{0.10}$
power surplus over the Poisson prediction. The program's diagnosis prices it at
$P(\text{close with current technology}) \approx 0.3$–$0.4$ — hard, but measurably easier
than §2, whose missing input is research-grade.

### 5.3 Bottom line

A proof of (A) or (B) closes the deep brick of the last open lemma at once — the chain
from it to the first hypothesis of Theorem 1′ is proved and machine-audited end to end —
and leaves a single estimate of the same genus, at its shallow end, between the program and
the unconditional theorem *"there are infinitely many $n$ such that
$n(n-1) \mid \binom{2n}{n}$, and the set of such $n$ has positive lower logarithmic
density."* Independently of the application, (A)/(B) would be the first sign-sensitive
bound to beat divisor counting on a cross-moduli coincidence family in the Selberg range —
exactly the species of input that the sign-change, equidistribution, and
dispersion-beyond-conductor problems quoted in §3.3 are all waiting for.


## ADDENDUM (June 12; wp15 round 1)

Three further approaches are now priced and dead, each with structural proofs: the wall is **moment-invariant** (4th-moment chain reduces to the same estimate; the 4-linked class CRT-collapses), **cell-independent** (proved: all cell-gains cancel exactly; closure would need $Q \ge x^{2u'}$), and **coefficient-sign-independent**: the Vaaler/Dirichlet coefficients factor as (exact phase) × (nonnegative amplitude), and the phase's total travel over the full parameter cell is $\approx 3$ rotations (the completion degree times the window sweep is identically 1) — so **the weights in both forms of the estimate may be taken nonnegative**. Consequence: the required cancellation comes from the distribution of modular inverses (the $q$-arithmetic) alone. This further sharpens where a solution must act: equidistribution/sign structure of $\{\overline{p\ell}\bmod q\}$ over the coincidence graph, not coefficient interference.


## ADDENDUM 2 (June 12/13; wp15-verify-audit — ERRATUM 7, FAVORABLE): THE WALL IS POLYLOG-DEEP

The power-deficit $x^{2\lambda-0.725}$ of the main text is an **artifact of the harmonic-tuple decomposition**. A physical-side Hölder chain (P1)–(P3) — (P1) the record's own lemma (W1.4)(ii); (P2) new but elementary (inverse-injectivity + orbit-gap counting, no equidistribution input); (P3) trivial — gives **unconditionally**
$$\mathbb E_{p,q}\,|D^{\pm}_\Lambda|^2 \;\le\; C'(R+1)^2 L,$$
verified line-by-line and by five scaling discriminators at model $x = 10^6$–$10^{12}$ (`wp15-verify-audit.md`). The three floor theorems are reconciled: they price harmonic-tuple chains, pair-level-absolute mass, and weight-uniform sieves respectively — the physical chain lives outside all three. The chain *implies* the D3-INEQ* negative-main-term evaluation at strength $1-O(x^{-(2\lambda-0.725)}L^{O(1)})$.

**The open problem is hereby restated:** improve the proved bound $C'(R+1)^2L$ by a factor $L^{3+a}$ (to the load-bearing budget $20\,\delta_0(\eta R)^2L^{-2}$) — a polylogarithmic refinement of an unconditional estimate, not a power-saving against a trivial bound. Caveat from the integer side: Form A as stated in §2 is FALSE at full period (the LHS attains $+x^{2\lambda-0.425}$); the correct target is the (W1.1)-windowed form throughout.
