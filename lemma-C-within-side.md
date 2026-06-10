# Lemma C: Within-Side Digit Equidistribution Against Multiplicative Weights

**STATUS: DIAGNOSIS COMPLETE (WP3, June 10, 2026 — see `wp3-lemma-C-diagnosis.md`). The hardest ingredient (two-band-prime thin progressions) is the manuscript's §§6–8 two-frequency machinery under a change of variables — already proved/counted; the weighted layer reduces to Granville–Shao ($x^{20/39}$, PINNED) + Drappeau–Granville–Shao (smooth-supported, $x^{3/5}$) + Daboussi–Montgomery–Vaughan. The Friedlander–Iwaniec dependency is retired (not locatable; superseded). Empirics: major arcs collapse under multiplicative weights (resonant ensemble $z$: 13.1 unweighted → 0.78 under Liouville).** Probability: ~85–88%. **Update June 10: the formal reduction is written (manuscript §14) — change of variables to the two-frequency machinery (proved), weighted minor pairs modulo DMV, major-pair absorption modulo a Halász-type input, single-prime case on GS/DGS. Remaining: the FK gluing (W3).**

---

## Statement (informal)

Conditional on the anatomies of both $n$ and $n-1$, the digit/carry conditions at $n$'s own primes equidistribute at their expected rates, **uniformly against any 1-bounded multiplicative weight living on $n-1$**. (This is the "one side decorated, other side multiplicative" half of independence; Lemma D adds the second decoration.)

## Structural corrections from testing (bake into the statement)

- **Interior digits only:** equidistribution must be claimed for digit positions strictly below the top. The **top digit is deterministic** given the size ratio — it follows Ford–Konyagin's piecewise law in $\{1/u\}$. State the lemma for interior digits; handle the top slot by the exact FK law.
- The measured ~4% finite-scale within-side deviation is **fully explained**: for two band primes $p_1,p_2$ the cofactor range is far shorter than $p_1p_2$, so the joint residues live on thin progressions rather than filling the grid; the ensemble average over prime pairs restores independence. This is precisely the phenomenon treated by **Friedlander–Iwaniec's section on simultaneous fractional parts — the hardest ingredient here.**

## Toolbox

Ford–Konyagin's exponential-sum machinery (their hardest section), re-run with a multiplicative twist; the twist lands on **multiplicative functions in APs to large moduli on average** — Bombieri–Vinogradov-for-multiplicative-functions territory: Granville–Shao and successors, Matomäki–Radziwiłł–Tao averaged Elliott. Residual risk: uniformity ranges of the multiplicative-BV literature at the moduli we need, and non-pretentious-weight corner cases.

## Interface

Work after the Lemma D gate (G1): C's final form depends on which version of D it must feed (full vs lower-bound).
