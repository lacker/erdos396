# Roadmap: Density of $n$ with $n(n-1) \mid \binom{2n}{n}$

**Status document, v0.3 — June 9, 2026.**
v0.3 is rebuilt against the **full chat export** of the original working session ("Selecting an Erdős problem for AI-assisted decomposition"). All substantive claims below are now recovered from that transcript unless explicitly tagged **[reconstructed]** (my re-derivation, to be verified) or **[N]** (established fresh in the June 9 session, citable). One caveat on the export: the *artifacts* the old sessions produced (the skeleton document, `HYPOTHESES_CHECK.md`, the test scripts) were stripped from it — their content survives in the session reasoning and is captured below, but the files themselves must be re-created (see WP4).

---

## 1. The problem, the target, and the constants

**Parent problem [N].** Erdős Problem 396: for every $k$, does some $n$ satisfy $\prod_{0\le i\le k}(n-i)\mid\binom{2n}{n}$? Known: $(n+1)\mid\binom{2n}{n}$ always; Pomerance (2014): infinitely many $n$ with $(n-k)\mid\binom{2n}{n}$ for each $k$, upper density $<1/3$; the $(n+i)$-product version holds with density 1. Witnesses for the literal problem are known computationally up to $k=7$; for $k=1$ the literal question is trivial ($n=2$). The mathematical content is "for every $k$" — and, as far as the original session's literature review found, even **infinitude of $W_1$ is not in the literature**.

**Notation.** $W_1=\{n: n(n-1)\mid\binom{2n}{n}\}$. $D_0=\{m: m\mid\binom{2m}{m}\}$ is **Pomerance's governor set**; by Kummer, $m\in D_0$ iff for every $p^e\,\|\,m$ the carry count $\kappa_p(m)=\#\{j: 2(m\bmod p^j)\ge p^j\}$ is $\ge e$; the smoothness condition $P^+(m)\le\sqrt{2m}$ is necessary. Ford–Konyagin proved $D_0$ has density $c_1 = 0.11424$. Empirics: $W_1\ni 2, 210, 460,\ldots$, measured pair density at $10^9$ is $0.92\cdot c_1^2$ (finite-scale, converging); $c_1^2\approx 0.01305$.

**Lemma 0 — exact sandwich (done, verified).** $q\mid n-1$ shifts the base-$q$ digits of $n$ by exactly $q^{-j}$ in fractional-part terms ($\{(n-1)/q^j\}=\{n/q^j\}-q^{-j}$), so the carry conditions for $n$ at the primes of $n-1$ are the governor conditions of $n-1$ itself up to margins of width $q^{-j}$. With margin-modified governor sets:
$$D_0\cap(D_0^{(+)}+1)\ \subseteq\ W_1\ \subseteq\ D_0\cap(D_0^{(-)}+1)$$
**exactly** — not merely up to Pomerance's density-0 equivalence. Verified with zero exceptions on 60,000 cases and by sampling at $10^9$; the margin sets differ from $D_0$ in density by $\le 10^{-4}$ (measured $\approx 6\times 10^{-5}$ at $10^9$), and the lower set captures 98.7% of $W_1$.

**Target theorem hierarchy.**
- **Theorem 1 (rung i):** the events $n\in D_0$ and $n-1\in D_0$ are asymptotically independent; the **log-density** of $D_0\cap(D_0+1)$ is $c_1^2$.
- **Theorem 1″ (realistic form):** density $c_1^2+O(\log^{-c}x)$ at **almost all scales** — this implies both infinitude and the log-density asymptotic. "Almost all scales" is the field's frontier (Tao–Teräväinen's own results carry the same limitation), not a concession.
- **Theorem 1′ (lower-bound fallback):** positive log-density of $W_1$, via the mitigations in §5/WP2′.

---

## 2. State ledger

| Item | Content | Status |
|---|---|---|
| Lemma 0 | Exact sandwich (above) | **Done**, machine-verified; writeup pending |
| Lemma A | Two-sided "primes below $n^\delta$ ignorable" — FK's digit-counting adapts with one line changed (low digits $(1,0^{v-1})$ instead of $0^v$) | [known-adapt], ready to write |
| Lemma B | Anatomies of $n$ and $n-1$ independent (consecutive-smooth technology) | **Essentially citable**: Tao–Teräväinen (arXiv 2512.01739, Dec 2025) prove the smooth-pair asymptotic $\rho(u)\rho(v)$ quantitatively at almost all scales; our indicators enter via the $z$-interpolation trick. Remaining: a half-page lemma + three fine-print checks (§4, WP3b) |
| Lemma C | Conditional on both anatomies, $n$-side digit conditions equidistribute uniformly against bounded multiplicative weights on $n-1$ — FK's hardest section with a twist | [new, standard toolbox]; needs multiplicative-BV inputs averaged over moduli **plus the top-digit deterministic law** (state equidistribution for interior digits only; top digit follows FK's piecewise law). Known quantitative reality: ~4% finite-scale within-side deviation, fully explained (thin-progression effect; Friedlander–Iwaniec §4 simultaneous fractional parts is the hardest ingredient) |
| Lemma D | Cross-side digit independence — the hard core | Open. Fully reduced (§3); empirically immaculate (cross-side ratio $1.003\pm0.012$, three runs $0.984/1.003/0.995$); partial unconditional tools derived (§3.3) |

---

## 3. Lemma D in full (recovered)

### 3.1 Setup and reduced form

Band primes are those in $((2n)^{1/3},\sqrt{2n}]$; write $p=x^u$ for a band prime of $n$ and $q=x^{u'}$ for one of $n-1$, with $u,u'\in(1/3,1/2)$. Dominant configuration: $n=pa$, $n-1=qb$, so $pa-qb=1$ — a Titchmarsh-divisor-type problem with congruence constraints. The $(n-1)$-side digit condition at $q$ is exactly: $n\equiv 1\pmod q$ **and** $(n-1)/q\bmod q\in[q/2,q)$ — i.e. $n$ in specific classes mod $q^2$ above $1\bmod q$, with $q^2$ ranging over $[x^{2/3},x]$, far beyond classical dispersion (Bombieri–Friedlander–Iwaniec) for general coefficients.

Harmonic dual: $(\mathbb{Z}/q^2)^*\cong\mathbb{Z}/(q-1)\times\mathbb{Z}/q$, and the mod-$q^2$ refinement of $1\bmod q$ is detected by the **depth-1 characters** $\chi_\lambda(n)=e(\lambda\,\ell_q(n)/q)$, $\ell_q(n)=\frac{n^{q-1}-1}{q}\bmod q$ the **Fermat quotient** — a group homomorphism, so $\ell_q(pa)=\ell_q(p)+\ell_q(a)$ and the phases factor completely over $n=pa$ (Vinogradov/Vaughan decompositions essentially for free).

**Estimate D\* (final reduced form).** Structuring the proof so Lemmas B/C deliver the undecorated count, Lemma D's *entire* new content is the deep-character error term: on average over band primes $q\sim Q$,
$$E_q\;=\;\sum_{0\ne\lambda\bmod q} c_\lambda \sum_{\substack{p\sim P,\ pa\le x\\ pa\equiv 1\ (\mathrm{mod}\ q)}} v(a)\, e\!\Big(\frac{\lambda\,\ell_q(pa)}{q}\Big)\;\ll\;\frac{x}{q}\,(\log x)^{-c},$$
where $c_\lambda\ll\min(1,q/|\lambda|)$ are the Fourier coefficients of $[q/2,q)$ and $v$ is 1-bounded, carrying the $n$-side digit decoration (non-multiplicative but mod-$p$-structured). Equivalent Vaaler form: with $H=\log^C x$, need $\max_{0<|h|\le H}\sum_{q\sim Q}|S_w(q,h)|\ll x(\log x)^{-c}$, uniformly across slot levels (moduli $q^{j-1}$ at slot boundaries $q\approx(2n)^{1/j}$, where $T/M=x^{1-j\gamma}$), multi-prime variants, and top slivers. Higher exponents $q^e\,\|\,n-1$ and multiple band primes per side = the same framework mod $q^{e+1}$ with deeper characters — bookkeeping.

**Hardness diagnosis (settled).** Parity-free: the indicators are non-negative, positive-mean, local — the Chowla-type parity wall does not apply. The true class is BV-type equidistribution to large moduli on average. Orthogonality over the deep family is a **Wieferich-type condition** ($\sum_\lambda\chi_\lambda(y)=q\cdot\mathbf{1}[y^{q-1}\equiv 1\bmod q^2]$): pointwise intractable, average-friendly. The Teichmüller subgroup $T_q$ and **Heilbronn sums** $\sum_s e(hs^q/q^2)$ are the algebraic backbone (Heath-Brown, Heath-Brown–Konyagin, Shkredov bounds available).

### 3.2 The Tao–Teräväinen / Pilatte verdict (reading session — COMPLETE)

- Pilatte (arXiv 2310.19357): power-of-log saving for two-point logarithmic Chowla. Multiplicativity of $\lambda$ is invoked in **exactly two places** — the centring step (via Matomäki–Radziwiłł–Tao) and the dilation step ($\lambda(pn)=\lambda(p)\lambda(n)$). The **spectral engine** (eigenvalue bound on the divisibility matrix, §§4–13) needs only 1-boundedness.
- TT Theorem 3.1 has **asymmetric hypotheses**: $g_1$ must be equidistributed (real case) or non-pretentious (complex case); $g_2$ needs only 1-bounded multiplicative.
- **Verdict for Lemma B: citable** (put the awkward function in the $g_2$ slot). Three fine-print checks remain: (1) uniformity — their theorems assume fixed functions, ours scale with $x$ (bands $\sim x^\alpha$); (2) confirm the conclusion delivers correlation $=$ product of means (the equidistributed case does — this is how they handle $\omega(n)=\omega(n+1)$); (3) verify the exact Theorem 3.1 statement (fetch was in progress at cutoff).
- **Verdict for Lemma D: blocked as a black box.** The dilation step needs $F(dn)=F(d)F(n)$; digit conditions are not dilation-invariant (multiplying $n$ by $d$ scrambles base-$p$ digits). The almost-all-scales route is blocked for the same reason. **But** the spectral engine survives as a tool for a dispersion-style argument with a re-weighted (Möbius-like) matrix — inspiration, not citation.

### 3.3 Unconditional partial results — DERIVED BUT NEVER WRITTEN (salvaged from the export; the cutoff killed the writeup)

- **Proposition (Teichmüller energy) [reconstructed from session reasoning — re-verify]:** the multiplicative energy of $[N]$ against $T_q$ — i.e. the count of Wieferich-type pairs $n_1\equiv t\,n_2\ (\mathrm{mod}\ q^2)$, $t\in T_q$ — is unconditionally $\ll N^2/q+qN$ (positivity + completeness of the deep character family).
- **Corollary (deep large sieve):** over the family $\{(q,\chi_\lambda)\}$, per-$\lambda$ RMS bound $\sqrt{qN}$ — a saving of $\sqrt{N/q}$ over trivial, nontrivial whenever $N>q^{1+\varepsilon}$.
- **Application to D\*:** the $a$-side always qualifies ($N_a=x^{1-u}>x^{u'}$ since $u'<1/2<1-u$): unconditional saving $x^{(1-u-u')/2}$ after Cauchy–Schwarz in $p$. The $p$-side qualifies only when $u>u'$ — half the band.
- **Identified open corners:** (i) the top of the band $\gamma\to 1/2$ on both sides — addressable by the $\eta$-trim (restrict to $\gamma\le 1/2-\eta$; the top sliver contributes only $O(\eta)$ density), at least for lower-bound versions; (ii) the $u<u'$ region for prime sums; (iii) whether per-$\lambda$ savings survive the $\lambda$-sum (weights total $\sum|c_\lambda|\approx\log q$).
- **The flagged main theoretical question:** a genuine large sieve averaged over $(q,\lambda)$ pairs *tailored to the bilinear structure* could close the entire gap. For fixed $p$, the map $q\mapsto\ell_q(p)$ behaves randomly across $q$ (Wieferich heuristics) — exactly what a $q$-averaged mean-value theorem would exploit.

**Relevant literature [N, searched June 9]:** Heath-Brown: consecutive-argument Fermat-quotient sums nontrivial for $N\ge q^{1/2+\varepsilon}$; **Shparlinski (arXiv 1104.3909): averaging over the prime modulus, nontrivial for $N\ge q^\varepsilon$** (Garaev + Baier–Zhao large sieve) — the structural precedent for our band-averaging; Chang (Acta Arith. 152): short character sums with Fermat quotients; BKS (Michigan Math. J. 59) on divisibility of Fermat quotients; Shkredov refinements of Heilbronn-sum bounds. Note: Shparlinski's open-problem list flags nearby individual regimes (e.g. Fermat-quotient sums in ranges $N\le p$) as very difficult — the bet is that averaging substitutes for what is open individually.

### 3.4 Mitigations for the lower-bound version (the three, plus the trim)

1. **Automatic-carry band:** $q^2\in(n,2n]$ forces the slot-2 carry deterministically — the $(n-1)$-side band-digit condition is free there. (Fine structure of the deterministic slivers is mapped: $q^2\in(n/2,2n/3]$ deterministic success, log-measure 0.288; $q^2\in(2n/3,n]$ deterministic failure, log-measure 0.405; analogous alternation at each slot boundary.)
2. **Margin freedom:** the sandwich margins cost $\le 6\times10^{-5}$ in density — negligible room that any one-sided argument can spend.
3. **Positive-proportion anatomy subclass suffices** for Theorem 1′ — no need to control all anatomy classes.
4. ($\eta$-trim, part of the slot strategy:) excluding $\gamma\in(1/2-\eta,1/2]$ costs $O(\eta)$ density and removes the worst regime.

---

## 4. Dead-ends registry — DO NOT REPAY (proofs of death recovered)

- **Union bounds** across the digit layer: total failure mass is $\Theta(1)$ (loglog-many primes). Dead.
- **Smooth-cofactor designs:** always lose $\rho(c/\delta)$ vs $e^{-c/\delta}$ — smoothness probability $u^{-u}$ is exponentially weaker than the failure mass $2^{-u}$ it must cover (this retroactively explains the Tier-B $m^2$ disappointment). Dead, including the "favorable anatomy class bypasses D" variant: Theorem 1′ still requires conditional digit independence within at least one positive-probability anatomy class — a D-type statement.
- **Semiprime trick:** dies on excluding the prime case.
- **Pilatte/TT as black box for D:** dead at the dilation step (and almost-all-scales route with it) — see §3.2.
- **Crude Cauchy–Schwarz over $\chi_1$ in the deep family:** discards the deep twist; error $\sim x/q$, zero savings.
- **Heilbronn-completion via max-over-intervals:** error $q^{1-\delta_0}$ dominates the main term $P/q$; must average over the actual intervals $p_2^{-1}[P,2P)$ instead.

---

## 5. The roadmap (hardest first, de-risk before prove)

### WP1 — Lemma D de-risking sprint (partially complete; finish it)

- **WP1.1 — Formal Estimate D\* [salvage task].** The reduced form exists (§3.1) but only as session reasoning. Write it as a formal statement with exact ranges, weights, and required exponents. ~1 session.
- **WP1.2 — T–T hypothesis check: DONE.** Verdict in §3.2. No further work; record in manuscript.
- **WP1.3 — Write up the deep large sieve [highest-value salvage].** The Teichmüller-energy proposition and its corollary (§3.3) exist only as reasoning in the export. Re-derive carefully, verify the energy bound $N^2/q+qN$, and write the proof. This is the program's only *new unconditional theorem-grade* artifact so far and it is currently unwritten. ~1 session.
- **WP1.4 — Numerology table.** For $(u,u')\in(1/3,1/2)^2$: required saving per $(q,\lambda)$ vs what the deep large sieve gives vs what the literature gives (Heath-Brown, Shparlinski-on-average, Chang, Heilbronn bounds). Output: the precise uncovered region (expected: the $u<u'$ prime-sum corner and the $\lambda$-sum bookkeeping). This was planned in the final session and never built.
- **WP1.5 — The never-run empirics.** Script exists in plan only: verify $\ell_q(mn)=\ell_q(m)+\ell_q(n)$ and the $\chi_\lambda$ formalism on small $q$; for ~5 band primes $q\sim10^3$–$10^4$ build $n$-populations along $1+q\mathbb{Z}$ (inner populations $10^4$–$10^5$), compute $T_q(\lambda)$ and report $|T|/\sqrt{N_{\text{class}}}$ against the square-root benchmark; stratify by $\gamma$ (the top stratum is the diagnostic); measure the phase-aligned $\sum_q S(q,h)$ per stratum; validate the $E_q$ error terms at scale $\sim10^9$. If the cancellation is messy, the approach fails — kill signal. ~1 day of compute.
- **WP1.6 — Gate G1.** Pass: numerology table + empirics show the uncovered region is shrinkable by the identified ideas (tailored $(q,\lambda)$-averaged large sieve; bilinear Wieferich counting) → WP2. Weakened pass: covered region + mitigations close a lower bound → WP2′. Kill: uncovered region provably equivalent to individually-open bounds with no averaging help → record precisely (it *is* the rung-ii estimate) → WP4/WP5.

### WP2 — Prove Lemma D (after G1 pass)

Toolkit, in order of expected leverage: (a) the deep large sieve + complete bilinearity from the $\ell_q$ homomorphism + $q$-averaged Wieferich counting; (b) the tailored $(q,\lambda)$-averaged mean-value theorem (the flagged main question); (c) the Pilatte spectral engine re-weighted for the $q\mid n-1$ divisibility structure (1-boundedness suffices there). **P(full D) today: ~25–30%** — up from v0.1: parity-freedom is settled, soft tools already cover real parts of the range unconditionally, and the uncovered corners are identified and specific; held down by the $u<u'$ prime corner and $\lambda$-sum bookkeeping.

### WP2′ — Route B: lower-bound theorem via mitigations

Combine the covered region (deep large sieve + $\eta$-trim + automatic band + margin freedom + one good anatomy subclass) and check the one-sided sandwich closes. **P(headline-worthy unconditional lower-bound statement | weakened pass): ~60%.**

### WP3 — Lemma C

As recovered (§2), with the structural correction from testing: equidistribution stated for interior digits; top digit deterministic via FK's piecewise law; Friedlander–Iwaniec §4 (simultaneous fractional parts) is the hardest ingredient. **P: ~75%.**

### WP3b — Close Lemma B

Verify TT Theorem 3.1's exact statement; run the three fine-print checks; write the half-page lemma; re-derive the $z$-interpolation trick. **[reconstructed, verify]:** since $n\le x$ has $\le 3$ prime factors above $x^{1/3}$, take $g_z$ completely multiplicative with $g_z(p)=z$ on band primes and $1$ off; then $g_z(n)=z^{\#\{\text{band primes}\mid n\}}$ with exponent in $\{0,\dots,3\}$, and interpolation at 4 values of $z$ (Vandermonde) expresses each band-count indicator as a finite combination of 1-bounded multiplicative functions. **P: ~85%.**

### WP4 — Manuscript spine (parallel, zero risk)

Now doubly urgent: it locks rung (ii) *and* re-creates the lost artifacts (the skeleton, the dead-ends §8, HYPOTHESES_CHECK, the verified Lemma 0 writeup, the deep-large-sieve proposition). The export is the only backup of several derivations; paper form is the durable one. **P(rung-ii paper): ~90%.**

### WP5 — Constructive route for general $k$ (parked)

Balog–Wooley-style witnesses; the carry calculus, Lemma A, and digit laws transfer. $k$-point correlation technology is the frontier (open even for smoothness; log-Chowla open for even $k\ge4$ — though our functions are parity-free, so smoothness-type $k$-point may be more tractable). Revisit on a G1 kill or after the $k=1$ paper.

---

## 6. Decision tree and calibration

```
WP1 finish (D de-risk: salvage writeups + numerology + empirics)
 ├─ G1 PASS ──────► WP2 prove D ─┬─ success ► + WP3/WP3b ► Theorem 1″ (rung i)
 │                               └─ stall   ► fall to weakened handling
 ├─ G1 WEAKENED ──► WP2′ lower-bound theorem + rung-ii paper
 └─ G1 KILL ──────► exact obstruction recorded ► rung-ii paper + WP5
                        (WP4 manuscript runs in parallel throughout)
```

- Rung (i), full theorem at almost all scales: **~25–30%**
- Unconditional lower-bound theorem (Route B): **additional ~25–30%**
- Rung (ii) conditional paper with everything else verified: **~90%**
- Contribution to literal Erdős 396 (general $k$): **~15–40%** by ambition level

## 7. Immediate next actions

1. **WP1.3** — write the Teichmüller-energy proposition + deep large sieve properly (the derivation currently exists nowhere but the export and this document).
2. **WP1.1** — formal Estimate D\*.
3. **WP1.4** — numerology table over $(u,u')$.
4. **WP1.5** — empirics script (the final session's planned measurements, never run).
5. **WP3b** — fetch TT 2512.01739 Theorem 3.1 and finish the citability check; re-derive $z$-interpolation.
6. **WP4** — start the manuscript spine; fold §§3–4 of this document into it.

## 8. Method note

Hardest-first governs risk-resolution order, not all effort. The refinement that proved its worth in the original sessions: the first unit of work on the riskiest item is diagnosis, and dead ends get recorded with proofs of death so they are never repaid. v0.3's main lesson: derivations that exist only in a session's working memory are one context-limit away from oblivion — WP1.3 and WP4 exist to make everything durable.
