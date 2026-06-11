# WP11: E3-lb via the citation bridge

**STATUS: DRAFT — UNVERIFIED**

Session goal: prove E3-lb (lower-bound form of anatomy-dispersion) using the
Kloosterman-sums-over-primes literature (Korolev–Changa 2020, Baker 2012,
Bourgain 2005) identified in wp9-frontier.md, plus a BFI-grade dispersion
reduction, plus a seam analysis at Lambda ~ Q.

Standing notation (program-standard; wp8-e3 / wp9-frontier): L = log x;
P = x^u, Q = x^{u'}; top cell U = (1/2-2eta, 1/2-eta), u, u' in U;
R = x/(pq) = x^{1-u-u'} in [x^{2eta}, x^{4eta}] on the cell; y = (2x)^{1/3};
A = x^{1-u}; a_0 = (p^{-1} mod q) in [1,q); theta_mu = mu q/p - lambda p/q;
<mu> = min(mu, p-mu); mu_0 = L^{2c+6}; harmonics 0 < |lambda| <= L^C;
B = max(C+c+4, 2C+2c+10) (retuned, wp9-theorem1prime); delta_0 = exceptional
q-density budget. In-band: u+u' > 2/3 (R < y), u+2u' > 1 (A < Q^2).
On the TOP CELL: 1-u, 1-u' in (1/2+eta, 1/2+2eta), so A = x^{1-u} is just
above Q = x^{u'} — see Sec. 3 (this makes the "hard sub-range" mass O(eta)).

Contents:
1. Verbatim load-bearing citations
2. Dispersion reduction lemma (completion + reciprocity, two-sided, q-averaged)
3. Seam analysis: Lambda in (y, Q^{1+eps}] on the top cell
4. E3-lb theorem in chain-consumable form + proof
5. Numerics (model-scale variance probe)
6. Adversarial self-check
7. Verdict + downstream deltas

---

## 1. Verbatim load-bearing citations

Provenance note. The statements below are transcribed from M. A. Korolev's
HKU survey slides "Kloosterman sums over prime numbers" (Oct 15-19, 2018;
hkumath.hku.hk/~imr/event/SRC/files/slides_Maxim_Korolev.pdf — full text
re-extracted THIS session from the PDF, pypdf), which state each theorem
formally. Slide-grade = survey-author transcription, not the original
papers. Korolev-Changa 2020 postdates the slides; its statement is pinned
separately below (Sec. 1.4). Notation of this section: q = modulus
(NOT the program's band prime), N = length, n* = inverse of n mod q,
T_q(N) = sum_{n<=N, (n,q)=1} Lambda(n) e_q(a n* + b n),
W_q(N) = sum_{p<=N, p∤q} e_q(a p* + b p).

### 1.1 Bourgain 2005 (prime modulus, the q^{1/2+eps} threshold)

> **Theorem (J. Bourgain, 2005).** Given eps > 0, q >= q_0(eps) is prime;
> then there exists eta = eta(eps) such that
>   T_q(N) << N q^{-eta}   for   q^{1/2+eps} <= N <= q.

[Slide 21 verbatim. The slide does not restrict to b = 0; Bourgain's
sum-product-era methods handle the full phase a n* + b n, (a,q) = 1.
Original: J. Bourgain, "More on the sum-product phenomenon in prime fields
and its applications", IMRN 2005. eta(eps) ineffective/unspecified.
WE USE THIS ONLY for prime modulus ell in the q-aspect orientation
(seam, Sec. 3), where b = 0 anyway.]

### 1.2 Baker 2012 (composite modulus incl. squarefree, explicit saving)

> **Theorem (R. Baker, 2012).** Suppose that squarefull part of q is
> <= q^{1/4}, then
>   T_q(N) << N q^{-eta}   for   q^{1/2+eps} <= N <= q   and
>   eta = eps^4/2000.

[Slide 21 verbatim, including the definition: q = uv, (u,v) = 1, u
squarefree, v squarefull; the hypothesis is v <= q^{1/4}. A SQUAREFREE
composite modulus (squarefull part 1) qualifies. Original: R. C. Baker,
"Kloosterman sums with prime variable", Acta Arith. 156 (2012) 351-372.
CAUTION (flagged, Sec. 6): the slide states the full phase a n* + b n;
the b-range/uniformity and the (a,q)=1 condition must be confirmed
against the paper. Our use has pair-dependent numerators a = n(q_1,q_2,h)
with (a, ell_1 ell_2) controlled, b bounded — within the standard
uniformity "for all (a,q)=1, any b" of this literature.]

### 1.3 Korolev 2017/2018 (arbitrary composite modulus, explicit Delta)

> **Theorem 1 (M.K., 2018).** Given eps > 0, prime q >= q_0(eps) > 0, for
> q^{1/2+eps} <= N <= q we have for b = 0:
>   sum_{n<=N} Lambda(n) e_q(a n*) << N q^{-eta},  eta = eps^2/20.
>
> **Theorem 2 (M.K., 2017).** Given eps, arbitrary composite q >= q_0(eps),
> then  sum_{n<=N} Lambda(n) e_q(a n*) << N (q^{7/10} N^{-1})^{5/37} q^eps
> for any q^{7/10+eps} <= N <= q.
>
> **Theorem 3 (M.K., 2018).** Given eps, arbitrary composite q >= q_0(eps),
> then  sum_{n<=N} Lambda(n) e_q(a n*) << N Delta q^eps, where
>   Delta << (q^{5/8} N^{-1})^{1/5}      for q^{5/8}   <= N <= q^{85/96},
>   Delta << (q^{1/16} N^{2/5})^{-1/8}   for q^{85/96} <= N <= q^{107/96},
>   Delta << (N q^{-7/4})^{1/10}         for q^{107/96} <= N <= q^{7/4}.
> Nontrivial for q^{5/8+eps} <= N <= q^{7/4-eps}.

[Slides 26, 28, 29 verbatim. Theorem 3's middle-regime display as printed
on the slide is (q^{1/16} N^{2/5})^{-1/8}; sanity-checked numerically in
Sec. 5 (it interpolates continuously with the two side regimes at the
break-points N = q^{85/96} and q^{107/96} — verified). b = 0 throughout
Thms 1-3; b != 0 composite is Thm 4 (range only q^{3/4+eps}..q^{1-eps},
NOT used here).]

### 1.4 Korolev-Changa 2020 (arbitrary modulus, q^{1/2+eps} <= N << q^{3/2})

Math. Notes 108:1 (2020) 87-93 / Mat. Zametki 108:1, 39-48,
"New estimate for Kloosterman sums with primes". Springer landing page
(fetched this session): "an estimate for a Kloosterman sum with primes
for an arbitrary modulus q whose length X satisfies the conditions
q^{1/2+eps} <= X << q^{3/2}. This estimate refines the results obtained
earlier by E. Fouvry and I. E. Shparlinski (2011), and by Korolev
(2018, 2019)." Exact Delta: transcription pending (paywall) — see Sec. 1.5
status. NOT load-bearing below: the reduction (Sec. 2) is routed through
Baker 2012 (whose explicit statement IS pinned above) on the hard
sub-range, with Korolev Thm 3 as an independent cross-check on its upper
part; Korolev-Changa is kept as belt-and-braces / future simplification.

### 1.5 Citation status summary

| Input | pinned grade | load-bearing here? |
|---|---|---|
| Baker 2012 (squarefull part <= q^{1/4}, N >= q^{1/2+eps}, eta = eps^4/2000) | slide-verbatim; paper-level b-uniformity UNVERIFIED | YES (hard sub-range, K-single) |
| Korolev 2018 Thm 3 (arbitrary composite, N >= q^{5/8+eps}) | slide-verbatim | cross-check only (covers Lambda >= Q^{5/4+eps}) |
| Bourgain 2005 (prime modulus, N >= q^{1/2+eps}) | slide-verbatim; eta ineffective | YES (seam top edge, q-aspect, b=0... see Sec. 3 — on the top cell its role is small) |
| Korolev-Changa 2020 (arbitrary q, N << q^{3/2}) | abstract-grade only | NO (belt-and-braces) |
| Weil/Hooley complete-sum bound (S(ell;a,b) <= 2 sqrt(ell), prime ell) | classical | YES (Lambda <= Q regime + completion) |
| Montgomery-Vaughan spaced large sieve | classical (already consumed by T1) | YES (via T1) |

## 2. The reduction lemma

### 2.0 Range-compatibility of the Baker-2012 bridge (top cell, computed)

Top cell u = u' = 1/2 - 1.5eta. Pair-terms (wp8-e3 P2): sum_{q ~ Q prime}
e(h1 a_0 qbar/ell1 - h2 a_0 qbar/ell2), ell_i ~ Lambda prime, h_i <= H
polylog; CRT modulus m = ell1 ell2 ~ Lambda^2 squarefree (Baker's
squarefull-part hypothesis trivially met). Baker needs N >= m^{1/2+eps}.
Hard sub-range: Lambda = x^lam, lam in (u', min(3u'/2, 1-u)]; at eta = 0.05
that is (0.425, 0.575] (capped by A, not Q^{3/2}); at eta = 0.02,
(0.47, 0.53]. All margins below are x-exponents, eps -> 0+; computed
numerically on a 1000-point lam-grid (/tmp/baker_bridge.py, this session).

| # | variable summed | length N | modulus m | size of m | condition N >= m^{1/2+eps} | eta=0.05 | eta=0.02 |
|---|---|---|---|---|---|---|---|
| (i) | q (prime) | Q = x^0.425 / x^0.47 | ell1 ell2 | Lambda^2 = x^{2lam}, 2lam in (0.85,1.15] / (0.94,1.06] | u' >= lam(1+2eps); but lam > u' on the whole sub-range | FAIL, deficit lam-u' in (0, 0.15] | FAIL, deficit in (0, 0.06] |
| (ii-a) | ell1 (prime; double reciprocity, q and ell2 fixed) | Lambda = x^lam | q (prime) | Q = x^0.425 / x^0.47 | lam >= u'(1/2+eps); lam > u' gives eps up to 1/2 | OK, margin in [0.213, 0.363] | OK, margin in [0.235, 0.295] |
| (ii-b) | ell (prime; reciprocity + q-square opened) | Lambda = x^lam | q1 q2 | Q^2 = x^0.85 / x^0.94 | lam >= u'(1+2eps), i.e. Lambda >= Q^{1+2eps} | OK on lam >= u'(1+2eps); margin lam-u' in (0, 0.15], seam sliver (Q, Q^{1+2eps}] excluded | same; margin in (0, 0.06] |
| (iii) | q (prime; one flip, ell2-fraction reciprocated) | Q = x^0.425 / x^0.47 | ell1 (prime) | Lambda = x^lam | u' >= lam(1/2+eps); max lam = 1-u < 2u' | OK, margin in [0.138, 0.212]* | OK, margin in [0.205, 0.235]* |

*(iii) caveat: range-OK only; the leftover phase e(h2 ellbar2/q) oscillates
in the summation variable q and is NOT of Baker's a nbar/m + b n/m shape —
structurally inadmissible as a single-modulus Baker call without further work.

Commentary (range verdict only; structural admissibility deferred to 2.1ff):
The native orientation (i) is range-obstructed on the ENTIRE hard sub-range
(deficit lam - u' > 0, up to 0.15 at eta=0.05, 0.06 at eta=0.02): Lambda > Q
forces N < m^{1/2}. Reciprocity rescues it: (ii-a), ell vs prime modulus q,
is OK on the FULL sub-range incl. the seam Lambda ~ Q, with margin >= 0.21
(eps up to 1/2 — Baker's eta = eps^4/2000 then a genuine x-power). The
DOUBLE q-average (ii-b), modulus q1q2 ~ Q^2 vs ell-length Lambda > Q —
condition Lambda >= Q^{1+eps}: CHECKS — OK on all of the sub-range except
the seam sliver Lambda in (Q, Q^{1+2eps}], where (ii-a) (or Sec. 3) covers.

STATUS: BRIDGE-COMPATIBLE-[(ii-a) full hard sub-range Lambda in (Q, A];
(ii-b)/double-q on Lambda >= Q^{1+eps}; (i) obstructed, deficit <= 0.15].
