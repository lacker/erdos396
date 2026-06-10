# WP8: Attack on Hypothesis C† (Erdős-396 program)

DRAFT — UNVERIFIED AGENT ATTACK REPORT

Date: 2026-06-10 (agent attack, narrow scope: C†-pair via BFI dispersion +
lb-variant only). Targets read: `manuscript/sections/14-lemmaC-reduction.tex`
(hyp:Cdagger, prop:C-cov, prop:C-single), `lemma-alpha-beta.md` §3,
`wp8-e3.md` §5 (lb-template), trim registry (`04-architecture.tex`).
Notation: $L=\log x$, $p_i\sim P_i=x^{u_i}$, $u_i\in(\tfrac13,\tfrac12)$,
$q=p_1p_2\in(x^{2/3},x^{1-2\eta})$, $R=x/(p_1p_2)\ge x^{2\eta}$. Object:
$V(p_1,p_2;\vartheta_{h,k})=\sum_{a\le R}g(p_1p_2a-1)\,\e{a\vartheta_{h,k}}$,
$\vartheta_{h,k}=\frac{hp_2}{p_1}+\frac{kp_1}{p_2}$, $g$ fixed $1$-bounded
multiplicative with Siegel–Walfisz; target $|V|\ll RL^{-c}$ on average over
band pairs.

## Status

- (C†-single): OPEN — not attacked here (scope). Its $\alpha$-shortfall
  stands as recorded (`lemma-alpha-beta.md` §3: Route 1 short by
  $q^{1-\kappa}$; Route 2 by $x^{2u'-1/2}$; Route 2′ discards the deep
  twist). New here: §1 shows C†-pair *reduces to* C†-single on axis
  harmonics, so the two stand or fall together.
- (C†-pair via BFI dispersion): NEGATIVE for this angle (method, not truth).
  The dispersion runs — diagonal and same-modulus terms close with power
  room — but the distinct-moduli term saturates the budget exactly and its
  completion conductor $p_1p_2p_2'>x$ leaves a deficit
  $x^{3u_2+\frac32u_1-1}$ ($\ge x^{1/2}$ band-wide) under even optimistic
  Weil accounting; benchmark cap (all known dispersion ranges
  $\le x^{3/5}<x^{2/3}\le q$) confirms. The $p_2$-average reduces conductor
  $p_1^2p_2^2\to p_1^2$, NOT modulus $\to p_1$: the hoped-for
  Granville–Shao reduction fails. Confidence in the negative method-verdict:
  ~0.85. C† itself remains plausible-true (empirics unchanged).
- (C†-lb, lower-bound variant): STATED (§ Lower-bound). A single
  second-moment upper bound per fixed harmonic over minor pairs suffices
  for Theorem 1′; majors discardable (Halász-along-AP debt vanishes);
  $B\le1$ anatomy subclass removes the pair case entirely; a $B=0$ escape
  hatch is flagged for consumer audit.

## Attack log

### 1. Coordinates, and what the $p_2$-average can and cannot remove

**Phase identity.** With $b:=p_2a$ (so $n=p_1b-1$, $b\le x/p_1$ — the cutoff
is clean in $b$, no $p_2$-entanglement):
$$a\vartheta_{h,k}\equiv \frac{hb}{p_1}+\frac{kap_1}{p_2}\pmod 1 .$$
Hence for the **axis harmonics $(h,0)$** the $p_2$-averaged object is an
*exact identity*:
$$\sum_{p_2\sim P_2}w(p_2)\,V(p_1,p_2;\vartheta_{h,0})
=\sum_{b\le x/p_1}g(p_1b-1)\,\e{\tfrac{hb}{p_1}}\,c_0(b),\qquad
c_0(b)=\sum_{p_2\sim P_2,\ p_2\mid b}w(p_2).$$
This is **C†-single at $p_1$ with a divisor-weighted population** (and
symmetrically $(0,k)$ at $p_2$ via the $p_1$-average). So: (i) the
$p_2$-average genuinely removes the factor $p_2$ — modulus $p_1p_2\to p_1$,
conductor $p_1^2p_2^2\to p_1^2$ in $n$-coordinates ($b\bmod p_1
\leftrightarrow n\bmod p_1^2$ on $n\equiv-1\ (p_1)$; Lemma $\beta$
structure); (ii) but what survives is **not** "$g$ in APs mod
$p_1\le x^{1/2-\eta}$" (which would be inside Granville–Shao $x^{20/39}$):
the binding twist $\e{hb/p_1}$ rides *in the AP parameter*, total conductor
$p_1^2=x^{2u_1}\in(x^{2/3},x^{1-2\eta})$ — beyond GS ($x^{20/39}$) and DGS
($x^{3/5}$) on the **whole band** ($2u_1>2/3>3/5$ always). The twist is
removable only at $(h,k)=(0,0)$ — the main term, not a binding harmonic.
The conductor $p_1^2$ is *intrinsic*: the binding digit is a datum of
$(n+1)/p_1 \bmod p_1$, i.e. of $n\bmod p_1^2$; no substitution trades it
away (iterating $b'=p_1b$ leaves a phase in $b'/p_1$, not a function of
$b'$ to any small modulus). **Answer to the lever question: the
$p_2$-average halves the conductor (pair→single), it cannot reach
modulus $p_1$.** This is Route 2′ of `lemma-alpha-beta.md` §3 rediscovered
from the pair side: the deep twist is exactly what cannot be discarded.

**$g$-intact orientations (recorded, then abandoned).** Keeping $g$ whole
and opening the second moment lands on binary correlations either way:
Cauchy in $a$, pairs $(p_2,p_2')$: $\sum_a g(p_1p_2a-1)\bar
g(p_1p_2'a-1)\e{a\Delta\vartheta}$; Cauchy in $p_2$, pairs $(a,a')$:
correlations along two linear forms in $p_2$. Both are Elliott-type binary
correlations with form coefficients $\asymp x^{2/3+}$ *exceeding the
variable length* ($R<x^{1/3}$, resp. $P_2<x^{1/2}$) — outside even the
qualitative log-averaged two-point Elliott theorem (Tao–Teräväinen; fixed
or slowly-growing coefficients only), and far outside the quantitative
Liouville case (Helfgott–Radziwiłł). Dead as stated; abandoned for the
bilinear route, which is the genuine BFI setting.

### 2. The dispersion (bilinear orientation, fixed $p_1$, average over $p_2$)

Decompose $g(n)=\sum_{n=m\ell}\alpha_m\beta_\ell$ (GS-style combinatorial
decomposition for SW-multiplicative $g$; $O(L^{O(1)})$ pieces, coefficients
divisor-bounded — $L$-power losses tracked into $c$), $m\sim M=x^{\mu}$,
$\ell\sim N=x^{\nu}$, $\mu+\nu=1$. Then
$$\Sigma:=\sum_{p_2\sim P_2}w(p_2)V
=\sum_{p_2,m}w\alpha_m\sum_{\substack{\ell\sim N\\ m\ell\equiv-1\,(p_1p_2)}}
\beta_\ell\,\e{\phi_{p_2,m}(\ell)},\qquad
\phi_{p_2,m}(\ell)=\frac{h\,[\frac{m\ell+1}{p_1}\bmod p_1]}{p_1}
+\frac{k\,[\frac{m\ell+1}{p_2}\bmod p_2]}{p_2},$$
target $|\Sigma|\ll\pi(P_2)RL^{-c}\approx x^{1-u_1}L^{-c-1}$. Cauchy–Schwarz
in $\ell$ (the long smooth variable): $|\Sigma|^2\le N\mathcal D$,
$\mathcal D=\sum_\ell|\sum_{p_2,m}\cdots|^2$, **budget
$\mathcal D\ll x^{1-2u_1+\mu}L^{-2c-2}$**. Opening $\mathcal D$ gives pairs
$((p_2,m),(p_2',m'))$ with $\ell$ in the CRT class of
$(-\bar m\bmod p_1p_2,\ -\bar m'\bmod p_1p_2')$; the shared factor $p_1$
forces $m\equiv m'\ (p_1)$ — *this congruence is what the $p_2$-average
buys*. Three terms:

**(D1) Diagonal** $(p_2,m)=(p_2',m')$:
$\mathcal D_1\approx\sum_{p_2,m}\frac{N}{p_1p_2}\approx x^{1-u_1}L^{-1}$.
Within budget iff $M\ge p_1L^{2c+1}$, i.e. $\mu\ge u_1+\varepsilon_L$. ✓
with power room.

**(D2) Same-modulus off-diagonal** $p_2=p_2'$, $m\ne m'$: compatibility
needs $m\equiv m'\ (p_1p_2)$ — *empty* if $M<p_1P_2$
($\mu<u_1+u_2$). If nonempty, write $m'=m+jp_1p_2$: the differenced phase
is $\Delta\phi(\ell)=-j\ell\,\vartheta_{h,k}$ — the original digit phase
reappears — and on the AP $\ell\equiv\ell_0\ (p_1p_2)$ it is **constant**
(increment $-jp_1p_2s\vartheta_{h,k}\equiv -js(hp_2^2+kp_1^2)\equiv0$): the
digit phase is dispersion-invisible in this sector. No oscillation needed
though: $\mathcal D_2\approx\frac{M^2N}{p_1^2P_2^2}\cdot\frac{P_2}{L}
=x^{1+\mu-2u_1-u_2}L^{-1}$ — saves $x^{u_2}$ against budget. ✓ either way.

**(D3) Distinct moduli** $p_2\ne p_2'$, $m\equiv m'\ (p_1)$: quadruple
count $\approx\frac{P_2^2}{L^2}\cdot\frac{M^2}{p_1}$, class density
$\frac{1}{p_1p_2p_2'}$ over length $N$:
$$\mathcal D_3^{\mathrm{main}}\approx\frac{M^2N}{p_1^2}L^{-2}
=x^{1+\mu-2u_1}L^{-2}\quad\text{— \textbf{saturates the budget exactly}};$$
all of C†-pair rides on $L^{2c}$ cancellation here. The regime is
sub-one-solution-per-class: $D:=p_1p_2p_2'=x^{u_1+2u_2}>x\ge N$ **always**
in-band ($u_1+2u_2>1$ since $u_1+u_2>\tfrac23$, $u_2>\tfrac13$) — per
quadruple the $\ell$-sum is a 0/1 detector; no per-quadruple bound exists,
cancellation must come from the quadruple aggregate. Completing the
interval indicator mod $D$ yields harmonics $\e{r\ell_0/D}$ with
$\ell_0$ the CRT class — **Kloosterman fractions $\bar m\bmod p_2$,
$\bar m'\bmod p_2'$ against arbitrary $\alpha_m\bar\alpha_{m'}$**. Even
granting full square-root cancellation per completed aggregate (optimistic
Weil: $\sqrt D\,L^{O(1)}$ per $(p_2,p_2',\delta)$, $\delta=(m-m')/p_1$):
$$\mathcal D_3^{\mathrm{err}}\approx
\frac{P_2^2}{L^2}\cdot\frac{M}{p_1}\cdot x^{\frac{u_1+2u_2}{2}}L^{O(1)}
=x^{\mu+3u_2-\frac{u_1}{2}}L^{O(1)}
\ \le\ x^{1+\mu-2u_1}\iff 3u_2+\tfrac32u_1\le1,$$
**$\mu$-independent**, and $3u_2+\tfrac32u_1\ge\tfrac32$ on the band:
fails by $\ge x^{1/2}$ everywhere. No choice of split rescues it.

**Exponent checks** (deficit $=3u_2+\tfrac32u_1-1$; benchmark deficit
$=(u_1+u_2)-\tfrac35$ vs the largest known dispersion range, DGS
smooth-supported $x^{3/5}$; BFI well-factorable $x^{4/7}$, Maynard
$x^{11/21}$, GS $x^{20/39}$ all smaller):

| | $(0.35,0.35)$ | $(0.45,0.45)$ |
|---|---|---|
| $q=p_1p_2$, $R$ | $x^{0.70}$, $x^{0.30}$ | $x^{0.90}$, $x^{0.10}$ (needs $\eta\le0.05$) |
| residual single conductor $p_1^2$ | $x^{0.70}$ (vs DGS $x^{0.60}$) | $x^{0.90}$ |
| admissible $\mu$ (D1; D2 empty) | $[0.35{+}\varepsilon,\,0.70)$ | $[0.45{+}\varepsilon,\,0.90)$ |
| D1 margin / D2 saving | ✓ / $x^{0.35}$ | ✓ / $x^{0.45}$ |
| D3: saturation | exact | exact |
| D3 deficit (optimistic Weil) | $x^{0.575}$ | $x^{1.025}$ |
| benchmark deficit | $x^{0.10}$ | $x^{0.30}$ |

**Adversarial self-checks.** (i) Phase identity and the D2 annihilation
($p_1p_2\vartheta_{h,k}\in\mathbb Z$) verified symbolically twice.
(ii) The deficit being $\mu$-independent closes the "shorten $N$" loophole.
(iii) Dispersing over both $p_1,p_2$ jointly: compatibility congruence
disappears (coprime moduli), completion conductor grows to
$p_1p_1'p_2p_2'\sim x^{1.4+}$ — strictly worse; same-modulus swap pairs
$\{p_1,p_2\}=\{p_2',p_1'\}$ arise only for overlapping bands and are
measure-negligible. Fixed-$p_1$ is the optimal orientation.
(iv) The optimistic-Weil accounting overstates what is provable (arbitrary
$\alpha_m$ admit no per-harmonic Weil without a second Cauchy, which
doubles the loss); a *failure* under optimistic accounting is therefore
robust. (v) Cross-check against the literature cap: even granting every
known refinement (factorable moduli à la Zhang/Polymath8, gains of order
$x^{0.01}$), the band floor $u_1+u_2>2/3$ exceeds the best known range
$3/5$ by $\ge x^{1/15}$ — order-of-magnitude consistent with the explicit
deficit, and independent of my bookkeeping.

## Obstructions

1. **Intrinsic conductor $p^2$.** The binding digit is a mod-$p_1^2$ datum
   of $n$; every coordinate change preserves it. The $p_2$-average performs
   the maximal possible reduction $p_1^2p_2^2\to p_1^2$ (pair→single); the
   GS-range hope ("modulus $p_1\le x^{1/2-\eta}$") is unattainable for any
   binding harmonic.
2. **Budget saturation in D3.** The distinct-moduli expected count equals
   the budget identically (dispersion phenomenology); the needed $L^{2c}$
   must come from oscillation over quadruples in the sub-one-per-class
   regime ($D>x\ge N$), where the harmonics are bilinear Kloosterman
   fractions with prime-inverse arguments beyond the Weil range. This is
   the **same species as the D† second-moment core**
   (`lemma-alpha-beta.md` §5: $\e{-\lambda s\bar p_2/q}$ over prime pairs
   in APs) — the program's two dispersion debts (C†, D†/E3-adjacent)
   converge on one named frontier: *bilinear Kloosterman with
   prime-restricted variables at super-square-root moduli*
   (Bourgain–Garaev / FKM-adjacent; to pin in `citations.md`).
3. **$g$-intact orientations** hit binary Elliott correlations with form
   coefficients exceeding the variable length — outside even qualitative
   log-Elliott. (Both Cauchy orientations; bracketing as in
   `lemma-alpha-beta.md` §3.)
4. **What the empirical truth-evidence ($z$: $13.1\to0.78$) is telling
   us**, in this light: the collapse is a statement about the *quadruple
   aggregate* oscillating — square-root-type cancellation in exactly the
   D3 sector. The evidence says the saturated term cancels; no known
   technology extracts it.

## Lower-bound-sufficient variant (weakest C†-form for Theorem 1′)

**Hypothesis C†-lb (exceptional-set / second-moment form).** There is an
absolute $\delta_0>0$ such that for each fixed harmonic pair
$0<\langle h\rangle\langle k\rangle\le L^{2C}$ (single case: each fixed
$0<|h|\le L^C$), over **minor** band pairs only (Prop. C-cov conditions;
majors excluded), the centered weighted sums satisfy the *single
second-moment upper bound*
$$\frac{1}{\#\{(p_1,p_2)\ \mathrm{minor}\}}\sum_{(p_1,p_2)\ \mathrm{minor}}
\big|V(p_1,p_2;\vartheta_{h,k})\big|^2\ \ll\ \delta_0\,R^2L^{-2c-2C-10},$$
and its single-prime analogue at conductor $p^2$ for
$\sum_{m\le x/p}g(pm-1)\e{hm/p}$ (centered; the $(0,0)$ main term belongs
to the FK law). By Chebyshev plus a union bound over the $O(L^{2C})$
harmonics (weights $\sum 1/\langle h\rangle\langle k\rangle\ll L^2$), this
gives the full per-pair C†-bound *pointwise* outside a set of band pairs
of density $\le\delta_0$, which the sandwich discards at main-term cost
$O(\delta_0)$ (trim registry items 1–4). **No asymptotic, no main-term
evaluation, no uniformity in $g$-class beyond the one fixed $g$, and only
an upper bound on one variance is needed.** Strictly weaker forms that
still suffice: a positive-proportion form on a single positive-measure
sub-band cell (the analogue of E3-lb's item 2, `wp8-e3.md` §5).

Two structural simplifications are specific to Theorem 1′. *(a) Majors are
discarded, not absorbed:* the statusO remark in §14 (Halász/MRT does not
control means of $g$ along APs of modulus $>$ length) is a debt only of
the asymptotic track; major/resonant pairs lie on the Family-A/B
exceptional curves with density $O(L^{-\mathrm{pos}})$ for the standing
$B$, well inside the $\delta_0$ budget — so C†-lb carries **no
major-pair absorption clause at all**. *(b) Sub-population:* by trim
registry item 4, Theorem 1′ may restrict to one positive-proportion
anatomy subclass; choosing **$\le1$ band prime per side** (positive
proportion by the anatomy laws) the two-prime population never arises and
C†-lb reduces to its **single-prime case only** (conductor
$p^2=x^{2u}$, fixed $h$, variance over $p\sim x^u$ minus auto-carry
slivers, where the slot-2 digit is deterministic and C† is void —
log-measure $0.288$ free). Flag for a consumer audit (§06/§15 gluing, not
checked here): the subclass $B(n)=B(n-1)=0$ (no band-prime divisors on
either side) has positive density and makes Lemma C's weighted layer
*empty* — if the assembly permits it, C† exits Theorem 1′ entirely. This
is a bookkeeping check, not an analytic one, and is the highest-value next
action on the lb-track.

What does *not* weaken: the surviving variance is precisely the
pre-Cauchy dispersion quantity $\sum_{p}|V|^2$ of the attack above (single
case: the Lemma-$\alpha$/Route-2′ object with its recorded shortfalls), and
its distinct-moduli term saturates the budget exactly as in §2 — the
lb-weakening removes uniformity, majors, and full density, but not the
analytic core. So C†-lb is genuinely weaker as a *statement* (and the
right citation target), but with current tools it is open for the same
reason C† is — unless the $B=0$ escape validates, which would moot it.

## Verdict

**NEGATIVE for this angle; hypothesis C† remains OPEN and is now sharply
located.** The BFI dispersion for C†-pair runs cleanly through its
diagonal and same-modulus sectors (power room $x^{u_2}$), reduces
pair→single on axis harmonics (conductor $p_1^2p_2^2\to p_1^2$ — the real
content of the BFI lever here), and then dies in the distinct-moduli
sector: budget saturated exactly, completion conductor $p_1p_2p_2'>x$,
deficit $x^{3u_2+3u_1/2-1}\ge x^{1/2}$ band-wide under optimistic
accounting ($x^{0.575}$ at $(0.35,0.35)$, $x^{1.025}$ at $(0.45,0.45)$),
benchmark-confirmed ($u_1+u_2>2/3>3/5=$ best known dispersion range).
The effective modulus is **not** reduced to $p_1$; the Granville–Shao
window is never entered. Unification finding: C†'s residual core and D†'s
second-moment core are the same bilinear-Kloosterman-over-primes frontier.
Confidence: ~0.85 (negative method-verdict; exponent arithmetic checked
adversarially at both requested points and $\mu$-independence closes the
split loophole). For Theorem 1′: C†-lb (above) is the weakest sufficient
form — single second moment, fixed harmonic, minor pairs, $\delta_0$
exceptions, single-prime case only under the $B\le1$ subclass — with a
flagged $B=0$ consumer audit that could remove C† from the lower-bound
track altogether.
