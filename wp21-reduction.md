# WP2.1: The Two-Frequency Reduction of Estimate D† (Digit Layer)

**STATUS: REDUCTION DERIVED AND EXPERIMENTALLY VALIDATED (June 9, 2026).** D†'s digit layer reduces, exactly and elementarily, to a minor/major-arc dichotomy: minor arcs cancel to $O(\mathrm{polylog})$ (measured: median $z=0.08$, aggregate $0.8\%$ of trivial); major arcs are localized on the explicit curves $p\approx q\sqrt{\mu/\lambda}$ and must be **counted, not bounded**. Remaining work splits into three named pieces (§5). Script: `wp21_test.py`.

---

## 1. The reduction (exact, elementary)

Fix a band prime $q$ and small $\lambda\ne0$. Cauchy–Schwarz D† in the $p$-variable; for fixed $p$ the inner object on the progression $a\equiv\bar p\ (\mathrm{mod}\ q)$, $a=a_0+qt$, is
$$V_p(\lambda)=\sum_{t\le R}\sigma(a_0{+}qt)\,f\big((a_0{+}qt)\bmod p\big)\,e(-\lambda pt/q),\qquad R=\frac{x}{pq},$$
with $f$ the centered half-interval indicator mod $p$ (the digit weight) and $\sigma$ the cofactor-anatomy indicator. (Linearization machine-checked to $10^{-14}$: the true Fermat-quotient phase equals a constant times $e(-\lambda pt/q)$.) Fourier-expanding $f$ mod $p$ ($\hat f_0=0$ by centering, $|\hat f_\mu|\asymp1/|\mu|$ for odd $\mu$):
$$V_p(\lambda)=\sum_{\mu\ne0}\hat f_\mu\,e(\mu a_0/p)\sum_{t\le R}\sigma(a_0{+}qt)\,e\big(t\,\theta_{\mu}\big),\qquad \theta_\mu=\frac{\mu q}{p}-\frac{\lambda p}{q}=\frac{\mu q^2-\lambda p^2}{pq}.$$
**The digit layer of D† is a family of linear exponential sums at the two-frequency phases $\theta_\mu$.** With $\sigma\equiv1$ (anatomy off) each inner sum is geometric: $|{\cdot}|\le\min(R,\|\theta_\mu\|^{-1}/2)$.

## 2. The dichotomy

- **Minor arcs** ($\|\theta_\mu\|$ not small for all small $\mu$, i.e. $p/q$ not near any $\sqrt{\mu/\lambda}$): summing the geometric bounds over all $\mu$ gives $|V_p|=O(\mathrm{polylog})$ — far below square-root.
- **Major arcs:** $\theta_\mu\approx0\iff\mu q^2\approx\lambda p^2\iff p/q\approx\sqrt{\mu/\lambda}$. There the digit weight (slowly walking, step $q\bmod p$ small) phase-locks with the slowly-rotating deep phase, and $|V_p|$ can reach $cR$. These cannot be bounded individually; they must be **counted**: for each small $\mu$, the resonant $p$ lie in an explicit window around $q\sqrt{\mu/\lambda}$, and — crucially for D†'s average over $q$ — each $p$ is resonant for only a vanishing proportion of $q\sim Q$.

## 3. Experimental validation ($q=4787$, $\lambda\in\{1,2\}$, 260 primes $p\in[3000,60000]$, $x_{\rm model}=10^{11}$, $\sigma\equiv1$)

- Typical case: median $z=|V|/\sqrt{R/4}=0.08$; 90th pct $0.40$; aggregate $\sum_p|V_p|=0.8\%$ of trivial. **Massively sub-square-root, as the geometric theory predicts.**
- Major arcs observed exactly where predicted: $p=4759,4813$ ($\approx q$: the $\mu/\lambda{=}1$ curve) with $|V|\approx0.3R$, $z\approx41$; $p=8171$ at $\lambda=2$ ($(p/q)^2\approx2.91$: the $\mu/\lambda{=}3$ curve). 26/520 cases exceeded a naively truncated bound — all traceable to major-arc width undercounting, none to the mechanism failing.
- **Correction recorded:** the per-$p$ truncated upper-bound formula is *not* the right tool on major arcs (slow-lock makes many $\mu$ conspire); the right statement is the dichotomy above. The earlier "z drifts up at small $\lambda$, top of band" flag in `empirics-D.md` §4 is now explained: top-of-band has $p$ near $q$ — the $\mu/\lambda=1$ major arc. The flag was the major arcs announcing themselves.

## 4. What this changes

D†'s digit layer is no longer an amorphous dispersion problem; it is: *(minor arcs: provable now)* + *(major arcs: an elementary-looking Diophantine count along $p\approx q\sqrt{\mu/\lambda}$, with the $q$-average diluting each curve)*. The Kloosterman-flavored second-moment core of `lemma-alpha-beta.md` §5 is bypassed on this route (no inverses of primes appear — the reciprocal $\bar a_0\equiv p$ collapsed it).

## 5. Remaining work, named

1. **D†-minor (draft now):** full-$\mu$-sum with honest tails ⇒ $|V_p|\le(\log x)^{O(1)}$ off the major arcs. Elementary; write it.
2. **D†-major (the count):** $\#\{(p,q,\mu):|\mu q^2-\lambda p^2|\le pq/R\}$ along each curve; show total resonant mass $\ll$ population$\,\times L^{-c}$ after the $q$-average (each contributes trivially $\le R$). Lattice-point counting near conics; looks elementary; the $\eta$-trim and the $\mu/\lambda{=}1$ curve at the top of the band interact — check whether the trim already eats the worst curve.
3. **D†-anatomy:** reinstate $\sigma$ (cofactor anatomy): need exponential sums of smooth-type indicators at the frequencies $\theta_\mu$ — known territory (de la Bretèche–Tenenbaum, Fouvry–Tenenbaum: exponential sums over smooth numbers; to pin in `citations.md`). Minor arcs should survive; major arcs are counted regardless of $\sigma$ (use $|\sigma|\le1$).
