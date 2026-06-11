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
