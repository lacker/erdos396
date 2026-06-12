# Literature dependencies of the conditional Theorem 1′

**Scope.** Theorem 1′ (W₁ = {n : n(n−1) | C(2n,n)} has positive lower log-density, hence is
infinite), CONDITIONAL on the two named estimates **E3-lb (two-sided, λ-uniform)** and
**C†-single-lb(g₀)** stated verbatim in `wp9-theorem1prime.md` links 7 and 9. This file lists
every EXTERNAL theorem the verified chain (links 1–6, 8, 10–11 + write-up gaps G1–G8) consumes,
and nothing else. Attack corpus for the two hypotheses (Korolev/Baker/Bourgain/DFI, the wp13
Kuznetsov corpus) is deliberately EXCLUDED — see §3. Generated June 11, 2026 from
`wp9-theorem1prime.md`, `wp10-g1.md`, `wp11-e3lb.md`, `wp12-cdagger-lb-diagnosis.md`,
`wp13-kuznetsov-bridge.md`, `manuscript/sections/*.tex`, `citations.md`.

Verification-grade vocabulary: **paper-verbatim** (close-read against the source) >
**slide-verbatim** > **abstract-grade** > **located** (bibliographic only) > **classical**
(textbook; exact source may still need pinning).

## 1. The table

| # | Source | Exact statement location (our doc + section) | Consumed by (chain link) | Grade | What breaks if it's wrong |
|---|---|---|---|---|---|
| 1 | Kummer 1852 (carry formula) | prop:kummer, `manuscript/sections/02-preliminaries.tex`; proof reproduced in-house | Everything (Lemma 0, all digit bookkeeping) | classical, **proof in-house ✓** | Nothing — citation is provenance; the proof is ours |
| 2 | **Ford–Konyagin [FK21]**, Trans. AMS 374 (2021): piecewise top-digit/band-coin law; per-class probabilities; c₁ = 0.11424 (§7) | FK law: `04-architecture.tex` lines 12–16, 115; c₁: `15-spine-bookkeeping.tex` line 171, `04-architecture.tex` line 210; Lemma A §2 framework: `04-architecture.tex` lines 37–45 (provenance only — proof in-house at `15-spine` lines 78–102) | Link 5 (window measures ≈ 1/2, slot-2 carry mechanics, sufficiency check (g)); Gap G3 (FK per-class probability lower bounds); links 2/11 (c₁, minor role for bare positivity) | **PARTIAL / abstract-grade** — no close-read with our notation on record; G8 names the §7-constant + law pinning | Link 5's imposed-coin measures and G3's per-class lower bounds would need re-derivation; κ_lb's numeric value changes. Positivity is robust (windows are explicit and elementary given Kummer) but the written chain would carry a wrong law. **FLAGGED: load-bearing, not paper-grade** |
| 3 | **Tao–Teräväinen [TT25]**, arXiv:2512.01739 v2, **Thm 3.1** | Verbatim transcription: `lemma-B-anatomy-independence.md` (§"Citation route — VERIFIED"); consumer: prop:B-assembled, `13-lemmaB-closure.tex` lines 123–149 | Link 4 (anatomy-pair lower bound, TT-route) | **paper-verbatim ✓** (v2 TeX source close-read, WP3b June 9; three fine-print checks resolved) | Link 4 falls back to [Hil85] (row 4) — lb-track survives; the asymptotic track loses Lemma B. Hygiene: `bibliography.tex` TT25 note "verification pending" is stale (G7) |
| 4 | **Hildebrand [Hil85]**, PAMS 95 (1985), 517–523 (elementary stable-set method) | Registered: `04-architecture.tex` lines 96–98; fallback role: wp9-theorem1prime link 4 + Gap G4 | Link 4 FALLBACK only (TT-free anatomy lower bound) | **located** — exact statement + scope-check for "one cell prime × friable cofactor" boxes NOT done (G4) | Only matters if TT route is dropped; then link 4 has no proof until G4's scope-check is done. **FLAGGED: fallback unpinned** |
| 5 | **SL2′** (classical ψ-over-primes / divisor-switch cancellation; "same family as lem:SL2") | lem:SW, `13-lemmaB-closure.tex` lines 96–121 (statusP modulo SL2′); ledger: `10-remaining.tex` lines 26–27 | Link 4 (lem:SW → prop:B-assembled, TT-route) and link 8 item 3 (SW admissibility of g₀'s g_z-components) | **standard-toolbox, UNWRITTEN** — and G7 records that the printed sibling lem:SL2 has a known error (third term √s → √(Ps)); the corrected form must be the one pinned | lem:SW loses its proof → TT-route admissibility AND the GS-criterion application in link 8 item 3 hang. The lb-chain's single most exposed "standard" input. **FLAGGED: load-bearing, not paper-grade, statement not even fixed on paper yet** |
| 6 | **Granville–Shao [GS]**, Adv. Math. 350 (2019) (BV for mult. functions, moduli to x^{20/39−δ}) + **Forum Math. Sigma companion** (BV ⟺ Siegel–Walfisz criterion) | prop:C-single classical clause, `14-lemmaC-reduction.tex` lines 138–154; criterion clause: `13-lemmaB-closure.tex` lines 105–107; pin record: `wp3-lemma-C-diagnosis.md` | Link 8 item 3 (cofactor-prime coins at conductors ℓ² = x^{2v}, v ≤ 10/39) | **paper-grade** (WP3 pin, June 10) — but G8 still owes the explicit range re-check at our conductors, and the **companion has no bibliography entry** | Cofactor coins for v ≤ 10/39 lose their citation; DGS (row 7) covers all of (δ, 3/10] alone IF its range claim holds — single point of failure becomes row 7 |
| 7 | **Drappeau–Granville–Shao [DGS]**, arXiv:1704.04831 (smooth-supported mult. functions in APs to x^{3/5−ε}) | Named: `14-lemmaC-reduction.tex` lines 149–152; ledger `10-remaining.tex` lines 37–38; pin record: citations.md only | Link 8 item 3 (cofactor coins, v ∈ (10/39, 3/10] — beyond GS's range) | **located ONLY — never close-read; no bibliography entry** | The coins at v ∈ (10/39, 3/10] have no citation → link 8 item 3 incomplete → the imposed-coin factor E[2^{−ω}] unproven on part of its range (alternative: lower the friability cutoff to 10/39 — changes class constants, NOT priced anywhere). **FLAGGED: the weakest-graded load-bearing item on the whole chain** |
| 8 | **Khinchin**, *Continued Fractions* (1964), Ch. I–II (best-approximation spacing / convergent facts) | lem:cf, `07-minor.tex` lines 51–79 (cited at line 79) | Link 6b (thm:minor), link 6d (T1's CF spacing), G1 (wp10 tangency count; Ostrowski/CF write-up item) | **classical-located** (bibliography ✓; only textbook facts consumed, lem:cf proof written) | Nothing real — facts are textbook; worst case is a reference swap |
| 9 | **Montgomery–Vaughan spaced large sieve** (Σ_j |S(x_j)|² ≤ (N + δ^{−1}) Σ|a_n|²) | Consumed inside T1: `wp8-e3.md` §3 items (3)/(L) (lines 110–111, 190–217); verified `wp9-verify-e3cd.md` §B | Link 6d (T1, VERIFIED-DRAFT) | **classical — exact source NOT pinned, not in bibliography** (pin with G6's T1 transcription) | Nothing mathematical (the inequality is standard); a missing reference blocks G6's transcription only. **FLAGGED: pin source** |
| 10 | **Vaaler 1985 / Selberg majorants–minorants** (one-sided trigonometric approximants of interval indicators) | Demand: link 5 + Gap G3 (`wp9-theorem1prime.md` link 5: "truncation … in MINORANT form … standard but unwritten"); cognate uses `12-e1e2.tex` line 62, `14-lemmaC-reduction.tex` line 58 | Link 5 (positivity-preserving harmonic truncation of imposed windows) | **classical construction — source TO-PIN, not in bibliography** | G3's assembly can't truncate the window expansions without losing positivity; standard fix, but currently neither written nor cited. **FLAGGED: pin source with G3** |
| 11 | Pomerance [Pom15], Monthly 122 (2015) | `01-intro.tex` lines 8–10; `03-sandwich.tex` line 88 | Intro framing only | located | Nothing — framing |
| 12 | Erdős–Graham [ErGr80] | `01-intro.tex` line 5 | Problem source | located | Nothing — framing |

**In-house inputs masquerading as citations (none external, listed to close the audit):**
lem:fewcarries + Lemma A proof (15-spine, statusP); lem:sandwich/lem:margins (statusPM/P);
prop:depth, prop:one-large, prop:species (statusPM); lem:beta, lem:linearization, prop:two-freq
(statusPM), prop:largelambda, thm:minor/cor:minor (statusP); thm:dls (§5, self-contained);
wp8-e2 Family-B theorem, T1, wp8-cdagger lb-closure, wp10 G1 count (VERIFIED-DRAFT grade, internal;
their only external inputs are rows 8–9 above); Lemma R (wp8-e1, elementary, internal).

## 2. Ruthless flag list — load-bearing items NOT at paper-grade

In descending order of exposure:

1. **DGS (row 7): located only.** Never close-read; no bibliography entry. Consumed quantitatively
   (conductor range (x^{20/39}, x^{3/5}]). Highest-priority G8 item.
2. **SL2′ (row 5): unwritten, and its printed sibling lem:SL2 is wrong as printed (G7).**
   Feeds BOTH link 4 (TT-route via lem:SW) and link 8 item 3 (SW admissibility). Must be stated,
   then either proved (Vaughan + van der Corput, IK04 Ch. 13 territory) or pinned.
3. **FK21 (row 2): PARTIAL.** The FK law and per-class probabilities are consumed by links 5/G3;
   the promised re-read with our notation (citations.md row A3, G8) has never been done.
4. **Vaaler/Selberg minorants (row 10) and MV spaced large sieve (row 9): classical but unpinned**
   — pure G6/G3 bookkeeping, zero mathematical risk, nonzero transcription blockage.
5. **Hil85 (row 4): fallback unpinned** (statement + G4 scope-check) — only an exposure if the
   TT route is abandoned.

Paper-grade and clean: TT25 Thm 3.1 ✓ (row 3, v2 source); GS ✓ (row 6, modulo G8 range re-check
and the companion's missing bibitem); Kummer/Khinchin/Pomerance/ErGr80 ✓ (classical/framing).

## 3. Explicitly NOT consumed by the conditional theorem (common confusions)

| Item | Why it is absent |
|---|---|
| E1, E2 (hyp:E1/hyp:E2, `08-major.tex`) | lb-track replaces them: difference branch by lem:branch + rem:E1-signed (PROVED); sum branch by the G1 count (wp10, CLOSED-modulo-write-up); (M2*) by wp8-e2's unconditional theorem + Markov (E2 DISCHARGED) |
| **MV77** (Invent. Math. 43; the DMV input, lem:DMV §14) | Asymptotic-track only: the lb chain's weighted-minor-pair consumer is VOID (link 8 item 1 — no two-band-prime n in the class). Pinned paper-verbatim anyway |
| (Hal) Halász-type absorption (`14-lemmaC-reduction.tex` lines 120–134) | VOID on the lb-track (link 8 item 2): majors are discarded, not absorbed |
| hyp:Cdagger as printed (`14-lemmaC-reduction.tex` lines 156–164) | Over-engineered; the chain uses only C†-single-lb(g₀) = OPEN-HYP 2 (a named hypothesis, not a citation) |
| Vinogradov/Balog + Vaughan identity (anatomy Type-I/II ranges) | Asymptotic-track write-up; the lb b-side hard mass exits via the wp11 §3.4 (b3) population sandwich at O(η) cost, no Type-II cancellation consumed |
| Korolev 2018/Korolev–Changa, Baker 2012, Bourgain 2005, DFI 1997, Weil/Hooley | Attack corpus for proving OPEN-HYP 1 (E3-lb), inside the wp11 ladder — the conditional theorem takes E3-lb as a hypothesis |
| DI 1982, Drappeau 2017, KMS/BFKMM, Bettin–Chandee, Sarnak–Tsimerman/Steiner, Kuznetsov, Xi 2024 | wp13's priced-and-dead spectral corpus for the W4.6 closing estimate — all DOES-NOT-COVER; see citations.md §G |
| Baier–Zhao 2008, Bourgain–Garaev, Heilbronn corpus, Shparlinski FQ corpus | C†-lb / old-D attack corpus (wp12 routes; none closes); the conditional theorem takes C†-single-lb(g₀) as a hypothesis |

## 4. Status of the two named estimates themselves (context, not dependencies)

Both hypotheses are stated verbatim in `wp9-theorem1prime.md` (links 7, 9). As of June 11
(wp9 header update; wp11 §4.7.4; wp12 §4; wp13 §4): the elementary ladder under **E3-lb** is
complete and bottomed out; the single missing input for BOTH hypotheses' current attack plans is
EXTERNAL — the W4.6-class signed cross-moduli coincidence estimate (Form A/B, `wp13` §4), which
no published technology covers (wp13 verdict, confidence ≥ 0.9 on the fetched corpus). If either
hypothesis is eventually proved via wp11's (b3)+first-moment plan, **Korolev 2018 Thm 3 enters the
dependency table at slide-verbatim grade only** (wp11 §§4.3.4, 4.6.3) and must first be upgraded
to paper-verbatim — recorded here so the future merge does not silently inherit slide-grade.
