# Lemma D: Cross-Side Digit Independence — THE HARD CORE

**STATUS: OPEN — GATE G1 PASSED (June 9).** De-risking complete: no exponent gap (`numerology-D.md`), cancellation empirically clean on the real coupled object (`empirics-D.md`). Active work: write-up and uniformity bookkeeping — **no identified structural obstruction remains** (`wp23-anatomy.md`): digit layer closed modulo write-up; anatomy layer unwinds exactly ($u_f<2$) into Type-I/II + primes-in-AP sums; pending = fine-anatomy-class check, two equidistribution rigorizations, Type-II ranges. Calibration: **~45% full strength** (down from the inflated 35–40; the empirical truth-evidence stands, the provability path is a genuine dispersion fight); ~60% lower-bound version if D† resists in full. Empirically immaculate: cross-side ratio $1.003\pm0.012$ (original runs) and now the direct $E_q$-integrand probe at $x=10^8$: $z=O(1)$ at all strata (`empirics-D.md`).

---

## 1. Statement (informal)

Conditional on the anatomies, the digit conditions on the $n$-side and the $(n-1)$-side are jointly independent: the $(n-1)$-side digit layer still equidistributes after conditioning on the anatomy **and the digit outcome of the $n$-side**. Formally: $\sum_{n\le x}F_1(n)F_2(n-1)$ factors as the product of means, where the $F_i$ carry anatomy + digit data.

## 2. The reduction (final form, recovered from the original sessions)

Band primes: $((2n)^{1/3},\sqrt{2n}]$; parametrize $p=x^u\mid n$, $q=x^{u'}\mid n-1$, $u,u'\in(1/3,1/2)$. Dominant configuration $n=pa$, $n-1=qb$, i.e. $pa-qb=1$ (Titchmarsh-divisor type with congruence decorations).

The $(n-1)$-side digit condition at $q$: $n\equiv1\ (\mathrm{mod}\ q)$ **and** $(n-1)/q\bmod q\in[q/2,q)$ — residue classes mod $q^2$ above $1\bmod q$, $q^2\in[x^{2/3},x]$: beyond classical dispersion (BFI) for general coefficients. Harmonic dual: the mod-$q^2$ refinement is detected by depth-1 characters $\chi_\lambda(n)=e(\lambda\ell_q(n)/q)$ (see `prop-deep-large-sieve.md`), and $\ell_q(pa)=\ell_q(p)+\ell_q(a)$ makes the phases **completely bilinear** — Vinogradov/Vaughan decompositions for free.

**Estimate D\* (the whole of Lemma D, once B/C deliver the undecorated count):** on average over band primes $q\sim Q$,
$$E_q=\sum_{0\ne\lambda\bmod q}c_\lambda\!\!\sum_{\substack{p\sim P,\ pa\le x\\ pa\equiv1\ (\mathrm{mod}\ q)}}\!\! v(a)\,e\!\Big(\frac{\lambda\,\ell_q(pa)}{q}\Big)\;\ll\;\frac{x}{q}(\log x)^{-c},$$
with $c_\lambda\ll\min(1,q/|\lambda|)$ (Fourier coefficients of $[q/2,q)$) and $v$ 1-bounded, mod-$p$-structured (the $n$-side decoration), non-multiplicative. Equivalent Vaaler form: $H=\log^Cx$, need $\max_{0<|h|\le H}\sum_{q\sim Q}|S_w(q,h)|\ll x(\log x)^{-c}$, uniformly over slot levels (moduli $q^{j-1}$ near slot boundaries $q\approx(2n)^{1/j}$, where $T/M=x^{1-j\gamma}$), multi-prime variants, and top slivers. Higher exponents $q^e\|n-1$ / multiple band primes: same framework mod $q^{e+1}$, deeper characters — bookkeeping.

## 3. Hardness diagnosis (settled)

- **Parity-free.** Indicators are non-negative, positive-mean, local; the Chowla parity wall does not apply.
- True class: **BV-type equidistribution to large moduli on average.**
- Orthogonality over the deep family $\Leftrightarrow$ Wieferich-type condition $y^{q-1}\equiv1\ (\mathrm{mod}\ q^2)$: pointwise hopeless, average-friendly. Algebraic backbone: Teichmüller subgroup + **Heilbronn sums** $\sum_s e(hs^q/q^2)$ (Heath-Brown; Heath-Brown–Konyagin; Shkredov).

## 4. Tao–Teräväinen / Pilatte verdict (reading session — COMPLETE)

Blocked as a black box: Pilatte's multiplicativity enters at exactly two steps — centring (via MRT) and **dilation** ($F(dn)=F(d)F(n)$), and digit conditions are not dilation-invariant; the almost-all-scales route inherits the block. **But** the spectral engine (eigenvalue bound on the divisibility matrix) needs only 1-boundedness and survives as a tool for a dispersion-style argument with a re-weighted (Möbius-like) matrix — inspiration, not citation.

## 5. Partial results (PROVED — see `prop-deep-large-sieve.md`)

Single-modulus deep large sieve $(N+q^2)\|a\|^2$; per-$\lambda$ RMS $\sqrt{qN}$ for $N\le q^2$; AP-restricted version. Consequences: the **$a$-side is always covered** (saving $x^{(1-u-u')/2}$); the **$p$-side is covered iff $u>u'$** (half the band).

## 6. Open corners — superseded by `numerology-D.md` (WP1.4, June 9)

The WP1.4 analysis sharpened this section. Summary: (i) the $\lambda$-aggregation correction — mean-square alone closes D\* only when $u+2u'<1$, empty in the band; split at $\Lambda_0=x^{u+2u'-1+\varepsilon}$; (ii) large $\lambda$ covered unconditionally by the deep large sieve; (iii) on the AP the deep layer **linearizes** (verified): $T_p(\lambda)$ is a 1-bounded weight against $e(-\lambda p s/q)$ over a sub-period progression; (iv) **[corrected in WP2.0]** the citation-adaptation route through $\alpha,\beta$ falls short by a power of $q$ — see `lemma-alpha-beta.md` §3 and the Erratum in `numerology-D.md`; the residual is **Estimate D†** (AP-native, small-$\lambda$, $q$-dependent weight, log-saving on average over the band) with second-moment core = Kloosterman-flavored sums over prime pairs in APs (`lemma-alpha-beta.md` §§4–5). Lemmas $\alpha,\beta$ are proved and kept as tools; $\gamma$ parked.

## 7. Mitigations for the lower-bound version

1. **Automatic-carry band:** $q^2\in(n,2n]$ forces the slot-2 carry deterministically — that digit condition is free. (Deterministic slivers mapped: $q^2\in(n/2,2n/3]$ success, log-measure $0.288$; $q^2\in(2n/3,n]$ failure, log-measure $0.405$; alternation repeats at each slot boundary.)
2. **Margin freedom:** sandwich margins cost $\le6\times10^{-5}$ density.
3. **A single positive-proportion anatomy subclass suffices** for Theorem 1′.
4. **$\eta$-trim:** exclude $\gamma\in(1/2-\eta,1/2]$ at $O(\eta)$ density cost.

## 8. Dead ends specific to D (do not repay)

- TT/Pilatte black-box (dilation; §4). Favorable-anatomy bypass (union bound collapses: $u^{-2u}\ll2^{-u}$) — a D-type statement is needed in at least one class regardless. Crude Cauchy–Schwarz over $\chi_1$ (discards the deep twist; error $\sim x/q$, zero saving). Heilbronn completion via max-over-intervals (error $q^{1-\delta_0}$ dominates main term $P/q$; must average over the actual intervals $p_2^{-1}[P,2P)$).

## 9. Attack plan

(a) Deep large sieve + full bilinearity + $q$-averaged Wieferich counting; (b) the tailored $(q,\lambda)$-averaged mean-value theorem (§6.4); (c) the re-weighted Pilatte spectral engine. Sequencing and kill-criteria: roadmap WP1/WP2.
