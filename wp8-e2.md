# DRAFT — UNVERIFIED AGENT ATTACK REPORT

## WP8: Hypothesis E2 / Proposition `prop:familyB` on the FULL band

Date: 2026-06-10 (agent attack). Targets read: `manuscript/sections/08-major.tex`
(hyp:E2, prop:familyB, prop:digit-assembly), `12-e1e2.tex` (partial E2, sub-band
`16u+10u'>10`), `07-minor.tex` ((M2\*), `lem:cf`), `main.tex` (macros).
Notation: $L=\log x$, $P=x^u$, $Q=x^{u'}$, $u,u'\in(\tfrac13,\tfrac12)$,
$R=x^{1-u-u'}$, $G_0=R L^{-B}$, $\|\cdot\|$ = distance to $\mathbb Z$.

**VERDICT: PROVED** — not by proving the literal averaging statement of
Hypothesis E2, but by proving **Proposition `prop:familyB` unconditionally on the
full band** (in fact for *all* $P,Q,R,B$ with $G_0\ge 8$ — no band geometry, no
trim, no exponential sums over primes, no SL2). The role of hyp:E2 is thereby
discharged: `prop:familyB` and the Family-B line of `prop:digit-assembly` no
longer need any hypothesis. Confidence: **high (~0.9)** — the proof is fully
elementary (continued-fraction best approximation + smooth periodic majorant +
geometric series + the block reciprocal-sum lemma), every exponent inequality
was checked numerically at the corners, and a Monte Carlo probe confirms both
the count shapes and the tightness of the key truncation. Self-checked
adversarially; the two places a reader should scrutinize are flagged
(Steps 1 and 3 below).

---

## 1. Statement proved

**Theorem (Family B count, unconditional).**
Let $x$ be large, $B\ge1$, $G_0:=R\,L^{-B}\ge 8$, and let $P,Q\ge2$,
$2\le R$, with $P,Q\le x$. Then
$$
N_{\mathrm{fail}}:=\#\Big\{(p,q)\ \text{prime pairs},\ p\in(P,2P],\
q\in(Q,2Q],\ p\ne q:\ \exists\ \text{convergent denominator } s\le R
\text{ of } q/p \text{ with } s^{+}>sG_0\Big\}
$$
$$
N_{\mathrm{fail}}\;\ll\;\frac{PQ\,L^{B+1}}{R}\;+\;\frac{P^{2}\,L^{B+2}}{R},
$$
with an absolute implied constant. The second term equals
$PQ\cdot x^{2u-1}L^{B+2}$ on the band, power-small under the top trim
$u\le\frac12-\eta$, exactly as in the current statement of
`prop:familyB` (one extra factor $L$ on the second term; harmless downstream,
see §5).

This is precisely what `prop:familyB` asserts "modulo E2", now with **no
hypothesis and no sub-band restriction** — valid at and through
$(u,u')=(\tfrac13,\tfrac13)$.

---

## 2. Attack log (what was tried, in order)

1. **Angle (2'), per-$(p,s)$ reformulation with prime $q$ + Erdős–Turán +
   Vinogradov (modulus $p$).** Computed first. *Fails structurally:* at scale
   $S\asymp R$ the expected count per pair $(p,s)$ is
   $Q/(SG_0)\asymp x^{3u'+2u-2}L^B$, which is a **negative** power of $x$ at
   $(\tfrac13,\tfrac13)$ ($=x^{-1/3}L^B$). Per-pair equidistribution errors are
   bounded below by the prime exponential-sum bound
   ($\ge\sqrt{Qp}$-type $\gg1$), so any per-pair ET argument over prime $q$ is
   off by a positive power of $x$ aggregated over $PS$ pairs. Rare-event
   counting cannot be done pair-by-pair. Abandoned.

2. **Key structural observation — witness truncation (new).** For a prime pair
   $p\ne q$ and any non-final convergent denominator $s<p$ of $q/p$ one has
   $p\nmid sq$, hence $\|sq/p\|\ge1/p$; and a witness has
   $\|sq/p\|\le1/s^{+}<1/(sG_0)$. Therefore **every witness satisfies
   $s<p/G_0\le 2P/G_0$**: all dyadic scales $S>2P/G_0$ are *empty*. The
   manuscript's prop:E2 evaluates its bound at "worst case $S\asymp R$" — an
   empty scale whenever $3u+2u'<2$ (which includes the whole problematic
   lower-left region, e.g. $(\tfrac13,\tfrac13)$ and $(0.4,0.4)$). This single
   observation already kills the $PS$-endpoint term (see §4, Step 0) but not
   the $S^2Q$-endpoint term: the trivial $O(1)$-per-$(p,a,s)$ bound still
   overshoots by $x^{2u+u'-1}L^{B-1}$ after truncation. More is needed.

3. **Re-check of the manuscript's Vinogradov-in-$p$ route with truncation.**
   Even at the truncated worst scale $S_{\max}=\min(R,\,PL^B/R)$ the route
   fails: the term $(S^2Q/P)\cdot(P/\sqrt S)=S^{3/2}Q$ needs $2u+u'<1$ —
   violated **everywhere** in-band. Numerically confirmed failure at
   $(0.4,0.4)$, $(0.36,0.36)$, $(\tfrac13,\tfrac12)$, $(0.35,0.45)$ (§6,
   table D). Side-finding: the third term of SL2 as stated ($\sqrt s$) should
   be $\sqrt{Ps}$ (classical Vinogradov/Vaughan: $(Ps^{-1/2}+P^{4/5}+
   (Ps)^{1/2})\log^{O(1)}P$); with the corrected term the claimed sub-band
   $16u+10u'>10$ of prop:E2 appears to shrink further (e.g.
   $(\tfrac13,\tfrac12)$, where $16u+10u'=10.33>10$, fails my recomputation:
   the aggregated bound is $x^{23/30}>x^{2/3}=PQ/R$). Moot after this report,
   but `12-e1e2.tex` should not be trusted as-is.

4. **Winning combination (angle (2) + the majorant half of angle (1)):**
   per-$(p,s)$ reformulation (no $a$-sum) **+ relax $q$ from primes to
   integers** (free for an upper bound — this removes all prime exponential
   sums in $q$; the $q$-sums become geometric and are bounded by
   $\min(Q,\|hs/p\|^{-1})$ with **modulus $p\asymp P$, the large parameter**)
   **+ a smooth periodic majorant of the window** (Fourier coefficients of
   size $\delta$, not $1/h$ — this is the only "smoothing" actually needed;
   the threshold $s^{+}>sG_0$ stays sharp, so *nothing downstream changes*)
   **+ the elementary block reciprocal-sum lemma** $\sum_{h\le H}
   \min(N,\|hb/r\|^{-1})\ll(H/r+1)(N+r\log r)$ with $r=p$ prime
   **+ the witness truncation** $S\le2P/G_0$ from item 2. Result: per dyadic
   scale the full count (main + all boundary effects) is
   $\ll PQ/G_0+P^2L/G_0$, i.e. exactly the `prop:familyB` budget per scale.
   Complete proof in §4.

---

## 3. Two lemmas (elementary, self-contained)

**Lemma R1 (block reciprocal sum).** Let $r\ge2$, $(b,r)=1$, $H,N\ge1$. Then
$$
\sum_{h=1}^{H}\min\Big(N,\ \frac{1}{2\|hb/r\|}\Big)
\;\le\;\Big(\frac Hr+1\Big)\big(N+r(\log r+1)\big).
$$
*Proof.* Partition $\{1,\dots,H\}$ into $\le H/r+1$ blocks of at most $r$
consecutive integers. Within a block the residues $hb\bmod r$ are pairwise
distinct. At most one $h$ in the block has $r\mid h$ (contributing
$\min(N,\cdot)\le N$); the others contribute at most
$\sum_{j=1}^{r-1}\frac{1}{2\|j/r\|}\le\sum_{1\le j\le r/2}\frac rj\le
r(\log r+1)$. $\square$

**Lemma R2 (smooth periodic majorant).** For $0<\delta\le\tfrac18$ there is
$\Phi_\delta:\mathbb R/\mathbb Z\to[0,\infty)$ with
(i) $\Phi_\delta(t)\ge1$ whenever $\|t\|\le\delta$;
(ii) $\widehat{\Phi_\delta}(0)\le4\delta$;
(iii) $|\widehat{\Phi_\delta}(h)|\le C_A\,\delta\,(1+|h|\delta)^{-A}$ for any
fixed $A\ge2$.
*Proof.* Fix smooth $\eta$ with $\mathbf 1_{[-1,1]}\le\eta\le\mathbf
1_{[-2,2]}$ and set $\Phi_\delta(t)=\sum_{k\in\mathbb Z}\eta((t+k)/\delta)$.
Then $\widehat{\Phi_\delta}(h)=\delta\,\widehat\eta(\delta h)$;
$\widehat\eta(0)=\int\eta\le4$ and $|\widehat\eta(\xi)|\ll_A(1+|\xi|)^{-A}$ by
smoothness. $\square$

(A Selberg majorant of degree $H\asymp1/\delta$ works equally well, at the
cost of one extra $\log$; the essential point is *coefficient size
$O(\delta)$ at every frequency*, which the sharp-cutoff Fourier expansion with
$1/h$-coefficients does not give — that $1/h$ vs $\delta$ discrepancy at small
$h$ is precisely where ET-style arguments lose.)

---

## 4. Proof of the Theorem

**Step 0 (witness truncation).** Suppose $(p,q)$ fails, with witness
convergent $a/s$ of $\alpha=q/p$: $s\le R$, $s^{+}>sG_0$. Since the final
convergent denominator of $\alpha$ is $p$ and $s$ has a successor, $s<p$. By
`lem:cf(1)` (proved in `07-minor.tex`),
$$
\|s\alpha\|\le\frac1{s^{+}}<\frac{1}{sG_0}.
$$
On the other hand $p$ is prime, $p\nmid s$ (as $0<s<p$) and $p\nmid q$ (as
$q\ne p$ is prime), so $sq\not\equiv0\pmod p$ and
$\|s\alpha\|=\|sq/p\|\ge1/p$. Combining:
$$
s\;<\;\frac{p}{G_0}\;\le\;\frac{2P}{G_0}.
$$
*(Adversarial note: this is the step that uses primality of $p$ essentially —
twice. The Monte Carlo probe (§6, A) found witnesses with $sG_0/p$ up to
$0.999$ and $1.000^{-}$, i.e. the truncation is tight and correctly strict.)*

**Step 1 (per-scale majorization).** Assign each failing pair to one witness
and its dyadic block $s\in[2^k,2^{k+1})$, $0\le k\le K$, where
$2^K\le\min(R,\,2P/G_0)$, so $K+1\le\log_2 x\le L$ blocks (for $x\ge e$).
Counting triples instead of pairs, dropping the convergent property of $s$
(any integer $s$ in the block is allowed), and relaxing $q$ from prime to
integer — all enlargements, legitimate for an upper bound:
$$
N_{\mathrm{fail}}\;\le\;\sum_{k=0}^{K}\ \sum_{\substack{p\in(P,2P]\\ \text{prime}}}\
\sum_{2^k\le s<2^{k+1}}\ \#\Big\{q\in(Q,2Q]\cap\mathbb Z:\
\big\|\tfrac{qs}{p}\big\|<\tfrac{1}{sG_0}\Big\}.
$$
*(Adversarial note: relaxing $q$ to integers admits $q$ with $p\mid qs$
(possible once $Q\ge P$), for which $\|qs/p\|=0$ and which would have defeated
the truncation had it been applied after the relaxation. The order matters:
truncation in Step 0 uses primality of both $p,q$ and is applied to the
original count; the relaxation happens only inside the already-truncated
scales. The spurious $p\mid qs$ integers are then genuinely counted on the
majorant side — they sit in the $h\equiv0\pmod p$ terms of Lemma R1 and are
covered by its $N$-term.)*

**Step 2 (Fourier expansion of the majorant).** Fix a block $k$ and set
$\delta_k:=2^{-k}/G_0$; for $s$ in the block, $1/(sG_0)\le\delta_k\le1/G_0\le
\tfrac18$. By Lemma R2 (with $A=3$),
$$
\#\{q\}\;\le\;\sum_{q\in(Q,2Q]}\Phi_{\delta_k}\Big(\frac{qs}{p}\Big)
\;=\;\sum_{h\in\mathbb Z}\widehat{\Phi_{\delta_k}}(h)
\sum_{q\in(Q,2Q]}\e{\frac{hqs}{p}}
\;\le\;4\delta_k(Q{+}1)\;+\;C\sum_{h\ge1}\frac{\delta_k}{(1+h\delta_k)^{3}}
\min\Big(Q{+}1,\frac{1}{2\|hs/p\|}\Big),
$$
the interchange being absolutely convergent, the geometric-series bound
$|\sum_{q\sim Q}e(h qs/p)|\le\min(Q+1,\tfrac{1}{2\|hs/p\|})$ standard.

**Step 3 (Lemma R1 in dyadic $h$-ranges).** Here $s<p/G_0<p$ and $p$ is prime,
so $(s,p)=1$ and $hs/p$ has exact denominator $p$ unless $p\mid h$ — Lemma R1
applies with $r=p$, $b=s$. Splitting $h\le2/\delta_k$ and
$h\in(2^{j}/\delta_k,2^{j+1}/\delta_k]$, $j\ge1$, where the coefficient is
$\le\delta_k2^{-3(j-1)}$:
$$
\sum_{h\ge1}\frac{\delta_k}{(1+h\delta_k)^{3}}\min\Big(Q{+}1,\frac1{2\|hs/p\|}\Big)
\;\ll\;\delta_k\sum_{j\ge0}2^{-3j}\Big(\frac{2^{j+1}}{\delta_k\,p}+1\Big)
\big(Q+p(\log p+1)\big)
\;\ll\;\Big(\frac1p+\delta_k\Big)\big(Q+p\log 2p\big).
$$
*(Adversarial check of the worst sub-term: $j$-sum of
$2^{-3j}\cdot2^{j+1}/p$ converges to $O(1/p)$; $j$-sum of
$2^{-3j}\delta_k=O(\delta_k)$. Both clean. This is where the modulus being
$p\asymp P$ — large — pays: the "$H/r$" inflation factor of Lemma R1 is $O(1)$
because the effective $H\asymp1/\delta_k=2^kG_0\le2p$ by the truncation.)*

**Step 4 (assembly).** Sum over $\le P$ primes $p\in(P,2P]$ and $\le2^k$
integers $s$ in the block, using $p\le2P\le2x$ so $\log 2p\le3L$:
$$
\text{(block }k)\;\ll\;P\,2^k\Big(\frac1P+\frac{2^{-k}}{G_0}\Big)(Q+PL)
\;=\;\Big(2^k+\frac{P}{G_0}\Big)(Q+PL)
\;\le\;\frac{3P}{G_0}\,(Q+PL),
$$
the last step by the truncation $2^k\le2P/G_0$ — **for every block, including
the largest**. The main ($h=0$) part of Step 2 totals
$\ll P\,2^k\,\delta_kQ=PQ/G_0$ per block, of the same size. Summing over the
$\le L$ blocks:
$$
N_{\mathrm{fail}}\;\ll\;\frac{P(Q+PL)}{G_0}\cdot L
\;=\;\frac{PQ\,L^{B+1}}{R}+\frac{P^{2}L^{B+2}}{R}.\qquad\blacksquare
$$

Remarks. (i) Primality of $q$ was used only in Step 0; primality of $p$ in
Steps 0 and 3. (ii) The threshold $s^{+}>sG_0$ is the sharp one throughout —
the smoothing lives entirely in the counting majorant, so the (M2\*)
certificate, `cor:minor`, and `prop:digit-assembly` consume the result
verbatim. (iii) No top trim, corner trim, or band condition is used in the
Theorem itself; the trims enter only downstream (as before) to make the
$P^2$-term acceptable and $R$ polylog-large.

---

## 5. Downstream re-verification (`prop:digit-assembly`)

The new bound has $L^{B+2}$ (not $L^{B+1}$) on the $P^2$-term. Re-run the
assembly arithmetic with both terms taken as $L^{B+2}$:
per $q\sim Q$ on average, failing $p$ number
$\ll PL^{B+2}/R+(P^{2}/(QR))L^{B+3}$ (a factor $L$ from $1/\pi(Q)$); each
contributes $\le R$ to $\sum_p|V_p|$; budget $\pi(P)RL^{-c-1}\gg PRL^{-c-2}$:

* $P L^{B+2}\le PR L^{-c-2}$ ⟺ $R\ge L^{B+c+4}$ — implied by the corner trim
  $\sqrt R\ge L^{B/2+c+5}$ (which gives $R\ge L^{B+2c+10}$). OK with room.
* $(P^{2}/Q)L^{B+3}\le PRL^{-c-2}$ ⟺ $x^{2u-1}L^{B+c+5}\le1$ — power-saving
  under the top trim $u\le\frac12-\eta$. OK with room.

So `prop:digit-assembly` stands **unchanged** (same $B=C+c+4$, same trims),
now **modulo E1 only**. Suggested manuscript edits: delete hyp:E2 (or mark
"discharged — see WP8"); restate `prop:familyB` unconditionally with
$L^{B+2}$ on the second term and the proof of §4; in `10-remaining.tex` move
"D$^\dagger$: digit, major" to "modulo E1"; SL2 is no longer needed for E2
(it remains cited for Siegel–Walfisz/$g_{\mathbf z}$), and its statement
should anyway be corrected to $(\sqrt{Ps}+P/\sqrt s+P^{4/5})\log^{O(1)}P$.

---

## 6. Numerics (run with `.venv/bin/python`; probe script not retained per WP
instructions — logic summarized here, outputs verbatim)

**(D) Exponent arithmetic at the corners.** For the NEW bound the per-scale
worst exponents are $\max(\sigma_{\max}+u',\,2u+u'-1+u')$ (Q-piece, target
$2u+2u'-1$) and $\max(\sigma_{\max}+u,\,3u+u'-1)$ (P-piece, target $3u+u'-1$),
$\sigma_{\max}=\min(1-u-u',\,2u+u'-1)$. Verified $\le$ (with equality — the
bound exactly meets the budget shape, never beats it, never exceeds it):

```
 (u,u')=(0.333,0.333): NEW Qpiece=0.3333<=tgt 0.3333 True | Ppiece=0.3333<=P2tgt 0.3333 True | OLD-route 0.3333 ok
 (u,u')=(0.333,0.500): NEW Qpiece=0.6667<=tgt 0.6667 True | Ppiece=0.5000<=P2tgt 0.5000 True | OLD-route 0.7667 FAILS
 (u,u')=(0.500,0.333): NEW Qpiece=0.6667<=tgt 0.6667 True | Ppiece=0.8333<=P2tgt 0.8333 True | OLD-route 0.5833 ok
 (u,u')=(0.400,0.400): NEW Qpiece=0.6000<=tgt 0.6000 True | Ppiece=0.6000<=P2tgt 0.6000 True | OLD-route 0.7200 FAILS
 (u,u')=(0.360,0.360): NEW Qpiece=0.4400<=tgt 0.4400 True | Ppiece=0.4400<=P2tgt 0.4400 True | OLD-route 0.4800 FAILS
 (u,u')=(0.450,0.350): NEW Qpiece=0.6000<=tgt 0.6000 True | Ppiece=0.7000<=P2tgt 0.7000 True | OLD-route 0.6600 ok
 (u,u')=(0.350,0.450): NEW Qpiece=0.6000<=tgt 0.6000 True | Ppiece=0.5000<=P2tgt 0.5000 True | OLD-route 0.6800 FAILS
```
("OLD-route" = corrected-Vinogradov-in-$p$ bound *with* the new truncation;
it still fails on most of the band, including $(\tfrac13,\tfrac12)$ inside the
previously claimed sub-band — see §2 item 3.)

**(A)+(C) Monte Carlo, $x=2\cdot10^9$, $\Lambda:=R/G_0=8$** (sampled
$400\times400$ prime pairs, exact convergents):

```
[near-corner] u=u'=0.36: P=2230 Q=2230 R=402 G0=50.2: failures 10300/75625, density 0.1362
              vs main-term shape Lam*logR/R = 0.1193 (ratio 1.14); truncation violations: 0; max s*G0/p = 0.999
[asym u>u']  u=0.40 u'=0.34: density 0.1953 vs 0.1706 (ratio 1.15); violations 0; max s*G0/p = 1.000-
[asym u<u']  u=0.34 u'=0.40: density 0.1971 vs 0.1706 (ratio 1.16); violations 0; max s*G0/p = 1.000-
```
Failure density matches the proved main-term shape with constant $\approx1.15$;
the witness truncation $sG_0<p$ holds with zero exceptions and is attained up
to $0.1\%$ (tight, as the proof predicts).

**(B) Per-scale triple counts** $T(S)=\#\{(p,s,q):s\sim S,\ \|qs/p\|<1/(sG_0)\}$
($p$ prime, $q$ integer — the exact quantity bounded in Step 4) vs the proved
per-scale bound $(S+P/G_0)(Q+P\log P)$, at $x=10^8$:
all ratios $\le0.07$ ($u=u'=0.36$, all $S\le S_{\max}$) and $\le0.005$
($u=0.42$, $u'=0.34$); even against the log-free skeleton $(S+P/G_0)(Q+P)$ all
ratios $\le0.26$. The implied constant is comfortably absolute.

---

## 7. Obstructions encountered (all resolved or routed around)

1. *Per-pair rarity*: expected hits per $(p,s)$ are a negative power of $x$ in
   the lower band — rules out every per-pair equidistribution argument over
   prime $q$ (including the prompt's reformulation (2) taken with prime $q$ +
   Vinogradov modulus $p$: the $\sqrt{Qp}$ term times $PS$ pairs loses $x^{1/3}$
   at the corner). Resolution: aggregate counting with integer $q$.
2. *The $1/h$ ET loss at small frequencies*: for $h\le p/(sQ)$ the geometric
   $q$-sum has no cancellation; sharp-cutoff Fourier coefficients $1/h$ then
   produce a spurious $Q\log$ per pair. Resolution: majorant with
   $O(\delta)$-coefficients (Lemma R2) — the only "smoothing" needed; the
   threshold stays sharp (the stronger half of attack angle (1) — replacing
   the threshold itself — turned out unnecessary).
3. *The $h\equiv0\bmod p$ spikes* (integer-$q$ relaxation admits $p\mid qs$):
   covered by the $N$-term of Lemma R1; harmless because the truncation makes
   the number of $h$-blocks $O(1)$.
4. *Composite $p$ would break Steps 0 and 3* (gcd bookkeeping, $qs\equiv0$
   solutions): not needed — $p$ is prime in the application.
5. The literal hyp:E2 statement (per-scale endpoint average
   $\ll PS(SQ/P{+}1)L^{-B}$) is *not* proved and at small $S$ is likely
   stronger than true relative to this method's resolution; it is simply no
   longer needed — `prop:familyB` is its only consumer.

## 8. Verdict

**PROVED** (Proposition `prop:familyB` unconditional on the full band
$u,u'\in(\tfrac13,\tfrac12)$ — and beyond; Hypothesis E2 discharged; the
digit-major layer of `prop:digit-assembly` now rests on E1 alone).
Confidence: high (~0.9). Residual risk: transcription-level — the constants in
Lemmas R1/R2 and the block bookkeeping in Step 4 should be re-derived
independently before the manuscript is updated; the structural steps
(truncation, relaxation order, modulus-$p$ reciprocal sums) were each checked
adversarially and numerically.
