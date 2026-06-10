# WP5 Diagnosis: The Constructive Route to Literal Erdős 396

**STATUS: DIAGNOSIS COMPLETE (June 10, 2026).** Verdict: the route is *coherent but blocked at general $k$ by a quantifiable entropy obstruction*; two genuine discoveries: (i) the constructive route's digit core is the **same Fermat-quotient equidistribution** the $k=1$ program already built tools for (the deep large sieve is dual-use); (ii) the binding requirement is **entropy-rich families of $\sqrt{2n}$-smooth windows**, which exist in the literature only for $k\le2$. Probability that this approach resolves literal 396: **~10%** (sharpened, not lowered: the mass moved from "unknown" to "known obstruction with named attack surface"). Script: `wp5_witness_scan.py`.

Literal problem (pinned, erdosproblems.com/396): *for every $k$, does there exist $n$ with $\prod_{0\le i\le k}(n-i)\mid\binom{2n}{n}$?*

---

## 1. Witness landscape (data)

Scan to $2\times10^6$ + re-verification of all seven A375077 records (1→2, 2→2480, 3→8178, 4→45153, 5→3648841, 6→7979090, 7→101130029 — all PASS):

| $k\ge$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| density | $1.20\times10^{-1}$ | $1.26\times10^{-2}$ | $1.22\times10^{-3}$ | $1.21\times10^{-4}$ | $1.0\times10^{-5}$ |

**Almost exactly geometric with ratio $\approx10\approx1/c_1$** ($c_1=0.1142$): the data supports density $\approx c_1^{k+1}$, i.e. *independence at every order* — strong truth-evidence for the analytic route at all $k$ (and for the conjecture that witnesses have positive density for every fixed $k$, far beyond the problem's ask).

## 2. The coin model fails informatively

On the $\sqrt{2n}$-smooth-window population at $k=2$ (the only population where witnesses can live — Tier-B's exact lemma), conditioning on the number $m$ of band primes in the window:

P(witness | m) = .069, .060, .061, .052, .039, .030, .016 for m = 0..6 — per-band-prime cost ≈ 0.75–0.87, **not** 1/2.

Reason: by *count*, band primes cluster near the top of the band, where the Ford–Konyagin piecewise law makes the slot-2 carry **deterministic by size alone**: $q^2\in(n,2n]$ auto-success, $q^2\in(2n/3,n]$ auto-fail, alternating slivers (≈29% of band primes by count sit in the first auto-success sliver). A constant fraction of band primes are free wins; only the rest are coins. Also $P(\text{witness}\mid m{=}0)=6.9\%$, not $\approx1$: mid-depth primes ($\ge2$ free slots each) still carry $\Theta(1)$ aggregate failure mass. The right model is the FK *product* law over all window primes, not band-coins only.

**Design consequence:** a construction should select band primes into auto-success slivers — an archimedean (size) condition needing *zero* digit input — and only the mid-depth primes need genuine digit equidistribution.

## 3. Absolute counting is dead at every smoothness level (unified dead-end)

Any density comparison "bad-digit mass vs window-family mass" with *absolute* (unconditioned) FK-type counts loses: window families of $n^{1/u}$-smooth strings have density $\lesssim\rho(u)^{k+1}\approx e^{-(k+1)u\log u}$, while the unconditioned bad-digit mass at primes of size $n^{1/u}$ is $\asymp2^{-u}=e^{-u\log2}$; winning needs $(k+1)\log u<\log2$, i.e. $u<2^{1/(k+1)}<2$ — but the Tier-A lemma **forces** $u\ge2$ ($\sqrt{2n}$-smoothness). Dead for all $k\ge1$. This unifies and quantifies the two recorded dead-ends (smooth-cofactor $\rho$ vs $e^{-c/\delta}$; union bounds): *any* viable argument must equidistribute digits **within** the window family (or construct families where digits are controlled). The data says the same thing: $P[C\mid S]=11\%$ at $k=1$ — carries cost full price inside the smooth population.

## 4. Anatomy of the Balog–Wooley construction (source read, June 10)

B–W 1998 (J. Austral. Math. Soc. A **64**, 266–276; now PINNED): for every $u>1$, infinitely many strings $n+1,\dots,n+t(n)$ of $n^{1/u}$-smooth integers with $t(n)=[\log_4n/\log(3u)]\to\infty$. Mechanism (their Lemma 2.2 with $k_i=1,a_i=1,b_i=i$):

- Partition primes $\le y$ into classes $P_1,\dots,P_t$ (Lemma 2.1); $\gamma_j=\prod_{p\in P_j}p$, $\Gamma=\gamma_1\cdots\gamma_t\le e^{5y/4}$ with $y\asymp\log_2n$ — **polylog-size moduli**.
- CRT-choose exponents and set $x=2^\Gamma\prod_ja_j^{\lambda_j}b_j^{\mu_j}$; then $x-i=i(z_i^{\gamma_i}-1)$ with explicit $z_i$, **simultaneously for all $i$** — equivalently $x=i\,z_i^{\gamma_i}$ for every $i$.
- Smoothness of each $z^{\gamma}-1$ via cyclotomic factorization: all prime factors $\le z^{\varphi(\gamma)}$, and $\varphi(\gamma)/\gamma$ is small by the class design.

**Discovery (route convergence).** For a window prime $q\mid x-i$: $q\mid z_i^{\gamma_i}-1$, and the slot-2 digit of $x$ base $q$ is
$$\frac{x}{q}\bmod q\ \longleftrightarrow\ i\cdot\frac{\gamma_i}{e}\cdot\frac{z_i^{e}-1}{q}\bmod q\qquad(e=\mathrm{ord}_q(z_i)),$$
**a Fermat-quotient of $z_i$ at $q$** — the exact object of `prop-deep-large-sieve.md`. The constructive route's digit layer and Lemma D's digit layer share their core; the homomorphism $\ell_q(z\cdot a^m)=\ell_q(z)+m\,\ell_q(a)$ even makes the digit *linear in the construction's exponent parameters*, so digits at chosen primes can be CRT-forced.

## 5. The entropy obstruction (the route's proof-of-death at general $k$, as currently equipped)

Forcing/averaging digits requires parameter entropy comparable to the window's prime log-mass ($\asymp\log x$). The B–W family's free parameters are exponent shifts $\lambda_j\mapsto\lambda_j+r_j\gamma_j$: the $x\le X$ values number $(\log X)^{O(t)}$ — **entropy $O(t\log\log X)\lll\log X$**. So within pure B–W one can force digits at only $o(1)$ of the prime mass, and there is no room to average. The route therefore needs **dense families of $\sqrt{2n}$-smooth windows** (entropy $\gtrsim\log x$, i.e. $X^{\theta}$-many strings):

| $k$ | dense $\sqrt{}$-smooth window family known? |
|---|---|
| 1 | YES — Hildebrand '85 / Balog–Ruzsa: positive density of $n^{\beta}$-smooth pairs, any $\beta>0$ |
| 2 | MARGINAL — Hildebrand's $k$-strings: positive density at smoothness $\alpha>e^{-1/(k-1)}$; for $k=2$, $\alpha\in(0.368,0.5)$ is admissible — inside the $\sqrt{}$-ceiling |
| $\ge3$ | NO — $e^{-1/(k-1)}>1/2$ for $k\ge3$; only the entropy-poor B–W-type constructions exist |

This is a clean, quantitative reduction: **literal 396 via this route $\Leftarrow$ entropy-rich $\sqrt{2n}$-smooth window families for every $k$ + family-FQ-digit equidistribution (deep-large-sieve species, upper-bound-only).** The first input is an open problem adjacent to a known-hard area (consecutive smooth numbers); the second is the program's existing wheelhouse.

## 6. Verdict, calibration, and live sub-routes

- **$k=2$ rung (next theorem after $k=1$): genuinely approachable.** Hildebrand-density windows at $\alpha\in(0.368,0.5)$ + the $k=1$ program's D-machinery run on a positive-density family (upper-bound form, the easier mode). Data: 2433 witnesses to $2\times10^6$; band-free 3-windows exist with positive-looking density. Recommended as WP5a when the $k=1$ paper stabilizes.
- **General $k$:** blocked pending either (a) entropy-rich smooth-window constructions (a concrete, well-posed open target — e.g. multi-base B–W variants; entropy grows linearly in the number of independent bases; flag for a future reading/derivation session), or (b) the analytic $(k{+}1)$-point route (field frontier). The data ($c_1^{k+1}$ geometric decay) says the *statement* is true at every order; the obstruction is technology, not truth.
- **Dead ends recorded:** absolute-counting comparisons at any smoothness (§3, subsumes two old dead-ends); pure-B–W + CRT forcing (entropy count, §5); $n=m^2$ family (Tier-B, retained).
- **P(literal 396 resolved by this program's approach): ~10%** — sharpened: ~½ of the residual mass sits on "entropy-rich windows turn out constructible," ~½ on the long-horizon analytic route. P($k=2$ theorem by this program: ~35–40%). The $k=1$ targets are unaffected (~50% full / ~75% lower-bound).

## 7. Citations to pin (added to ledger)

Balog–Wooley 1998 (PINNED, source read); Hildebrand, *On integer sets containing strings of consecutive integers* (the $k$-string positive-density input — pin exact statement next); Balog–Ruzsa (smooth pairs positive density); Eggleton–Selfridge (early strings); Balog–Erdős–Tenenbaum + Heath-Brown (pair smoothness $\exp(8\log n\log_3n/\log_2n)$ — the depth record for pairs).
