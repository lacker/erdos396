# WP2.2: D†-Minor Lemma and the Major-Arc Counts

**STATUS: SUPERSEDED IN PART BY THE WP4 WRITE-UP (`manuscript/`, June 9 evening) — see Erratum §0.** D†-digit (anatomy off) remains closed modulo the two average-equidistribution steps (now Hypotheses E1/E2, stated precisely in manuscript §8), but both the minor-lemma statement and the Family-B definition below needed repair when the proof was actually written. The corrected minor bound is **proved** (manuscript §7). The conclusion-level claims of this memo survive; the intermediate statements (§§1,3) do not.

## 0. ERRATUM (June 9, evening — from the WP4 consolidation sprint)

Writing the minor-arc proof rigorously (manuscript §7) exposed two errors, one per hypothesis:

1. **(M2) as stated below is insufficient.** A convergent denominator near $R$ controls only the blocks at scale $\approx R$. At scale $M \ll R$ the governing structure is the convergent gap *at scale $M$*: a long gap there admits a "graze" configuration — a run-progression approaching the origin at the (M1)-floor — carrying mass $\asymp\sqrt{s^+/s}$ in full consistency with (M1).
2. **The polylog conclusion is false in general.** The first partial quotient of $q/p$ is $\asymp p/q$, so for $u>u'$ *every* pair carries the structural gap $s=1$, $s^+\asymp p/q$, and the graze reaches $\sqrt{p/q}$ — a power. No sparsity condition can excise it.

**The correct theorem (proved, manuscript §7):** under (M1) alone,
$$|V_p(\lambda)| \ll L^{B+3}\bigl(1+\mathcal D_R(q/p)\bigr) + L^2\,R/s_0, \qquad \mathcal D_R(\alpha):=\sum_{s\le R \text{ convergent}}\sqrt{s^+/s},$$
with $s_0$ the largest convergent denominator $\le R$. Minor set redefined by the all-scale gap-ratio threshold $s^+/s \le R L^{-B}$ ("(M2*)"), which **automatically exempts the structural $s=1$ gap** under the top trim ($p/q \le RL^{-B} \iff x^{2u-1} \le L^{-B}$). On the minor set: $|V_p| \ll \sqrt{R}\,L^{B/2+4} + RL^{2-B}$ — square-root scale, not polylog, but **within the assembly budget with room** ($\sqrt R \ge L^{B/2+c+5}$ corner trim). Typical pairs still see polylog: $\mathbb E_{p,q}\,\mathcal D_R \ll L^2$. Family B recounted at threshold $G_0=RL^{-B}$: $\ll PQL^{B+1}/R$ pairs (+ power-small), still ample. Empirics agree: observed minor medians sit at $z\approx0.08$ in $\sqrt R$-normalized units — square-root scale with small constants, which the original polylog claim would have contradicted at scale. Same genre as the WP2.0 erratum: the de-risk discipline (draft the proof before trusting the note) did its job twice.

---

## 1. Lemma D†-minor (statement)

Fix $q\sim Q$, $0<\lambda\le L^{C}$, and $p\sim P$ a band prime; $R=x/(pq)$, $\alpha=q/p$, $\theta_\mu=\mu\alpha-\lambda p/q$. Call $p$ **minor** for $(q,\lambda)$ if:
- **(M1)** $\dfrac{1}{\mu}\min\!\big(R,\tfrac{1}{2\|\theta_\mu\|}\big)\le L^{B}$ for every $0<\mu\le R$;
- **(M2)** $q/p$ has a continued-fraction convergent with denominator $r\in[R/L^{B},\,R\,L^{B}]$.

Then, with $\sigma\equiv1$ (anatomy off): $|V_p(\lambda)|\ll L^{B}\log x$.
**Proof ingredients.** $|V_p|\le\sum_{\mu\ne0}\frac{C}{\min(\mu,p-\mu)}\min(R,\frac{1}{2\|\theta_\mu\|})$; dyadic blocks $\mu\sim M$ via the inhomogeneous Vinogradov lemma at the (M2)-convergent denominator $r\asymp R$ give $\ll\log x$ per block for $M\ge R$, and $\ll R/r+\log\ll L^{B}$-controlled for $M<R$ with the single-frequency excesses excluded termwise by (M1). Standard but fiddly; cite Iwaniec–Kowalski / Vaughan Lemma 2.2-type inhomogeneous variants in the write-up. The exact lattice structure $\{\theta_\mu\}=\{(j-\beta)/p\}$ (a bijection $\mu\leftrightarrow\mu q\bmod p$) is what makes the bookkeeping clean.

## 2. Family A count (quadratic resonances — (M1)-failures)

(M1) fails iff $\exists\,\mu\le R/L^{B}$ with $\|\theta_\mu\|\le\frac{1}{2\mu L^{B}}$, i.e. $|\mu q^2-\lambda p^2-kpq|\le\frac{pq}{2\mu L^{B}}$ — lattice points near the conics $p\approx q\sqrt{\mu/\lambda}$. Counting $p\sim P$ with $\|\theta_\mu(p)\|\le\delta_\mu$: the average count is $2\delta_\mu P$ (the wrap-boundary terms $\asymp\mu Q/P+\lambda P/Q$ **average out over $q\sim Q$** — this is one of the two equidistribution steps to rigorize; the worst-case-per-$q$ version stands for the lower-bound track). Summing $\mu\le R$, $\lambda\le L^{C}$:
$$\mathbb{E}_{q\sim Q}\,\#\{p\ \text{(M1)-major}\}\ \ll\ \frac{P\,L^{C+1}}{L^{B}}\,,$$
**polylog-sparse in $p$ for $B\ge c'+C+2$.** Damage: each major $p$ contributes $\le R$ to $T_q$ vs budget $\asymp\pi(P)R\,L^{-c}$ — controlled.

## 3. Family B count ((M2)-failures: a CF gap straddling $R$)

(M2) fails iff some convergent $a/r$, $r<R/L^{B}$, has $|qr-pa|\le p/(RL^{B})=:w'$ with successor denominator beyond $RL^{B}$. Lattice count near the lines $qr=pa$: per coprime $(a,r)$, on average over $p$, $\#q\approx w'/r$; summing $r\le R/L^{B}$, $a\asymp rQ/P+O(1)$:
$$\#\{(p,q)\ \text{(M2)-major}\}\ \ll\ \frac{PQ}{L^{2B}}\;+\;\frac{P^{2}\log x}{R\,L^{B}},$$
and the second piece is **power-small**: $P^2/(RQP)=x^{2u-1}\to0$ since $u<\tfrac12$. Sparse. (Second equidistribution step to rigorize: the average of the per-$p$ $O(1)$ boundary terms.)

## 4. Assembly for D†-digit, and the anatomy layer

Per $q$: $|T_q|\le\pi(P)\,L^{B+1}+R\cdot\#\{\text{major }p\}$. With §§2–3: $|T_q|\le N_q^{\rm pop}L^{-c}$ on average over $q$, **provided $R\ge L^{B+c+2}$** — i.e. excluding an $\eta''$-sliver at the corner $u+u'\to1$ (a third trim; $O(\eta'')$ density cost; record alongside the others). **So D†-digit closes modulo: the minor-lemma write-up and the two average steps.**

**Anatomy layer (σ reinstated).** By the conditional architecture, $\sigma$ here is the *anatomy-only* part of the cofactor weight (within-side digit conditions belong to Lemma C's uniformity clause — state this interface explicitly in the manuscript). Needed: minor-arc bounds for exponential sums of smooth-type indicators at the rational frequencies $\theta_\mu$ (denominator $pq$), plus major-arc asymptotics to merge with the counts above. Pinned literature (June 9): **Harper 2016, Compositio 152** (minor arcs, mean values, restriction for smooth Weyl sums — the exact dichotomy needed); **de la Bretèche–Tenenbaum 2007, Funct. Approx. 37** (friable exponential sums at *rational arguments*); de la Bretèche 1998, PLMS 77; **Fouvry–Tenenbaum 1991, PLMS 63** (friable numbers in APs); Drappeau 2015, Canad. J. Math. 67; Drappeau–Shao 2016; de la Bretèche–Granville 2022, Trans. AMS (exponential sums with multiplicative coefficients). Risk note: our cofactor condition ("no prime in the band above $p$" + size constraints) is smooth-*type*, not literally $y$-friable — expect an adaptation layer, not a citation.

## 5. Status after WP2.2

| Piece | Status |
|---|---|
| D†, large $\lambda$ | covered (deep large sieve) |
| D†-digit, minor arcs | lemma stated; standard-toolbox proof; write-up pending |
| D†-digit, major arcs | counted: A polylog-sparse (q-avg), B sparse + power-small |
| D†-anatomy | open; matched literature pinned; adaptation expected |
| trims accrued | top-of-band $\eta$; corner $u{+}u'\to1$ $\eta''$ (lower-bound track unaffected) |
