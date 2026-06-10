# WP2.0: Adaptation Lemmas $\alpha$, $\beta$ — and the Assembly Accounting

**STATUS: $\alpha$ PROVED (sketch below; write-through is verbatim Shparlinski with weights). $\beta$ PROVED (and numerically verified). Assembly accounting: NEGATIVE RESULT** — composing $\alpha+\beta$ falls short of Estimate D\* by a power of $q$; the "covered modulo adaptations" row of `numerology-D.md` is **withdrawn** (see its Erratum §9). The gap re-localizes to **Estimate D†** (§4 below), with a new concrete second-moment core (§5). Net: the de-risk sprint did its job — this overcount was caught one session after it was made, by drafting the lemmas.

---

## 1. Lemma $\alpha$ (weighted average bound for primitive characters mod $q^2$)

**Statement.** Let $w:\mathbb{N}\to\mathbb{C}$, $|w|\le1$, **independent of $q$**. For fixed $\nu\ge1$, $N\le Q^2$, and any lengths $N_q\sim N$:
$$\sum_{q\sim Q\ \mathrm{prime}}\ \max_{\chi\ \mathrm{primitive}\ \mathrm{mod}\ q^2}\Big|\sum_{n\le N_q}w(n)\chi(n)\Big|^{2\nu}\ \ll\ \big(Q^3+N^\nu+\min\{N^\nu Q^{1/2},N^{\nu/2}Q^2\}\big)N^\nu Q^{o(1)} .$$
**Proof sketch.** Garaev's completion applies to the weighted restriction verbatim: $\sum_{n\le N_q}w\chi=\sum_{m\le M}w(m)\chi(m)\mathbf{1}[m\le N_q]$ with $M=2N$, Fourier-expanding the indicator; Hölder in the frequency $b$; the $\nu$-th power produces coefficients $\rho^w_{b,\nu}(k)=\sum_{m_1\cdots m_\nu=k}\prod w(m_i)\,e_M(b\sum m_i)$ with $|\rho^w(k)|\le\tau_\nu(k)=k^{o(1)}$; Gauss-sum conversion (primitivity); Baier–Zhao square-moduli sieve with the coefficient sequence $\rho^w$. $\square$
**The load-bearing hypothesis:** $w$ must be $q$-independent — the Baier–Zhao step requires one fixed coefficient sequence across all moduli. This is exactly where the application breaks (§3).
**Corollary $\alpha'$.** For any $\varepsilon,\delta>0$ there is $\kappa>0$: for all but $O(Q^{1/2+\delta})$ primes $q\sim Q$, $\max_\chi|\sum_{n\le N_q}w\chi|\le Nq^{-\kappa}$, for $N\ge Q^\varepsilon$.

## 2. Lemma $\beta$ (AP-opening; verified numerically at $q=11,31$)

**Statement.** Let $q$ be prime, $\lambda\not\equiv0$, $w$ any weight. Then
$$\sum_{\substack{n\le x\\ n\equiv1\,(q)}}w(n)\chi_\lambda(n)=\frac{1}{\varphi(q)}\sum_{\chi_1\ \mathrm{mod}\ q}\ \sum_{\substack{n\le x\\(n,q)=1}}w(n)\,(\tilde\chi_1\chi_\lambda)(n),$$
and **every** $\tilde\chi_1\chi_\lambda$ is **primitive mod $q^2$**: the lift $\tilde\chi_1$ is trivial on $1+q\mathbb{Z}$, while $\chi_\lambda(1+qu)=e(-\lambda u/q)$ is nontrivial there, so the product is nontrivial on the kernel of reduction. $\square$ (Identity and primitivity machine-checked to $10^{-14}$.)

## 3. The assembly accounting (the negative result)

Target per band prime: $E_q\ll(x/q)(\log x)^{-c}$. Composing $\beta$ then $\alpha'$ (or family mean-squares):
- **Route 1 (max over characters):** $E_q\ll(\log q)\max_\chi|S(\chi)|\le x\,q^{-\kappa}\log q$. Required exponent: $\kappa\ge1-o(1)$. Available: $\kappa=O(\delta/\nu)$ (Cor. $\alpha'$) or $1/12$ (Cor.-10 grade). **Shortfall: factor $\approx q^{1-\kappa}$.**
- **Route 2 (bilinear + Cauchy–Schwarz over the full mod-$q^2$ family):** $\sum_{(\chi_1,\lambda)}|S_PS_A|\le((P+q^2)P)^{1/2}((A+q^2)A)^{1/2}\approx q^2\sqrt{x}$, so $E_q\ll q\sqrt{x}$. Required: $q^2\le\sqrt{x}$, i.e. $u'\le1/4$ — outside the band. **Shortfall: $x^{2u'-1/2}\in(x^{1/6},x^{1/2})$.**
- **Route 2′ (coset-restricted C–S, fixed $\lambda$):** $\sum_{\chi_1}|S_P(\tilde\chi_1\chi_\lambda)|^2\le\varphi(q)\#\{p_1\equiv p_2\,(q)\}\approx P^2+qP$ — recovers the $1/q$ but **discards the deep twist entirely**, landing at $E_q\approx x/q$ with zero saving. (This is the original session's dead end, rediscovered from the dual side — the two C–S routes bracket the problem.)

**Diagnosis.** The AP-opening converts a *log-saving* problem on a length-$x/q$ object into a *power-$q$-saving* problem on length-$x$ objects; family-average tools return square-root-type savings, never the factor $q$. Equivalently: the weight's $q$-dependence *through the AP itself* ($m\mapsto w(1+qm)$) is essential, and it is precisely what Lemma $\alpha$'s load-bearing hypothesis forbids. Lemma $\gamma$ (prime-variable adaptation) is **mooted** for this route and parked.

## 4. Estimate D† — the corrected residual core (AP-native)

For each fixed $0<|\lambda|\le\log^Cx$, on average over band primes $q\sim Q$:
$$\sum_{m\le M_q}W_q(m)\,e(\lambda m/q)\ \ll\ M_q(\log x)^{-c},\qquad W_q(m)=w(1+qm),\ \ M_q=\tfrac{x-1}{q},$$
with $w$ the (1-bounded, centered) population-and-digit decoration. What stands from the earlier analysis: **large $\lambda$ remain covered unconditionally** (the deep-large-sieve split was AP-native and is unaffected); the unweighted layer is geometric; parity-freedom; and `empirics-D.md` measured **exactly this object** — true with square-root room. What changed: small-$\lambda$ D† is *not* reachable by citation-adaptation of the average-over-modulus machinery; it is the genuine dispersion fight ($\delta$), as the original sessions' instincts had it.

## 5. The second-moment core (new — the WP2.1 target)

Opening $|{\textstyle\sum_q}\,\text{D†}|^2$ by dispersion and linearizing pair ratios ($p_1\equiv p_2\,(q)\Rightarrow p_1\bar p_2\equiv1+qs\bar p_2\ (\mathrm{mod}\ q^2)$, $s=(p_1-p_2)/q$) reduces beating the Route-2′ diagonal to cancellation in
$$\sum_{p_2\sim P}\ \sum_{\substack{p_1\sim P\\ p_1\equiv p_2\,(q)}}e\!\Big(\!-\lambda\,\frac{s\,\bar p_2}{q}\Big)\qquad(\bar p_2=p_2^{-1}\bmod q),$$
**Kloosterman-flavored sums over prime pairs in APs** — the inverse of a prime in the frequency. Adjacent literature: bilinear Kloosterman sums and reciprocals of primes (Bourgain–Garaev; Fouvry–Michel-type sums over primes; Irving, Khan–Milicevic–et al. — to pin in `citations.md`). This is a named, attackable object, and it is where $\delta$ now lives.
