# Skeleton tests addendum — results, discoveries, status updates

Companion to `K1_SKELETON.md`. All measurements at $n\in[5\times10^8,
2\times10^9]$, $250{,}000$ samples per run, three independent runs
(`lemma_tests.py`, `lemma_tests_clean.py`, `lemma_tests_interior.py`).

## 1. Test results

**T1 — Lemma B (anatomy independence on $(n,n-1)$).**

| event pair | $P(n)$ | $P(n{-}1)$ | joint/product | SE |
|---|---|---|---|---|
| $\sqrt{2n}$-smooth | 0.3113 | 0.3120 | 0.969 | 0.006 |
| $\ge1$ band prime | 0.3212 | 0.3209 | 0.994 | 0.006 |
| $P^+\le n^{0.40}$ | 0.1295 | 0.1300 | 0.936 | 0.015 |

Mild finite-scale anti-correlation, same magnitude as the $0.92$ ratio in the
governor-pair measurement — exactly the deviation [T18] says vanishes in
logarithmic density. **PASS.**

**T2 — digit marginals.** Raw band primes: $P(\text{succ})=0.525$, decile
$\chi^2=380$ — *explained, not anomalous* (see §2.1). Restricted to interior
digits ($p^2\le n^{0.95}$): $P(\text{succ})=0.4969/0.5005$ ($\pm0.0018$),
$\chi^2 = 15.2/24.0$ on df $9$. **PASS after the top-digit correction.**

**T3 — within-side joint (FK's own territory).** Ratio joint/product $=0.952,
0.959, 0.962$ across the three runs ($\pm0.011$–$0.016$ each; jointly
$\sim5\sigma$ below 1). A real finite-scale effect — see §2.2. Not a skeleton
risk (FK's theorem already covers the asymptotic), but a quantitative
benchmark any error-term bookkeeping must beat.

**T4 — cross-side joint (Lemma D core).** Ratio $=0.984,\ 1.003,\ 0.995$
($\pm0.010$–$0.013$): consistent with $1$ in every run. Sharpest conditioning
probe: $P(\text{succ}_n)=0.5326$ vs
$P(\text{succ}_n\mid n{-}1\ \text{smooth})=0.5321$ ($\pm0.0032$) — dead flat.
**PASS. The hard core's independence assumption is empirically immaculate,
and notably cleaner than the within-side case.**

**T5 — Theorem 1 quantities at $10^9$.** $P(n\in D_0)=0.12308$ (FK's own
finite-scale value: $0.1238$); margin costs: $D_0^{(+)}$ identical to $D_0$
on the sample, $D_0^{(-)}$ larger by $6\times10^{-5}$ — **Lemma 0′ is
numerically free**; joint/product $=0.917\pm0.015$, consistent with all prior
measurements and with convergence to $c_1^2=0.01305$.

## 2. Two structural discoveries (both now folded into the skeleton)

**2.1 Top-digit determinism.** For band primes ($\tfrac13<u<\tfrac12$) the
$j{=}2$ carry digit is the *top* base-$p$ digit of $n$, so its law is the
explicit piecewise function of the size ratio $n/p^2$: forced success for
$p^2\in(n,2n]$ and $p^2\in(n/2,2n/3]$, forced failure for $p^2\in(2n/3,n]$,
etc., converging to a fair coin only deep in the interior. This is precisely
what Ford–Konyagin's $g_j=\lfloor 1/U_j\rfloor-1$ integrates; the raw data
fingerprints their boundary terms ($0.577$ success in the $u\in[0.45,0.52)$
bucket; restored to $0.500$ interior). *Drafting consequence:* Lemmas C/D
must claim equidistribution only for interior digits, with the top digit
handled by this deterministic law.

**2.2 Equidistribution is ensemble-only.** For fixed primes, cofactor ranges
are far shorter than products of the relevant moduli, so joint digit
uniformity is false pointwise and emerges only after averaging over the prime
ensemble — the precise reason FK's "simultaneous fractional parts" section is
the analytic heart, and the correction applied to the skeleton's §6 (the old
"CRT, no obstruction" remark was too glib). The persistent within-side
$\approx4\%$ deficit (T3) is this phenomenon at finite scale; intriguingly the
cross-side coupling (T4) shows *no* measurable counterpart — the $+1$ shift
appears to decorrelate better than the within-integer multiplicative link, a
small empirical gift to Lemma D.

## 3. Literature assessment: Tao–Teräväinen arXiv:2512.01739 (+ Pilatte)

The December 2025 Tao–Teräväinen paper supplies, as its core tool, *"a general
quantitative estimate for two-point correlations of multiplicative functions
with a small power of logarithm saving"*, derived from Pilatte's recent
correlation estimates, and applies it through a **circle method (frequencies)
→ Pilatte minor arcs → sieve major arcs** pipeline to prove a genuine joint
statement about $(n,n+1)$ (the Erdős–Pomerance–Sárközy asymptotic for
$\omega(n)=\omega(n+1)$) at almost all scales. Implications:

1. **Lemma B status upgrade:** quantitative two-point correlation engines now
   exist (Pilatte) with power-of-log savings — enough room to compose with
   FK-style error terms; the $z$-trick functions are bounded real
   multiplicative, squarely in scope. Risk drops to low.
2. **Lemma D has a named template:** our digit conditions are already
   frequency-side objects ($e(\theta n/p^a)$), i.e. the circle-method encoding
   is *native* to our problem; the open question is precisely whether Pilatte's
   minor-arc estimates tolerate frequencies tied to divisors of $n$
   (under $n=pm$ the phase is a function of the cofactor — the invariance
   their dilation arguments exploit). This is now a *reading task with a
   concrete target*, not a blank-page problem.
3. **The fallback ladder is the frontier:** their stated limitation —
   pairwise correlation technology requires logarithmic averaging or almost
   all scales — is verbatim our Theorem 1/1″ dichotomy. Theorem 1″ (almost
   all scales) may be the realistic first theorem; it still yields infinitude,
   i.e. genuine progress on Erdős 396's hard side.

## 4. Updated risk register

| item | before | after tests + literature |
|---|---|---|
| Lemma 0/0′ | verified small-scale | verified at $10^9$; margins free; ready to write formally |
| Lemma A | [KA] | [KA] — unchanged, ready to write |
| Lemma B | [N plausible] | [N, low risk] — Pilatte/TT engines named; empirics clean |
| Lemma C | [N] | [N] — restate with top-digit law; FK finite-scale benchmark recorded |
| Lemma D | [HC] | [HC, plausibility ↑] — empirics immaculate (3 runs), TT pipeline template identified |
| Theorem 1″ | fallback | likely the realistic first theorem (matches technology frontier) |

## 5. Next actions, in order

1. Fetch Pilatte's paper and TT's general two-point estimate (their §2);
   check hypotheses against the $z$-trick functions (Lemma B) and the
   cofactor-invariance structure (Lemma D). One session of careful reading.
2. Write Lemma 0/0′ and Lemma A formally (lowest risk; fully specified;
   ~2–3 pages total). This is the natural start of an actual manuscript.
3. ~~Stability probe of $D_0$~~ **DONE**: $D_0$ is *not* Hildebrand-stable —
   disagreement rates under dilation by $d=2,3,5$ are $0.177,\,0.143,\,0.179$
   at $n<3\times10^5$ (stability needs $\to0$; independence would give
   $0.207$ — membership of $n$ and $dn$ is mildly positively correlated, but
   stability fails outright). The soft route is closed even for pairs; the
   skeleton's correlation machinery is the only road. (`stability_probe.py`)
4. Then the fork: attempt Lemma B via Pilatte (paper-writing mode), or run
   the BW-witness carry-profile computation (the $k\ge2$ track) in parallel.

