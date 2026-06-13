# WP15: The Ten-Idea Brainstorm (June 12) — full list with outcomes

Origin: with the missing estimate framed (pre-erratum-7) as a research-grade
sign-sensitive divisor correlation, ten ideas were generated, each chosen to
violate an assumption the floor theorems actually used. Status after the round:

| # | Idea | Status | Outcome / report |
|---|------|--------|------------------|
| 1+2 | Dirichlet-kernel phase lever + R-averaging | EXECUTED — FAILS (structural: completion×sweep ≡ 1; kill region empty) | `wp15-phaselever.md`. Deliverable: **weights may be taken nonnegative** |
| 3 | (M2*)-pruned coincidence graph (CF structure) | EXECUTED — FAILS (p cancels exactly from the alignment real; mass is the lattice mean) | `wp15-cfprune.md`. Deliverable: **D3 localization** (one positivity step, Kloosterman species) |
| 4 | Cell-shopping | EXECUTED — WALL-CELL-INDEPENDENT (proved) | `wp15-cellshop.md`. Side-catch: η=0.05 cell absorption-invalid at constant level |
| 5 | Bandlimited Selberg majorants (support-needs not sign-needs) | NOT EXECUTED — partially mooted: phaselever showed the Vaaler layer already saturates the mollification scale; the nonneg-weights finding removes the premise | re-rank: LOW |
| 6 | δ-method / Ramanujan redistribution of the divisor condition | NOT EXECUTED | post-erratum-7 re-rank: LOW (the harmonic decomposition itself was the artifact; δ-method digs deeper into harmonics) |
| 7 | Gallagher larger sieve on the Wieferich dual | EXECUTED (retargeted at D3) — FAILS (3 kills) | `wp15-largersieve.md`. Deliverable: **D3-INEQ\*** — the input is an EVALUATION with negative main term (numerics 0.97–1.01), not a bound |
| 8 | Fourth moment | EXECUTED — NEUTRAL (wall moment-invariant; 4-linked class CRT-collapses) | `wp15-moment4.md` |
| 9 | Representation-function reformulation (signs in r±(n)) | NOT EXECUTED | post-erratum-7 re-rank: LOW-MEDIUM (the physical chain bypasses the harmonic object r± lives in) |
| 10 | Function-field model | EXECUTED — split verdict + **the audit flag that became ERRATUM 7** | `wp15-ffmodel.md`, confirmed by `wp15-verify-audit.md` |

Honorable mentions (never executed): Hecke/level-aspect spectral accounting;
sum-product/additive-energy on the coincidence graph. Both re-ranked LOW
post-erratum-7 (they attack the harmonic object).

## Net outcome of the round

The wall was a **harmonic-decomposition artifact** (erratum 7, favorable,
verified): the physical chain (P1)–(P3) gives E|D±|² ≤ C′(R+1)²L
unconditionally; the open problem is now a polylog refinement (factor
L^{3+a}). See THE-OPEN-PROBLEM.md Addendum 2. The executed ideas' deliverables
(nonneg weights, D3 localization, D3-INEQ* evaluation framing) remain valid
and useful: they characterize what the polylog refinement must respect.

## Rescued probes

`probes/` holds scripts referenced by committed reports but formerly living
only in /tmp: baker_bridge.py (wp11 §2.0 range table), sum_branch_probe.py
(wp9-verify-e1e2), wp11_step4.py, wp11_iib.py (wp11 §§2,3 pricing).
