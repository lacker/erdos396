# WP1.5: Band Empirics — The $\delta$-Probe

**STATUS: COMPLETE (June 9, 2026). VERDICT: square-root cancellation confirmed on real coupled populations → G1 = PASS** (with one localized flag, §4). Script: `empirics_d.py`, runtime ~minutes at $x=10^8$.

---

## 1. Design

The linearization fact ($\ell_q(1+qm)=-m$) makes the probe direct: for band primes $q$ at five strata $\gamma\in\{0.37,0.40,0.43,0.46,0.48\}$, build the **real Lemma-D population** — $n=1+qm\le x$, sieved to exactly one simple band prime $p\mid n$, cofactor $a=n/p$ — and measure
$$T_q(\lambda)=\sum_{\text{pop}}\Big(\mathbf{1}[a\bmod p\ge p/2]-\tfrac12\Big)\,e(-\lambda m/q),$$
the centered, digit-decorated deep-character sum: **exactly the $E_q$ integrand**, coupling and all. Benchmark $z=|T|/\sqrt{\sum w^2}$: square-root cancellation $\Rightarrow z=O(1)$ (Rayleigh, RMS 1); genuine cross-side correlation $\Rightarrow z\sim\sqrt{N_{\text{pop}}}/2\approx30\text{–}80$ at these sizes. Controls: the *unweighted* sum on the same population (isolates population-shape effects, which belong to Lemmas B/C, not D), and an interior-$p$ restriction ($p^2\le x/2$, guarding the $n$-side top-digit determinism).

## 2. Results ($x=10^8$; populations 3.6k–27.5k per stratum)

| $\gamma$ | $q$ | $N_{\text{pop}}$ | RMS $z$ ($\lambda\in[1,8]\cup$mid) | max $z$ | unweighted control $z$ ($\lambda=1,2,3$) | $P(\text{digit})$ / interior |
|---|---|---|---|---|---|---|
| 0.37 | 919 | 27531 | 0.95 | 1.77 | 0.88, 0.45, 0.77 | 0.453 / 0.486 |
| 0.40 | 1597 | 15854 | 1.19 | 2.53 | 0.52, 0.16, 0.87 | 0.446 / 0.480 |
| 0.43 | 2767 | 9161 | 1.22 | 2.20 | 2.27, 1.25, 0.74 | 0.449 / 0.482 |
| 0.46 | 4787 | 5273 | 1.19 | 2.01 | **5.47**, 1.93, 1.53 | 0.453 / 0.489 |
| 0.48 | 6947 | 3615 | 1.39 | 2.46 | **3.72, 3.23, 2.97** | 0.459 / 0.498 |

Cross-$q$ phase-aligned aggregate at $h=1$: $z=2.00$ (no constructive alignment across the band).

## 3. Interpretation

1. **The $\delta$-probe is clean.** The decorated centered sums sit at $z=O(1)$ at every stratum and every harmonic — RMS 0.95–1.39 against the Rayleigh baseline of 1, with max 2.5 over ~55 draws (unremarkable). Correlation-scale signal would be $z\approx30$–$80$. **The assembly cancellation is real in data.**
2. **The conditional structure of Lemma D is visible.** At the top strata the *unweighted control* blows up ($z=5.5$ at $\gamma=0.46$, $\lambda=1$) — the known boundary effect: $M/q=x^{1-2\gamma}$ is only ~2 periods at $\gamma=0.48$, so the anatomy-selected population itself doesn't equidistribute mod $q$. **But the decorated sums stay flat even there**: the digit decoration decorrelates from $m\bmod q$ even when the population is biased. That is precisely the division of labor in the proof (B/C own the undecorated count; D only needs the decoration to decorrelate) — confirmed empirically.
3. **Known fine structure reproduced.** Raw digit rate 0.45 (vs 0.5), recovering to 0.48–0.50 on interior $p$ — the FK top-digit piecewise law, matching the original session's 0.4841 finding.

## 4. The one flag

At $\lambda=1$ the decorated $z$ rises monotonically with $\gamma$ (0.82 → 2.46). Interior-$p$ restriction flattens the top of the trend (1.37 at $\gamma=0.48$), implicating residual top-digit/boundary structure rather than cross-side correlation. Magnitude is tiny (2.5 vs correlation-scale 30+), and the $\eta$-trim mitigation covers it for the lower-bound track — but this is the empirical marker of where the **full**-asymptotic version must work hardest: smallest harmonics, top of band. **[Resolved by WP2.1]:** the drift is the $\mu/\lambda=1$ major arc ($p$ near $q$ at the top of the band) — see `wp21-reduction.md` §3. It is structure to be counted, not noise to shrink.

## 5. Gate decision

**G1 = PASS** — basis re-examined after the WP2.0 erratum and retained: (i) the empirical evidence here measured Estimate D†'s object *directly* and stands unchanged; (ii) D† is log-target, parity-free, with an identified second-moment core adjacent to named literature; (iii) no kill criterion met. The withdrawn part was the numerology's coverage claim, not anything measured here. Proceed to WP2: draft adaptation lemmas $\alpha,\beta,\gamma$, then attack the assembly $\delta$ with the deep large sieve + Shparlinski mechanism + the moving-frequency linearized form. Full-D probability: **~35–40%** (empirics removed the "structurally broken" branch; provability risk in $\delta$ remains).
