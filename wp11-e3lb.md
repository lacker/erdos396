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
3. Pricing the variance route (ii-b) (budget computation — added)
4. (planned) Seam analysis: Lambda in (y, Q^{1+eps}] on the top cell
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
| Korolev 2018 Thm 3 (arbitrary composite, N >= q^{5/8+eps}) | slide-verbatim | YES (Sec. 4.3 Step C: per-q route, N ≍ q, middle regime); also cross-check on (ii-a) |
| Korolev 2018 Thm 1 (prime q, b = 0, q^{1/2+eps} <= N <= q, eta = eps^2/20) | slide-verbatim | YES (Sec. 4.3.4 fallback: covers the p <= q half unconditionally on prime-q-verbatim grade) |
| Bourgain 2005 (prime modulus, N >= q^{1/2+eps}) | slide-verbatim; eta ineffective | YES (seam top edge, q-aspect, b=0... see Sec. 3 — on the top cell its role is small); second fallback for Sec. 4.3.4 (p <= q half) |
| Korolev-Changa 2020 (arbitrary q, N << q^{3/2}) | abstract-grade only | fallback only (Sec. 4.3.4: p > q half if Thm 3 excludes prime q) |
| DFI 1997 Thms 1-3 (bilinear Kloosterman fractions, l^2-normalized) | preprint-verbatim, fetched this session (Sec. 4.3.2) | NO (route fails on thin-coefficient normalization, Sec. 4.3.3) |
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

### 2.1 STEP 1: completion of the window (exact identity + truncated form)

Fix band primes p != q, a_0 = (pbar mod q) in [1,q), a prime ell ~ Lambda
(dyadic: ell in (Lambda, 2Lambda]), ell != q, and the root
nu_ell = (-a_0 qbar) mod ell in [0, ell) (Prop S, wp8-e3 §1). For theta real
put G_R(beta) = sum_{0<=t<=R} e(t beta), so |G_R(beta)| <= min(R+1,
1/(2||beta||)). Viewing f(nu) = 1[nu <= R] e(nu theta) as a function of the
canonical residue nu in {0,...,ell-1}, discrete Fourier inversion on Z/ell
gives the EXACT identity (h running over symmetric representatives
|h| <= (ell-1)/2):

  1[nu_ell <= R] e(nu_ell theta) - (1/ell) G_R(theta)
    = sum_{0 < |h| <= (ell-1)/2} c_h(ell; theta) e(h nu_ell / ell),
  c_h(ell; theta) := (1/ell) G_R(theta - h/ell)
    = (1/ell) sum_{0<=t<=R} e(t theta) e(-t h/ell).

The h = 0 term (1/ell)G_R(theta) is the main/centering term: at theta = 0 it
is (R+1)/ell (the "R/ell" of the section header), and summed over ell it is
the kappa' G(theta_mu) main term absorbed exactly by cor:minor (wp8-e3 §2
item 6) — so the CENTERED root sum over the block,

  E_Lambda(q; theta) := sum_{ell ~ Lambda prime, ell != q}
      ( 1[nu_ell <= R] e(nu_ell theta) - (1/ell) G_R(theta) ),

is exactly sum_{ell} sum_{0<|h|<=(ell-1)/2} c_h(ell;theta) e(h nu_ell/ell).

Coefficient shape. Since ||theta - h/ell|| >= (|h - ell theta'|)/ell for the
representative theta' of theta nearest h/ell-scale, one has the
min(R/ell, 1/|h|)-shape RECENTERED at the dilation point h_0(ell) =
round(ell theta) (theta taken in (-1/2,1/2]):
  |c_h(ell; theta)| <= min( (R+1)/ell , 1/(2 |h - ell theta|) ),
and at theta = 0 this is the classical |c_h| <= min((R+1)/ell, 1/(2|h|)).
Uniformly in theta, the total mass is logarithmic:
  sum_{0<|h|<=(ell-1)/2} |c_h(ell;theta)| <= 2 + log ell.
(Proof: the h with ||theta - h/ell|| <= 1/(2(R+1)) number at most
ell/(R+1) + 2, each contributing <= (R+1)/ell, total <= 3; the rest
contribute <= 2 sum_{1<=j<=ell} 1/(2j) <= log ell + 1.)

Truncation at H (stated for completeness; NOT used below): for any
1 <= H <= ell/2,
  1[nu_ell <= R] e(nu_ell theta) - (1/ell)G_R(theta)
    = sum_{0<|h - ell theta| <= H} c_h e(h nu_ell/ell) + O(E_H),
  E_H := sum_{|h - ell theta| > H} |c_h| <= log(ell/(2H)) + 2,
i.e. sharp-cutoff truncation saves only down to log-size error; the proof
below therefore uses the EXACT (untruncated) identity — legitimate because
Step 3 applies one and the same uniform bound to EVERY harmonic h, so no
tail needs a trivial estimate. (A Vaaler-smoothed completion would give
error <= (R+1)/H per point; unnecessary here.)

Caution recorded for Step 3: the dominant-harmonic location h_0(ell) =
round(ell theta) MOVES with ell across the dyadic block (the dilated-phase
phenomenon flagged in link 7's "dilated-phase species"); for fixed integer h
the sup over ell ~ Lambda of |c_h(ell;theta)| therefore has total h-mass
  sum_h sup_{ell ~ Lambda} |c_h(ell;theta)| <= 3 + log Lambda + 2||theta||R
(the resonance h/ell ≈ theta sweeps through ~ ||theta||*Lambda integers h,
each at sup (R+1)/Lambda). At theta = 0 (population count) the sweep is
absent and the mass is O(L). Both cases are priced in Step 4.

### 2.2 STEP 2: reciprocity — one flip, prime ell-variable vs prime modulus q

Exact identity. For (q, ell) = 1 with qbar q == 1 (mod ell) and
ellbar ell == 1 (mod q):
  q qbar + ell ellbar == 1 (mod q ell)
(check mod ell: q qbar == 1; mod q: ell ellbar == 1; CRT), so
k := (q qbar + ell ellbar - 1)/(q ell) is an INTEGER and
  qbar/ell + ellbar/q = (1 + k q ell)/(q ell) == 1/(q ell)  (mod 1).
Hence for every integer n (here n = h a_0):
  e(n qbar/ell) = e(-n ellbar/q) * e(n/(q ell)),
exactly the section-header form e(h a_0 qbar/ell) =
e(-h a_0 ellbar/q) e(h a_0/(q ell)). Applied to the completed phase of 2.1,
e(h nu_ell/ell) = e(-h a_0 qbar/ell) (since nu_ell == -a_0 qbar mod ell and
e(./ell) depends only on the residue):
  e(h nu_ell/ell) = e( h a_0 ellbar / q ) * e( -h a_0 / (q ell) ).

The smooth factor. phi_h(ell) := -h a_0/(q ell) has
|phi_h'(ell)| = |h| a_0 / (q ell^2) < |h|/ell^2 (a_0 < q), so its total
variation over ell ~ Lambda is < |h|/Lambda <= 1/2 + O(1) for the harmonics
|h| <= ell/2 — i.e. e(phi_h(ell)) is a monotone-phase factor of total
variation O(1), removable by partial summation in ell at multiplicative
cost O(1) (it converts the bound on the pure sum below into the same bound
times 1 + 2 pi |h| a_0/(q Lambda) <= 1 + pi).

Resulting object. For FIXED q (and fixed p, mu, lambda through a_0, theta)
and fixed harmonic h, the inner sum of 2.1 becomes, after stripping
c_h(ell;theta) e(phi_h(ell)) by partial summation,

  T_{q,h}(I) = sum_{ell in I, ell prime, ell != q} e( h a_0 ellbar / q ),
  I a subinterval of (Lambda, 2Lambda],

a KLOOSTERMAN-TYPE SUM OVER PRIMES ell to the PRIME modulus q, numerator
a = h a_0 mod q, b = 0 (the e(b ell)-part is empty — the smooth factor
carried it away), length N = Lambda.

Range placement (the §2.0 table, row (ii-a), now read at BOTH ends):
- Lower end: N >= q^{1/2+eps} amply satisfied — N = x^lam, q = x^{u'},
  lam - u'/2 >= 0.213 (eta = 0.05) resp. 0.235 (eta = 0.02) on the whole
  hard sub-range: eps may be taken up to 1/2 - o(1).
- Upper end (NEW, not in the §2.0 table, which checked only
  N >= m^{1/2+eps}): on the hard sub-range Lambda > Q, i.e. N > q
  THROUGHOUT (up to the dyadic sliver Lambda in (Q, 2Q]). The verbatim
  Bourgain 2005 and Baker 2012 statements (§1.1, §1.2) carry the upper
  restriction N <= q and therefore cover NONE of the hard sub-range in this
  orientation. The geometry: Lambda <= A = x/p = qR, so
  N/q <= R = x^{1-u-u'} <= x^{4 eta}, i.e. N <= q^{rho} with
  rho = lam/u' in (1, 1.353] at eta = 0.05, (1, 1.128] at eta = 0.02 —
  squarely inside Korolev 2018 Thm 3's window [q^{5/8+eps}, q^{7/4-eps}]
  (§1.3; b = 0 there, which is exactly our shape) and inside
  Korolev-Changa 2020's window [q^{1/2+eps}, q^{3/2}) (§1.4). Citation
  selection and savings: Step 3.

### 2.3 STEP 3: the citation, and the per-q assembly

Citation choice for (ii-a): **Korolev 2018 Theorem 3** (§1.3, slide-verbatim),
NOT Bourgain 2005. Why. The prompt-level expectation was that prime modulus
q makes Bourgain 2005 the clean citation; but Bourgain's stated range is
q^{1/2+eps} <= N <= q, and 2.2 shows (ii-a) lives at N = q^rho, rho > 1, on
the ENTIRE hard sub-range — Bourgain (and Baker 2012, same upper end)
verbatim-covers only the dyadic seam sliver Lambda in (Q, 2Q]. Thm 3 fits
(ii-a) exactly: b = 0 (our post-partial-summation phase), N-window
[q^{5/8+eps}, q^{7/4-eps}] containing our rho-range with margins >= 0.375
(bottom) and >= 0.397 (top) in the rho-variable at both eta values, and an
EXPLICIT saving. TRANSCRIPTION CAVEAT (flagged): the slide says "arbitrary
composite q"; if "composite" is exclusive (prime q not allowed), the
prime-modulus/N > q fallback is Korolev-Changa 2020 (§1.4 — "arbitrary
modulus", but abstract-grade, exact Delta unpinned). This caveat is
inherited by the status line (2.6).

Savings, in q-exponents (eta_0 defined by Delta <= q^{-eta_0}; ell-sum over
(Lambda, 2Lambda] obtained from two initial segments T(2Lambda) - T(Lambda),
both in-window; Lambda(n) -> primes costs one L by partial summation +
O(sqrt N) prime powers):
  rho in (1, 107/96]:    eta_0(rho) = 1/128 + rho/20   (middle regime),
  rho in (107/96, 7/4):  eta_0(rho) = (7/4 - rho)/10   (top regime);
on our range: eta_0 in [0.0397, 0.0635] at eta = 0.05 (worst at
rho = 1.353), eta_0 in [0.0578, 0.0635] at eta = 0.02. So per (q,h) with
q NOT dividing h (coprimality (h a_0, q) = 1 then holds, see Step 5):

  |T_{q,h}(I)| <= N Delta q^{o(1)} <= Lambda q^{-eta_0(rho)} L^{O(1)},

a saving of q^{eta_0}/L^{O(1)} against the trivial bound
pi(2Lambda) - pi(Lambda) ~ Lambda/log Lambda = Lambda/L-grade.

DEGENERATE SECTOR q | h (nonempty precisely because Lambda > q — in the
N <= q regime |h| <= ell/2 < q would forbid it): for h = qm != 0 the phase
is e(h a_0 ellbar/q) = 1 identically — the citation hypothesis (a, q) = 1
FAILS and no cancellation in the mod-q aspect exists. Writing
q m nu_ell == -m a_0 (mod ell), these terms equal
sum_ell c_{qm}(ell;theta) e(-m a_0/ell): a q-free oscillation, generically
non-cancelling (e.g. a_0 |m| <= Lambda/10 makes the phase nearly constant).
Trivial pricing of the sector: sum_{m != 0} min(R/Lambda, 1/(q|m|)) * Lambda
<= (Lambda/q)(1 + log R) <= R L — recorded as E_degen <= (Lambda/q) L-grade.

Per-q bound for the centered inner root sum (collecting 2.1 + 2.2 + the
citation, with the Step-1 coefficient masses; partial-summation Var-cost of
c_h(ell;theta) in ell is >= sup-grade only for the resonant h, absorbed in
the same ||theta||R sweep term):

  |E_Lambda(q; theta)| <= [ (3 + log Lambda + 2||theta||R) L^{O(1)} ]
                          * Lambda q^{-eta_0(rho)}
                          + (Lambda/q) L-grade
  <= Lambda q^{-eta_0} L^{O(1)} * (1 + ||theta||R)  +  (Lambda/q) L.

This is a genuine, unconditional, POINTWISE-IN-q estimate (modulo the
named citation), uniform in a_0, i.e. in p, and in mu, lambda through
theta. Whether it has any value is pure exponent arithmetic: Step 4.

### 2.4 STEP 4: exponent arithmetic — the pointwise-in-q test FAILS

If the 2.3 bound met link 7's per-q scale R L^{-c-C-5} (so that
(1/pi(Q)) sum_q |E_Lambda|^2 <= delta_0 R^2 L^{-2c-2C-10} held with NO
exceptional set), the variance/Chebyshev layer of links 7/10 would
collapse. Test, in x-exponents, BEST case (theta-sweep and degenerate
sector set aside, i.e. granting the idealized bound Lambda q^{-eta_0}
L^{O(1)}): need
  lam - u' eta_0(rho) < r := 1 - u - u'   (any polylog then absorbable),
i.e. deficit d(lam) := lam - u' eta_0(lam/u') - r < 0. Computed on a
1001-point lam-grid (/tmp/wp11_step4.py, this session, .venv python):

| top cell | r | hard sub-range lam | eta_0 range | deficit d(lam) | d at Weil ceiling eta_0 = 1/2 |
|---|---|---|---|---|---|
| eta = 0.05 (u = u' = 0.425) | 0.150 | (0.425, 0.575] | [0.0397, 0.0635] | min 0.2504 (at lam = Q+), max 0.4081 (at A) | min 0.0625, max 0.2125 |
| eta = 0.02 (u = u' = 0.47) | 0.060 | (0.47, 0.53] | [0.0578, 0.0635] | min 0.3828, max 0.4407 | min 0.1750, max 0.2350 |

The deficit is a POSITIVE POWER OF x everywhere on the hard sub-range, at
both eta values — and remains so even at the absolute ceiling eta_0 = 1/2
(complete-Kloosterman/Weil-grade cancellation, unattainable for sums over
primes). The trim direction makes it WORSE (smaller eta shrinks r faster
than the range). Structural reading: the per-q completed bound
Lambda q^{-eta_0} is not merely short of the target — it exceeds the
TRIVIAL count ~ R/L of the windowed sum (Lambda/R >= x^{lam - r} >=
x^{0.225} resp. x^{0.41}), because the window nu_ell <= R has relative
density R/Lambda below Lambda^{-1/2}-scale: a Polya-Vinogradov-type
barrier — NO single-(q,h) completion bound, however strong, can detect a
window this far below the square-root scale. The degenerate sector
(Lambda/q) L of 2.3 says the same thing intrinsically: at the top of the
range it alone reaches R L > target. CONCLUSION: in orientation (ii-a) the
citation bridge produces a true theorem whose strength is VOID for link 7;
the pointwise-in-q shortcut does NOT exist, and the q-average (variance /
exceptional-set layer) is NOT dispensable — the saving must come from
summing OVER q against the citation (orientations (i)/(ii-b)), not from a
fixed-q application. The §2.0 range margins of (ii-a) (>= 0.21) are real
but cannot be cashed: range-compatibility != budget-compatibility, exactly
the deferral §2.0's commentary stipulated.

### 2.5 STEP 5: uniformity in the numerator h a_0 mod q

Requirement: for FIXED q the Step-3 bound must hold for ALL numerators
a = h a_0 mod q with (a, q) = 1 — a_0 = (pbar mod q) sweeps essentially
arbitrary reduced residues as p varies over the band, h sweeps all
non-degenerate harmonics, and the proof fixes (q, h, p) before citing.
Audit of the §1 statements:
- Korolev 2018 Thm 3 (the load-bearing choice): stated for
  sum_{n<=N} Lambda(n) e_q(a n*) with the standing convention (a, q) = 1 of
  the survey's T_q/W_q definitions (§1 provenance note); the bound carries
  no dependence on a — uniformity over ALL reduced residues a, as is
  standard throughout this literature (the Vinogradov/Vaughan + bilinear
  machinery never localizes a). NOT an almost-all statement. Grade:
  slide-verbatim; the "for all (a,q)=1" quantifier should be re-confirmed
  against the original paper when Thm 3's transcription is upgraded
  (same caveat-class as §1.2's b-uniformity note for Baker).
- Bourgain 2005 / Baker 2012 (seam-sliver only, after 2.2/2.3): full phase
  a n* + b n, (a, q) = 1, uniform in a and b per the slide statements and
  §1.2's commentary. Same paper-level re-confirmation flag.
- Korolev-Changa 2020 (fallback if Thm 3 excludes prime q): abstract-grade
  only; uniformity in a UNVERIFIED — transcription pending (§1.4).
So: no almost-all-numerators defect among the pinned statements.
The one GENUINE uniformity failure is internal, not in the citations: the
degenerate harmonics q | h (2.3), where (h a_0, q) = q != 1 and the
hypothesis itself is violated. For fixed q this is a structural sector of
the completion (present because Lambda > q), not a removable technicality:
it survives every choice of citation and is part of the 2.4 obstruction.
Verdict: uniformity OK for all numerators COPRIME to q (as the §1
statements provide); the needed quantifier "all (a,q)=1, fixed prime q,
N up to q^{1.36}" is exactly what Korolev Thm 3 / Korolev-Changa assert,
modulo the two named transcription caveats.

### 2.6 STEP 6: status + downstream deltas

STATUS: OBSTRUCTED-[(ii-a)-pointwise: window/completion budget — per-q
citation output Lambda q^{-eta_0} L^{O(1)} exceeds even the trivial R/L by
x^{lam-r-u' eta_0} >= x^{0.25} (Korolev Thm 3 saving) and >= x^{0.0625}
even at the unattainable Weil ceiling eta_0 = 1/2; independently, the
degenerate harmonics q | h (nonempty since Lambda > q) carry uncancellable
mass up to (Lambda/q) L ~ R L. Steps 2.1-2.3 ARE proved (completion,
reciprocity, citation application — modulo Korolev-2018-Thm-3
slide-transcription incl. its prime-q/"arbitrary composite" reading), but
the resulting pointwise theorem is void for link 7's target.]

Downstream deltas (3):
1. E3-lb does NOT follow pointwise in q; the delta_0-exceptional-set /
   Chebyshev layer of links 7+10 remains NECESSARY, and the live reduction
   routes stay (ii-b) (Lambda >= Q^{1+eps}, K-single mod q1q2, q-average
   kept through C-S) + (i)-variance + the Sec. 3 seam — unchanged.
2. §2.0's table needs an upper-end column (N <= q vs N <= q^{7/4}): with it,
   Bourgain 2005/Baker 2012 verbatim cover NO part of the (ii-a) hard
   sub-range (Lambda > Q = q there); §1.5's Bourgain row ("seam top edge"
   role) stands, its Baker row's "K-single" role is (ii-b)-only.
3. WARNING for the (ii-b) write-up (next session): the same completion-loss
   barrier ((Lambda/R)^2 harmonics vs Q^{2 eta_0} saving) threatens any
   variant that takes absolute values in (ell, h) before summing over q;
   wp9-frontier §4's "power room is available" claim must be re-priced with
   the 2.4 arithmetic before (ii-b) is drafted — the q-average must hit the
   phase BEFORE the coefficient masses are paid, or the budget dies the
   same death at exponent scale lam - r vs u' eta_0.

---

## 3. Pricing the variance route (ii-b)

**STATUS: BUDGET COMPUTATION ONLY (this session) — exponent pricing, not a
proof.** Numeric provenance: /tmp/wp11_iib.py (1001-point lam-grid, both
eta values; system python). All deficits/surpluses are x-exponents on the
top-cell midpoint u = u' = 1/2 - 1.5 eta (the 2.0/2.4 convention);
"deficit" = (route's exponent) - (target's exponent), positive = FAIL.

### 3.0 Object, target, and ordering

Fix p minor and lambda; fix a core mu (theta = theta_mu) — the max-over-mu,
sum-over-p, and lambda-union layers of link 7 are polylog assembly overhead
(E3-4/E3-5 territory), set aside as non-exponent-bearing. The priced object:

  Var := (1/pi(Q)) sum_{q ~ Q} |E_Lambda(q; theta)|^2,
  target: Var <= delta_0 R^2 L^{-2c-2C-10}  (link 7 variance form;
  E3-5-strengthened delta_0^2 R^2 L^{-(4c+18+C)} — both polylog-grade,
  identical at exponent level: target exponent 2r, r = 1 - u - u').

Heeding 2.6-delta-3, the square is opened FIRST and completion in (h1, h2)
is performed only after the q-sum exists:

  Var = (1/pi(Q)) sum_{ell1, ell2 ~ Lambda} sum_q
        [centered_{ell1}(q) x conj(centered_{ell2}(q))],
  centered_ell = sum_{h != 0} c_h(ell; theta) e(h nu_ell(q)/ell)
  (only h1, h2 != 0 occur — centering removed the h = 0 line exactly).

MODEL CAVEAT (flagged once, applies to all of 3.2-3.3): nu_ell(q) =
(-a_0 qbar) mod ell is priced with a_0 FROZEN. The true a_0(q) = pbar mod q
layer (wp8-e3 §4's third inverse layer) destroys every periodicity used
below — the honest conductor per pair is p ell1 ell2 > x, wp8-cdagger-D3
territory. The frozen model therefore yields an UPPER bound on what any
citation can deliver; routes that die in the model are dead a fortiori.

### 3.1 Diagonal ell1 = ell2: exact, unconditional, OK

|centered_ell|^2 <= 1[nu_ell <= R](1 + 2(R+1)/ell) + (R+1)^2/ell^2, and the
per-q window count is unconditionally bounded:
  N_win(q) := #{ell ~ Lambda : nu_ell(q) <= R} <= ((1+r)/lam)(R+1)
            <= 3(R+1)
(each of the R+1 values t has q(b+pt)+1 <= x^{1+r+o(1)}, which has at most
(1+r)/lam < 3 prime factors > Lambda — no equidistribution input). Hence

  Diagonal <= (1+o(1)) * 3(R+1) + 2(R+1)^2/(Lambda L) <= 4R   (R <= Lambda),

versus target R^2 L^{-(2c+2C+10)}-grade: satisfied iff R >= L^{2c+2C+12},
free on the cell (R >= x^{2eta}). Margin: a full power x^r. DIAGONAL OK —
matches wp8-e3 P2's diagonal accounting on q-average alone.

### 3.2 (b1) Generic off-diagonal: Weil-after-double-completion — the ladder

Per pair (ell1 != ell2): sum_{h1,h2 != 0} c_{h1} conj(c_{h2}) K with
K = K(ell1,ell2,h1,h2) = sum_{q ~ Q prime} e(h1 nu_{ell1}(q)/ell1 -
h2 nu_{ell2}(q)/ell2). In the frozen model the integrand is periodic mod
ell1 ell2 ~ Lambda^2, and the q-range covers Q/Lambda^2 < 1/Q < 1 periods:
the SUB-ONE-SOLUTION regime (same territory as wp8-cdagger D3) — no
per-tuple equidistribution exists, and the prime-variable literature needs
N >= m^{1/2+eps} while here N = Q = m^{u'/(2 lam)} with u'/(2 lam) < 1/2 on
the whole hard sub-range: BELOW the entire Korolev range, in both aspects.

Assembly: Var_offdiag <= (L/Q) * [sum_{ell ~ Lambda} sum_h |c_h|]^2 *
sup|K| = (L/Q) Lambda^2 L^{O(1)} sup|K|. The L^1 x L^1 coefficient masses
(sum_h |c_h| <= 2 + log ell per ell, Step 1) are FORCED in this ordering:
with h1, h2 independent and absolute values taken per tuple, no Parseval
pairing exists (the min(R/ell, 1/h)^2-masses live only on the shared-h
slice — Sec 3.3). The ladder of granted per-tuple bounds, deficit vs 2r:

| granted |K| per tuple | Var exponent | deficit, eta=0.05 | deficit, eta=0.02 |
|---|---|---|---|---|
| trivial pi(Q) | 2 lam | 2(lam-r): [0.550, 0.850] | [0.820, 0.940] |
| complete q-range + Weil 2 sqrt(ell1 ell2) L | 3 lam - u' | 3lam-u'-2r: [0.550, 1.000] | [0.820, 1.000] |
| sqrt-cancellation sqrt(Q) | 2 lam - u'/2 | [0.338, 0.638] | [0.585, 0.705] |
| GOD-MODE O(1) (every tuple fully cancels) | 2 lam - u' | [0.125, 0.425] | [0.350, 0.470] |

Readings. (a) Weil-after-double-completion is WORSE than trivial by exactly
lam - u' in (0, 0.15] / (0, 0.06] (= the §2.0 row-(i) deficit): the
completed-sum bound sqrt(Lambda^2) = Lambda exceeds the trivial count Q —
completion buys strictly negative value below the square-root scale.
(b) The decisive row is GOD-MODE: even granting K = O(1) for EVERY tuple —
strictly stronger than any conceivable citation — the budget fails by
x^{2lam-u'-2r} >= x^{0.125} (eta = 0.05), >= x^{0.35} (eta = 0.02), worse
under trim. No per-tuple estimate, of any strength, closes (b1): the
L^1 x L^1 completion mass (Lambda-grade per ell-line, vs the window's
Parseval mass (R/Lambda)^{1/2}-grade) is paid before the q-average — 2.6
delta-3's flagged condition is violated STRUCTURALLY in this ordering, not
fixably. The needed cancellation lives in the 4-fold (ell1,ell2,h1,h2)
aggregate against the signed c-coefficients — pair correlation of roots,
i.e. E3-dagger proper, for which no citation exists. (b1): ROUTE-DEAD.

Corollary (re-pricing wp9-frontier §4 item 1). The q1q2-orientation (the
§2.0 (ii-b) row: first moment in q, C-S in (ell,h), open the q-square,
Baker on sum_ell e(n ellbar/(q1 q2))) dies at the SAME ledger line: its
C-S q1 = q2 diagonal is pi(Q) (sum_{ell,h} w)^2-grade = Q Lambda^2
L^{O(1)} against the budget Q^2 R^2 L^{-...}, deficit 2lam - u' - 2r —
identical to the GOD-MODE floor, BEFORE Baker is even invoked (and Baker's
explicit saving on the off-diagonal, eta_B = eps^4/2000 with eps =
lam/(2u') - 1/2 <= 0.176, is Q^{-2 eta_B} ~ x^{-4e-7}: real but irrelevant
against a x^{0.125} deficit). wp9-frontier §4's "power room is available"
is hereby re-priced: FALSE in every ordering that takes absolute values in
(ell, h) before the q-average; the §2.0/§2.6 range-compatibility of (ii-b)
was real but, as for (ii-a) in 2.4, budget-incompatible.

### 3.3 (b2) Near-diagonal h1 = h2 = h, ell1 != ell2

On the shared-h slice the masses ARE Parseval-grade: sum_h sup_ell
|c_h(ell;theta)|^2 <= (R/Lambda)(3 + 2||theta||R)-grade (theta = 0-grade
R/Lambda quoted below; the 2.1 theta-sweep multiplies by <= (1+||theta||R),
adding at most r to each deficit — no verdict changes). Reciprocity (2.2)
turns the phase into h a_0 (ellbar1 - ellbar2)/q + smooth, so per (q, h),
q not dividing h, the ell-pair sum is |T_{q,h}|^2 + O(Lambda) — the (ii-a)
object SQUARED: the variance form genuinely doubles the citation exponent.

- Unconditional mass: (R/Lambda)(Lambda/L)^2 L^{O(1)} = R Lambda L^{O(1)},
  exponent lam + r vs 2r: SURPLUS lam - r in (0.275, 0.425] (eta=0.05),
  (0.41, 0.47] (eta=0.02). The near-diagonal is MAIN-TERM-CARRYING: it
  must oscillate; it cannot be dodged by mass (answers the (b2) question).
- With Korolev Thm 3 per (q,h) (eta_0 in [0.0397, 0.0635] / [0.0578,
  0.0635]): R Lambda Q^{-2 eta_0}, deficit lam - r - 2u' eta_0 in
  [0.226, 0.391] (eta=0.05), [0.356, 0.412] (eta=0.02). DEAD.
- Needed saving: eta_0 >= (lam - r)/(2u') in [0.324, 0.500] / [0.436,
  0.500] — Weil-grade cancellation for sums over primes, a factor 5-8
  above the entire literature (ceiling 0.0635). Not a bookkeeping gap.
- Weil-ceiling test (eta_0 = 1/2): deficit lam - r - u' = lam - (1-u)
  <= 0, vanishing only at Lambda = A. The near-diagonal is the FIRST
  object in this work-package to PASS a ceiling test (contrast 2.4, where
  even eta_0 = 1/2 left +0.0625): q-average-hits-phase-first + Parseval
  masses is the structurally correct ordering; what is missing is purely
  the SIZE of the prime-variable saving.
- Degenerate sector q | h (the 2.3/2.4 killer, revisited in variance): the
  mod-q phase dies; terms = c_{qm}(ell1) conj(c_{qm}(ell2))
  e(-m a_0/ell1 + m a_0/ell2), no q-oscillation at all. But now |c_{qm}|
  <= 1/(2qm) (Lambda < qR = A on the open range), so the sector's mass is
  <= zeta(2)(Lambda/q)^2 L^{-2} = R^2 L^{-2} x^{2(lam - (1-u))}: a
  NEGATIVE power of x for Lambda <= A x^{-delta} — and the same holds for
  the full degenerate block (q|h1 AND q|h2, h1 != h2) of (b1). The
  variance form thus TAMES the degenerate-harmonic obstruction (pointwise
  (Lambda/q)L ~ RL fatal in 2.3; squared (Lambda/q)^2 absorbable), EXCEPT
  on the top ~ (2c+2C+12) log_2 L dyadic blocks Lambda in (A L^{-K'}, A],
  where it sits at R^2 L^{-2}: polylog-short of target, needs its own
  polylog-only treatment — recorded as input to the planned Sec 4
  (seam/top analysis). (b2): ROUTE-DEAD as a citation bridge; alive only
  as the marker of where eta_0 ~ 1/3-grade new technology would land.

### 3.4 (b3) The O(eta) hard-mass dodge — checked against wp9-b0-audit §5

Mass accounting (computed). Hard-range ell-mass sum_{Q < ell <= A} 1/ell =
log((1-u)/u') = 6 eta + O(eta^2) at the cell midpoint: 0.3023 (eta=0.05),
0.1201 (eta=0.02). The audit's "~ 4 eta" (§5a) is the BEST corner
u = u' = 1/2 - eta (0.2007 / 0.0800 — reproduced); worst corner ~ 8 eta.
As a FRACTION of the full unwound support (x^{3/10}, A] (mass
log((1-u)/0.3) = 0.651 / 0.569) the hard range is 46% / 21% — not small at
eta = 0.05; what is O(eta) is the absolute mass. The b-side mirror (moduli
against p) has the same shape, ~ 6 eta. AUDIT CLAIM CONFIRMED as a mass
statement, with the constant pinned (6 eta midpoint, 4 eta best corner).
Below Q the q-interval exceeds every modulus (complete-sum regime): T1 +
per-ell Weil cover Lambda <= Q, so the entire (ii-b) burden indeed lives in
the O(eta)-mass range Lambda in (Q, A].

BUT mass-is-O(eta) does NOT by itself absorb the burden into delta_0. Two
genuine conditions surfaced by the pricing:

(1) ORDER OF THE TRIANGLE INEQUALITY. The hard-range terms admit the
uniform bound |E_hard(q; theta_mu)| <= N_hard(q) + 6 eta R (1+o(1)) with
N_hard(q) = #{ell > Q : nu_ell(q) <= R} — uniform in mu AND lambda, so
both killer quantifiers (max-mu inside, E3-4's lambda-inside-event)
dissolve for free. But paid AFTER the harmonic mu-expansion it meets
sum_{<mu> <= mu_0} 1/<mu> ~ 2 log mu_0 = (4c+12) loglog x: error
~ eta R loglog x, DIVERGENT against the O(R) main term. The dodge is only
legitimate BEFORE the mu-expansion: sandwich at the population level via
the exact identity 1[P+(a) <= x^{3/10}] = 1 - sum_{soft ell} 1[ell|a]
- sum_{hard ell} 1[ell|a] (prop:one-large), run the D-step only on the
soft-unwound part, and bound the hard POPULATION in absolute value — an
O(eta) R loss against the class main term c_0 R (c_0 the audit-§6 ledger
constant), positive for eta small. This RESTRUCTURES E3-lb: the hard range
exits the oscillation demand entirely; no variance at Lambda > Q is needed.

(2) THE RESIDUAL FIRST MOMENT (open). Absorption still requires
  E_{p,q} N_hard <= C eta R   (C an absolute constant),
after which Markov prices the bad q into delta_0 and the loss into the
sandwich's O(eta). The trivial 3.1-bound gives N_hard(q) <= 2(R+1) always
(<= 2 prime factors > Q per shifted value): constant-grade but NOT
proportional to eta — the dodge is NOT closed by trivial counting. What it
needs is theta = 0, phase-free, mu/lambda-free, constant-precision
equidistribution ON (q, ell)-AVERAGE of the root window: #{(q, m):
m = pbar mod q, ell | m, m in the length-qR window} over q ~ Q,
ell in (Q, A] — the Titchmarsh-divisor/BFI count of wp8-e3 §4 route 2, at
constant precision instead of polylog. This is strictly the WEAKEST demand
in the whole E3 complex (first moment, no phases, no quantifiers,
constant-factor target). It is NOT covered by the §1 citations: pointwise
in ell the q-sum still carries the a_0(q)-layer (conductor p ell > x), and
per-(ell,h) absolute values re-pay the Lambda-grade L^1 mass against an
eta R = x^r target (deficit ~ lam - r again) — the ell-average with signed
window coefficients (i.e. genuine dispersion) must be kept. Route-2's
"plausibly provable with current technology, paper-scale" assessment
(wp8-e3 §4) applies, now with a constant-precision-only demand.

### 3.5 Section status

STATUS: PRICED. (b1) ROUTE-DEAD-[no per-tuple bound suffices: GOD-MODE
floor 2lam-u'-2r >= 0.125 (eta=0.05) / 0.35 (eta=0.02); Weil-after-double-
completion is below-trivial by lam-u'; the q1q2/K-single C-S ordering dies
at the same diagonal line — wp9-frontier §4's "power room" claim is
withdrawn for all absolute-(ell,h) orderings]. (b2) ROUTE-DEAD-[as
citation: needs eta_0 in [0.32, 0.50] vs 0.0635 available; passes the
Weil-ceiling test (deficit lam-(1-u) <= 0) — correct ordering, wrong-sized
literature; degenerate q|h sector variance-tamed except the top L^{O(1)}
sliver of Lambda]. (b3) BURDEN-ABSORBABLE-CONDITIONALLY-[O(eta) hard mass
confirmed (6 eta midpoint, audit's 4 eta = best corner); absorption needs
(i) the sandwich BEFORE the mu-expansion (after it: loglog-divergent) and
(ii) the open constant-precision first moment E_{p,q} N_hard <= C eta R —
BFI/Titchmarsh species, weakest demand in the E3 complex. If (ii) holds,
the Lambda > Q variance burden exits into delta_0 + O(eta) and routes
(b1)/(b2)/E3-dagger-proper are NOT NEEDED for E3-lb].

Downstream deltas (2): 1. The live E3-lb plan is now: (b3)-sandwich +
route-2 first moment at constant precision on Lambda in (Q, A]; T1 + Weil
on Lambda <= Q; the top-sliver degenerate blocks (3.3) into the Sec-4
seam/top analysis. E3-dagger proper (pair correlation with phases) is
demoted to fallback. 2. wp9-theorem1prime link 7's variance-form remark
inherits 3.2: the variance route as a CITATION route is closed; link 7
should be discharged via the restructured (b3) form, not the variance.

## 4. The first moment (E_{p,q} N_hard <= C eta R) — written in-session (main loop)

### 4.1 Step A: reduction to window counts (bookkeeping, PROVED)

Fix (q, ell) with q < ell (the sliver ell <= 2Q where ell <= q can occur
is handled in 4.4). By Prop S, the t-existence condition on p is
nu_ell = (-a_0 qbar mod ell) <= R, i.e.

    a_0 mod ell \in W(q,ell) := {(-qt) mod ell : 0 <= t <= R},

an AP mod ell with difference -q and R+1 terms. Since the canonical
representative a_0 lies in [1,q] and q < ell, the condition is
a_0 \in W cap [1,q] as integers. Hence exactly:

    E[N_hard] = (1/(pi(P)pi(Q))) Sum_{ell in (Q,A]} Sum_{q ~ Q}
                Sum_{p ~ P} 1[a_0(p,q) \in W(q,ell) cap [1,q]].

Target main term: if the p-mean of the indicator is
#(W cap [1,q])/q x (1+o(1)) on (q,ell)-average, then since
#(W cap [1,q]) = (R+1)q/ell + E_AP, summing R/ell over ell in (Q,A]
(Mertens) gives (R+1) log(log A / log Q) <= 6 eta (R+1) on the top
cell: the target with C = 7.

### 4.2 Step B: completion (bookkeeping, PROVED)

Completing the window indicator mod ell (coefficients
|c_h| <= min((R+1)/ell, 1/|h|), truncation H = ell):

    E[N_hard] - (main) = (1/(pi(P)pi(Q))) Sum_ell Sum_{0<|h|<ell} c_h
                          B(ell, h) + (E_AP-aggregate),

    B(ell,h) := Sum_{q ~ Q} Sum_{p ~ P, prime} e(-h a_0(p,q) qbar_ell / ell),

where a_0(p,q) \in [1,q] is the canonical representative of pbar mod q.
The E_AP-aggregate is absorbed into the same completed form (it IS the
h != 0 mass). BUDGET: Sum_ell (1/ell-type weights) ~ eta-mass and
Sum_h |c_h| ~ log: any uniform bound

    |B(ell,h)| <= pi(P) pi(Q) L^{-3}        (*)

for 0 < |h| < ell, ell in (Q,A], closes the first moment with room
(total error <= eta-mass x log x L^{-3}-savings aggregation; exponent
check in 4.4). [BUDGET LINE WITHDRAWN (this session, 4.4): the error
sum carries NO 1/ell weight — the 1/ell weights belong to the MAIN
term only. The exponent check in 4.4 shows (*) at ANY pointwise
strength, including below square-root, does NOT close the first
moment; (*) itself is nevertheless PROVED in 4.3, with power saving.]

### 4.3 Step C: the bilinear bound (*) — RESOLVED this session

Claim (*): |B(ell,h)| <= pi(P) pi(Q) L^{-3} uniformly for
0 < |h| <= L^{B'}, ell in (Q,A] prime, at the top cell
P = Q = x^{0.425}, A = x^{0.575}. Verdict: see 4.3.5. Conventions:
p runs over primes in (P,2P], q over primes in (Q,2Q], p != q (a_0
undefined at p = q; if the program's band-pair convention admits
p = q, those <= pi(Q) terms are excluded here and cost
pi(Q) <= pi(P)pi(Q) x^{-0.425} L — absorbed), and q != ell (qbar_ell
undefined; possible only in the sliver ell <= 2Q; the excluded single
q costs <= pi(P) = pi(P)pi(Q) x^{-0.425} L-grade — absorbed; see 4.4).

#### 4.3.1 Step C-1: the reciprocity flip (exact)

Failed routes first, for the record. (i) Pointwise in q BEFORE any
flip, the p-sum is Sum_p e(c_q a_0(p,q)) with the REAL frequency
c_q = -h qbar_ell/ell applied to the integer a_0 in [1,q]: not a
character sum mod q — no citation matches. (ii) Cauchy-Schwarz in q:
the diagonal alone gives pi(Q) sqrt(pi(P)) << target (fine), but the
off-diagonal phase difference a_0(p1,q)-a_0(p2,q) is parametrized by
(k1,k2) with a_0(p_i,q) = (1+k_i q)/p_i, and the (k1,k2)-cells are
q-APs mod p1 p2 ~ P^2 >> Q: ONE q per cell — the cell decomposition
degenerates to unit terms, no cancellation accessible. Mirror route
(Cauchy in p) dies the same way mod q1 q2. So: flip first.

The flip. For primes q != ell, with qbar = qbar_ell (inverse mod ell)
and ellbar = ellbar_q (inverse mod q), the exact three-term
reciprocity of §2.2 (q qbar + ell ellbar == 1 mod q ell) gives

    qbar/ell + ellbar/q == 1/(q ell)   (mod 1).

Apply it to n = -h a_0(p,q):

    e(-h a_0 qbar/ell) = e(h a_0 ellbar_q / q) * e(-h a_0/(q ell)).

Smooth factor: |e(-h a_0/(q ell)) - 1| <= 2 pi |h| a_0/(q ell)
<= 2 pi |h|/ell (a_0 <= q), so for |h| <= L^{B'} replacing it by 1
costs, after trivial summation over (p,q),

    E_smooth <= 2 pi L^{B'} pi(P) pi(Q) / ell
             <= pi(P) pi(Q) x^{-0.425 + o(1)}   — negligible.

(No partial summation needed, unlike §2.2: there the harmonics ran to
|h| ~ ell/2; here the L^{B'} truncation makes the factor POINTWISE
close to 1. This is the one place |h| <= L^{B'} is used essentially;
the argument below survives up to |h| <= x^{0.4}, see 4.3.5.)

Main factor: a_0 == pbar (mod q) and e(./q) depends only on the
residue mod q, so

    e(h a_0 ellbar_q/q) = e(h pbar_q ellbar_q/q)
                        = e(h (p ell)bar_q / q),

a CLEAN Kloosterman fraction. Exact outcome of Step C-1:

    B(ell,h) = Sum_{q ~ Q, q != ell} Sum_{p ~ P, p != q}
               e( h (p ell)bar_q / q )  +  O(pi(P) pi(Q) L^{B'}/ell).

The modulus is now q ~ Q (it was ell), the numerator is
a = h ellbar_q mod q, and — decisively — q | h is IMPOSSIBLE:
0 < |h| <= L^{B'} < Q < q. The degenerate sector that §2.3 met
(there h ran to ell/2 > q) is EMPTY in this orientation:
(a, q) = 1 for EVERY q in the sum.

#### 4.3.2 Step C-2: DFI 1997, fetched statement (verbatim)

Provenance: fetched THIS session from the author preprint
math.ucla.edu/~wdduke/preprints/bilinear.pdf (pdftotext extraction;
published as Invent. Math. 128 (1997) 23-43). Object (their (1.2)):

> B(M,N) = Sum Sum_{(m,n)=1} alpha_m beta_n e(a mbar/n),
>
> "where a is a fixed (but possibly large) positive integer and
> alpha_m, beta_n are arbitrary complex numbers for M < m <= 2M,
> N < n <= 2N, respectively and m mbar == 1 (mod n)."
> Trivial bound (1.3): |B(M,N)| <= 2 ||alpha|| ||beta|| (MN)^{1/2},
> ||.|| the l^2-norm.
>
> **Theorem 1.** For any positive integer a we have
>   B(M,N) << ||alpha|| ||beta|| ( (M+N)^{1/2}
>             + (1 + a/(MN))^{1/2} min(M,N) ) (MN)^eps.
>
> **Theorem 2.** For any positive integer a we have
>   B(M,N) << ||alpha|| ||beta|| (a + MN)^{3/8} (M+N)^{11/48 + eps},
> the implied constant depending only on eps.
>
> **Theorem 3.** For any positive integer a and any complex numbers
> alpha_m, beta_n:
>   B(M,N) << ||alpha|| ||beta|| (a + MN)^{14/29} (M+N)^{1/58 + eps}.
>
> Corollary: the same bounds hold for the weighted form
> B_F(M,N) = Sum Sum alpha_m beta_n e(a mbar/n) F(m,n), with
> F^{(j,k)}(m,n) << eta^{j+k} m^{-j} n^{-k} (0 <= j,k <= 2,
> eta >= 1), at the multiplicative cost eta^2.

[Paper's own commentary, transcribed: "In case a << MN ... the above
result (Thm 2) improves the trivial bound (1.3) provided
N > M^{5/6+eps} and M > N^{5/6+eps}." Thm 1 is nontrivial only for
imbalanced M, N. PDF archived at the session's webfetch cache.]

#### 4.3.3 Step C-3: range/normalization arithmetic — the DFI route FAILS on sparsity

Cast 4.3.1's output as B(M,N): m := p ell (ell FIXED inside B(ell,h)),
n := q, a := |h| (conjugate if h < 0). Then m in (P ell, 2P ell],
dyadic with M = P ell; n dyadic with N = Q; (m,n) = 1 holds term-by-term
(p, q, ell prime, p != q != ell); a <= L^{B'} << MN. Coefficients:
alpha_m = 1{m = p ell, p prime in (P,2P]} — supported on multiples of
ell, ||alpha||^2 = pi(P)-grade; beta_n = 1{n prime} ||beta||^2 =
pi(Q)-grade. All hypotheses of §4.3.2 hold VERBATIM — this is a
genuinely admissible DFI pair (the wp9-frontier §2c pair-dependence
blocker is absent: the numerator a = |h| is fixed). The arithmetic,
top cell (M = x^{0.85}..x^{1.0} as ell runs over (Q,A], N = x^{0.425},
MN = x^{1.275}..x^{1.425}):

  Sparsity threshold. The DFI bounds are ||.||_2-normalized; ours is a
  THIN pair: ||alpha|| ||beta|| = (pi(P)pi(Q))^{1/2} = x^{0.425-o(1)},
  while the true trivial count is pi(P)pi(Q) = x^{0.85-o(1)}. A bound
  ||alpha|| ||beta|| D beats (*) iff D <= (pi(P)pi(Q))^{1/2} L^{-3}
  = x^{0.425-o(1)}.

  | bound | D at ell = Q+ | D at ell = A | vs x^{0.425} |
  |---|---|---|---|
  | trivial (1.3): (MN)^{1/2} | x^{0.6375} | x^{0.7125} | FAIL +0.21/+0.29 |
  | Thm 1: (M+N)^{1/2} + min(M,N) | x^{0.425}+x^{0.425} | x^{0.5}+x^{0.425} | FAIL (at-threshold x (MN)^eps at ell=Q+; +0.075 at A) |
  | Thm 2: (MN)^{3/8}(M+N)^{11/48} | x^{0.673} | x^{0.748} | FAIL +0.248/+0.323 |
  | Thm 3: (MN)^{14/29}(M+N)^{1/58} | x^{0.630} | x^{0.705} | FAIL +0.21/+0.28 |
  | DRZ26 (wp9-frontier §2c): (MN)^{1/4}(M+N)^{1/6}N^{1/3}M^{-1/12} | x^{0.532} | x^{0.581} | FAIL +0.11/+0.16 |

  Structural reading: DFI-type savings are powers of (MN) gained over
  the DENSE trivial bound (MN)^{1/2}; our thin support sits a factor
  x^{0.2125..0.2875} BELOW that baseline ((MN)^{1/2}/(pi(P)pi(Q))^{1/2}),
  and the best available saving ((MN)^{-1/48}-grade ~ x^{-0.027}) cannot
  recover it. Bettin-Chandee's trilinear upgrade needs an AVERAGE over
  the numerator a (we have a single fixed h) and is equally
  ||.||_2-normalized. VERDICT for the route as prompted: OBSTRUCTED-
  [thin-coefficient normalization; deficit x^{0.11} (DRZ26, best) to
  x^{0.32}] — closed for (*) at the top cell, NOT by pair-dependence.
  The flip of 4.3.1 is still the right move: see 4.3.4.

#### 4.3.4 Step C-4: the per-q citation route — (*) PROVED, with power saving

Return to 4.3.1's exact form and bound it POINTWISE IN q. For fixed
q (prime, q != ell, q ∤ h since 0 < |h| <= L^{B'} < Q < q):

  S_q := Sum_{p in (P,2P], p prime, p != q} e( a pbar_q / q ),
  a := h ellbar_q mod q,  (a, q) = 1.

This is exactly the §1 species — Kloosterman sum over primes, PRIME
modulus q, numerator coprime to q, b = 0 — and, decisively, in the
range where the literature LIVES: length N = P with q in (Q, 2Q] =
(P, 2P], i.e. q/2 <= N < q-grade, N ≍ q. (Contrast §2.3-2.4: there
the modulus was ell with N = Lambda > ell-windowed-by-R and the
TARGET was R-scale, x^{0.275..0.425} below trivial. Here the target
L^{-3} is polylog below trivial: the Polya-Vinogradov barrier of
§2.4 is not in play for (*) itself.)

Citation: Korolev 2018 Thm 3 (§1.3). Window check: N-values needed
are all N in [P, 2P] (intermediate cutoffs for partial summation);
q^{85/96} <= (2Q)^{85/96} = x^{0.3763+o(1)} < P = x^{0.425} and
2P = 2q-grade <= q^{107/96+o(1)} = x^{0.4737+o(1)}: ENTIRELY inside
the MIDDLE regime [q^{85/96}, q^{107/96}], with x-exponent margins
0.049 and 0.049. Saving: Delta <= (q^{1/16} N^{2/5})^{-1/8}
<= 2^{1/20} q^{-37/640} for N >= q/2; at q = x^{0.425+o(1)}:

  Delta <= x^{-(0.425)(37/640) + o(1)} = x^{-0.02457 + o(1)}.

Lambda-to-primes: Sum_{P<n<=N} Lambda(n) e_q(a nbar) =
Sum_{P<p<=N} (log p) e_q(a pbar) + O(P^{1/2} L) (prime powers), and
Abel summation against 1/log t gives, using the Thm-3 bound at every
intermediate N in [P, 2P],

  |S_q| << P q^{-37/640} q^{o(1)} / L + P^{1/2} L
        << P x^{-0.02457 + o(1)},

UNIFORMLY in the numerator a coprime to q (§2.5 audit) — hence
uniformly in (ell, h). Summing over the <= pi(2Q) moduli q and
adding 4.3.1's errors:

  |B(ell,h)| <= pi(Q) L-grade * P x^{-0.02457+o(1)}
                + pi(P)pi(Q) L^{B'} x^{-0.425+o(1)}   [E_smooth]
                + pi(P) * 1{ell <= 2Q}                [q = ell term]
             <= pi(P) pi(Q) x^{-0.0245 + o(1)}.

Citation stack and caveats (inherited, none new):
- PRIMARY: Korolev 2018 Thm 3, slide-verbatim (§1.3). Caveat (as in
  §2.3/§2.5): the slide says "arbitrary composite q"; if prime q is
  excluded by that wording, then (i) the sub-sum over p <= q is
  covered VERBATIM by Korolev 2018 Thm 1 (§1.3: prime q, b = 0,
  q^{1/2+eps} <= N <= q; here N >= q/2, so eps = 1/2 - o(1), explicit
  eta = eps^2/20 = 1/80: saving q^{-1/80} = x^{-0.0053}) and
  independently by Bourgain 2005 (§1.1, ineffective); (ii) only the
  sub-sum over p in (q, 2P] (length < q, but cutoff 2P in (q, 2q))
  needs the N > q extension — Korolev-Changa 2020 (§1.4: "arbitrary
  modulus", q^{1/2+eps} <= N << q^{3/2} covers N <= 2q with margin
  x^{0.16}) at abstract grade, Delta unpinned.
- The half p <= q is therefore UNCONDITIONAL on pinned prime-modulus
  statements; the transcription caveat burdens only the p > q half.

#### 4.3.5 Step C-5: verdict for (*)

(*) PROVED — at strength STRICTLY STRONGER than demanded:

  |B(ell,h)| <= pi(P) pi(Q) x^{-0.0245 + o(1)}
             (<= pi(P) pi(Q) L^{-3} with power-of-x room),

uniformly for 0 < |h| <= L^{B'} and ell in (Q, A] prime (sliver
included, 4.4), at the top cell. Grade: PROVED-MODULO-[Korolev-2018-
Thm-3 slide transcription: prime-modulus admissibility + a-uniformity
re-confirmation against the paper — the §2.3/§2.5 caveat class, no new
citations introduced; fallback stack pinned in 4.3.4]. The h-range
extends as-is to 0 < |h| <= x^{0.4} (E_smooth still <= pi(P)pi(Q)
x^{-0.025}; q ∤ h still automatic). REMARK (full completed range): for
x^{0.4} < |h| < ell/2 the same bound holds with an extra L: complete
the a_0-VALUE range mod q (cost: one L of b-harmonics); the phase
becomes e((h ellbar + b) pbar/q); the degenerate b == -h ellbar
(mod q) terms have, for fixed (ell,h), at most ONE prime q in (Q,2Q]
per b-value (q | b ell + h <= x^{0.85-} < Q^2), totaling
<= pi(P) L = pi(P)pi(Q) x^{-0.425} L^2; the q | h moduli (now
possible) are likewise <= 1 prime in (Q,2Q] per h, costing pi(P).
So (*) holds for ALL 0 < |h| < ell/2 — §4.2's tail-truncation
bookkeeping (and its erroneous "L^{-B'+1}" tail estimate) is moot.

Numerics (this session, /tmp, .venv python): (i) the 4.3.1 flip
identity e(-h a_0 qbar_ell/ell) = e(h (p ell)bar_q/q) e(-h a_0/(qell))
verified EXACTLY on 2000 random tuples (p, q ~ 2000..4000 prime,
ell up to 5400, h <= 12; max deviation < 1e-9). (ii) Model scale
x = 1e7, P = Q = x^{0.425} (129 primes each side, trivial = 16641,
sqrt = 129): |B| = 289 / 121 / 39 at (ell/Q, h) = (1.3, 1) /
(2.7, 3) / (5.0, 7) — square-root-scale, consistent with the proved
power saving and the random-model benchmark of 4.4.2.

WARNING — sufficiency, not strength, is the issue: (*) is proved,
but the §4.2 budget line claiming (*) closes the first moment is
WRONG. Exponent check in 4.4 (as §4.2 stipulated), where the
aggregation over ell is priced honestly.

### 4.4 Exponent bookkeeping and the ell <= 2Q sliver — written this session

#### 4.4.1 The ell <= 2Q sliver: harmless

On the sliver ell in (Q, 2Q], the modulus ell and the variable
q in (Q, 2Q] share a dyadic cell, so q >= ell and q = ell can occur.
Three layers, all fine:
- (*) itself: the 4.3 proof used only ell prime in (Q,A], ell != q,
  ell > Q (for E_smooth) — NEVER ell > 2Q. It covers the sliver
  verbatim; the q = ell column is excluded from B by convention
  (qbar_ell undefined) at recorded cost <= pi(P) = pi(P)pi(Q)
  x^{-0.425+o(1)} L-grade, inside the 4.3.4 constants.
- Step B on the sliver: §4.1's integer-interval identification
  (a_0 in W cap [1,q] AS integers) used q < ell, but it is packaging
  only. The §4.2 completion expands the mod-ell window indicator
  1[nu_ell in [0,R]], nu_ell = (-a_0 qbar) mod ell — exact for ALL
  (q, ell) = 1 in either order, needing only R < ell (R = x^{0.15}
  << Q). Main term per (q,ell): exactly c_0 = (R+1)/ell, unchanged.
  So drop the q < ell restriction and run §4.2 as-is on the sliver.
- q = ell pairs: Prop S's condition is undefined; bound the
  contribution of ell = q to N_hard(p,q) by 1 — adds <= 1 << eta R
  to E[N_hard]. Total sliver overhead: absorbed, no new terms.

#### 4.4.2 Final exponent table — the aggregation check (*) was waiting for

Top cell u = u' = 0.425, eta = 0.05, R = x^{0.15}, all entries
x-exponents-with-constants where pinned:

| quantity | value |
|---|---|
| main term Sum_{ell in (Q,A]} (R+1)/ell | 0.3023 (R+1) = 6.05 eta (R+1) |
| error budget (target C = 7) | ~ 0.95 eta R ~ x^{0.15}/21 |
| # moduli ell in (Q,A] | pi(A) - pi(Q) ~ x^{0.575}/(0.575 L) |
| per-ell harmonic mass Sum_{h != 0} abs(c_h) (sharp window) | 1 + log(R+1) ~ 0.15 L |
| (*) proved strength D := sup abs(B)/(pi(P)pi(Q)) | x^{-0.0246+o(1)} |
| per-ell completed error <= 0.15 L D | x^{-0.0246+o(1)} |
| per-ell MAIN term (R+1)/ell | x^{-0.275} (ell=Q) .. x^{-0.425} (ell=A) |
| total completed error <= 0.26 x^{0.575} D | x^{0.5504+o(1)} |
| deficit vs budget | x^{0.40} |
| uniform D needed to close | <= 0.18 x^{-0.425} ~ (pi(P)pi(Q))^{-1/2} L^{-2}-grade |
| random-model benchmark for abs(B) | typical (pi(P)pi(Q))^{1/2} ~ 0.42 x^{0.425}/L; sup over the ~x^{1.15} pairs (ell,h): another sqrt(L)-factor |
| ceiling test: GRANT abs(B) = (pi(P)pi(Q))^{1/2} for every (ell,h) | sharp window: total ~ 0.11 L R (miss ~2L); Selberg majorant (O(1) harmonic mass, H ~ ell/R): total ~ 1.48 R (miss ~ constant 30) |

CONCLUSION (the §4.2 budget claim REFUTED; (*) proved AND shown
insufficient). The needed uniform strength sits at/below the
random-model floor: per-ell the error must beat the per-ell main term
R/ell = x^{-0.275..-0.425}, while pi(A) ~ x^{0.575}/L moduli each pay
at least the square-root floor (pi(P)pi(Q))^{-1/2} = x^{-0.425}L —
the pointwise route misses by ~2L at the sharp-cutoff ceiling, by a
constant ~30 even with a Selberg-majorant completion (O(1) harmonic
mass) at EXACT square-root cancellation for every (ell,h), and the
sup over x^{1.15} pairs genuinely exceeds the square-root floor by
sqrt(L)-factors in the random model. No pointwise-in-(ell,h) bound —
provable or true — closes the first moment. This is §3.4(2)'s
warning ("per-(ell,h) absolute values re-pay the Lambda-grade L^1
mass ... the ell-average with signed window coefficients (i.e.
genuine dispersion) must be kept") re-derived quantitatively; §4.2's
budget line had contradicted it and is withdrawn.

What survives, precisely: Steps A-B (exact, sliver included, 4.4.1),
the bound (*) at power-saving strength for ALL 0 < |h| < ell/2
(4.3.4-4.3.5), and the structural gain of the 4.3.1 flip (modulus
moved from ell to q; degenerate sector emptied for |h| < Q). What the
first moment still needs: the SIGNED aggregate
  Sum_{ell in (Q,A]} Sum_{0<|h|<ell} c_h B(ell,h)
treated with the ell-sum INSIDE — per (p,q) this is
Sum_ell [1(nu_ell <= R) - (R+1)/ell], a dispersion/second-moment-in-
ell object (large-sieve species over the ~x^{0.575} moduli ell), NOT
a per-(ell,h) absolute-value object. The 4.3.1-flipped form
Sum_q Sum_p e(h (p ell)bar_q/q) with modulus q FIXED across ell is
the natural input: the ell-dependence now sits ONLY in the numerator
h ellbar_q mod q — a complete-sum average over ellbar mod q is
available per q. That is the recommended Step D (not attempted here).

STATUS (Sec. 4): Steps A-B PROVED (sliver included). Step C = (*)
PROVED-MODULO-[Korolev-2018-Thm-3 transcription caveats, §2.3/§2.5
class] at strength pi(P)pi(Q) x^{-0.0245}, all 0 < |h| < ell/2,
all ell in (Q,A]. FIRST MOMENT NOT CLOSED: the §4.2 pointwise budget
is refuted (deficit x^{0.40} at proved strength; >= constant-to-L
even at the square-root ceiling); requires dispersion in ell
(Step D, framed above; EXECUTED in 4.5).

### 4.5 Step D: the ell-sum brought inside — executed this session

Object (4.4's framing, via 4.3.1's flip): per (p,q), with the ell-range
(Q,A] tiled by dyadic blocks (Lambda, 2Lambda], Lambda = 2^j Q (top block
clipped at A), the first-moment error is

    D(p,q) = Sum_{Lambda} Sum_{h != 0} [ Sum_{ell ~ Lambda, ell prime}
             c_h(ell) s_h(ell) e( a_h ellbar_q / q ) ],

    a_h := h pbar_q mod q,   s_h(ell) := e(-h a_0(p,q)/(q ell))  (smooth),

and the first moment closes iff sup_{p,q} |D(p,q)| <= 0.95 eta R-grade
(C = 7; signed (p,q)-averaging would also do, but Step D as framed bounds
per (p,q) — see D3/D5). All numerics at BOTH eta = 0.05 (top cell
P = Q = x^{0.425}, A = x^{0.575}, R = x^{0.15}) and eta = 0.02
(Q = x^{0.47}, A = x^{0.53}, R = x^{0.06}). Standing identity used
throughout: A = Q R exactly (x^{1-u} = x^{u'} x^{1-u-u'}).

#### 4.5.1 D1: the completion coefficients as functions of ell

Exact shape (geometric sum; window [0,R] mod ell, §4.2):

    c_h(ell) = (1/ell) Sum_{n=0}^{R} e(-h n/ell)
             = (1/ell) e(-hR/(2 ell)) sin(pi h (R+1)/ell)/sin(pi h/ell).

NO arithmetic content in ell: c_h(t) is C^infty in t on each dyadic
block. Bounds (|h| <= t/2): sup |c_h(t)| <= min((R+1)/t, 1/(2t||h/t||))
<= min((R+1)/Lambda, 1/(2|h|))-grade on t ~ Lambda; derivative
(term-by-term, Abel on Sum_n n e(-hn/t)):

    |c_h'(t)| <= min(R+1, t/(2|h|)) t^{-2} (1 + 4 pi |h| R / t),

so Var_{(Lambda,2Lambda]}(c_h) <= min((R+1)/Lambda, 1/(2|h|))
(1 + 4 pi |h| R/Lambda). The smooth factor: sup|s_h| = 1,
Var(s_h) <= 2 pi |h| a_0/(q Lambda) <= 2 pi |h|/Lambda. Partial
summation (BV x oscillation), for any phase X(ell) on the block:

    |Sum_{ell ~ Lambda} c_h s_h X(ell)|
        <= W(h,Lambda) max_{I subset block} |Sum_{ell in I} X(ell)|,
    W(h,Lambda) := C_1 min((R+1)/Lambda, 1/|h|) (1 + |h| R/Lambda).  (D1.1)

THE INFLATION (1 + |h|R/Lambda) IS REAL: the endpoint phase
e(-hR/(2t)) rotates ~ |h|R/Lambda times across the block; it cannot be
removed by smarter calculus (opening the n-sum gives the same mass).
It destroys the 1/|h| tail: Sum_{0<|h|<=Lambda/2} W(h,Lambda)
= [h <= Lambda/R: ~3/2] + [Lambda/R < h <= Lambda/2: ~log R + R/2]
~ R/2 per block. Sharp-window verdict: even with the D2 Kloosterman
input the assembly is Sum_Lambda (R/2) Lambda Delta ~ x^{0.15+0.558}
= x^{0.708} per (p,q) (eta = 0.05) — WORSE than 4.4.2's pointwise
route. The sharp completion is dead in this orientation too.

Repair — truncate BEFORE the oscillation threshold. Only harmonics
|h| <= Lambda/(R+1) are inflation-free, and that is exactly the
Selberg budget. Per block, replace the sharp window by the
Vaaler-Selberg sandwich S^- <= 1_{[0,R] mod ell} <= S^+ of degree

    H_Lambda := ceil(Lambda/(R+1)),

(Vaaler 1985 / Montgomery, Ten Lectures, Ch. 1; window length R+1
mod ell): S^pm(nu/ell) = Sum_{|h| <= H} chat^pm_h(ell) e(h nu/ell),

    chat^pm_0(ell) = (R+1)/ell pm 2 theta/(H+1),  theta in [0,1],
    |chat^pm_h(ell)| <= 1/(H+1) + min((R+1)/ell, 1/(pi |h|)).

The ell-dependence of chat^pm_h enters only through 1/ell amplitudes
and endpoint phases e(-h R'/ell)-type with R' <= R+1 (explicit Vaaler
formula), so the derivative has the SAME shape as (D1.1); on the
truncated support |h| R/Lambda <= H R/Lambda <= 1 + R/Lambda <= 2,
hence inflation <= 1 + 8 pi = O(1) and

    W^pm(h,Lambda) <= C_2 (1/(H+1) + min((R+1)/Lambda, 1/|h|)),
    C_0 := Sum_{0<|h|<=H} W^pm(h,Lambda) <= 30  (absolute).      (D1.2)

[Lemma-grade check deferred: the ell-derivative of the explicit Vaaler
coefficients — pure calculus, no arithmetic; flagged, not load-bearing
for the verdict below.]

Sandwich price (main term): |chat^pm_0 - (R+1)/ell| <= 2/(H+1)
<= 4(R+1)/ell on the block, so the extra main-term mass is
<= 4(R+1) Sum_{ell in (Q,A]} 1/ell = 4(R+1)(0.3023) = 1.21(R+1)
= 24.2 eta (R+1) at eta = 0.05: absorbed into the target constant
(C: 7 -> 32; still "<= C eta R"-form). BONUS (kills the framed
exceptional sector): H_Lambda <= ceil(A/(R+1)) <= Q < q for EVERY
block, by A = QR — so q | h is IMPOSSIBLE throughout Step D, the
exact analogue of 4.3.1's "degenerate sector empty" mechanism. D1
DONE: ell-dependence tamed at O(1) weight-mass per block, O(eta R)
sandwich slack, no exceptional moduli.

#### 4.5.2 D2: the prime-ell Kloosterman sum per (h,q,p) — Korolev Thm 3

After (D1.2)'s partial summation the arithmetic factor per
(h, q, p, Lambda) is the incomplete Kloosterman sum over primes

    K_q(a; I) := Sum_{ell in I, ell prime, ell != q} e(a ellbar_q/q),
    I = (Lambda', Lambda''] subset block,  a = h pbar_q mod q.

Coprimality: 0 < |h| <= H_Lambda <= Q < q (D1, A = QR) and p != q
prime, so q does not divide h p: (a, q) = 1 for EVERY (h,q,p) in the
sum — no exceptional moduli at all (the framing's "O(1) per (h,p)"
allowance is unused). q | ell impossible (ell != q excluded; cost in
D4). Conversion: Korolev's T_q(N) = Sum_{n<=N} Lambda(n) e_q(a n*) to
primes-in-I by prime-power removal O(Lambda^{1/2} L) + Abel against
1/log t + differencing two cutoffs, all uniform in a with (a,q)=1
(§2.5 audit class; same chain as 4.3.4).

Range check, Korolev 2018 Thm 3 (§1.3), both cutoffs of every I:
- eta = 0.05: q = x^{0.425+o(1)}; q^{5/8} = x^{0.2656} << Lambda in
  [x^{0.425}, x^{0.575}] <= q^{7/4-eps} = x^{0.7438-}: margins
  x^{0.159} (bottom) / x^{0.169} (top). Regime boundary
  q^{107/96} = x^{0.4737}: MIDDLE regime (Delta = q^{-1/128}
  N^{-1/20}) for Lambda <= x^{0.4737}, TOP regime
  (Delta = (N q^{-7/4})^{1/10}) above. (q^{85/96} = x^{0.3763} < Q:
  the bottom Thm-3 regime is never entered.)
- eta = 0.02: q = x^{0.47+o(1)}; q^{5/8} = x^{0.2938} << Lambda in
  [x^{0.47}, x^{0.53}] <= q^{7/4} = x^{0.8225}: margins x^{0.176} /
  x^{0.293}. Boundary q^{107/96} = x^{0.5238}.

OUTPUT, per (h, q, p, Lambda):

    |Sum_{ell ~ Lambda} chat^pm_h(ell) s_h(ell) e(a ellbar_q/q)|
      <= W^pm(h,Lambda) max_I |K_q(a;I)|
      <= C_3 W^pm(h,Lambda) Lambda Delta(q,Lambda) q^{o(1)},     (D2.1)

with Delta x-exponents (continuous in lambda = log_x Lambda):
- eta = 0.05: Delta = x^{-0.0246} (Lambda = Q) -> x^{-0.0270}
  (Lambda = x^{0.4737}, regime break, continuous) -> x^{-0.0169}
  (Lambda = A). Worst block: x^{-0.0169}.
- eta = 0.02: x^{-0.0272} (Q) -> x^{-0.0299} (x^{0.5238}) ->
  x^{-0.0293} (A). Worst block: x^{-0.0272}.

Citation caveats (recorded; one NEW weight vs 4.3.4): (i) "arbitrary
composite q" wording vs our prime q — the inherited §2.3/§2.5 class.
(ii) NEW: here N = Lambda EXCEEDS the modulus q on all but the bottom
block (N/q up to x^{0.15}); the prime-modulus-verbatim fallbacks
(Korolev Thm 1, Bourgain 2005: both need N <= q) cover ONLY
Lambda in (Q, q]; everything above leans on Thm 3's stated range
N <= q^{7/4}, with Korolev-Changa 2020 (arbitrary modulus,
N << q^{3/2} = x^{0.6375} >= A, margin x^{0.0625}; abstract grade,
Delta unpinned) as backup. This caveat is IMMATERIAL for the verdict:
D3 shows even Delta = Lambda^{-1/2} q^{o(1)} — square-root
cancellation, far beyond any citation — cannot close. D2 DONE.

#### 4.5.3 D3: assembly — the budget arithmetic, every line

Sum (D2.1) over 0 < |h| <= H_Lambda ((D1.2): mass C_0 <= 30) and over
the <= 0.22 L dyadic blocks; add D1's sandwich slack and D4's
residues:

    |D(p,q)| <= C_4 Sum_{Lambda = 2^j Q} Lambda Delta(q,Lambda)
                q^{o(1)}  +  24.2 eta (R+1)  +  (D4: O(1) + tiny).

Sanity: per (h, Lambda) Korolev DOES beat trivial — Lambda Delta vs
pi(Lambda) ~ Lambda/L is a win of Delta L = x^{-0.017+o(1)}. The
failure is the budget, not absence of cancellation. Exponent ledger
of f(Lambda) = Lambda Delta (eta = 0.05; lambda := log_x Lambda;
exponent = 0.95 lambda - 0.0033 middle / 1.1 lambda - 0.0744 top —
increasing in lambda, so the TOP block dominates geometrically):

  lambda:    0.425    0.45     0.4737   0.50     0.55     0.575
  Delta:    -0.0246  -0.0258  -0.0270  -0.0244  -0.0194  -0.0169
  LamDelta:  0.4004   0.4242   0.4467   0.4756   0.5306   0.5581

    Sum_Lambda Lambda Delta <= 2.1 x^{0.5581};
    budget 0.95 eta R = x^{0.15}/21:
    DEFICIT = x^{0.5581 - 0.15 + o(1)} = x^{0.408 + o(1)}.

  eta = 0.02: exponent peaks at lambda = 0.53: ledger
  lambda:    0.47     0.50     0.5238   0.53
  Delta:    -0.0272  -0.0287  -0.0299  -0.0293
  LamDelta:  0.4428   0.4713   0.4940   0.5008
    total <= 2.1 x^{0.5008}; budget 0.02 x^{0.06}:
    DEFICIT = x^{0.441 + o(1)}.  (Smaller eta is WORSE: R shrinks
    as x^{3 eta} while A only as x^{1/2 + 1.5 eta}.)

Where the framing's heuristic ("O(1) harmonic mass per block x
#blocks x q^{-eta_0} vs eta") broke: the per-h inner object is a sum
of LENGTH pi(Lambda) ~ x^{0.575}/L, so the O(1)-mass line reads
O(1) x Lambda Delta per block, not O(1) x Delta. Closing needs
Lambda Delta <= eta R/L-grade, i.e.

    Delta <= eta R/(Lambda L):  x-exponent -0.275 (bottom block)
             to -0.425 (top block) at eta = 0.05,

a power OF LAMBDA, not a power-saving margin. Korolev's currency
(x-exponent -0.017..-0.030) is the wrong denomination by x^{0.25-0.41}.

CEILING TEST (grant |K_q(a;I)| <= Lambda^{1/2} for every (h,q,p,I):
square-root cancellation over the primes ell, strictly stronger than
anything provable for a single modulus): per block C_0 Lambda^{1/2},
total <= 3.5 C_0 A^{1/2}:
  eta = 0.05: x^{0.2875+o(1)} vs x^{0.15}/21: DEFICIT x^{0.1375+o(1)}.
  eta = 0.02: x^{0.265+o(1)}  vs 0.02 x^{0.06}: DEFICIT x^{0.205+o(1)}.
General eta (top cell u = u' = 1/2 - 1.5 eta):

    ceiling-deficit exponent = (1-u)/2 - (1-u-u') = 1/4 - 2.25 eta,

POSITIVE for all eta < 1/9 — and eta = 1/9 is exactly the in-band
edge u + u' = 2/3 (R = y). The per-(h,q,p) route fails by a power of
x throughout the band, INDEPENDENTLY of the prime-ell Kloosterman
input's quality.

Structural reading (exact dual of 4.4.2). Per (p,q) and top block,
Step D asks the harmonic count of {ell ~ Lambda : nu_ell <= R}
(true size ~ R/L) to absolute accuracy eta R/L-grade out of a sum of
pi(Lambda) ~ x^{0.575}/L unimodular terms: relative accuracy
x^{-0.425}, BELOW the square-root floor x^{-0.2875} of any
harmonic-analysis treatment of one (p,q). So absolute values may not
be taken even at the per-(p,q) level (a fortiori per-(h,q,p));
4.4.2 showed they may not be taken at the per-(ell,h) level. Together:
NO single-variable aggregation closes the first moment — it requires
SIGNED averaging over at least one of p, q jointly with the
ell-cancellation. D3 DONE (negative).

#### 4.5.4 D4: residues — E_AP, sliver, exceptional q, conversions

- E_AP: no separate term. The sandwich REPLACES the §4.2 completion
  identity; the h != 0 sandwich mass IS the E_AP aggregate (as §4.2
  noted for the sharp window), and both inequalities
  S^- <= 1 <= S^+ are exact pointwise — bookkeeping is two runs of
  D1-D3 (majorant for the upper bound on E[N_hard]; minorant only if
  a matching lower bound is ever needed).
- Sliver ell in (Q, 2Q] (4.4.1 carries over verbatim): the ell = q
  column is excluded from K_q at cost sup_h |chat^pm_h s_h| summed
  over |h| <= H: <= C_0-grade = O(1) per (p,q) per block, total O(1)
  << eta R. p = q excluded as in 4.3 (cost pi(Q)-grade, absorbed).
  ell = p is NOT excluded — a legitimate term, no degeneracy
  (q does not divide h p^2).
- Exceptional q | h p: EMPTY (D1/D2: H_Lambda <= Q < q by A = QR;
  q != p prime). The framing's fallback handling is not needed.
- Lambda(n)-to-primes + Abel + interval differencing:
  O(Lambda^{1/2} L) per (h,q,p,I); summed with (D1.2)-mass this is
  <= C_0 Lambda^{1/2} L per block — the same size as D3's ceiling
  line, hence absorbed in its constants (and at Korolev strength
  absorbed by q^{o(1)}).
- Smooth factor s_h(ell): handled INSIDE the BV weight (D1) — exact;
  Step D needs no E_smooth term and no |h| <= L^{B'} truncation
  anywhere (contrast 4.3.1; this is why h up to H ~ Lambda/R is
  admissible here).
D4 DONE: all residues O(1) per (p,q) or absorbed; nothing leaks into
the D3 verdict.

#### 4.5.5 D5: verdict for Step D

OBSTRUCTED-[per-(h,q,p) ell-aggregation deficit: x^{0.408+o(1)} at
Korolev-2018-Thm-3 strength at eta = 0.05 (x^{0.441+o(1)} at
eta = 0.02); >= x^{1/4 - 2.25 eta} (= x^{0.1375} / x^{0.205}) even
granting square-root cancellation in every prime-ell sum; the deficit
exponent vanishes only at eta = 1/9, the band edge u + u' = 2/3].
FIRST MOMENT REMAINS OPEN. Step D as framed — absolute values at the
(h,q,p) level after bringing the ell-sum inside — is hereby priced
and CLOSED: it is the exact dual of the 4.4.2 failure (there:
x^{0.40} deficit on per-(ell,h) absolute values of (p,q)-sums; here:
x^{0.41} on per-(h,p,q) absolute values of ell-sums — the symmetry is
A x (best saving)/(eta R) in both orientations). Together the pair
PROVES: no aggregation that takes absolute values at any
single-variable level closes E[N_hard] <= C eta R anywhere in the
band; cancellation must be harvested jointly in ell AND (signed) in
at least one of p, q.

Positive payload (sound, reusable, this session's net gain):
- (D1.1): the completion coefficients c_h(ell) are BV in ell with the
  exact inflation law (1 + |h| R/Lambda); sharp windows are
  unusable in ANY ell-inside route (Sum_h W ~ R per block).
- (D1.2): the Selberg-sandwich-at-degree-Lambda/(R+1) packaging:
  O(1) weight-mass per block, <= 24.2 eta (R+1) main-term slack,
  q | h sector emptied by the identity A = QR. This is the correct
  completion for every future treatment of this object.
- (D2.1): per-(h,q,p) prime-ell Kloosterman bound
  Lambda Delta q^{o(1)}, Delta <= x^{-0.0169} on all blocks (both
  eta values), no exceptional moduli — the per-modulus input any
  dispersion argument will call as its "first moment after Cauchy".
- The forward object, now FORCED (unique survivor): per block,
    T_h(Lambda) := Sum_{q ~ Q} Sum_{p ~ P}
                   | Sum_{ell ~ Lambda} chat_h(ell) s_h(ell)
                     e( h (p ell)bar_q / q ) |^2
  — BFI-grade dispersion (equivalently 4.4's Sum_ell-inside second
  moment; the §3 variance ladder, §3.2-3.4 pricing applies). Quick
  feasibility floor: the un-completed per-(p,q) variance diagonal is
  Sum_{ell ~ Lambda} (R/ell)(1 - R/ell) ~ R/L per block, so with
  controlled off-diagonals E_{p,q}|D_Lambda| ~ (R/L)^{1/2}-grade and
  the block-total ~ (R L)^{1/2} << eta R iff R >= eta^{-2} L^3-grade:
  HOLDS with x^{0.15-o(1)} of room at R = x^{0.15}. The variance
  route has room exactly where Step D has none; its obstruction
  ladder ((b1)/(b2) off-diagonals) is already priced in §3.2-3.3.

STATUS (Step D / Sec. 4.5): EXECUTED, OBSTRUCTED-[x^{0.408} deficit
at citation strength; x^{1/4-2.25 eta} structural deficit at the
square-root ceiling — quantified, both eta values]. First moment NOT
closed by Steps A-D; A, B proved, C proved-with-power-saving (4.3),
D priced and closed (4.5): the §3 variance/dispersion ladder is the
unique remaining route, with feasibility floor verified.
