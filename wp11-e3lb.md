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
