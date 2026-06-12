# Erdős 396 program: $n(n-1)\mid\binom{2n}{n}$

Research program proving infinitude/log-density $c_1^2$ of $W_1=\{n: n(n-1)\mid\binom{2n}{n}\}$ (rung $k=1$ of Erdős problem 396). Pure math + numerical verification scripts; no build system. State as of June 9, 2026.

## Conventions

- One document per lemma/work-package; **strategy, sequencing, and risk live in `roadmap.md`** — start there.
- Every doc opens with a bold **STATUS** line; keep it current.
- Sources and citation verification statuses live in `citations.md` (PINNED / PARTIAL / TO-PIN).
- Dead ends are recorded with proofs of death (roadmap §Dead-ends, lemma-D §8) — do not re-attempt them.
- Any derivation must be written to a file immediately; chat sessions are not durable storage.
- `program-state.md` is a generated single-file bundle (`python3 make_bundle.py`), **retired as of June 10, 2026**: the claude.ai phone-side mirror is no longer used (the user drives this repo from anywhere via Claude Code remote control). Kept as an archival snapshot; regenerate only if a single-file export is needed. Never edit it directly.

## Glossary (plain-language decoder for the accreted names)

| Code | Meaning |
|---|---|
| Lemmas A/B/C/D | The four pieces of the k=1 proof, lettered in order; D = the hard core |
| D\* → D† | The key estimate in D; † = the corrected version after erratum 1 |
| C† | Lemma C's hard kernel, named by analogy with D† (same species of object) |
| -lb | "lower bound" — the weakened form sufficing for Theorem 1′ |
| Theorem 1′ / 1″ | Infinitude+positive density / exact density $c_1^2$, both for k=1 |
| E1, E2, E3 | Equidistribution hypotheses, numbered by discovery. E1, E2: closed. E3-lb = **the rough-cofactor count** (needs a bespoke dispersion estimate) |
| C†-lb | **The weighted coin-flip estimate** (untouched; difficulty unknown) |
| wpN-\*.md | Work-package reports; DRAFT = unverified agent output, trusted only after a wp-verify pass |

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
| `empirics_d.py` | WP1.5 band-empirics probe ($T_q(\lambda)$ on real populations, 5 strata; ~minutes at $x=10^8$) |
| `manuscript/` | **The WP4 manuscript spine** — LaTeX, full proofs of everything proved, status tags on every statement, remaining-gaps ledger in §10. Build: `tectonic main.tex` (installed via brew). Keep it in sync with the per-lemma docs |
| `wp8-*.md` … `wp12-*.md` | **The hypothesis-attack era** (June 10–11): prover/verifier/audit reports per work package. Always read the matching `wp*-verify-*.md` before trusting a claim; `wp9-theorem1prime.md` = the Theorem 1′ chain; `wp11-e3lb.md` = the E3-lb ladder log (see its STATUS header); `wp12-cdagger-lb-diagnosis.md` = the other brick. Current frontier: Kuznetsov/DI bridge (roadmap WP12b) |
| `THE-OPEN-PROBLEM.md` | **The program's capstone**: self-contained statement of the one missing estimate (number-theorist-ready) |
| `literature-dependencies.md` | The audited table: every external theorem the conditional theorem consumes, with verification grades |
| `archive/` | Recovered session artifacts + full transcripts — historical; see `archive/README.md` |

## Scripts

Python 3 with `numpy` and `sympy`, installed in the repo venv: run with `.venv/bin/python verify_dls.py`. All identities verified passing on this machine (June 9, 2026).

## History

The program was built in two claude.ai sessions on June 9, 2026 (problem selection → k=1 skeleton → Lemma D de-risk → WP2.0–2.3), then migrated here. The original session's artifacts and both full transcripts are preserved under `archive/` — grep there before re-deriving anything. Docs predating the WP2.0 erratum carry inflated coverage claims; the repo-root docs are canonical.

## Where work happens next (roadmap §Immediate next actions)

Consolidation sprint WP4 (write up the closed-modulo-write-up pile), TT Thm 3.1 verification (WP3b), then the fine-anatomy-class check and the two equidistribution rigorizations on Lemma D.
