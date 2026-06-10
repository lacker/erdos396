# Erdős Problem 396 — Tier B findings

**Problem.** Is it true that for every $k$ there exists $n$ with
$\prod_{0\le i\le k}(n-i)\mid\binom{2n}{n}$?

**Reformulation used throughout (Kummer).**
$$v_p\!\binom{2n}{n}=\#\{\,j\ge 1: 2(n\bmod p^j)\ge p^j\,\},$$
so divisibility holds iff for every prime $p$,
$\sum_{i=0}^{k} v_p(n-i)\le v_p\binom{2n}{n}$. All scans use only digit
arithmetic — no big binomials.

## 0. Tooling validated (two independent ways)

- `carries()` agrees with the Legendre digit-sum formula on 20,000 random
  $(n,p)$ with $n<10^9$.
- Full checker `check()` agrees with big-integer `math.comb` brute force for
  all $n\le1200$, $k\le6$.
- Reproduces **all seven** published OEIS A375077 witnesses
  $(k\mapsto n)$: $1\!\to\!2,\ 2\!\to\!2480,\ 3\!\to\!8178,\ 4\!\to\!45153,\
  5\!\to\!3648841,\ 6\!\to\!7979090,\ 7\!\to\!101130029$, with no smaller $n$ in
  $[n-50,n)$ passing.

## 1. Witness density is *stable in magnitude* for each fixed k

Sampled witness density $\Pr[\,\prod(n-i)\mid\binom{2n}{n}\,]$:

| k | n ~ 10^4 | n ~ 10^5 | n ~ 10^6 |
|---|----------|----------|----------|
| 1 | 0.01010  | 0.01125  | 0.01240  |
| 2 | 0.00088  | 0.00123  | 0.00143  |
| 3 | 0.00010  | 0.00005  | 0.00010  |

Exact counts up to $X=200{,}000$: $k=1$ gives 2187 witnesses, $k=2$ gives 212,
$k=3$ gives 18.

**Read.** For fixed $k$ the density does **not** decay with magnitude (it is flat
or mildly increasing). This is positive numerical evidence for the much stronger
statement that witnesses have **positive lower density for each fixed $k$** —
well beyond the "infinitely many" the problem asks. The decay is *in $k$*, not in
$n$, consistent with a per-prime independence heuristic (each added factor
imposes more carry constraints).

## 2. There are two independent hurdles, not one

Let (S) = "the window $n,\dots,n-k$ is $\sqrt{2n}$-smooth" and (C) = full
divisibility (our checker).

| k | $\sqrt{2n}$-smooth windows $\le X$ | witnesses $\le X$ | $\Pr[C\mid S]$ | $\Pr[S\mid C]$ |
|---|---|---|---|---|
| 1 ($X{=}10^5$) | 9385 | 1029 | 0.110 | **1.000** |
| 2 ($X{=}2\!\cdot\!10^5$) | 5147 | 212 | 0.041 | **1.000** |
| 3 ($X{=}3\!\cdot\!10^5$) | 1981 | 32 | 0.016 | **1.000** |

**Read.**
- **Necessity of smoothness is exact**: every witness is $\sqrt{2n}$-smooth
  ($\Pr[S\mid C]=1$ in all ranges). Proof: a prime $p>\sqrt{2n}$ dividing some
  $n-i$ has $p^2>2n$, so its only base-$p$ carry slot is the units digit, which
  is $i<p/2$ ⇒ no carry ⇒ $p\nmid\binom{2n}{n}$. This is now a clean lemma for
  Tier A.
- **Smoothness is far from sufficient** and gets worse with $k$: only 11% → 4% →
  1.6% of smooth windows are witnesses. So a construction that only produces
  smooth windows is **not enough**; the carry/exponent conditions are the real
  obstruction.

## 3. The residual obstruction is "medium primes," one carry slot each

Restricting to smooth-but-failing $n$, the dominant failing prime moves into the
band $p\in\big((2n)^{1/3},(2n)^{1/2}\big]$ (it cannot be larger, by smoothness):

| k | dominant prime $<(2n)^{1/3}$ | in $\big((2n)^{1/3},(2n)^{1/2}\big]$ |
|---|---|---|
| 1 | 2975 | 5381 |
| 2 | 1533 | 3402 |
| 3 | 609  | 1340 |

Such a prime has $p^2\le 2n<p^3$, so it gets **exactly one** carry slot above the
units digit. With $p\| (n-i)$ it needs that one slot to fire, i.e. the second
base-$p$ digit of $n$ must be $\ge p/2$ — an essentially independent ~½ event
per medium prime. "Single medium prime, exponent 1, deficit 1" accounts for
23% / 11% / 6% of smooth-window failures at $k=1,2,3$; the rest are several such
primes failing together.

**This is the quantity a proof must control.** It behaves like a product of
near-independent coin flips over the medium primes dividing the window — exactly
the structure in Pomerance's density model for $n^\ell\mid\binom{2n}{n}$.

## 4. The $n=m^2$ construction (Tier C item 8): partial, and instructive

For $m\in[2,2000)$: $n=m^2$ windows are $\sqrt{2n}$-smooth 99.9% of the time
(only $m=2$ fails), because $n=m^2$ has $P(n)\le m\le\sqrt n$ and
$n-1=(m-1)(m+1)$ splits into two $\approx\sqrt n$ pieces. **But** the witness
rate among squares is 0.85% — *below* the global ~1.1%.

**Read (a useful negative result).** The square family solves hurdle 1
(smoothness) essentially for free but does **nothing** for hurdle 2 (carries),
and the slight suppression suggests $m^2$'s base-$p$ digits are, if anything,
mildly anti-correlated with carrying. Conclusion: *do not* base a construction on
"force smoothness." Tier D should instead aim to control the medium-prime carry
digits directly (e.g. pick $n$ in residue classes mod a product of medium primes
that force their second digit $\ge p/2$), while smoothness is obtained as a
by-product.

## Implications for the plan

1. **Tier A lemma confirmed and provable**: witness ⇒ $\sqrt{2n}$-smooth window.
   Promote to a stated lemma.
2. **Target restated**: not "produce smooth windows" but "produce smooth windows
   whose medium primes ($p\in((2n)^{1/3},\sqrt{2n}]$) each have second base-$p$
   digit $\ge p/2$." This is a CRT-style condition on $n$ modulo those primes.
3. **Positive-density conjecture is well-supported** for each fixed $k$ (Section
   1), so the right theorem to chase is "positive lower density," conditional on
   a smooth-window-in-residue-class input — which is the Balog–Wooley regime
   (Tier D item 9).
4. The $n=m^2$ seed is **deprioritized** as a standalone construction (Section 4).

## Reproducibility

Scripts in this folder: `divcheck.py` (core + self-tests), `validate_oeis.py`,
`tierb_scan.py`, `smooth_test.py`, `carry_hurdle.py`, `square_family.py`,
`decay.py`. All run under a few minutes single-threaded.

