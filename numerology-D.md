# WP1.4: Numerology Table for Estimate D\*

**STATUS: ANALYSIS COMPLETE — WITH ERRATUM (§9).** The original headline ("no exponent gap; covered modulo adaptations") was an overcount, caught in WP2.0 when the lemmas were drafted (`lemma-alpha-beta.md` §3). What stands: the large-$\lambda$/small-$\lambda$ split, the linearization, the log-only requirement *in the AP-native formulation*, and the parameter maps. What is withdrawn: the claim that the Shparlinski mechanism covers small $\lambda$ modulo mechanical adaptations.

---

## 1. What is actually required

$E_q\ll(x/q)(\log x)^{-c}$ on average over band primes $q\sim Q=x^{u'}$, against the trivial bound $\asymp(x/q)\log q$. **The required total saving is a power of $\log$, not a power of $x$** — Estimate D\* is BV-type, and every tool below delivers *power* savings where it applies. This asymmetry (power savings available, log savings needed) is the program's core margin.

## 2. Correction to the v0.3 accounting (the $\lambda$-aggregation)

The deep large sieve's per-$\lambda$ RMS saving does **not** survive naive aggregation: Cauchy–Schwarz over $\lambda$ costs $\sqrt q$, and the mean-square route alone closes D\* only when $u+2u'<1$ — **empty in the open band** (since $u,u'>1/3$). The correct structure is a split at $\Lambda_0=x^{\,u+2u'-1+\varepsilon}$ (note $\Lambda_0<q$ always, since $u+u'<1$):

- **$|\lambda|\ge\Lambda_0$: COVERED unconditionally** by the deep large sieve (dyadic blocks + Cauchy–Schwarz per block; the weights $|c_\lambda|\ll1/|\lambda|$ make large-$\lambda$ blocks cheap).
- **$0<|\lambda|<\Lambda_0$: the live regime.** Per-$(q,\lambda)$ mean-square says nothing about individual small $\lambda$; everything below is about this regime.

## 3. New structural fact (verified numerically, $q\le4001$)

On the progression $a\equiv\bar p\ (\mathrm{mod}\ q)$, the deep layer **linearizes**: $\ell_q(a_0+qs)=\ell_q(a_0)-s\,\overline{a_0}\pmod q$, and since $\overline{a_0}\equiv p$,
$$T_p(\lambda)=e(\theta_{p,\lambda})\sum_{s<A/q}v(a_0+qs)\,e(-\lambda p\,s/q).$$
So per fixed $p$, the small-$\lambda$ object is a 1-bounded structured weight against a **classical additive character mod $q$**, over a progression of length $A/q=x^{1-u-u'}$ — *shorter than the period $q$* (since $1-u<2u'$): no free equidistribution; cancellation must come from the weight's structure or from averaging. Two averaging directions are available: over $q$ (the band), and over $p$ (the frequency $\lambda p/q$ moves with $p$).

For $v\equiv1$ the sum is geometric: $|T_p(\lambda)|\le\min(A/q,\|\lambda p/q\|^{-1})$ — the unweighted layer is main-term bookkeeping, COVERED.

## 4. Route II: the Shparlinski–Garaev–Baier–Zhao mechanism (close-read June 9)

Shparlinski (Bull. LMS 2011; arXiv:1104.3909), Theorem 8: for $N\le P^2$,
$$\sum_{p\sim P}\max_{(a,p)=1}|S_p(a;N_p)|^{2\nu}\le\big(P^3+N^\nu+\min\{N^\nu P^{1/2},N^{\nu/2}P^2\}\big)N^\nu P^{o(1)},$$
via Heath-Brown's identification of FQ sums as primitive character sums mod $p^2$, Garaev's completion (coefficients $\rho_{b,\nu}$ divisor-bounded), Gauss-sum conversion, and the **Baier–Zhao large sieve for square moduli**. Three properties verified against the source that matter for us:
1. **(10): the bound holds for arbitrary primitive characters mod $p^2$** — not only FQ characters. Our AP-opening characters $\chi_1\chi_\lambda$ (conductor exactly $q^2$ when $\lambda\ne0$) are in scope.
2. **Lengths may vary with the modulus** ($N_p\sim N$) — required by our band geometry.
3. **§4: the method extends to sums over primes** ("as in Garaev"; no individual bound known) — our $p$-variable.
Consequences (Cor. 9): nontrivial with **power saving $q^{-\kappa}$ for all but $O(Q^{1/2+\delta})$ moduli**, for lengths $\ge q^\varepsilon$. Exceptional moduli cost us $O(Q^{1/2+\delta})\cdot(x/q)\ll xQ^{\delta-1/2}$ — power-small. Known caveat: the method handles **initial intervals only** (their §4) — our AP restriction must be opened by characters (lemma $\beta$ below), not absorbed as a shifted interval.

## 5. Parameter map (lengths as powers of $Q$)

| Variable | Length | $\beta=\log_Q(\text{len})$ | In Thm-8 range $[Q^\varepsilon,Q^2]$? |
|---|---|---|---|
| $a$-side | $x^{1-u}$ | $(1-u)/u'\in(1,2)$ | YES (boundary corner $u,u'\to1/3$ where $\beta_a\to2$: reduce by periodicity mod $q^2$) |
| $p$-side | $x^{u}$ | $u/u'\in(2/3,3/2)$ | YES (for $\beta_p>2$ never; $\beta_p<5/6$ handled by Cor. 9's large-$\nu$ form) |
| AP-quotient $s$ | $x^{1-u-u'}$ | $(1-u-u')/u'\in(0,1)$ | YES (sub-period; the regime the average is *for*) |

Both variables sit comfortably inside the average-over-modulus machinery's range, with power savings against a log requirement.

## 6. The remaining gap, precisely

Three **adaptation lemmas** (expected mechanical-to-moderate) plus one **assembly risk** (genuine):
- **($\alpha$) Weighted Theorem 8:** insert 1-bounded weights into Garaev's completion; $\rho_{b,\nu}$ stays divisor-bounded. Mechanical.
- **($\beta$) AP-opening:** $n\equiv1\ (q)$ via mod-$q$ characters $\chi_1$; products $\chi_1\chi_\lambda$ are primitive mod $q^2$; apply (10). Mechanical, must be written.
- **($\gamma$) Prime-variable version:** realize §4's remark (Vaughan decomposition inside the completion). Moderate.
- **($\delta$) Bilinear assembly — the residual risk:** the coupling $pa\le x$, $a\equiv\bar p\ (q)$, with $v$ mod-$p$-structured, is where dispersion arguments traditionally die. Mitigating factors: complete bilinearity of the phases ($\ell_q(pa)=\ell_q(p)+\ell_q(a)$), the moving frequency $\lambda p/q$ in the linearized form, the deep large sieve / Wieferich energy as an unconditional backstop, and the log-only requirement.
Upgrade path: Zhao's conjecture (classical-shape large sieve for square moduli) would simplify everything to textbook form.

## 7. Verdict table

| Regime / object | Trivial | Required | Available | Status |
|---|---|---|---|---|
| $\lambda=0$ (classical mod-$q$ layer) | — | — | anatomy machinery | routed to Lemmas B/C |
| $\|\lambda\|\ge\Lambda_0$ | — | log | deep large sieve: power | **COVERED** (ours, unconditional) |
| small $\lambda$, $v\equiv1$ | $A/q$ | log | geometric series | **COVERED** (bookkeeping) |
| small $\lambda$, weighted, fixed $q$ | $A/q$ | log | none (Shp. open-problems list) | open pointwise — *not needed* |
| small $\lambda$, weighted, avg over $q\sim Q$ | $x/q$ | log | Thm 8/Cor 9/(10): power, exc. $O(Q^{1/2+\delta})$ | **COVERED modulo $\alpha,\beta,\gamma$** |
| bilinear assembly ($\delta$) | — | log | dispersion + deep sieve + energy | **OPEN — the residual risk** |
| top of band $\gamma\to1/2$ | — | — | $\eta$-trim, $O(\eta)$ loss | mitigated (lower bd) / live (full) |

## 8. G1 recommendation

Leaning **PASS**: no exponent gap on average over the band; required savings logarithmic against available power savings; residual risk concentrated in ($\delta$), exactly where WP1.5's empirics probe (measure the $E_q$-type sums on real populations — if the assembly cancellation is messy in data, that is the kill signal; if clean, proceed to WP2 = write $\alpha,\beta,\gamma$ and attack $\delta$). Probability update: full D ~35% (from 25–30%): the gap shrank from "large-moduli equidistribution, generic" to "three adaptations + one assembly," but ($\delta$) is the kind of step that has sunk dispersion arguments before — hence not higher.


## 9. ERRATUM (June 9, later session — from WP2.0)

The row "small $\lambda$, weighted, avg over $q$: COVERED modulo $\alpha,\beta,\gamma$" is **withdrawn**. Drafting the lemmas exposed the accounting error: the AP-opening ($\beta$) trades the log-saving target on a length-$x/q$ object for a power-$q$ target on length-$x$ objects, and the average-over-modulus machinery ($\alpha$, i.e. weighted Shparlinski) returns savings $q^{-\kappa}$ with $\kappa\ll1$ — short by $\approx q^{1-\kappa}$. The family mean-square route is short by $x^{2u'-1/2}$. Full accounting: `lemma-alpha-beta.md` §3. The corrected residual is **Estimate D†** (ibid. §4) with the new second-moment core (ibid. §5). The deeper reason: $\alpha$'s load-bearing hypothesis is $q$-independence of the weight, and D's weight is $q$-dependent through the AP itself — essentially, not technically.
