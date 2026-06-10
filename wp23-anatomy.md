# WP2.3: The Anatomy-Layer Hypothesis Check — Verdict

**STATUS: PASS — STRONGER THAN EXPECTED (June 9, 2026).** The heavy friable-sums literature is **not needed** for the dominant configuration: the cofactor's friability parameter is $u_f=3(1-u)\in(1.5,2)$, **strictly below 2**, and the anatomy layer unwinds by an *exact* identity into classical Type-I/II objects. Harper 2016 and de la Bretèche–Tenenbaum 2007 are demoted to fallback. All numerical checks pass (identity exact; decomposition exact to $10^{-14}$; friable-weighted minor-frequency sums at $z=O(1)$).

---

## 1. The structural fact

The cofactor $a=n/p\le A=x^{1-u}$ must be $y$-friable with $y=(2x)^{1/3}$ (governor membership forbids primes $>\sqrt{2n}$; "exactly one band prime" forbids band primes in $a$). Since $y^2=(2x)^{2/3}\ge A$ for $u\ge1/3$, $a$ has **at most one prime factor above $y$, with multiplicity one**. Hence the *exact* identity
$$\mathbf{1}\big[P^+(a)\le y\big]\;=\;1-\sum_{\substack{\ell>y\ \mathrm{prime}\\ \ell\mid a}}1\qquad(a\le A),$$
verified with zero violations on the actual progression.

## 2. The decomposition (exact; machine-checked)

$$W(\theta)=\sum_{t\le R}\mathbf{1}\big[P^+(a_0{+}qt)\le y\big]e(t\theta)\;=\;G(\theta)\;-\;\sum_{y<\ell\le A}e(t_\ell\theta)\!\!\sum_{s\le(R-t_\ell)/\ell}\!\!e(s\,\ell\theta),$$
with $t_\ell$ the first index divisible by $\ell$. So D†-anatomy splits by dyadic $\Lambda=\ell$-size into entirely classical species:
- **Small/medium $\Lambda$** (many terms per $\ell$): geometric sums at the **dilated frequencies $\ell\theta_\mu$** — same Vinogradov-type counting as D†-minor; the resonant $\ell$ ($\|\ell\theta_\mu\|$ small) join the major-arc counting framework as a third, *linear* (hence easier) family.
- **Large $\Lambda$** (one term per $\ell$): write $a=\ell b$: **Type-II bilinear sums** over $(\ell,b)$ with $\ell b\equiv a_0\,(q)$ — standard bilinear cancellation; at the extreme $\Lambda\sim A$ ($b$ bounded): **primes in APs mod $q$ against linear phases** $e(b\theta_\mu s)$ — Vinogradov/Balog technology, with $q=x^{u'}$ comfortably inside its range. Transition zones via the usual Vaughan splitting.

## 3. Verdict and residue

**Verdict: applies — via elementary unwinding; no friable black box required.** Residue (all classical-toolbox, to be written): (i) the Type-I/II ranges with uniformity in $(q,\mu,p)$ and the Vaughan gluing; (ii) the $\ell$-resonance count (third major-arc family, linear); (iii) **the one genuine check left**: Lemma B's finer anatomy classes (sizes/counts of primes in sub-bands) condition beyond bare friability — each class adds inclusion–exclusion layers of the *same species*, but the per-class verification must be done (this is the analogue of the fine-print checks on the B side). Fallback if (iii) misbehaves: the pinned friable literature (Harper 2016; dlB–T 2007 rational arguments; Fouvry–Tenenbaum 1991 APs).

## 4. Consequence for Lemma D

Every layer of D† is now either proved, counted, or classical-toolbox-pending-write-up:
| Layer | Status |
|---|---|
| large $\lambda$ | proved (deep large sieve) |
| digit, minor arcs | lemma stated; standard proof pending |
| digit, major arcs (2 families) | counted (q-average; 2 steps to rigorize) |
| anatomy, generic | exact unwinding → Type I/II + primes-in-AP (this memo) |
| anatomy, fine classes | per-class check pending (same species) |

**No identified structural obstruction remains on the path to full Lemma D.** What remains is uniformity bookkeeping at scale — which is real risk of a different kind. Calibration: **~45%** full strength (swing-warning from the roadmap applies; Type-II range pinches and the fine-class check are where surprises would live).
