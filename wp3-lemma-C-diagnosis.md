# WP3: Lemma C Diagnosis

**STATUS: DIAGNOSIS COMPLETE (June 10, 2026). Verdict: C's "hardest ingredient" is already built — the thin-progression core is the manuscript's two-frequency machinery under a change of variables; the weighted layer reduces to pinned literature (Granville–Shao at $x^{20/39}$, Drappeau–Granville–Shao smooth-supported at $x^{3/5}$, Daboussi–Montgomery–Vaughan minor arcs). The phantom Friedlander–Iwaniec citation is retired. C: ~75% → ~85–88%.** Script: `lemma_c_probe.py`.

---

## 1. The structural discovery: C's core = D's machinery

C's hardest configuration is $n=p_1p_2a$ with two band primes. The joint slot-2 digit conditions are
$$\Big\{\frac{n}{p_1^2}\Big\}=\Big\{\frac{p_2a}{p_1}\Big\}\ge\tfrac12,\qquad
\Big\{\frac{n}{p_2^2}\Big\}=\Big\{\frac{p_1a}{p_2}\Big\}\ge\tfrac12,$$
with $a\le R=x/(p_1p_2)$ far shorter than $p_1p_2$ — the thin-progression problem. Fourier-detecting both conditions produces the phases
$$a\cdot\Big(\frac{hp_2}{p_1}+\frac{kp_1}{p_2}\Big)=a\cdot\frac{hp_2^2+kp_1^2}{p_1p_2},$$
**which are exactly the two-frequency phases $\theta_\mu$ of manuscript §6** under $(\mu,\lambda,q,p)\to(h,-k,p_2,p_1)$, with the same range $R$. Consequences, immediate:

- **Minor pairs** (in the (M1)/(M2*) sense, with the Diophantine functional $\mathcal D_R(p_2/p_1)$): the proved Theorem (manuscript §7) bounds the joint-digit sums. No new mathematics.
- **Major pairs** ($p_2/p_1\approx\sqrt{h/k}$): the Family A/B counts (§8, modulo E1/E2 — both diagnosed benign in WP2.4) bound their number; the within-side ensemble average over $(p_1,p_2)$ is the same $q$-average we already run.
- The "Friedlander–Iwaniec section on simultaneous fractional parts," carried since the original session as C's hardest dependency, **could not be located as an actual paper** (searched June 10) and is now unnecessary: retired from the ledger, superseded by §§6–8.

## 2. Empirics ($x=10^8$, three pair-ensembles, `lemma_c_probe.py`)

| ensemble | pairs | per-pair $z$ (med/90%/max) | bias $P(\text{joint}){-}P_1P_2$ | ens. $z$, $g{=}1$ | $g{=}\lambda$ | $g{=}\chi_3$ |
|---|---|---|---|---|---|---|
| generic ($p_2/p_1\sim1.6$) | 308 | 0.26 / 0.98 / 12.1 | $+0.002$ | 1.53 | **0.08** | 0.61 |
| resonant ($p_2/p_1\approx1$) | 132 | 0.90 / 7.75 / 11.4 | $-0.024$ | **13.14** | **0.78** | 1.29 |
| wide ($p_2/p_1\sim3.2$) | 429 | 0.44 / 1.31 / 6.4 | $-0.005$ | 5.57 | **0.89** | 1.72 |

Three readings:

1. **The thin-progression picture is confirmed and localized.** Individual pairs have heavy-tailed deviations (max $z\approx12$); the historical "~4% within-side deviation" concentrates on the resonance curves ($p_2/p_1\approx\sqrt{h/k}$: bias $-0.024$ on the resonant slice vs $+0.002$ generic). It is the major arcs announcing themselves — the same diagnosis as `empirics-D.md` §4, now on the within-side object.
2. **Generic ensembles equidistribute** (unweighted $z=1.5$): the ensemble-restoration mechanism works exactly as FK's framework needs.
3. **The C-specific discovery: multiplicative weights kill even the major arcs.** On the resonant ensemble the unweighted $z=13.1$ collapses to $0.78$ under Liouville and $1.29$ under $\chi_3$. The resonant structure lives in the digit/population layer and decorrelates from any genuinely oscillating multiplicative weight. Proof-shape consequence: in Lemma C the major-arc contributions pair with $\sum_a g(p_1p_2a-1)$ along structured ranges — a multiplicative mean value, small for non-pretentious $g$ (Halász/MRT) and equal to (main term)$\times$(mean of $g$) for pretentious $g$. **C's major arcs are absorbed into the main term, not counted against a budget — easier than D's.**

## 3. The weighted layer: literature pinned

- **Single band prime** ($n=pm$, condition mod $p$, weight $g(pm-1)$): mean values of $1$-bounded multiplicative functions in APs on average over moduli. **Granville–Shao** (arXiv:1703.06865, Adv. Math 2019): fixed residue class, moduli to $x^{20/39-\delta}$ — *beyond* $x^{1/2}$, covering the whole band including the top corner (the $\eta$-trim becomes a convenience, not a necessity, on the C side). Their companion (Forum Math. Sigma): BV holds for $g$ iff a Siegel–Walfisz criterion holds — the "non-pretentious corner cases" risk in the old C doc is exactly this criterion; pretentious $g$ are handled by the main-term dichotomy instead.
- **Bonus pin — Drappeau–Granville–Shao** (arXiv:1704.04831): *smooth-supported* multiplicative functions in APs to moduli $x^{3/5-\varepsilon}$. Our weights are supported on governor populations, which are $\sqrt{2n}$-smooth by the Tier-A lemma — the smooth-supported hypothesis is *native* to this program. Extra room beyond $20/39$.
- **Minor-arc weighted sums** ($\sum_ag(\cdot)e(a\theta)$, $\theta$ Diophantine-minor): Daboussi/Montgomery–Vaughan — cancellation uniform over $1$-bounded multiplicative $g$, with the rational-approximation hypotheses matching our (M2*)/$\mathcal D_R$ certificates.
- **Deep digits** ($j\ge3$): choose the detection position with $p^{\,j-1}\le x^{1/2}$ (always possible for $u<1/3$); upper-bound mode stays inside the GS range.
- **Top digit:** deterministic FK piecewise law, already in C's statement.

## 4. Remaining work on C (all named, none structural)

(i) Write the reduction of §1 formally (change of variables + interface to §§6–8; the within-side object has no deep character — it is the $\lambda$-free case, strictly simpler). (ii) The GS/DGS application with our weights: verify the Siegel–Walfisz criterion for the interpolation weights $g_z$ (same computation as Lemma B0 — likely shareable). (iii) The Daboussi/MV quantitative form at rational $\theta$ with large denominators. (iv) FK-gluing bookkeeping (their §§3–5 with the twist carried through). (v) The pretentious-$g$ main-term bookkeeping (population means mod small conductors — Lemma A/B territory).

## 5. Calibration

Lemma C: **~75% → ~85–88%** (hardest ingredient already proved; weighted layer on pinned literature with range to spare; both empirical signatures clean). Rung i (full $k=1$ theorem): **~50% → ~55%**. Risk now concentrates in: Type-II anatomy ranges, the assembly bookkeeping at scale, and the write-up pile — no open lemma of rung i lacks a diagnosed path.
