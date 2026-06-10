# Archive — recovered session artifacts (historical record)

Recovered June 9, 2026 from the claude.ai data export (`data-…-batch-0000.zip`), by replaying the
`create_file` / `str_replace` / heredoc tool calls in the exported conversations. These are the
artifacts the roadmap's WP4 lists as "lost" — they were destroyed when the original session's
sandbox died, but the export preserved the tool inputs that created them.

**⚠️ Historical, partially superseded.** The live per-lemma documents in the repo root are the
canonical state. In particular, anything here predating the WP2.0 erratum (the withdrawn
"covered modulo α,β,γ" claim in `numerology-D.md` §9) reflects the *older, inflated* accounting.
Use these for provenance, recovered derivations, and the WP4 write-ups — not as current status.

## original-session/ — "Selecting an Erdős problem for AI-assisted decomposition" (June 9, ~12:51 PDT)

The original session: problem selection (Erdős 396 chosen from a shortlist of ten), Tier-B/Tier-A
empirical feasibility scans, literature survey, the k=1 proof skeleton, and the Pilatte/TT reading
session. Died at the context cutoff mid-way through fetching Tao–Teräväinen Theorem 3.1.

| File | What it is |
|---|---|
| `TIER_B_REPORT.md` | First empirical scan (witness counts, smoothness hurdle, the m² family) |
| `TIER_A_REPORT.md` | Heuristic density model for general k; exact-scan validation |
| `LITERATURE_REPORT.md` | Survey: Pomerance, Ford–Konyagin, Balog–Wooley, Hildebrand, TT |
| `K1_SKELETON.md` | **The original k=1 proof skeleton** (Theorem 1/1′/1″, Lemmas 0/A/B/C/D) — WP4 lost artifact #1 |
| `SKELETON_TESTS_ADDENDUM.md` | Numerical stress-tests of the skeleton's lemmas |
| `HYPOTHESES_CHECK.md` | **The Pilatte/TT reading-session verdict** — WP4 lost artifact #2 |
| `*.py` (17 scripts) | The tests behind the above (Lemma 0 sandwich check = `lemma0_test.py`, etc.) |

## recovery-session/ — "Accessing previous chat history in projects" (June 9, ~16:34 PDT)

| File | What it is |
|---|---|
| `roadmap-v0.3.md` | The single-file v0.3 roadmap reconstructed before the per-lemma refactor (superseded by `roadmap.md` v0.4) |

All other recovery-session outputs are the live repo docs themselves (they came over via
`program-state.md`), plus `empirics_d.py`, restored to the repo root.

## transcripts/ — full conversation transcripts

Complete dumps (user/assistant text, thinking blocks, every tool call and result) of both
sessions. This is the durable backup of the derivations that the roadmap's method note worries
about; grep here before re-deriving anything that feels missing.
