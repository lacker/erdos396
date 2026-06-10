# Erdős Problem 396 — Tier A: the heuristic density model

**Goal.** Build a probabilistic model for the witness density
$D(k;X)=\Pr_{n\sim X}\big[\prod_{i=0}^{k}(n-i)\mid\binom{2n}{n}\big]$, compare
it to exact empirical data, and extract what a proof must control. Every
per-prime marginal is computed by Monte Carlo **against the true distribution
of $n$**, so each model's error isolates exactly one structural assumption.

## 1. The model ladder and what each rung tests

| rung | what is modeled | what is real | tests |
|---|---|---|---|
| v1 | product of per-prime marginals | each marginal | cross-prime independence |
| v2 | $k{+}1$ **iid** random integers, real joint factorizations, simulated carry digits | within-element factor structure | independence *across* elements |
| v2b | real **consecutive** windows, simulated digits | window factorizations | digit model |
| v0 | everything (exact empirical, sampled, $3\times10^5$ per range; verified checker) | — | — |

The carry digits may legitimately be simulated independently across primes
(CRT: for $n$ uniform over a long range, $n\bmod p^a$ and $n\bmod q^b$ are
independent), with the exact boundary effects (the guaranteed carry when
$n<p^{j}\le 2n$) built in — this is what makes v2's "factor structure +
fresh digit randomness" a faithful surrogate.

## 2. Headline: cross-prime independence fails by ~6×, for an identifiable reason

At $k=1$, $n\sim10^6$: v1 = 0.0801 vs empirical 0.0130. Attribution:

| step | value | factor | interpretation |
|---|---|---|---|
| v1 | 0.0801 | — | full independence |
| v2 | 0.0220 | **÷3.6** | **within-element cross-prime correlation** |
| v2b | 0.0194 | ÷1.14 | consecutive-window factorization correlation |
| v0 (empirical) | 0.0130 | ÷1.49 | small×medium correlation (÷1.26) + digit-sim boundary error (÷1.18) |

The dominant effect (÷3.6) is **log-mass conservation**: conditioned on an
element being $\sqrt{2n}$-smooth, the $\log n$ of multiplicative mass that
would typically sit in one large prime is redistributed into the medium range
$\big((2n)^{1/3},(2n)^{1/2}\big]$ — multiplying the number of one-slot carry
"coin flips" precisely on the windows that already paid for smoothness.
Failures cluster where success was otherwise likely; the independence product
misses this entirely.

The small×medium component is measured directly: unconditionally
$P(\text{small primes pass})=0.8575$ (and the model's $F_{\text{small}}=0.8576$
— marginals are exact), but conditioned on the medium/large conditions passing
it drops to $0.6806$ at $n\sim10^6$. Same mechanism, second instance.

**Modeling consequence.** The correct rigorous surrogate is the
Billingsley/Poisson–Dirichlet description of an integer's factorization — the
same object behind Pomerance's density formula for $n^\ell\mid\binom{2n}{n}$
(his $g_j$ process). v2 *is* an empirical PD sampler; a Tier-D analytic version
should model each window element by PD(1) jointly across all its prime sizes,
and only assume independence across the $k{+}1$ elements (empirical cost of
that residual assumption: ×1.14).

## 3. Scale behavior: densities increase toward a positive limit

Exact sampled densities (new $10^9$ point via vectorized trial division):

| k | $n\sim10^4$ | $10^5$ | $10^6$ | $10^9$ | extrapolated $\delta_k$ ($1/\log$ fit) |
|---|---|---|---|---|---|
| 1 | 0.01002 | 0.01156 | 0.01303 | 0.01412 | ≈ 0.017 |
| 2 | 0.00064 | 0.00112 | 0.00136 | 0.00176 | ≈ 0.0026 |
| 3 | 0.000037 | 0.000113 | 0.000113 | — | ≈ 0.0002 |

Monotone increasing in magnitude at every $k$, with shrinking increments
consistent with $D = \delta_k(1 - c_k/\log n + \cdots)$, $\delta_k>0$. Two
structural reasons, both now verified:

- **Scale invariance of the hard part.** Group medium primes into bands
  $L$ = number of base-$p$ digits of $2n$ ($p\in((2n)^{1/(L+1)},(2n)^{1/L}]$).
  The v1 budget table shows each band's $-\log$ contribution is a function of
  exponent *ratios* only (Mertens: $\sum_{\text{band}}1/p=\log\frac{L+1}{L}$),
  independent of magnitude. The carry difficulty does not grow with $n$.
- **The easy parts improve with $n$**: more digit positions per small prime
  ($P_{\text{small}}$: 0.67 → 0.86 → 0.96 across $10^4\to10^6\to10^9$) and the
  small×medium correlation washes out ($P(\text{small}\mid\text{med})$:
  0.29 → 0.68 → 0.92). Asymptotically $D\approx P_{\text{med}}$: **the
  problem reduces, in the limit, to smoothness + medium-prime carries only.**

Per-factor decay: $D(k{+}1)/D(k)\approx 0.06$–$0.13$ (mildly increasing with
scale), i.e. $\delta_k\approx \delta_1\cdot(0.1)^{k-1}$ roughly. Each added
factor costs about one decade of density — *but never zero*.

## 4. Validation against OEIS first witnesses (out-of-sample)

If witnesses behave like density-$D$ random hits, the least witness should
appear near $n(k)\sim 1/D(k)$. Using only the measured $D(1)$ and ratio
$r=0.10$:

| k | predicted $n(k)$ | OEIS A375077 | ratio |
|---|---|---|---|
| 2 | 1.0e3 | 2.5e3 | 0.40 |
| 3 | 1.0e4 | 8.2e3 | 1.22 |
| 4 | 8.6e4 | 4.5e4 | 1.91 |
| 5 | 7.7e5 | 3.6e6 | 0.21 |
| 6 | 7.7e6 | 8.0e6 | 0.96 |
| 7 | 7.1e7 | 1.0e8 | 0.70 |
| **8** | **~7e8** | *unknown* | **prediction** |
| **9** | **~7e9** | *unknown* | **prediction** |

Agreement within a factor of 5 across four orders of magnitude, with no fitting
to the witness data. Falsifiable predictions for the next OEIS terms included.

## 5. Implications for the proof program (updates to Tiers C/D)

1. **Positivity is robust.** All identified correlations are bounded $O(1)$
   multiplicative corrections (total ×6 at $k{=}1$, structure-explained), not
   decay-rate changes. A proof does not need exact constants — upper-bounding
   the correlation cost suffices for positive density.
2. **Asymptotic simplification (new).** Since $P(\text{small}\mid\text{med})\to1$,
   a positive-density proof may ignore primes $\le 31$ at the cost of $o(1)$:
   the analytic core is **only** (a) the window is $\sqrt{2n}$-smooth and
   (b) each medium prime power $p^e\,\|\,(n-i)$ collects $e$ carries among its
   $\lfloor\log_p 2n\rfloor - e$ free digit positions.
3. **The honest hard core.** Even ingredient (a) alone — positive density of
   $k{+}1$ consecutive $\sqrt{2n}$-smooth integers — is not known
   unconditionally (literature check needed to confirm current state; strings
   of consecutive smooth numbers are known to be infinite via Balog–Wooley-type
   constructions, which is weaker). Empirically the consecutiveness correlation
   costs only ×1.14, so a hypothesis of "bounded smooth-window correlation" is
   mild. Two routes, as restructured:
   - **R1 (existence, what 396 literally asks):** explicit families with
     congruence control on medium primes; Balog–Wooley parameters + CRT.
     Digit conditions are residue conditions on $n$ mod medium prime squares.
   - **R2 (positive density, conditional):** Pomerance's PD machinery extended
     from one shifted factor to the window, assuming the smooth-correlation
     hypothesis. The v2 model is the exact blueprint of the quantity to compute.
4. **Numerical targets.** $\delta_1\approx0.017$, $\delta_2\approx0.0026$;
   first witness for $k=8$ predicted near $7\times10^8$ (a C-speed scan with
   the smoothness prefilter could find it and extend A375077 — optional Tier B
   follow-up).

## 6. Consistency checks performed

- Model marginal $F_{\text{small}}=0.8576$ vs empirical $P_{\text{small}}=0.8575$
  (independent code paths).
- Vectorized $v_p$/carries vs verified scalar implementations (spot-checked).
- Empirical densities at $10^6$ reproduce Tier B's independent scan
  (0.0130 vs 0.0124, separate RNG and method).
- $10^9$ measurement uses a third factorization method (vectorized trial
  division + big-prime cofactor logic).

## Files

`heuristic.py` (v1 model + band budgets), `model_v2.py` (v2/v2b ladder),
`empirical_decomp.py` (exact sampled densities with small/medium split),
`extend_scale.py` ($10^9$ measurement), `model_densities.json`,
`model_v2.json`, `empirical_decomp.json`, `empirical_1e9.json`.

