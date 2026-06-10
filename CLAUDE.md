# Erdős 396 program: $n(n-1)\mid\binom{2n}{n}$

Research program proving infinitude/log-density $c_1^2$ of $W_1=\{n: n(n-1)\mid\binom{2n}{n}\}$ (rung $k=1$ of Erdős problem 396). Pure math + numerical verification scripts; no build system. State as of June 9, 2026.

## Conventions

- One document per lemma/work-package; **strategy, sequencing, and risk live in `roadmap.md`** — start there.
- Every doc opens with a bold **STATUS** line; keep it current.
- Sources and citation verification statuses live in `citations.md` (PINNED / PARTIAL / TO-PIN).
- Dead ends are recorded with proofs of death (roadmap §Dead-ends, lemma-D §8) — do not re-attempt them.
- Any derivation must be written to a file immediately; chat sessions are not durable storage.
- `program-state.md` is a generated single-file bundle of everything, for upload to Claude project knowledge. **Regenerate it after sessions that change state** (concatenate all docs + scripts in its table-of-contents order); never edit it directly.

## Document map

| File | What it is |
|---|---|
| `roadmap.md` | Strategy, work packages WP1–WP5, decision tree, calibration, next actions |
| `citations.md` | Citation ledger with verification statuses |
| `lemma-0-sandwich.md` | Exact governor sandwich $D_0\cap(D_0^{(+)}{+}1)\subseteq W_1\subseteq\dots$ — PROVED |
| `lemma-A-small-primes.md` | Small primes ignorable — KNOWN-ADAPT (FK §2 + one line) |
| `lemma-B-anatomy-independence.md` | Anatomy independence of $n,n{-}1$ — cite Tao–Teräväinen Thm 3.1; 3 checks pending |
| `lemma-C-within-side.md` | Within-side digit equidistribution vs multiplicative weights — OPEN |
| `lemma-D-cross-side.md` | Cross-side digit independence — THE HARD CORE; gate G1 passed |
| `prop-deep-large-sieve.md` | Deep large sieve for Fermat-quotient characters — PROVED |
| `numerology-D.md` | WP1.4 exponent bookkeeping for Estimate D\* (+ Erratum §9) |
| `empirics-D.md` | WP1.5 band empirics: square-root cancellation on real populations — G1 PASS |
| `lemma-alpha-beta.md` | WP2.0: lemmas $\alpha,\beta$ proved; assembly NEGATIVE; defines Estimate D† |
| `wp21-reduction.md` | WP2.1: D† digit layer → two-frequency minor/major-arc dichotomy |
| `wp22-minor-major.md` | WP2.2: D†-minor lemma + both major-arc families counted out |
| `wp23-anatomy.md` | WP2.3: anatomy layer unwinds elementarily ($u_f<2$) — PASS |
| `verify_dls.py` | Numerical verification of the deep large sieve (identities, fiber/energy/RMS) |
| `wp21_test.py` | Model test of the WP2.1 two-frequency reduction |

## Scripts

Python 3 with `numpy` and `sympy`; run directly (`python3 verify_dls.py`). `empirics_d.py` (WP1.5) is referenced but not yet recovered into the repo.

## Where work happens next (roadmap §Immediate next actions)

Consolidation sprint WP4 (write up the closed-modulo-write-up pile), TT Thm 3.1 verification (WP3b), then the fine-anatomy-class check and the two equidistribution rigorizations on Lemma D.
