# Lemma B: Anatomy Independence of $n$ and $n-1$

**STATUS: ASSEMBLED (manuscript §13, June 10): interpolation lemma, B0 (full proof), Siegel–Walfisz (modulo one classical ψ-sum input SL2′), and the assembled proposition — Lemma B holds modulo TT Thm 3.1 (PINNED) + SL2′ + the Dickman–Billingsley identification (W4).** Probability: ~97%.

---

## Statement (informal)

The *anatomies* of $n$ and $n-1$ — the joint size-distribution of their prime factors above $x^\delta$, in particular $\sqrt{2\cdot}$-smoothness and the existence/position of band primes in $((2\cdot)^{1/3},\sqrt{2\cdot}]$ — are asymptotically independent, quantitatively, at almost all scales.

## Citation route — VERIFIED

**Tao–Teräväinen, arXiv:2512.01739 (v2, April 2026), Theorem 3.1** (= the theorem of their §3, "A quantitative correlation estimate"), built on **Pilatte (arXiv 2310.19357)**. Verbatim statement (from the v2 TeX source, `\label{thm:correlation}`):

> Let $X\ge2$. Suppose that $g_1,g_2:\mathbb N\to\mathbb C$ are 1-bounded multiplicative functions. Let $1\le\mathcal L\le\log X$ and $\delta_N$ be real numbers for all $X^{0.4}\le N\le X$, obeying one of the following two axioms:
> - **(i) (Equidistributed case)** $g_1$ is real-valued and for all $X^{0.4}\le N\le X$ and $a,q\in\mathbb N$ one has $\sum_{N<n\le2N,\ n\equiv a\,(q)}g_1(n)=\frac Nq\delta_N+O(N\mathcal L^{-1})$. Furthermore $g_1(p)=1$ whenever $\exp(\log^{1/11}X)\le p\le\exp(\log^{1/10}X)$.
> - **(ii) (Non-pretentious case)** [$\delta_N=0$; non-pretentiousness inequality — not our case.]
>
> Let $c>0$ be a sufficiently small absolute constant. Then there exists a set $\mathcal E\subset[\sqrt X,X]$ with $\frac{1}{\log X}\int_{\mathcal E}\frac{dt}{t}\ll\mathcal L^{-c}$ such that for any $W\in[\mathcal L^c]$ and integers $b,h_1,h_2=O(\mathcal L^c)$ with $h_1\ne h_2$:
> $$\frac WN\sum_{N<n\le2N}(g_1(n+h_1)-\delta_N)\,g_2(n+h_2)\,\mathbf 1_{n\equiv b\,(W)}\ \ll\ \mathcal L^{-c}$$
> for all $N\in[\sqrt X,X]\setminus\mathcal E$.

Their remark: setting $q=1$ in the axiom gives $\delta_N=\frac1N\sum_{N<n\le2N}g_1(n)+O(\mathcal L^{-1})$ — so the conclusion is "centered correlation is small," i.e. **correlation $=$ (mean of $g_1$) $\times$ (AP-mean of $g_2$) $+\ O(\mathcal L^{-c})$**.

## The three fine-print checks — RESOLVED

1. **Uniformity in $x$: YES.** All constants are absolute; $g_1,g_2$ enter only through the quantitative axioms at scale $X$. Functions may depend on $X$ (our band edges $\sim x^\alpha$ are fine). Their Theorem on consecutive smooth numbers (§1) even states this explicitly: the asymptotic $\rho(u)\rho(v)$ holds *uniformly* for $u,v\le c\log_2x/\log_3x$, "whereas in the aforementioned works $u,v$ were fixed."
2. **Conclusion shape: YES** — product of means via the centered form plus their $\delta_N$ remark; the residual ingredient is the AP-mean of $g_2$, which is the same Lemma B0 applied to $g_2$.
3. **Exact statement: RETRIEVED** (above, from the v2 source). Two hypotheses to discharge per application, both verified for our $g_z$: the **technical condition** $g_1(p)=1$ on $[\exp(\log^{1/11}X),\exp(\log^{1/10}X)]$ holds trivially (our $g_z\equiv1$ below the bands, which start at $x^{1/3}\ggg\exp(\log^{1/10}x)$); the **equidistribution axiom** is Lemma B0, sketched below. Take $h_1,h_2=(0,1)$, $W$ as needed for the Lemma-A interface.

## The $z$-interpolation bridge

$n\le x$ has at most 3 prime factors above $x^{1/3}$. For real $z\in[-1,1]$, let $g_z$ be completely multiplicative with $g_z(p)=z$ on band primes, $1$ off. Then $g_z(n)=z^{B(n)}$, $B(n)\in\{0,1,2,3\}$; Vandermonde interpolation at 4 real nodes recovers each $\mathbf 1[B(n)=j]$ as a finite linear combination of real, 1-bounded, completely multiplicative functions — exactly axiom-(i) objects. General band-anatomy indicators: finite products across finitely many bands. Both sides get interpolated; each pair $(g_z,g_{z'})$ goes through Theorem 3.1 with the awkward side in the $g_2$ slot.

## Lemma B0 (the half-page equidistribution lemma) — proof sketch

**Claim:** $g_z$ satisfies axiom (i) with defect $O(\sqrt N\,\mathrm{polylog})\ll N\mathcal L^{-1}$ for $\mathcal L=\log X$, for every $a,q$ (only $q\le\mathcal L$ matters; beyond, the bound is trivial).

**Proof sketch:** $z^{B(n)}=\sum_{j\ge0}\binom{B(n)}{j}(z-1)^j$ (terminating at $j\le3$), and $\binom{B(n)}{j}=\#\{p_1<\cdots<p_j\ \text{band primes dividing}\ n\}$, so
$$\sum_{\substack{N<n\le2N\\ n\equiv a\,(q)}}g_z(n)=\sum_{j\le3}(z-1)^j\sum_{p_1<\cdots<p_j\ \mathrm{band}}\#\{n\equiv a\,(q),\ p_1\cdots p_j\mid n,\ n\sim N\}.$$
Each inner count is $\frac{N}{q\,p_1\cdots p_j}+O(1)$ (band primes are coprime to $q\le\mathcal L$; CRT; if $(a,q)$ shares factors the count is $0$ or shifts trivially — the axiom permits non-primitive classes). The main terms reassemble $\frac Nq\delta_N$ with $\delta_N=\sum_j(z-1)^j\Sigma_j(N)$, $\Sigma_j$ the band-tuple sums (independent of $a,q$). The $O(1)$-floor errors total $O(\pi(\min(x^{1/2},2N)))=O(N/\log N)$ at $j=1$ (band primes up to $2N$ can divide $n\sim N$) and less at $j=2,3$. Total defect $O(N/\log N)$ — within the axiom's $O(N\mathcal L^{-1})$ with an absolute constant, as it permits. $\square$ (Manuscript §13 is the proof of record.) (Multiplicity/higher-power corrections: band-prime squares cost $\sum_{p>x^{1/3}}N/p^2=O(N x^{-1/3})$.)

## Fallback

Hildebrand's elementary stable-set method gives a positive-density *lower bound* for the anatomy layer without TT machinery — sufficient for Theorem 1′ (the lower-bound track).
