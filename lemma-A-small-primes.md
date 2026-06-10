# Lemma A: Small Primes Are Ignorable (Two-Sided)

**STATUS: PROVED — written (manuscript §15, June 10), via the binomial digit-counting sublemma; the $(1,0^{v-1})$ adaptation carried out.**

---

## Statement (informal)

For every $\varepsilon>0$ there is $\delta>0$ such that the contribution to membership in $D_0$ (on both the $n$ and $n-1$ sides) from primes $p\le n^\delta$ alters the density computation by at most $\varepsilon$: the carry conditions at small primes are satisfied with probability so close to their product model that they factor out of all independence statements.

## Source and the one-line change

Ford–Konyagin's own small-prime digit-counting (their §2) applies essentially verbatim. The single adaptation: on the shifted side the relevant low-digit pattern is $(1,0^{v-1})$ instead of $0^v$ (because $n\equiv1$, not $0$, modulo primes of $n-1$). One line changes; the counting is identical.

## Notes

- Friedlander–Iwaniec-style handling is the fallback if any uniformity issue appears at the $\delta$-boundary.
- Output feeds the assembly as a removable $\varepsilon$-loss; no interaction with Lemmas B/C/D beyond fixing $\delta$.
