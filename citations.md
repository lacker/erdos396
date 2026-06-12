# Citations Ledger

Theorems and papers this proof needs (or may need) to cite. **Revised June 11, 2026** (post-WP10/11/12/13 audit): every row re-graded against its actual consumers (`wp9-theorem1prime.md` chain, `wp11-e3lb.md` ladder, `wp12-cdagger-lb-diagnosis.md`, `wp13-kuznetsov-bridge.md`, `wp10-g1.md`, `manuscript/sections/*.tex`).

**Status taxonomy (role-[consumer]-[grade]):**
- **LOAD-BEARING-[result]** — the named result consumes it quantitatively; grade appended:
  *paper-verbatim* (statement close-read against the source), *slide-verbatim* (transcribed from a survey/slides, paper re-confirmation flagged), *abstract-grade* (located, statement not extracted), *located* (bibliographic identification only), *classical* (textbook-standard).
- **SUPPORTING** — context, framing, provenance, or engine-behind-a-pinned-citation; nothing breaks if dropped.
- **FALLBACK** — held in reserve for a named alternative route; consumed only if the primary route is abandoned.
- **PRICED-DEAD-[reason]** — fetched/priced against a target and shown insufficient by a computed exponent gap; kept as proof-of-death (do not re-pay).
- **DEAD-END-CONTEXT** — belongs to an abandoned route or calibrates a dead end; context value only.
- **TO-PIN** — exact statement must still be located/verified before any citation.
- **UNVERIFIED-[why]** — claimed role could not be confirmed from the repo.

The conditional **Theorem 1′ chain** (the headline) consumes only the rows so marked in §A, §B, §D below; everything in §C, §F, §G is either attack-corpus for the two open hypotheses or dead. See `literature-dependencies.md` for the clean Theorem-1′-only table.

## A. The problem and its prior art

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Kummer 1852 | $v_p\binom{2n}{n}=\#$carries doubling $n$ base $p$ | Everywhere (prop:kummer, manuscript §2 — proof reproduced in-house) | LOAD-BEARING-[whole chain]-classical (proof in-house; citation is provenance) |
| Pomerance 2015, *Divisors of the middle binomial coefficient*, Amer. Math. Monthly **122 (2015), 636–644** [Pom15] (was misdated "2014") | Governor set $D_0$; infinitude of $(n-k)\mid\binom{2n}{n}$, upper density $<1/3$; $(n+i)$-product density 1 | §1 framing; sandwich context (03-sandwich line 88) | SUPPORTING-[intro/prior art]-located (bibliography entry ✓; exact statements still unchecked — harmless, nothing quantitative consumed) |
| Ford–Konyagin, *Divisibility of the central binomial coefficient*, **Trans. AMS 374 (2021), 923–953; arXiv:1909.03903** [FK21] (was misdated "2020") | $d(D_0)=c_1=0.11424$ (§7); small-prime digit counting (§2); piecewise top-digit/band-coin law; per-class probabilities; exponential-sum machinery (§§3–5) | **Theorem 1′ chain**: FK law (link 5, 04-architecture), per-class probability lower bounds (Gap G3 assembly), $c_1$ (§7) for links 2/11 + asymptotic target; Lemma A §2 = provenance only (proof now in-house, 15-spine lines 78–102) | **LOAD-BEARING-[link 5 windows + G3 assembly + $c_1$]-abstract-grade (PARTIAL)** — the close-read with our notation is still owed; G8 names the §7-constant + FK-law pinning explicitly |
| Granville–Ramaré 1996 | squarefree $\binom{2n}{n}$ (context only) | intro | SUPPORTING-TO-PIN (no bibliography entry yet) |
| Erdős–Graham 1980 [ErGr80] | problem source (Erdős 396) | intro | SUPPORTING-located (bibliography entry ✓) |

## B. Correlation machinery (Lemma B; D-verdict)

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Tao–Teräväinen, arXiv:2512.01739 (**v2, Apr 2026**), **Thm 3.1** (§3, `thm:correlation`) [TT25] | quantitative binary correlations; asymmetric hypotheses ($g_1$ equidistributed w/ explicit axiom + technical condition $g_1(p)=1$ on $[\exp(\log^{1/11}X),\exp(\log^{1/10}X)]$, $g_2$ only 1-bounded multiplicative); $W$-trick + shifts $O(\mathcal L^c)$; exceptional scale set $\mathcal L^{-c}$; smooth-pair $\rho(u)\rho(v)$ uniform in $u,v\le c\log_2x/\log_3x$ | **Theorem 1′ link 4** (TT-route of prop:B-assembled); Lemma B; D verdict | **LOAD-BEARING-[link 4 / Lemma B]-paper-verbatim** (WP3b June 9: v2 TeX source close-read; verbatim statement in `lemma-B-anatomy-independence.md`). HYGIENE: bibliography.tex note "verification pending" is STALE — fix with G7 |
| Pilatte, arXiv:2310.19357 [Pil23] | two-point log-Chowla, power-of-log saving; Thm 2.4 spectral engine needs only 1-boundedness | engine behind TT25 (not cited directly by the chain) | SUPPORTING-located (PARTIAL extraction; no direct consumer left) |
| Matomäki–Radziwiłł–Tao [MRT] (Algebra NT 9 (2015) + successors) | mult. fns in short intervals; averaged Elliott | Halász–MRT remark in 14-lemmaC (asymptotic track, statusO); Pilatte centring | SUPPORTING-TO-PIN (which successor papers — only if the asymptotic-track absorption remark is ever executed) |
| Hildebrand, *On a conjecture of Balog*, PAMS 95 (1985), 517–523 [Hil85] | positive-density lower bound for consecutive-smooth anatomy layer (elementary stable-set method) | **Theorem 1′ link 4 FALLBACK** (TT-free route; registered 04-architecture lines 96–98); scope-check for "one cell prime × friable cofactor" boxes = Gap G4 | **FALLBACK-[link 4]-located** (bibliography ✓; exact statement + scope check TO-PIN — G4/G8) |
| Tenenbaum–Tricot | smooth-pair probability $\rho(u)^2$ | smooth-cofactor dead-end analysis only | DEAD-END-CONTEXT (the smooth-cofactor design is a recorded no-go, 04-architecture remark) |

## C. Fermat quotients, Heilbronn sums, deep characters (Lemma D backbone — now largely superseded by the in-house two-frequency machinery + thm:dls)

The D†-digit layer is closed in-house (manuscript §§5–8, no external input); the deep large sieve (thm:dls, §5) is proved self-contained. This section's rows are therefore context/fallback unless marked otherwise.

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Heath-Brown 1996, *An estimate for Heilbronn's exponential sum* [HB96] | first power-saving Heilbronn bound | old D backbone | DEAD-END-CONTEXT (Heilbronn route superseded by two-frequency reduction; bibliography entry ✓) |
| Heath-Brown–Konyagin 2000, Quart. J. Math. 51 [HBK00] | improved Heilbronn/Gauss bounds | old D backbone | DEAD-END-CONTEXT (as above; bibliography ✓) |
| Shkredov (several, e.g. arXiv:1302.3839) | further Heilbronn refinements | old D backbone | DEAD-END-CONTEXT |
| Bourgain–Ford–Konyagin–Shparlinski 2010, Michigan Math. J. 59 | divisibility of Fermat quotients; subgroup tools | D context; checked as candidate for cor:crude's cross-moduli question | DEAD-END-CONTEXT-[wp13 §3(a): every statement is FIXED-q, count-level — the transpose of what cor:crude needs; NO MATCH] |
| **Shparlinski 2011, Bull. LMS (arXiv:1104.3909)** [Shp11] | Thm 8: FQ sums avg over modulus, $N\ge p^\varepsilon$; (10): arbitrary primitive chars mod $p^2$ | FQ-species calibration; thm:dls is now self-contained | SUPPORTING-[FQ context]-paper-verbatim (close-read June 9; no quantitative consumer left in the chain) |
| Garaev 2006, Monat. Math. 148 [Gar06] | completion method underlying Shp. Thm 8 | adaptation-lemma context | SUPPORTING-TO-PIN (bibliography ✓) |
| Baier–Zhao 2008, J. Number Theory 128 [BZ08] | large sieve for **square moduli** | wp12 Route 1b (C†-lb): coset+BZ second moment, citable stage | SUPPORTING-[wp12 Route 1b: improves deficit $x^{0.80}\to x^{0.35}$, then route saturates — cannot close C†-lb]-located (bibliography ✓; statement TO-PIN if Route 1 is ever written up) |
| Baier–Zhao 2005, Int. J. Number Theory 1 | large sieve, powerful moduli $p^k$ | higher-exponent bookkeeping | SUPPORTING-TO-PIN |
| Zhao 2004, Acta Arith. 112 (conjecture) | classical-shape square-moduli sieve | upgrade path only | SUPPORTING-TO-PIN (conjecture, not citable as input) |
| Shparlinski, Quart. J. Math. (character sums with FQ) | mult. character sums with $q_p(n)$ | context | DEAD-END-CONTEXT |
| Shparlinski, Bull. Aust. Math. Soc. (FQ of primes) | character sums with FQ of primes | context | DEAD-END-CONTEXT |
| Heath-Brown (consecutive FQ sums) | individual threshold $N\ge p^{1/2+\varepsilon}$ | D numerology baseline | SUPPORTING-located (PARTIAL) |
| Chang 2012, Acta Arith. 152 | short character sums with FQ | D numerology | DEAD-END-CONTEXT |
| Ostafe–Shparlinski 2011, SIAM J. Discr. Math. 25 | FQ pseudorandomness | context | DEAD-END-CONTEXT |
| Cilleruelo–Garaev | multiplicative energy: intervals vs subgroups | old D §6 | UNVERIFIED-[no surviving consumer found in repo]-TO-PIN |
| Bourgain–Garaev 2014, Izv. Math. 78 | sumsets of reciprocals; multilinear Kloosterman; special-phase prime-modulus reach $X\ge p^{1/2+\varepsilon}$ | was "D† second-moment core (priority)"; re-priced by wp13 | PRICED-DEAD-[wp13 §2.3: prime-modulus only, savings $x^{0.02}$-class vs needed $x^{0.125+}$ for W4.6; no other consumer] |
| Fouvry–Michel 1998, Ann. Sci. ENS 31 (+ FKM 2014, Duke 163, arXiv:1211.6043) | Kloosterman-type sums over primes (prime ARGUMENT) | priced against W4.6 dressing K2 | PRICED-DEAD-[wp13 §2.3(a), fetched verbatim: nontrivial only for length $\ge p^{6/7}$ (FM98) / $p^{3/4+\varepsilon}$ (FKM); ours is $\le\mathrm{mod}^{1/2}$, modulus composite; savings class $x^{0.02}$] |
| Harper 2016, Compositio Math. 152 [Harper16] | smooth Weyl sums, major/minor dichotomy | D†-anatomy fallback stack (09-anatomy remark) | FALLBACK-[D†-anatomy, asymptotic track]-located |
| de la Bretèche–Tenenbaum 2007, Funct. Approx. 37 [dlBT07] | friable exponential sums, rational arguments | D†-anatomy fallback stack | FALLBACK-located |
| Vinogradov / Balog (primes in APs vs linear phases) + Vaughan identity | large-$\Lambda$ ranges of the anatomy unwinding (prop:species write-up, statusN) | ASYMPTOTIC track only — the lb-chain's b-side hard mass exits via the wp11 §3.4 (b3) sandwich, no Type-II cancellation consumed | SUPPORTING-[asymptotic anatomy write-up]-standard refs (Vau97/IK04 ✓ in bibliography) |
| de la Bretèche 1998, PLMS 77 | foundational friable exponential sums | D†-anatomy fallback | FALLBACK-located |
| **Fouvry–Tenenbaum 1991, PLMS 63** [FT91] | friable numbers in arithmetic progressions | D†-anatomy fallback + B/C interfaces | FALLBACK-located (bibliography ✓) |
| Drappeau 2015, Canad. J. Math. 67 [Drap15]; Drappeau–Shao 2016, Acta Arith. 176 [DS16] | friable exponential sums, Weyl-type means | D†-anatomy fallback | FALLBACK-located (bibliography ✓) |
| de la Bretèche–Granville 2022, Trans. AMS 375 [dlBG22] | exponential sums with multiplicative coefficients | D†-anatomy alternative | FALLBACK-located (bibliography ✓) |
| Iwaniec–Kowalski [IK04] / Vaughan [Vau97] Lemma 2.2-type counting | D†-minor write-up; SL1 (Vaughan + van der Corput, IK04 Ch. 13) | wp22 §1; 12-e1e2 SL1 (asymptotic track) | SUPPORTING-standard (bibliography ✓) |
| Shparlinski, *Open problems...*, Problem 46 | nearby FQ regimes flagged "very difficult" | D risk register | SUPPORTING-paper-verbatim (read June 9; risk calibration only) |

## D. Dispersion / equidistribution / classical tools

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| Bombieri–Friedlander–Iwaniec (dispersion series) | dispersion to large moduli | framing; the BFI-dispersion angle on C† has a recorded proof-of-death (wp8-cdagger, deficit $\ge x^{1/2}$ in the distinct-moduli sector) | DEAD-END-CONTEXT-[as attack] + SUPPORTING-[framing citation]-TO-PIN |
| **Granville–Shao, arXiv:1703.06865** (Adv. Math. 350 (2019)) [GS] | BV for mult. functions, fixed residue class, moduli to $x^{20/39-\delta}$; **companion (Forum Math. Sigma): BV $\iff$ Siegel–Walfisz criterion** | **Theorem 1′ link 8 item 3** (cofactor-prime coins, conductors $\ell^2=x^{2v}$, $v\le10/39$; prop:C-single classical clause, 14-lemmaC lines 138–154) + lem:SW consequence clause (13-lemmaB lines 105–106) | **LOAD-BEARING-[link 8 cofactor coins + SW admissibility]-paper-grade** (WP3 June 10 pin) — BUT G8 still owes the exact range check at our conductors, and the **Forum Sigma companion has NO bibliography entry** (TO-PIN bibliographically) |
| **Drappeau–Granville–Shao, arXiv:1704.04831** [DGS] | *smooth-supported* mult. functions in APs to $x^{3/5-\varepsilon}$ | **Theorem 1′ link 8 item 3** (cofactor coins with $v\in(10/39,3/10]$ — the part beyond GS) | **LOAD-BEARING-[link 8 cofactor coins, upper sub-range]-located ONLY** — never close-read; **no bibliography entry**; G8 priority. This is the weakest-graded load-bearing item on the conditional chain |
| **Montgomery–Vaughan 1977, Invent. Math. 43, 69–82** [MV77] | $\sum_{n\le x}f(n)e(n\alpha)\ll x/\log x+(x/\sqrt R)(\log R)^{3/2}$, uniform over 1-bounded multiplicative $f$ | lem:DMV (weighted minor pairs, manuscript §14) — **ASYMPTOTIC track only: the lb-chain's C†-pair consumer is VOID (link 8 item 1), the (DMV) debt exits** | LOAD-BEARING-[asymptotic Lemma C only]-paper-verbatim (PINNED June 10). NOT consumed by Theorem 1′. HYGIENE: lem:DMV's "to be pinned verbatim" note is STALE; no bibliography entry yet |
| Montgomery–Vaughan **spaced large sieve** ($\sum_j\lvert S(x_j)\rvert^2\le(N+\delta^{-1})\sum\lvert a_n\rvert^2$ for $\delta$-spaced points) | the large-sieve step inside **T1** (wp8-e3 §3, items (3)/(L)) | **Theorem 1′ link 6d** (T1, VERIFIED-DRAFT); also wp11 ladder | **LOAD-BEARING-[T1 / link 6d]-classical** — but exact source NOT pinned and NOT in bibliography (Montgomery–Vaughan Hilbert-inequality form vs Selberg/Bombieri forms): TO-PIN with G6's T1 transcription |
| Khinchin, *Continued Fractions* (1964) [Khin] | CF toolkit: best-approximation spacing, convergent gaps (lem:cf, 07-minor, cited Ch. I–II) | **Theorem 1′ links 6b (thm:minor), 6d (T1), G1 count (wp10)** | **LOAD-BEARING-[lem:cf → links 6b/6d/G1]-classical-located** (bibliography ✓; lem:cf itself proved in manuscript with the citation for the standard facts) |
| ~~Friedlander–Iwaniec, simultaneous fractional parts~~ | RETIRED (WP3, June 10): not locatable (session-memory artifact); thin-progression phenomenon handled by our own two-frequency machinery (manuscript §§6–8) | Lemma C | RESOLVED |
| Vaaler 1985 (Bull. AMS 12) / Selberg majorants–minorants (e.g. Montgomery, *Ten Lectures*, Ch. 1) | trigonometric approximation of interval indicators, degree $H$; **MINORANT form needed for positivity** | **Theorem 1′ link 5 + Gap G3** (minorant truncation of imposed slot-2 windows); Selberg–Vaaler approximants in 12-e1e2/14-lemmaC; Vaaler weights in wp11 §4.7 | **LOAD-BEARING-[link 5/G3 minorants]-classical but TO-PIN** (standard construction; no bibliography entry — must be added with the G3 write-up) |
| Weil/Hooley complete-sum bound ($\lvert S(\ell;a,b)\rvert\le2\sqrt\ell$, prime $\ell$) | per-$\ell$ complete Kloosterman bound | E3-lb ladder, $\Lambda\le Q$ regime (wp11 §1.5/§3.4) — hypothesis-attack corpus, not the conditional chain | LOAD-BEARING-[E3-lb ladder, $\Lambda\le Q$]-classical |
| Burgess | character sums mod cube-free $q^2$ | old D classical layer | DEAD-END-CONTEXT |
| Balog–Wooley | explicit constructions with congruence freedom | Route C (general $k$) — see §E row (PINNED there) | duplicate of §E row |
| Tao(–Teräväinen) $k$-point correlation state of the art | bridge-to-general-$k$ risk calibration | WP5 | SUPPORTING-TO-PIN |

## E. Smooth windows / constructive route (WP5 — literal Erdős 396; NOT on the Theorem 1′ chain)

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| **Balog–Wooley 1998, J. Austral. Math. Soc. A 64, 266–276** | strings of $n^{1/u}$-smooth consecutive integers, length $\log_4 n$; cyclotomic mechanism; family entropy $O(t\log\log X)$ | WP5 core; FQ-convergence discovery; entropy no-go recorded | SUPPORTING-[WP5]-paper-verbatim (source read June 10) |
| Hildebrand, *On integer sets containing strings of consecutive integers* | $k$-strings of $n^{\alpha}$-smooth, positive density, $\alpha>e^{-1/(k-1)}$ | WP5a ($k=2$ rung). NOTE: distinct paper from [Hil85] (§B) | SUPPORTING-[WP5a]-TO-PIN (priority within WP5a only) |
| Balog–Ruzsa (smooth pairs) | positive density of $n$ with $n, an+c$ both $n^{\beta}$-smooth | $k=1$ window family | SUPPORTING-TO-PIN |
| Eggleton–Selfridge | early strings of $\le5$ smooth consecutive integers | context | DEAD-END-CONTEXT |
| Balog–Erdős–Tenenbaum + Heath-Brown construction | depth record for smooth pairs | WP5 upgrade path | SUPPORTING-TO-PIN |

## F. Kloosterman sums over primes (the E3-lb citation bridge, WP11 — attack corpus for OPEN-HYP 1, not the conditional chain)

Provenance: Korolev's HKU survey slides (Oct 2018), re-extracted from the PDF this program; verbatim transcriptions in `wp11-e3lb.md` §1. Slide-grade = survey-author transcription; paper re-confirmation flagged for every load-bearing use (wp11 §2.5).

| Ref | What it gives us | Used in | Status |
|---|---|---|---|
| **Korolev 2018, Thm 3** (arbitrary composite $q$, $b=0$, three-regime $\Delta$, nontrivial $q^{5/8+\varepsilon}\le N\le q^{7/4-\varepsilon}$) | the only citation whose window covers $N=q^\rho$, $\rho\in(1,1.36]$ | **LOAD-BEARING for the PROVED wp11 artifacts**: bound (*) (§4.3.4, power saving) and dispersion steps V1–V3 (§4.6.3) — both graded PROVED-MODULO-[its transcription]; also cross-check on dead (ii-a) | **LOAD-BEARING-[wp11 (*) + V1–V3]-slide-verbatim ONLY** — "arbitrary composite" prime-$q$ reading + "$\forall(a,q)=1$" quantifier must be confirmed against the original paper before any manuscript transcription (wp11 §2.3/§2.5 caveats) |
| Korolev 2018, Thm 1 (prime $q$, $b=0$, $q^{1/2+\varepsilon}\le N\le q$, $\eta=\varepsilon^2/20$) | unconditional $p\le q$ half of (*) | wp11 §4.3.4 fallback stack | LOAD-BEARING-[(*) fallback, $p\le q$ half]-slide-verbatim |
| Korolev 2017, Thm 2 (composite $q$, $N\ge q^{7/10+\varepsilon}$) | intermediate regime | none surviving | SUPPORTING-slide-verbatim |
| **Korolev–Changa 2020**, Math. Notes 108:1, 87–93 | arbitrary modulus, $q^{1/2+\varepsilon}\le N\ll q^{3/2}$ | fallback for (*) ($p>q$ half, if Thm 3 excludes prime $q$) | **FALLBACK-[(*) prime-$q$ escape]-abstract-grade** (exact $\Delta$ UNVERIFIED — paywall; transcription pending) |
| **Baker 2012**, Acta Arith. 156, 351–372 (squarefull part $\le q^{1/4}$, $\eta=\varepsilon^4/2000$) | composite-modulus prime-variable Kloosterman, explicit saving | was the designated K-single engine for routes (ii-a)/(ii-b) | **PRICED-DEAD-[wp11: (ii-a) verbatim-covers NONE of the hard sub-range ($N>q$ there, Baker needs $N\le q$, §2.6 delta 2); (ii-b) dies at the C-S diagonal GOD-MODE floor $2\lambda-u'-2r\ge x^{0.125}$ before Baker is invoked, its saving $x^{-4\cdot10^{-7}}$ irrelevant (§3.2)]** — grade slide-verbatim, paper-level $b$-uniformity UNVERIFIED |
| **Bourgain 2005** (IMRN; prime modulus, $q^{1/2+\varepsilon}\le N\le q$, $\eta(\varepsilon)$ ineffective) | prime-modulus threshold result | seam top edge ($q$-aspect, $b=0$); second fallback for (*) $p\le q$ half | **FALLBACK-[(*) and seam sliver only]-slide-verbatim** ($\eta$ ineffective; like Baker, verbatim-covers none of the hard sub-range in orientation (ii-a)) |
| **Duke–Friedlander–Iwaniec 1997** (*Bilinear forms with Kloosterman fractions*), Thms 1–3 | bilinear Kloosterman fractions, $\ell^2$-normalized | priced for (*) (§4.3.2–4.3.3) and W3b (§4.7.3) | **PRICED-DEAD-[$\ell^2$-normalization vs our thin coefficients (wp11 §4.3.3); requires ONE fixed modulus-side variable — inapplicable verbatim to the coupled family (W3b); range imbalance $N>M^{5/6+\varepsilon}$ fails]** — grade preprint-verbatim (fetched) |

## G. Kuznetsov / spectral corpus (WP13 — priced against the W4.6 closing estimate; ALL DOES-NOT-COVER)

Every row fetched and quoted verbatim from PDFs except DI82 (quoted via Drappeau's published superset, flagged). Full pricing in `wp13-kuznetsov-bridge.md`; verdict: no published technology covers W4.6 (confidence ≥0.9 for the fetched corpus).

| Ref | What it gives us | Priced against | Status |
|---|---|---|---|
| **Deshouillers–Iwaniec 1982**, Invent. Math. 70, 219–288, Thm 12 | sums of Kloosterman sums via Kuznetsov/spectral large sieve, arbitrary $b_{n,r,s}$ | W4.6 (all dressings) | **PRICED-DEAD-[gain lives at spectral conductor $C^2=x^{0.85}$; our coefficient mass sits at $x^{1.125..1.575}\gg C^2$ on every block; best allocation $x^{0.2875}$ ABOVE the divisor floor (machine-checked)]** — grade: quoted via Drappeau Thm 2.1 superset ONLY (original paywalled; any transcription must re-verify) |
| **Drappeau 2017**, Proc. LMS 114, 684–732 (arXiv:1504.05549), Thm 2.1 | dispersion-packaged DI in APs, $q^{3/2}$ loss; $b_{n,r,s}$ arbitrary | W4.6 | **PRICED-DEAD-[same conductor wall as DI82]** — grade paper-verbatim (fetched). POSITIVE deliverable: arbitrary $b_{n,r,s}$ **dissolves the wp9-frontier §2c numerator pair-dependence blocker** (deprioritize that blocker in future audits) |
| **Kowalski–Michel–Sawin 2017**, Ann. of Math. 186 (arXiv:1511.01636), Thms 1.1/1.3 + **BFKMM** (Prop. 3.1) | bilinear forms with (hyper-)Kloosterman trace functions, single prime modulus | W4.6 per-$q$ form | **PRICED-DEAD-[three mismatches: range ($MN<q^{5/4}$ vs our $x^{0.7..1.0}\gg q$), savings ($q^{-1/64}=x^{-0.0066}$ vs needed $x^{0.125+}$), category (ours is a PSD Gram form, not a trace-function bilinear)]** — paper-verbatim |
| **Bettin–Chandee** (Adv. Math.; trilinear Kloosterman fractions; quoted via Fouvry–Radziwiłł arXiv:1811.08672, Lemma 2.4) | trilinear forms, arbitrary $\ell^2$-weights on ALL variables incl. the modulus | W4.6 — the closest-fitting shape in the corpus | **PRICED-DEAD-[arity: our object is quadrilinear with coupled $\nu(q,a)$ (the self-similarity rider); and ranges: savings need $M\asymp N$, ours $M=x^{0.425}$ vs $N\ge x^{0.85}$ — at/above trivial on every block]** — verbatim via FR |
| **Sarnak–Tsimerman 2009** (Manin volume) / **Steiner 2017** (arXiv:1707.02113) | Kuznetsov $C^{1/6}$ in $C$-aspect; $(m,n)$-aspect uniformity | W4.6 aggregate | **PRICED-DEAD-[our family is deep in the Selberg range $C\le\sqrt{mn}$ by $x^{0.1375..0.2875}$, where verbatim "the trivial bound is still the best known bound"; and per-pair the $c$-object is a nonnegative divisor count — no $c$-oscillation exists to detect]** — verbatim via Steiner |
| Kuznetsov 1979 | $\sum_{c\le C}S(m,n;c)/c\ll C^{1/6}\log^{1/3}C$ | W4.6 per-pair | DEAD-END-CONTEXT-[category mismatch, see ST/Steiner row] |
| Fouvry–Michel 2003/07; Sivak-Fischler; Matomäki; **Xi 2024** (arXiv:2411.13170, $P_6$); Drappeau–Maynard (Siegel-zero-conditional, $P_2$) | spectral access to almost-prime moduli (sign-change literature) | prime-moduli restriction of W4.6 | DEAD-END-CONTEXT-[ladder stops at $P_6$; pure prime moduli open in the entire literature — AND **mooted by wp13's K3 positivity relaxation**: W4.6 may be attacked over ALL moduli $c\sim x^{0.425}$ at polylog cost] |
| Wieferich corpus (incl. arXiv:2508.08472 status check) | non-Wieferich infinitude: open unconditionally; Silverman 1988 under abc | cor:crude pointwise form (dual check) | DEAD-END-CONTEXT-[cor:crude's pointwise form is Wieferich-hard; count-level results provably cannot close W4.6 (needs SIGNS); a contrary web claim was checked against source and is an artifact] |

## Our own citable artifacts (updated June 11)

| Item | Status |
|---|---|
| Lemma 0 exact sandwich + Lemma 0′ margins (`lemma-0-sandwich.md`; manuscript §§3, 15) | PROVED (machine-verified); written |
| Lemma A small primes (manuscript §15) | PROVED; written (FK21 §2 = provenance only) |
| Deep large sieve for FQ characters (thm:dls + cors, manuscript §5) | PROVED (machine-verified); self-contained, no external input |
| Two-frequency reduction, D†-minor theorem, large-$\lambda$ coverage (manuscript §§6–7) | PROVED (lem:beta, lem:linearization, prop:two-freq statusPM; thm:minor statusP) |
| Family-B unconditional count (wp8-e2) | VERIFIED-DRAFT (UPHELD); transcription = G5 |
| T1 anatomy $\mu$-tail (wp8-e3 §3) | VERIFIED-DRAFT (UPHELD); transcription = G6; consumes MV spaced sieve + lem:cf |
| G1 sum-branch tangency count (wp10) | CLOSED-MODULO-write-up (wp9 header: lb-piece effectively CLOSED) |
| wp11 unconditional deliverables: (W4.0) linear reduction, (W4.2) fiber-count lemma, (W4.3)–(W4.4) kernel/variance bounds, first-moment reduction §§4.1–4.2, bound (*) §4.3 (modulo Korolev transcription), V1–V3 §4.6 | PROVED at the grades stated per-section in `wp11-e3lb.md` |
| wp12 Route-2 reduction (C†-single-lb-BDH form; exact coset/orthogonality identities) | PROVED (exact identities, machine-checked); registration of BDH form pending (~½ session) |
