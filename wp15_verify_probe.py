"""WP15-VERIFY probe: scaling test of the physical Hoelder chain (P1)-(P3)
vs the harmonic-chain mass, at growing model x.

Conventions = wp11_w4_probe / wp15_largersieve_probe: Q = P = round(x^0.425),
R = round(x^0.15), A = round(x^0.575), blocks (Q,2Q] (lam=0.425) and (A/2,A]
(lam~0.575, where the power-deficit x^{2lam-0.425-0.3} is largest).

Measured per scale/block (sharp window; Vaaler layer = analytic overhead L):
  ED2   = E_{p,q} |D_Lambda|^2,  D = N_win - (R+1) Sum 1/ell   (the W1 object)
  m1    = E_{p,q} N_win          ((P2) window first moment; claim <= C(R+1))
  mV    = E_{p,q} Sum_ell min(1,((R+1)/d)^2)  (Vaaler-tail proxy; (P2) tail claim)
  s1    = max_{p,q} N_win        ((P1); proved <= R+1 pointwise)
  sV    = max_{p,q} tail proxy   (pointwise tail; record allows ~ (R+1)L/c_V-grade)
  band[j] = E_{p,q} #{ell : nu_ell in band j}/(R+1)  (claim: O(1), j-UNIFORM)
  chain = (s1 + sV + drift) * (m1 + mV + drift)  (empirical Hoelder product (P3))
  harm  = (4.1 N_ell)^2 / q     (harmonic coincidence-mass grade x^{2lam-0.425})
  refs  : R^2 L (claimed grade of (P*)), budget 0.05 R^2/L^3 (delta_0 = 1/L)

DISCRIMINATOR: slopes vs log x. If (P*) is true and the deficit was a harmonic
artifact: ED2 and chain scale like x^{0.3+o(1)} or below at BOTH blocks, while
harm scales like x^{2lam-0.425} (x^{0.425} at lam=0.425, x^{0.725} at top): the
chain/harm ratio must FALL as a power at the top block. If instead the wall were
physical, ED2 would track harm.
"""
import math
import time

import numpy as np


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i:: i] = False
    return np.nonzero(s)[0]


JMAX = 8


def run_block(ells, ps, qs, q_arr_inv_cache, R, drift_const):
    """Returns aggregated stats over (p,q) for one block."""
    ED2 = m1 = mV = 0.0
    s1 = sV = 0.0
    band = np.zeros(JMAX + 2)  # band[0] = in-window, band[j] = dist in [j(R+1),(j+1)(R+1)), last = overflow
    nq = 0
    for q in qs:
        q = int(q)
        a0 = q_arr_inv_cache[q]  # pbar_q for p ~ P, p != q
        npb = len(a0)
        wins = np.zeros(npb)
        vsum = np.zeros(npb)
        bandtot = np.zeros(JMAX + 2)
        for ell in ells:
            ell = int(ell)
            if ell == q:
                continue
            w = pow(q, -1, ell)
            nu = ((ell - a0 % ell) * w) % ell  # (-a0 * qbar_ell) mod ell
            inwin = nu <= R
            d = np.where(inwin, 0, np.minimum(nu - R, ell - nu))
            j = np.where(inwin, 0, 1 + np.minimum((d - 1) // (R + 1), JMAX))
            bandtot += np.bincount(j, minlength=JMAX + 2)
            wins += inwin
            vsum += np.where(inwin, 0.0, np.minimum(1.0, ((R + 1) / np.maximum(d, 1)) ** 2))
        D = wins - drift_const
        ED2 += np.mean(D ** 2)
        m1 += np.mean(wins)
        mV += np.mean(vsum)
        s1 = max(s1, wins.max())
        sV = max(sV, vsum.max())
        band += bandtot / npb
        nq += 1
    return (ED2 / nq, m1 / nq, mV / nq, s1, sV, band / nq)


def main():
    scales = [1e6, 1e8, 1e10, 1e12]
    rows = {"Q": [], "top": []}
    for X in scales:
        t0 = time.time()
        L = math.log(X)
        Q = P = int(round(X ** 0.425))
        R = int(round(X ** 0.15))
        A = int(round(X ** 0.575))
        pr = sieve(max(A, 4 * Q) + 10)
        ps = pr[(pr > P) & (pr <= 2 * P)]
        qcand = pr[(pr > Q) & (pr <= 2 * Q)]
        nq = 6 if X < 1e12 else 4
        qs = qcand[np.linspace(0, len(qcand) - 1, nq).astype(int)]
        inv_cache = {}
        for q in qs:
            q = int(q)
            inv_cache[q] = np.array([pow(int(p), -1, q) for p in ps if int(p) != q],
                                    dtype=np.int64)
        print(f"\n=== x = {X:.0e}:  Q=P={Q}  R={R}  A={A}  L={L:.2f}  "
              f"N_P={len(ps)}  #q={nq}", flush=True)
        for name, lo, hi in [("Q", Q, 2 * Q), ("top", A // 2, A)]:
            ells = pr[(pr > lo) & (pr <= hi)]
            lam = math.log((lo + hi) / 2) / math.log(X)
            drift = (R + 1) * float(np.sum(1.0 / ells.astype(float)))
            ED2, m1, mV, s1, sV, band = run_block(ells, ps, qs, inv_cache, R, drift)
            qmid = float(np.mean(qs))
            harm = (4.1 * len(ells)) ** 2 / qmid
            chain = (s1 + sV + drift) * (m1 + mV + drift)
            r2l = (R + 1) ** 2 * L
            budget = 0.05 * R ** 2 / L ** 3  # delta_0 = 1/L
            rows[name].append((X, R, L, ED2, m1, mV, s1, sV, chain, harm, r2l, budget))
            print(f"  block {name:>3} (lam~{lam:.3f}): N_ell={len(ells)}  drift={drift:.2f}")
            print(f"    ED2={ED2:9.3f}  ED2/(R+1)={ED2/(R+1):7.3f}   "
                  f"m1/(R+1)={m1/(R+1):6.3f}  mV/(R+1)={mV/(R+1):6.3f}")
            print(f"    s1={s1:6.0f} (P1 bound R+1={R+1})  sV={sV:8.2f}  "
                  f"sV/((R+1)L)={sV/((R+1)*L):6.3f}")
            print(f"    chain={chain:12.1f}  R^2L={r2l:10.1f}  harm={harm:12.1f}  "
                  f"chain/harm={chain/harm:8.4f}  ED2/harm={ED2/harm:9.5f}")
            print(f"    budget(d0=1/L)={budget:8.3f}  chain/budget={chain/budget:10.1f}"
                  f"  = L^{math.log(chain/budget)/math.log(L):4.2f}")
            bs = "  ".join(f"{b/(R+1):.2f}" for b in band[: JMAX + 1])
            print(f"    E band-count/(R+1), j=0..{JMAX}: {bs}   ((P2): O(1), j-uniform)")
        print(f"  [{time.time()-t0:.1f}s]", flush=True)

    print("\n=== SCALING FIT (log-log slopes in x) ===")
    for name in ("Q", "top"):
        d = rows[name]
        lx = np.log([r[0] for r in d])

        def slope(idx):
            y = np.log([r[idx] for r in d])
            return np.polyfit(lx, y, 1)[0]

        print(f" block {name:>3}: slope ED2={slope(3):.3f}  m1={slope(4):.3f}  "
              f"mV={slope(5):.3f}  chain={slope(8):.3f}  harm={slope(9):.3f}  "
              f"R^2L={slope(10):.3f}")
    print("\n expectations: m1,mV ~ 0.15 ((P2): R-grade);  chain ~ 0.30+o(1);")
    print(" harm ~ 0.425 (Q-block) / 0.725 (top);  ED2 truth ~ 0.15 (diagonal).")
    print(" CONFIRMING pattern: chain slope ~ 0.30 << harm slope at top block,")
    print(" chain/budget ratio ~ polylog (L^c, c~3-4, slope ~ 0 in x).")


if __name__ == "__main__":
    main()
