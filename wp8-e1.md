# DRAFT — UNVERIFIED AGENT ATTACK REPORT

## WP8: Hypothesis E1 (wrap-boundary average, Family A), signed form

Date: 2026-06-10 (agent attack). Read: `manuscript/sections/08-major.tex`
(lem:branch, hyp:E1, rem:E1-signed, prop:familyA, prop:digit-assembly),
`12-e1e2.tex` (documented FATAL per-(mu,h) Selberg failure — not retried),
`07-minor.tex` ((M1), lem:cf), `wp24-e1-e2-fineclass.md`, `wp8-e2.md` (style
model), `main.tex` (macros).

Notation: $L=\log x$, $P=x^u$, $Q=x^{u'}$, $u,u'\in(\tfrac13,\tfrac12)$,
$R=x^{1-u-u'}$, $M_0:=RL^{-B}$, $\delta_\mu=1/(2\mu L^B)$,
$\theta_\mu(p,q)=\mu q/p-\lambda p/q$,
$N_q(\mu,\lambda,\delta)=\#\{p\in(P,2P]\cap\mathbb Z:\ \|\theta_\mu\|\le\delta\}
=2\delta P+E_q$. Target (signed form, per rem:E1-signed): for each
$0<\lambda\le L^C$,
$\big|\pi(Q)^{-1}\sum_{q\sim Q}\sum_{\mu\le M_0}E_q(\mu,\lambda,\delta_\mu)\big|
\ll PL^{1-B}+L^{O(1)}$ — in fact only the UPPER bound on the signed sum is
consumed downstream.

VERDICT: **PROVED-MODULO-[write-up]** (see §7). E1 in its downstream-
consumed form reduces to elementary lattice counting — no primes, no
exponential sums; one classical elementary input (Lemma R, averaged root
counts of quadratic congruences); exponent ledger machine-verified on the
closed band including the $(1/3,1/3)$ corner. Confidence ~0.7.

---

## 1. Two structural reductions (proved first; these set the frame)

### 1.1 Integer p was never needed as prime — already in lem:branch

`lem:branch` defines $N_q$ as a count over INTEGER $p$ ("count over integers
$p$; restricting to primes only decreases it"), and `prop:familyA` uses
$\#\{p\ \text{(M1)-major}\}\le\sum_\mu N_q$ — an upper bound on an excluded
set. So no prime-$p$ input is needed anywhere in E1. (Verified by reading
prop:familyA's proof: the major set is only excluded; integer-$p$ upper bound
suffices.)

### 1.2 Prime q can be relaxed to integer q at the cost of one factor L

$N_q\ge0$ termwise, so $\sum_{q\sim Q\,\mathrm{prime}}\sum_\mu N_q\le
\sum_{q\sim Q\,\mathbb Z}\sum_\mu N_q$. If we prove the INTEGER-q signed
bound
$$\Big|\frac1Q\sum_{q\sim Q\,\mathbb Z}\sum_{\mu\le M_0}E_q\Big|\ \ll\
P\,L^{A-B}\qquad(A\ \text{absolute, indep.\ of }B),\tag{E1$^\flat$}$$
then $\pi(Q)^{-1}\sum_{q\,\mathrm{prime}}\sum_\mu N_q\le(Q/\pi(Q))\,
[\sum_\mu2\delta_\mu P+PL^{A-B}]\ll PL^{1-B}\log R\cdot L+PL^{A+1-B}$,
i.e. prop:familyA's conclusion with one extra factor $L^{A+1}$; since $B$ is
a free parameter chosen LAST ($B=C+c+4$ in prop:digit-assembly), replacing
$B\to B+A+2$ absorbs this everywhere (the corner trim
$\sqrt R\ge L^{B/2+c+5}$ tightens by a polylog — an $O(\eta'')$-type cost
already registered). Also verified: $\lambda$ is an integer
($1\le\lambda\le L^C$; it is the Fermat-quotient character index of
`06-reduction.tex`). CONCLUSION OF §1: E1 reduces to E1$^\flat$, a pure
LATTICE-POINT statement: no primes anywhere. Both $p$ and $q$ are integers;
all that remains is floor-function counting. (Negative $\lambda$ / the
$\mu\mapsto p-\mu$ "sum branch" $\mu q/p+\lambda p/q$ is cognate: the conic
solution set is at most two p-intervals per $(q,\mu,k)$ instead of one, with
endpoints again linear in $q$; everything below applies verbatim.)

## 2. Exact moving-interval decomposition (the aggregation-before-cancellation)

Fix $\lambda\le L^C$ and $\mu\le M_0$, $q\sim Q$, $k\in\mathbb Z$. On $p>0$
the function $g(p)=\mu q/p-\lambda p/q$ is strictly decreasing, so
$$\{p:\ |g(p)-k|\le\delta_\mu\}=[c_-q,\ c_+q],\qquad
c_\mp=c(k\pm\delta_\mu),\quad
c(t):=\frac{\sqrt{t^2+4\lambda\mu}-t}{2\lambda},$$
i.e. the per-$(\mu,k)$ p-window is ONE interval whose endpoints are LINEAR
in $q$ with slopes $c_\pm$ INDEPENDENT of $q$. Hence with
$\psi(t)=t-\lfloor t\rfloor-\tfrac12$:
$$N_q(\mu,\lambda,\delta_\mu)=\sum_k\Big[\mathrm{len}_k(q)
+\psi(\text{left edge})-\psi(\text{right edge})\Big],$$
where for each $(\mu,k)$ the edges are $c_\mp q$ when the window lies inside
$(P,2P]$, and the constants $P,2P$ when clipped. Bookkeeping (all matching
lem:branch's proof):
- $\sum_k\mathrm{len}_k(q)$ reconstitutes $2\delta_\mu P$ + edge-window
  deficits; the edge term $\delta_\mu(\mu Q/P^2+\lambda/Q)^{-1}$ sums over
  $\mu$ unconditionally (lem:branch parenthetical: $\ll PL^{-B}+QL^{1-B}$).
- Clipped windows: for fixed $(\mu,k)$, the $q$ with a clipped window form
  $\le2$ subintervals; on them the error per $(q,\mu)$ is $O(1)$ — the
  unconditional $\sum_\mu O(1)\ll RL^{-B}\le PL^{-B}$ piece of
  rem:E1-signed, since at most $O(1)$ values of $k$ clip per $(q,\mu)$.
- $\lambda$-piece: per $(q,\mu)$ the number of contributing $k$ is
  $\le C(\mu Q/P+\lambda P/Q+1)$; the sub-range $\mu\le m_0:=
  \max(P/Q,\ \lambda P^2/Q^2,\ 1)$ (where $\mu Q/P\not\gg\lambda P/Q+1$)
  is bounded trivially, $O(1)$ per $(q,\mu,k)$ — uniform accounting in
  §2.1 (a first attempt that dropped the $L^{-B}$ of $M_0$ produced a
  spurious failure at $(1/2,1/3)$; resolved there).

So modulo §2.1, E1$^\flat$ reduces to: for each dyadic $m\in[m_0,M_0]$,
$$\mathcal E(m):=\sum_{\mu\sim m}\ \sum_{k}\ \sum_{\pm}
\Big|\sum_{q\in I_{\mu,k,\pm}}\psi\big(c_\pm(\mu,k)\,q\big)\Big|
\ \ll\ QP\,L^{-B+O(1)}/L,$$
with $k$ ranging over $\asymp mQ/P=:\bar K$ values, $I$ a subinterval of
$(Q,2Q]$, and slopes $c_\pm\asymp P/Q$.

### 2.1 The unconditional pieces, uniformly in the closed band (clean)

Per $(q,\mu)$, the number of $k$ treated trivially (error $O(1)$ each) is:
the $\le2$ clipped $k$'s, plus — when $\mu\le m_0$ — the whole $k$-range,
of size $\le C(\lambda P/Q+1)$ there (since $\mu Q/P\le\max(1,\lambda P/Q)$
for $\mu\le m_0$). Summing over $\mu\le M_0=RL^{-B}$:
$$\sum_{\mu\le M_0}C'(\lambda P/Q+1)\ \le\ C'\Big(\frac{\lambda RP}{QL^B}
+\frac{R}{L^B}\Big)\ \le\ C'P\,L^{C-B}\,x^{1-u-2u'}+PL^{-B}\ \le\
2C'P\,L^{C-B},$$
uniformly on the CLOSED band $[1/3,1/2]^2$, because $u+2u'\ge1$ there
(equality only at $(1/3,1/3)$, where $x^{1-u-2u'}=1$). This is exactly
rem:E1-signed's accounting; the $L^{-B}$ from $M_0$ is what makes it
uniform. ✓ No correction needed; $A\ge C$ suffices for these pieces.

## 3. The core machinery (all elementary except ONE named classical input)

Throughout: dyadic $m\in[m_0,M_0]$, $\mu\sim m$, $\bar K:=mQ/P$ ($\asymp$
the number of live $k$ per $\mu$; live range has $\bar K\ge1$), slopes
$c_\pm\asymp P/Q$. Sharpen $m_0$ by an absolute constant so that on the live
range $k\asymp\bar K$ and $\lambda P/Q\le\bar K/100$ (possible since
$m\ge m_0\gg\lambda P^2/Q^2$).

### 3.1 Convergent collapse (kills both the large-$H$ problem and the
high-frequency multiplicity blowup)

CLASSICAL CF/OSTROWSKI LEMMA (elementary; provable from `lem:cf`-style
three-distance facts in a few lines, or cite Kuipers–Niederreiter ch.2):
for real $c>0$, any interval $I\subseteq(Q,2Q]$, with convergents $n_i/s_i$
of $c$ and $\eta_i:=\|s_ic\|$,
$$\Big|\sum_{q\in I}\psi(cq)\Big|\ \ll\ L^2+L\sum_{i:\ s_i\le Q}
\frac{1}{s_i}\min\Big(Q,\ \frac1{\eta_i}\Big).$$
Consequences: (i) only $O(L)$ frequencies per $(\mu,k)$, all $\le Q$ — the
documented fatal large-$H$ coefficient-mass problem cannot arise; (ii) per
dyadic block $s\sim\bar s$ there are $\le3$ convergent denominators of any
fixed $c$, so the count of contributing $(\mu,k,s)$ per dyadic cell is
capped by $C\,m\bar K$, $\bar s$-FREE (this cap is decisive at high
frequencies — see §4 history); (iii) $(n_i,s_i)=1$, so the $\gcd$
stratification trivializes ($g_1=1$); (iv) $\eta_i<1/s_i$, so only deep
shells occur. The $L^2$ covers run-shell bookkeeping; the trivial
per-$(\mu,k)$ total cost $L^2\cdot\#\{(\mu,k)\}\le m\bar K L^2$, summed
over $m$: $\le QPL^{2-2B}x^{2-4u-2u'}\le QPL^{2-2B}$ ✓ ($2u+u'\ge1$ closed).

### 3.2 Resonance identity (exact, two-sided)

For a convergent $n/s$ of $c_\pm$ ($s\ge1$, $(n,s)=1$), $y=sc_\pm-n$,
$\eta=\|sc_\pm\|=|y|$. From $\lambda c^2+tc-\mu=0$ ($t=k\pm\delta_\mu$):
$$\lambda n^2+tsn-\mu s^2\ =\ -y\,(2\lambda n+ts+\lambda y).$$
With $J:=\mu s^2-ksn-\lambda n^2\in\mathbb Z$ ($\lambda,\mu,k,s,n$ all
integers; $\lambda$ is the integer harmonic index) and
$\sigma:=\delta_\mu sn=sn/(2\mu L^B)>0$:
$$|J\mp\sigma|\ =\ \eta\cdot|2\lambda n+ts+\lambda y|,\qquad
|2\lambda n+ts+\lambda y|\asymp s\bar K$$
(two-sided, absolute constants, on the live range — needs the $m_0$
constant-sharpening of the §3 preamble; numerically verified to $10^{-8}$ relative
error, §5). Hence $\frac1s\min(Q,\eta^{-1})\asymp\min(Q/s,\bar K/|J\mp
\sigma|)$: shells $W:=|J\mp\sigma|$ dyadic, bottom shell
$W_{\min}=\bar s\bar K/Q$ collecting everything deeper (weight $Q/\bar s$),
shell weight $w=\bar K/W$. The $n=0$ convergent (possible since
$c\asymp P/Q$ may be $<1/2$): $\eta=c$, per-$(\mu,k)$ cost
$\ll(1/1)\min(Q,Q/(c'P))\ll Q/P\cdot O(1)$; total
$\sum_m m^2(Q/P)^2\le QPL^{-2B}x^{2-5u-u'}\le QPL^{-2B}$ ✓ ($5u+u'\ge2$
closed band, equality at $(1/3,1/3)$).

### 3.3 The jump subtlety at near-integer slopes (diagnostic; no pairing used)

At $(u,u')=(1/3,1/3)$, $s=n=1$, $k=\mu-\lambda$ (i.e.\ $J=0$): $c\approx1$,
the window $[c_-q,c_+q]$ contains $p=q$ for ALL $q$ — the diagonal $p=q$ is
$(M1)$-resonant for every $\mu$, contributing genuinely
$\approx Q$ per $(\mu,k)$, total $QM_0=QPL^{-B}$: AT the budget boundary,
inside it. (Model-scale check, §5(3): each endpoint $\psi$-sum is
$\approx\mp Q/2$, the pair does NOT cancel — the sawtooth jump sits between
the endpoints. An attempted Fourier pair-cancellation cap
$(1/h)|S_h(c_-)-S_h(c_+)|\ll\Delta Q$ is UNSOUND for this jump component —
caught by numerics after the scanner had accepted it. It is not needed:
the corrected J0 count below absorbs the diagonal.)

### 3.4 The lattice count near the conic, by shells

Count, per dyadic cell $(m,\bar s,W)$,
$\nu:=\#\{(\mu,k,s,n):\mu\sim m,\ k\ \text{live},\ s\sim\bar s,\
n\sim\bar N:=\max(\bar sP/Q,1),\ n/s\ \text{convergent of}\ c_\pm,\
|J\mp\sigma|\le W\}$. Upper-bound by relaxing the convergent condition
(except in CAPC). Structure: for fixed $(\mu,s,n)$, $J$ runs over an AP of
step $sn$ as $k$ varies; $\mu$-solvability of $\mu s^2\equiv J+\lambda
n^2\ (\mathrm{mod}\ sn)$ holds iff $sg_1\mid J+\lambda n^2$, $g_1:=(s,n)$
(=1 for convergents; kept general since most bounds relax), and then
$\mu\equiv\mu_0\ (\mathrm{mod}\ n/g_1)$: $\#\mu\le mg_1/n+1$. Facts:
- (F1) $J=0$ admissible $\iff s/(s,n)\mid\lambda$; and $J=0$ requires
  $\sigma\le W$, i.e. $sn\le4mWL^B$.
- (F2) $J\ne0$ admissible $\Rightarrow g_1^2\mid J$.
- (F3) $J\ne0$ requires $\sigma_{\max}+W\ge1$: the half-window shift
  $\sigma$ QUANTIZES the spectrum (witness-truncation analogue of
  WP8-E2 Step 0); for $\sigma_{\max}\le1/4$, shells with
  $W<\min(\sigma_{\min},1)/2$ contain no $J\neq0$ points and no $J=0$
  points: EMPTY.
- (F4) CAPC: $\nu\le Cm\bar K$ — each $(\mu,k)$ has $\le3$ convergent
  denominators per dyadic $\bar s$ and $\le2$ signs. ($\bar s$-free; this
  replaces the naive $m\bar K\bar s$ and is decisive for
  $\bar s\ge x^{\epsilon}$-frequencies in the lower-left band region.)
- (F5) for fixed $(s,n)$, $\mu$-windows of distinct $J$ are disjoint up to
  multiplicity $O(W+1)$ ($\sigma(\mu)$ strictly monotone in $\mu$).
- (F6) exact factorization: with $j:=ks+\lambda n\in\mathbb Z$,
  $J=\mu s^2-nj$ — the conic is a SHIFTED DIVISOR equation; $k$-integrality
  $\iff j\equiv\lambda n\ (\mathrm{mod}\ s)$. (Used for intuition and
  cross-checks; the counting below does not need it.)

Term zoo (each $\times L^{O(1)}$; machine-verified sufficient, §4):
- A (measure): $CmW$ (the $2W/(sn)$ $k$-window density, integrated).
- J0: $C\min\big(\max(mWL^{B+1},\ \min(m^2WL^{B+2}/\bar N,\ m\bar s)),\
  \mathrm{CAPC}\big)$. Derivation: by (F1), pairs are $s=gh''$, $n=gn''$,
  $h''\mid\lambda$, $(h'',n'')=1$, $g^2h''n''\le4mWL^B$, count
  $\sum_{h''\mid\lambda}\sum_{g\le2\bar s/h''}\sum_{n''}(m/n''+1)$; the
  $g\le2\bar s/h''$ truncation gives the $m\bar s$ alternative (its
  omission was caught at the corner via the diagonal of §3.3).
- $J\ne0$ (gate $\max(\bar\sigma,W)\ge\tfrac12$, by (F3)); $\nu_{J\ne0}\le
  C\min(B_1,B_2,\mathrm{CAPC})$:
  - $B_1=$ JA + JB + J2 + SING with
    JA $=mW$ (AP-harmonic over admissible $J$: density $1/(\bar sg_1)$
    collapses $\sum_J 1/|J|$ to $L/(\bar sg_1)$, then $\sum_{s,n}$);
    JB (the $1/J_0$ sporadic harmonic): for $W\le\bar\sigma/8$:
    $mW\bar sL^2/\bar\sigma$ (since $J_0\asymp\bar\sigma$); else
    $mW(1+\bar s/\bar N)$ by LEMMA R;
    J2 $=\max(\bar\sigma,W)\,\bar N$ ($J$-measure $\times$
    $\mu$-singleton$\le1$; the $1/(\bar sg_1)$ density over the
    $\sigma$-range, $\sum_{s,n}1/(sg_1)\ll\bar N$);
    SING $=\min\big(\bar s\bar N,\ (\bar N\bar s^{1/2}+\bar s^{3/2})
    L^{O(1)}\big)$ (trivial vs LEMMA G singleton pairs).
  - $B_2=(W{+}1)\max(m\bar s,\mathrm{SING})$ — the (F5) union bound.

THE ONLY NON-FORMAL INPUT (everything else above is elementary counting):
- LEMMA R (averaged least-residue harmonics of quadratic congruences).
  With $d_0(s,n):=\min\{|J|\ge1:\ J\equiv-\lambda n^2\ (\mathrm{mod}\ s)\}$,
  $$\sum_{s\sim\bar s}\sum_{n\sim\bar N}\frac{1}{n\,d_0(s,n)}\ \ll\
  \Big(1+\frac{\bar s}{\bar N}\Big)L^{O(1)},\qquad\text{uniformly},\
  \lambda\le L^C.$$
  PROOF SKETCH (elementary, 4 steps): (i) each residue $x=n\bmod s$ occurs
  $\le\bar N/s+1$ times among $n\sim\bar N$, so the sum is
  $\le\sum_s(\tfrac1{\bar N})(\bar N/s+1)\sum_{x\bmod s}1/d_0(x)$;
  (ii) $\sum_{x\bmod s}1/d_0(x)=\sum_{1\le j\le s/2}\rho_{\mp j}(s)/j$,
  $\rho_a(s):=\#\{x:\lambda x^2\equiv a\ (s)\}$;
  (iii) the classical bound $\rho_a(s)\le4^{\omega(s)}\sqrt{(a,s)}\cdot
  (\lambda\text{-gcd factor})$ gives $\sum_j\rho_{\mp j}(s)/j\le
  4^{\omega(s)}\tau(s)\,L\cdot L^{O(C)}$;
  (iv) averaging over $s\sim\bar s$: $(1/\bar s)\sum_s4^{\omega(s)}\tau(s)
  =L^{O(1)}$. The per-individual-$s$ factor $4^{\omega}\tau$ can be
  $x^{o(1)}$ — the $s$-AVERAGE is essential and is exactly what the
  counting supplies. $\square$ (write-up owed: the $p=2$/squarefull cases
  of (iii) and the $(\lambda,s)$-stratification.)
- LEMMA G (incomplete quadratic Gauss sums) was provisionally introduced
  for the singleton pairs but the ABLATION TEST (§4) shows it is NOT
  load-bearing once the convergent cap (F4) is in place: the trivial
  $\mathrm{SING}=\bar s\bar N$ suffices everywhere. Dropped. Consequently
  the entire proof uses NO exponential sums and NO primes.

## 4. Exponent verification (machine-checked, closed band)

`e1_exponents.py`: every size tracked as $x^f L^{tB}$ ($B$ = free level
parameter chosen last); dyadic parameters $(m,\bar h,W)$ scanned over
$f$-grids PLUS $B$-offset grids $t\in\{0,-1,\dots,-4\}$ (this catches
polylog slivers like $\bar h\approx QL^{-2B}$); range endpoints carry their
exact $L$-powers ($M_0=RL^{-B}$ etc.). Acceptance: contribution
$x^eL^{aB}\le QP\cdot L^{-B}$ i.e. $e<u+u'$ strictly, or $e=u+u'$ and
$a\le-1$ — the correct uniformity criterion on the CLOSED band (margins
degenerate at $(1/3,1/3)$, $(1/2,1/3)$-type corners, so polylog-vs-power
bookkeeping at equality is what matters).

RESULT (final system of §3.4): ALL of the closed band passes IN THE
q-FRAME ALONE (no frame switching needed): corners $(1/3,1/3)$,
$(0.4,0.4)$, $(1/3,1/2)$, $(1/2,1/3)$, $(1/2,1/2)$, fine $17\times17$ band
grid, stress runs at parameter-grid resolution 24 — 0 violations. The
p-frame also passes everywhere (symmetric machinery; reassuring
redundancy, and it is the natural fallback if a write-up detail breaks in
one frame).

ADVERSARIAL HISTORY (each failure was a real mathematical gap, each fix a
structural lemma, not a tuning knob):
1. v1–v2 (naive shells): fail at corner by $x^{1/3}$ — missing any cap.
2. v3 (+quadruple cap $m\bar K\bar h$): corner fails by $x^{1/6}$ —
   harmonic-AP sum over admissible $J$ was overcounted; fixed by the
   $1/(\bar sg_1)$ congruence density (JA).
3. v5 passes — but a HAND-CHECK of the J0 derivation found a missing
   $\mu$-rich piece $m^2WL^{B+2}/\bar N$, which genuinely FAILS at the
   corner at $\bar s=1$ (the diagonal $p=q$ of §3.3).
4. A Fourier pair-cancellation cap was tried and passed the scanner —
   then MODEL-SCALE NUMERICS (§5(3)) disproved it: the sawtooth jump
   between the paired endpoints does not cancel. Retracted.
5. The honest fix: the $g\le2\bar s/h''$ truncation inside J0 gives
   $\min(\cdot,\ m\bar s)$ — passes, no pairing.
6. A units audit then found J2 had been encoded a factor $\bar h$ too
   small; the corrected $\mathrm{J2}=\max(\bar\sigma,W)\bar N$ broke the
   whole lower-left band (excess up to $x^{1/9}$, binding at small $m$,
   $\bar h\approx Q$, bottom shell) — REAL obstruction: per-$(\mu,k)$
   $h$-multiplicity at deep shells.
7. THE RESOLUTION: convergent collapse (§3.1). At deep shells the
   resonant $h$ of a fixed $c$ are multiples of CF denominators; passing
   to convergents makes the per-cell multiplicity $O(1)$ — CAP becomes
   $m\bar K$, $\bar s$-free. Full pass.
8. ABLATIONS: dropping Lemma G — still passes (G not needed); dropping
   Lemma R — fails near the lower-left diagonal ($(1/3,1/3)$, $(0.36,
   0.36)$, $u\approx u'$ strip): Lemma R is the unique non-formal input.

Corner roles: $(1/2,1/3)$: trivial counting suffices ($5u+u'\ge2$ with
room; the $\mu Q/P$ piece is small there anyway). $(1/3,1/2)$ and
$(0.4,0.4)$: A+J0+CAPC clear them. $(1/3,1/3)$: everything is needed —
the $L^{-B}$ from $M_0$, the quantization (F3), the J0 truncation, Lemma
R, and the convergent cap; margins degenerate to pure polylog there, and
the scanner's $(x^f,L^{tB})$ bookkeeping confirms the polylog ledger
closes with $B$ free.

## 5. Numerics (.venv/bin/python; scripts: `e1_exponents.py` kept in repo,
model probe summarized)

(1) EXACT DECOMPOSITION CHECK (model $x=10^{10}$, $u=u'=1/3.3$, $P=Q=1072$,
$L^B=30$, $\lambda=2$, 300 random $(q,\mu)$): the moving-interval identity
$N_q=\sum_k\#([c_-q,c_+q]\cap(P,2P]\cap\mathbb Z)$ — 0 mismatches against
direct counting. The decomposition in §2 is exactly right.

(2) RESONANCE IDENTITY (2000 random $(\mu,k,h,\pm)$): max relative error
$8.6\times10^{-9}$ (floating point) for
$|J\mp\sigma|=\|hc\|\cdot|2\lambda n+th+\lambda y|$. Exact as claimed.

(3) JUMP/DIAGONAL CHECK: at $\mu=M_0$, $k=\mu-\lambda$ (slope $c\approx1$):
$|\sum_q\psi(c_\pm q)|=535.7\approx Q/2$ each, paired sum $=1071\approx Q$
— pair-cancellation FALSE (this retracted step 4 of §4), diagonal
contribution real and $=QM_0\le QPL^{-B}$: inside budget, and the J0 count
($\le m\bar sL^2$ at $\bar s=1$) covers it with an $L^2$ to spare.

(4) EXPONENT SCAN: `e1_exponents.py` final version — full pass, both
frames, closed band; see §4. (Earlier signed-average numerics for E1
itself: `wp24-e1-e2-fineclass.md` table — signed averages 1–4% of the main
term at model scale; consistent.)

## 6. Obstructions encountered (all resolved or routed around)

1. The documented FATAL route (Selberg per $(\mu,h)$ + SL1 prime sums in
   $q$; coefficient mass $\log H$ per $\mu$ costs a factor $R$) — not
   retried, per instructions. The present route aggregates over $\mu$ and
   the Fourier index BEFORE any cancellation and needs no prime sums at
   all.
2. Required saving at $(1/3,1/3)$ is a full power $x^{1/3}$ over the
   trivial endpoint count — supplied by the conic lattice count, never by
   per-pair equidistribution.
3. Per-$(\mu,k)$ deep-shell $h$-multiplicity (step 6–7 of §4) — resolved
   by the convergent collapse; this is the E1-analogue of WP8-E2's witness
   truncation discovery, and the half-window shift $\sigma$ (F3) is the
   E1-analogue of E2's $\|s\alpha\|\ge1/p$ truncation.
4. The sawtooth jump at near-integer slopes (diagonal $p=q$) — genuinely
   at budget edge $QM_0=QPL^{-B}$; absorbed by the corrected J0 count.
   Any future tightening of E1's statement below $PL^{1-B}$ would be FALSE
   at the corner because of this diagonal — the hypothesis as stated is
   sharp there.
5. Lemma R's per-individual-modulus factor $4^{\omega(s)}\tau(s)$ is
   $x^{o(1)}$, not $L^{O(1)}$ — only the $s$-average is polylog;
   the counting must (and does) always close with the $s$-sum inside.
6. The $\lambda$-boundary and clip pieces degenerate at the closed-band
   corners $(1/3,1/3)$ resp. $(1/2,1/3)$ exactly where $x^{1-u-2u'}$ resp.
   $x^{2u-3u'}$ hit $1$; both are saved by the $L^{-B}$ carried by $M_0$
   (§2.1) — rem:E1-signed's accounting is correct as stated.

## 7. Verdict

**PROVED-MODULO-[write-up]** of Hypothesis E1 in the form actually
consumed downstream (rem:E1-signed / prop:familyA): the integer-relaxed,
signed (indeed absolute-value) bound E1$^\flat$ of §1.2 with
$PL^{A-B}$, $A$ absolute — sufficient for prop:familyA and
prop:digit-assembly after the harmless re-choice $B\to B+A+2$ (B is free).
The proof is ELEMENTARY throughout: moving-interval decomposition (§2,
exact), classical CF/Ostrowski psi-sum collapse (§3.1), the exact conic
resonance identity with the $\delta_\mu$-shift quantization (§3.2, F3),
and a fully itemized lattice-point count near the conic (§3.4) whose
exponent ledger is machine-verified on the closed band including all
degenerate corners (§4). No exponential sums over primes, no Gauss sums,
no SL1: the prime aspect of E1 was never needed (already integer-$p$ in
lem:branch; $q$ relaxed to integers at cost $L$, §1.2).

Named inputs owed for a manuscript-grade write-up:
(i) the CF/Ostrowski lemma in the stated interval form (citable /
half-page); (ii) Lemma R with the squarefull/$p=2$/$\lambda$-gcd cases
(one page, sketch in §3.4); (iii) prose expansion of the count
derivations A, J0, JA/JB, J2, SING, B2, CAPC (each is a short argument,
all recorded above); (iv) constants discipline in the §3 preamble and §3.2 ($m_0$
sharpening, two-sided resonance constants).

Confidence: **moderate-high (~0.7)** for "the route as recorded closes
E1 with B free". Basis: exponent ledger machine-verified at
$(x^f,L^{tB})$-resolution over the closed band with adversarial
parameter grids; the exact identities numerically verified; three real
errors found and fixed by independent methods (hand-audit, numerics,
units audit) — the system survived all of them. Residual risk:
(a) an unencoded count regime (the term zoo is hand-derived; though each
term was re-derived at least twice, a forgotten case class would not be
caught by the scanner); (b) the dyadic/constant bookkeeping in the
convergent collapse; (c) Lemma R edge cases. None of these is of the
fatal-structural kind that killed the prior attempt; all are
write-up-grade risks.

Suggested next steps: (1) write §12-replacement LaTeX for E1 along §§1–4;
(2) independent re-derivation of the J0 and JB counts (the two that
failed once); (3) port the WP8-E2 numerical harness to test E1$^\flat$
end-to-end at $x=10^9$–$10^{10}$ on the $(u\approx u')$ strip where
Lemma R binds.
