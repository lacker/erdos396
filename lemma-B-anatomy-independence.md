# Lemma B: Anatomy Independence of $n$ and $n-1$

**STATUS: LIKELY CITABLE — pending three fine-print checks and a half-page bridging lemma.** Probability: ~85%.

---

## Statement (informal)

The *anatomies* of $n$ and $n-1$ — the joint size-distribution of their prime factors above $x^\delta$, in particular $\sqrt{2\cdot}$-smoothness and the existence/position of band primes in $((2\cdot)^{1/3},\sqrt{2\cdot}]$ — are asymptotically independent, quantitatively, at almost all scales.

## Citation route

**Tao–Teräväinen (arXiv 2512.01739, Dec 2025), Theorem 3.1**, built on **Pilatte (arXiv 2310.19357)**: quantitative binary correlations with power-of-log savings; they prove the consecutive-smooth asymptotic $\rho(u)\rho(v)$ at almost all scales. Crucial structural fact: **the hypotheses are asymmetric** — $g_1$ must be equidistributed (real case) or non-pretentious (complex case), while $g_2$ needs only 1-bounded multiplicative. Strategy: put the awkward function in the $g_2$ slot.

## The $z$-interpolation bridge

**[reconstructed — re-verify against a clean derivation]:** $n\le x$ has at most 3 prime factors above $x^{1/3}$. For $z\in\mathbb{C}$, let $g_z$ be completely multiplicative with $g_z(p)=z$ on band primes, $1$ off. Then $g_z(n)=z^{B(n)}$ where $B(n)\in\{0,1,2,3\}$ counts band primes of $n$; interpolating at 4 values of $z$ (Vandermonde) expresses each indicator $\mathbf{1}[B(n)=j]$ as a finite linear combination of 1-bounded multiplicative functions — exactly TT-admissible objects. The general band-anatomy indicators are finite products/combinations of such $g_z$'s across finitely many bands.

## The three fine-print checks (open)

1. **Uniformity in $x$:** TT/Pilatte state theorems for fixed functions; ours scale with $x$ (bands $\sim x^\alpha$). Verify their estimates are uniform over this dependence (expected yes — the savings are explicit).
2. **Conclusion shape:** confirm Theorem 3.1 delivers correlation $=$ product of means $+\,$error (the equidistributed-case mechanism, the same way they treat $\omega(n)=\omega(n+1)$). Confidence: high.
3. **Exact statement of Theorem 3.1:** the verification fetch was in progress when the original chat died. Re-fetch and finish (task in roadmap).

Mean-value sanity check already done: for the relevant $g_z$, equidistribution holds (e.g. $g_z(2)=1$ forces equality of means over even vs all integers).

## Fallback

Hildebrand's elementary stable-set method gives a positive-density *lower bound* for the anatomy layer without TT machinery — sufficient for Theorem 1′ (the lower-bound track).
