# Citations Ledger

Theorems and papers this proof needs (or may need) to cite. **Status:** PINNED = exact statement verified against source; PARTIAL = located, statement extraction incomplete; TO-PIN = referenced from memory/sessions, must be located and verified before citation.

## A. The problem and its prior art

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Kummer 1852 | $v_p\binom{2n}{n}=\#$carries doubling $n$ base $p$ | Everywhere (Lemma 0) | PINNED (classical) |
| Pomerance 2014, *Divisors of the middle binomial coefficient*, Amer. Math. Monthly | Governor set $D_0$; infinitude of $(n-k)\mid\binom{2n}{n}$, upper density $<1/3$; $(n+i)$-product density 1 | §1 framing; Lemma 0 | PARTIAL (verify exact statements) |
| Ford–Konyagin 2020, *Divisibility of the central binomial coefficient*, Trans. AMS | $d(D_0)=c_1=0.11424$; digit-counting (§2, small primes); exponential-sum machinery; piecewise top-digit law; §7 numerics | Lemmas A, C; constants | PARTIAL (we use their internal structure heavily — re-read with our notation) |
| Granville–Ramaré 1996 | squarefree $\binom{2n}{n}$ (context only) | intro | TO-PIN |
| Erdős–Graham 1980 [ErGr80] | problem source | intro | TO-PIN |

## B. Correlation machinery (Lemma B; D-verdict)

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Tao–Teräväinen, arXiv:2512.01739 (**v2, Apr 2026**), **Thm 3.1** (§3, `thm:correlation`) | quantitative binary correlations; asymmetric hypotheses ($g_1$ equidistributed w/ explicit axiom + technical condition $g_1(p)=1$ on $[\exp(\log^{1/11}X),\exp(\log^{1/10}X)]$, $g_2$ only 1-bounded multiplicative); $W$-trick + shifts $O(\mathcal L^c)$; exceptional scale set $\mathcal L^{-c}$; smooth-pair $\rho(u)\rho(v)$ uniform in $u,v\le c\log_2x/\log_3x$ | Lemma B (cite); D verdict | **PINNED** (WP3b done June 9: v2 TeX source close-read; verbatim statement in `lemma-B-anatomy-independence.md`) |
| Pilatte, arXiv:2310.19357 | two-point log-Chowla, power-of-log saving; Thm 2.4 spectral engine needs only 1-boundedness; multiplicativity at exactly two steps (centring, dilation) | Lemma B engine; D attack (c) | PARTIAL |
| Matomäki–Radziwiłł–Tao | mult. fns in short intervals; averaged Elliott | Pilatte centring; Lemma C inputs | TO-PIN (which paper(s)) |
| Hildebrand (consecutive smooth, elementary) | positive-density lower bound for anatomy layer | Lemma B fallback | TO-PIN |
| Tenenbaum–Tricot | smooth-pair probability $\rho(u)^2$ | dead-end analysis (§ smooth-cofactor) | TO-PIN |

## C. Fermat quotients, Heilbronn sums, deep characters (Lemma D)

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Heath-Brown 1996, *An estimate for Heilbronn's exponential sum* | first power-saving Heilbronn bound | D backbone | PARTIAL |
| Heath-Brown–Konyagin 2000, Quart. J. Math. 51 | improved Heilbronn/Gauss-from-$k$th-powers bounds | D backbone | PARTIAL |
| Shkredov (several, e.g. arXiv:1302.3839) | further Heilbronn refinements; subgroup intersections | D backbone | TO-PIN (pick best exponent) |
| Bourgain–Ford–Konyagin–Shparlinski 2010, Michigan Math. J. 59 | divisibility of Fermat quotients; subgroup distribution tools | D | PARTIAL |
| **Shparlinski 2011, Bull. LMS (arXiv:1104.3909)** | Thm 8: FQ sums avg over modulus, $N\ge p^\varepsilon$; **(10): arbitrary primitive chars mod $p^2$**; lengths vary with modulus; §4: extends to primes; initial intervals only | D attack — backbone of small-$\lambda$ coverage | **PINNED (close-read June 9)** |
| Garaev 2006, Monat. Math. 148 | the completion method underlying Thm 8; sums over primes variant | adaptation lemmas $\alpha,\gamma$ | TO-PIN (read next) |
| Baier–Zhao 2008, J. Number Theory 128 | large sieve for **square moduli** (Lemma 6 in Shp.) | the engine | TO-PIN (read next) |
| Baier–Zhao 2005, Int. J. Number Theory 1 | large sieve, powerful moduli ($p^k$, $k\ge2$) | higher-exponent bookkeeping | TO-PIN |
| Zhao 2004, Acta Arith. 112 (conjecture) | classical-shape square-moduli sieve — would simplify everything | upgrade path | TO-PIN |
| Shparlinski, Quart. J. Math. (character sums with FQ) | mult. character sums with $q_p(n)$ | context | TO-PIN |
| Shparlinski, Bull. Aust. Math. Soc. (FQ of primes) | mult. character sums with FQ **of primes** | $\gamma$ context | TO-PIN |
| Heath-Brown (consecutive FQ sums) | individual threshold $N\ge p^{1/2+\varepsilon}$ | D numerology baseline | PARTIAL |
| Chang 2012, Acta Arith. 152 | short character sums with Fermat quotients | D numerology | TO-PIN |
| Ostafe–Shparlinski 2011, SIAM J. Discr. Math. 25 | pseudorandomness/dynamics of FQs | D context | TO-PIN |
| Baier–Zhao | large sieve with **square moduli** — directly our conductor family $q^2$ | D attack (b) | TO-PIN (priority) |
| Cilleruelo–Garaev | multiplicative energy: intervals vs subgroups | D §6 | TO-PIN |
| Bourgain–Garaev 2014, Izv. Math. 78 | sumsets of reciprocals in prime fields; multilinear Kloosterman | D† second-moment core | TO-PIN (priority) |
| Fouvry–Michel (and successors) | Kloosterman-type sums over primes | (bypassed by WP2.1 route; keep as fallback) | TO-PIN |
| Harper 2016, Compositio Math. 152 | smooth Weyl sums, major/minor dichotomy | D†-anatomy **fallback** (demoted by WP2.3: $u_f<2$ unwinding) | PINNED (located) |
| de la Bretèche–Tenenbaum 2007, Funct. Approx. 37 | friable exponential sums, rational arguments | D†-anatomy fallback | PINNED (located) |
| Vinogradov / Balog (primes in APs vs linear phases) + Vaughan identity | the large-$\Lambda$ ranges of the WP2.3 unwinding | D†-anatomy (primary now) | standard refs |
| de la Bretèche 1998, PLMS 77 | foundational friable exponential sums | D†-anatomy | PINNED (located) |
| **Fouvry–Tenenbaum 1991, PLMS 63** | friable numbers in arithmetic progressions | D†-anatomy + B/C interfaces | PINNED (located) |
| Drappeau 2015, Canad. J. Math. 67; Drappeau–Shao 2016, Acta Arith. 176 | friable exponential sums, Weyl-type means | D†-anatomy | PINNED (located) |
| de la Bretèche–Granville 2022, Trans. AMS 375 | exponential sums with multiplicative coefficients | D†-anatomy alternative route | PINNED (located) |
| Iwaniec–Kowalski / Vaughan Lemma 2.2-type (inhomogeneous Vinogradov counting) | the D†-minor write-up | `wp22-minor-major.md` §1 | standard refs |
| Shparlinski, *Open problems on exponential and character sums*, Problem 46 | nearby FQ regimes flagged "very difficult" — calibrates the $u<u'$ corner | D risk register | PINNED (read June 9) |

## D. Dispersion / equidistribution / tools

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Bombieri–Friedlander–Iwaniec (dispersion series) | dispersion to large moduli — what D sits beyond for general coefficients | D framing | TO-PIN |
| **Granville–Shao, arXiv:1703.06865** (Adv. Math 2019) | BV for mult. functions; fixed residue class to moduli $x^{20/39-\delta}$ (beyond $x^{1/2}$); companion (Forum Math. Sigma): BV $\iff$ Siegel–Walfisz criterion for $g$ | Lemma C weighted layer | **PINNED (WP3, June 10)** |
| **Drappeau–Granville–Shao, arXiv:1704.04831** | *smooth-supported* mult. functions in APs to $x^{3/5-\varepsilon}$ — native fit (our weights live on $\sqrt{}$-smooth populations) | Lemma C, extra range | PINNED (located June 10) |
| **Montgomery–Vaughan 1977, Invent. Math. 43, 69–82** | $\sum_{n\le x}f(n)e(n\alpha)\ll x/\log x+(x/\sqrt R)(\log R)^{3/2}$, uniform over 1-bounded multiplicative $f$, where $|\alpha-a/q|\le q^{-2}$, $(a,q)=1$, $R=\min(q,x/q)$ | Lemma C minor pairs (the DMV input, manuscript §14) | **PINNED (June 10)** |
| ~~Friedlander–Iwaniec, simultaneous fractional parts~~ | **RETIRED (WP3, June 10): not locatable as an actual paper (session-memory artifact); the thin-progression phenomenon is handled by our own two-frequency machinery (manuscript §§6–8)** | Lemma C | RESOLVED |
| Vaaler | trigonometric approximation of interval indicators, degree $H$ | D harmonic form | TO-PIN |
| Burgess | character sums mod cube-free $q^2$, nontrivial for $N>q^{2(1/4+\varepsilon)}$ | D (classical layer) | TO-PIN |
| Balog–Wooley | explicit constructions with congruence freedom | Route C (general $k$) | TO-PIN |
| Tao(–Teräväinen) $k$-point correlation state of the art; log-Chowla open for even $k\ge4$ | bridge-to-general-$k$ risk calibration | WP5 | TO-PIN |

## E. Smooth windows / constructive route (WP5)

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| **Balog–Wooley 1998, J. Austral. Math. Soc. A 64, 266–276** | strings of $n^{1/u}$-smooth consecutive integers, length $\log_4 n$; cyclotomic mechanism $x-i=i(z_i^{\gamma_i}-1)$, CRT exponents, polylog moduli; family entropy $O(t\log\log X)$ | WP5 core; the FQ-convergence discovery | **PINNED (source read June 10)** |
| Hildebrand, *On integer sets containing strings of consecutive integers* | $k$-strings of $n^{\alpha}$-smooth with positive density for $\alpha>e^{-1/(k-1)}$ — the dense-window input, admissible vs the $\sqrt{}$-ceiling only for $k\le2$ | WP5a ($k=2$ rung) | TO-PIN (priority — exact statement + density) |
| Balog–Ruzsa (smooth pairs) | positive density of $n$ with $n, an+c$ both $n^{\beta}$-smooth, any $\beta>0$ | $k=1$ window family | TO-PIN |
| Eggleton–Selfridge | early strings of $\le5$ smooth consecutive integers | context | TO-PIN |
| Balog–Erdős–Tenenbaum + Heath-Brown construction | pairs $n,n+1$ smooth to $\exp(8\log n\log_3 n/\log_2 n)$ — depth record for pairs | WP5 upgrade path | TO-PIN |

## Our own citable artifacts

| Item | Status |
|---|---|
| Deep large sieve for FQ characters (`prop-deep-large-sieve.md`) | PROVED June 9 (numerically verified); LaTeX pending |
| Lemma 0 exact sandwich (`lemma-0-sandwich.md`) | PROVED (machine-verified); writeup pending |
