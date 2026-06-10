# WP2.4: Diagnosis of Hypotheses E1/E2 + the Fine-Anatomy-Class Check

**STATUS: SUPERSEDED IN PART (June 10): E1 and E2 are now PROVED modulo the classical inputs SL1/SL2 (manuscript §12) — no longer open hypotheses. The diagnosis below stands as the record of why.** E1: true with large margin in data; only the *signed* average is needed (a refinement over the manuscript's statement); proof route classical. E2: tail law and moments confirmed in data; elementary counting + possibly a BV corner. Fine classes (ledger D4): PASS — structural argument + clean probe. Scripts: `e1_probe.py`, `e2_probe.py`, `fine_class_probe.py`.

---

## 1. E1 (Family-A wrap-boundary average) — diagnosis

**Refinement (record in manuscript):** the Family-A application sums nonnegative counts $N_q$, so only the **signed** average $\mathbb{E}_q\sum_\mu E_q$ is needed, not $\mathbb{E}_q\sum_\mu|E_q|$. This is strictly weaker and is what equidistribution heuristics actually deliver.

**Unconditional pieces:** of the branch-count bound $|E_q|\ll \mu Q/P+\lambda P/Q+1$, the $O(1)$ and $\lambda P/Q$ pieces sum acceptably *without any averaging*: $\sum_{\mu\le RL^{-B}} O(1)\ll RL^{-B}\le PL^{-B}$ (since $R<P$ always in the band), and $\sum_\mu \lambda P/Q \ll RL^{C-B}P/Q \le PL^{C-B+1}$ since $R/Q = x^{1-u-2u'}<1$ **always** ($u+2u'>1$ in the open band). **Only the $\mu Q/P$ branch piece needs the $q$-average**, and only in the sub-range $\mu \ge P/Q$ where the phase $\mu q/p$ has genuine oscillation.

**Proof route:** Fourier-expand the window indicator (Erdős–Turán); the signed error becomes $\sum_h \hat c_h \sum_{p,q} e(h(\mu q/p - \lambda p/q))$ — real-analytic hyperbolic phases; for the live range the $q$-sum is a geometric/van der Corput estimate at frequency $\mu/p$, and the aggregate is a standard lattice/divisor count near the hyperbolas $\mu q \approx kp$. Over primes: Vaughan. Nothing exotic. **Risk: LOW.**

**Numerics** (`e1_probe.py`, model $x=10^{11}$, $L^B=50$, $\mu\le30$, $\lambda\in\{1,2\}$, 60 moduli per geometry):

| geometry | signed $\mathrm{avg}_q\sum_\mu E_q$ | $\mathrm{avg}_q\sum_\mu\|E_q\|$ | worst-case bound | main term |
|---|---|---|---|---|
| $u>u'$ ($P/Q\approx6$), $\lambda=1$ | $-2.0$ | $41.0$ | $282$ | $155$ |
| $u>u'$, $\lambda=2$ | $-3.5$ | $40.1$ | $452$ | $155$ |
| $u<u'$ ($P/Q\approx1/12$), $\lambda=1$ | $+0.6$ | $14.1$ | $5062$ | $15.3$ |
| $u<u'$, $\lambda=2$ | $+0.3$ | $13.9$ | $5065$ | $15.3$ |

Signed averages are 1–4% of the main term and consistent with sample fluctuation (per-$q$ std / $\sqrt{60}$); the absolute sums are already 7–360× below the worst-case bound, and the signed cancellation buys another order of magnitude. **E1 is true with room.**

## 2. E2 (Family-B endpoint average) — diagnosis

**Reduction:** per coprime $(a,s)$, $s\sim S$, the endpoint $O(1)$ terms average over $p$ because the window position $pa/s \bmod 1$ cycles with period $s \le R < P$ (full periods + boundary). For integer $p$: exact. For prime $p$: primes in APs mod $s$; $s\le R$ can exceed $\sqrt P$ near the $(1/3,1/3)$ corner ($3u+2u'<2$), where on-average-over-$s$ input beyond Bombieri–Vinogradov would be needed *if* full asymptotics were required — but only the $O(1)$-endpoint aggregation is, which is second-order. **Risk: LOW** (elementary; one corner to watch).

**Numerics** (`e2_probe.py`, model $x=10^{11}$, 17.5k/18k pairs per geometry): the tail law $\#\{\text{pairs}: \text{some gap ratio} > G\}\sim C\cdot N_{\mathrm{pairs}}/G$ holds across three orders of magnitude ($\mathrm{frac}\times G \approx 5$–$9$ for $G=10\ldots1000$, mild log drift as predicted). Moments of the gap functional: $\mathbb E[\mathcal D_R]\approx14\approx2\log R$, $\mathbb E[\mathcal D_R^2]\approx210$ — polylog, as Prop. familyB's average claim asserts. The structural first gap is visible exactly where the corrected theory says: median first ratio $3.0$ ($\sim p/q=4$) in the $u>u'$ geometry, $2.0$ (generic) in $u<u'$. **The corrected Family-B picture is quantitatively right.**

## 3. Fine-anatomy-class check (ledger D4) — PASS

**Structural argument.** A fine Lemma-B class conditions the cofactor's primes above $x^\delta$ into sub-boxes. Each box condition unwinds by inclusion–exclusion over tuples of primes in the box dividing $a$; since $a$ has at most $1/\delta$ primes above $x^\delta$, the I–E **terminates exactly at bounded depth** (no truncation error). Each term fixes $\ell_1\cdots\ell_j \mid a$, i.e. a single class mod $\ell_1\cdots\ell_j$ by CRT, producing the same species as WP2.3 with composite dilation $\Lambda=\ell_1\cdots\ell_j$: geometric sums at dilated frequencies (small $\Lambda$), Type-II bilinear (large $\Lambda$), almost-primes in APs at the extreme. New cost: $\tau_j$-divisor weights in the resonance counts = log-power losses, absorbable. The Type-II range pinches remain the named residual risk — unchanged by fine classes.

**Numerics** (`fine_class_probe.py`, $x=10^8$, strata $\gamma\in\{0.40,0.43\}$): decorated $z$ on the *class-restricted* populations:

| class | $\gamma=0.40$ (N, rms z) | $\gamma=0.43$ (N, rms z) |
|---|---|---|
| F0 bare friable | 13709, 1.11 | 7948, 1.64 |
| F1 $P^+(a)\in(x^{0.20},x^{0.28}]$ | 5904, 1.00 | 3436, 1.13 |
| F2 $P^+(a)\le x^{0.20}$ | 2933, 1.29 | 1700, 1.66 |

All classes sit at $z=O(1)$ (correlation-scale would be $30+$); the digit decoration decorrelates from $m\bmod q$ *within every fine class*. (Note F0 here additionally enforces cofactor friability rem $=1$, a refinement over `empirics_d.py`'s population.)

## 4. Consequences

- The two open hypotheses of the digit layer are **diagnosed benign**: standard-toolbox proofs, numerically true with margin. Promote to "to write" status; they no longer carry structural risk.
- D4 closes as a check (write-up of the I–E bookkeeping still owed, same species).
- Residual risk on Lemma D now concentrates entirely in: the Type-II ranges (anatomy large-$\Lambda$), uniformity bookkeeping at scale, and the E1/E2 write-ups.
