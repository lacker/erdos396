# WP15 phase-lever probe: does R-averaging the Dirichlet-kernel phase
# e(-R w0/(2m)) reduce the signed cross-denominator coincidence mass (W4.6)?
# Model of the top cell at x = 1e8 (wp11_w4_probe.py conventions).
# Measures, on the j=0 coincidence graph {q | w0 = h ell' - h' ell} of the
# Lambda = Q block:
#   (a) rotation-count distribution (R_max-R_min)|w0|/(2m), mass-weighted
#       -> predict: essentially all mass at < 1 rotation (P3.2);
#   (b) S_abs = sum |c c' F_q| (absolute floor), |S(Rbar)| (fixed-R signed),
#       |avg_R S(R)| (R-averaged signed, honest amplitude drift included)
#       -> predict: |avg_R S| / S_abs = Theta(1), NO power drop;
#   (c) positively-aligned core (travel <= 1/6 turn): mass fraction and its
#       retained real part -> predict >= ~0.05 of S_abs survives any R-avg;
#   (d) theoretical per-pair sinc gain vs measured (consistency).
import numpy as np
import math, random

random.seed(396)
rng = np.random.default_rng(396)

X = 1e8
L = math.log(X)
Q = int(round(X ** 0.425))          # 2512
P = Q
A = int(round(X ** 0.575))

def primes_in(a, b):
    sieve = np.ones(b + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]: sieve[i*i::i] = False
    pr = np.nonzero(sieve)[0]
    return pr[(pr > a) & (pr <= b)]

qs = primes_in(Q, 2 * Q)
R_min = int(X // (4 * P * Q))       # cell-min R = x/(2P*2Q)
R_max = int(X // (P * Q))           # cell-max R
Rbar = (R_min + R_max) // 2
print(f"model x=1e8: Q=P={Q}, cell R(p,q) in [{R_min},{R_max}], Rbar={Rbar}, L={L:.2f}")

ells_all = primes_in(Q, 2 * Q)      # Lambda = Q block
print(f"block Lambda=Q: N_Lambda={len(ells_all)}")

def coeff(h, ell, R):
    """Exact Fejer-damped discrete completion coefficient c_h(ell;R), 0 if |h|>H(R)."""
    H = -(-ell // (R + 1))
    live = (np.abs(h) <= H)
    amp = np.where(live,
                   (1 - np.abs(h) / (H + 1)) * np.sin(np.pi * h * (R + 1) / ell)
                   / (ell * np.sin(np.pi * h / ell)), 0.0)
    return amp * np.exp(-1j * np.pi * h * R / ell)

NQ_SAMP = 6
NPAIR_SAMP = 4000
q_samp = [int(q) for q in rng.choice(qs, NQ_SAMP, replace=False)]
Rgrid = np.arange(R_min, R_max + 1)

agg = {"S_abs": 0.0, "S_fix": 0j, "S_avgR": 0j, "core_abs": 0.0, "core_re_avg": 0.0,
       "S_theory": 0.0, "rot_hist": np.zeros(6), "rot_edges": [0, .125, .25, .5, 1., 2., 1e9],
       "n_coinc": 0, "min_k": 1e18, "max_trav": 0.0}

H_of = {}   # uniform degree (4a): H at R_min (largest family)
for ell in ells_all:
    H_of[int(ell)] = -(-int(ell) // (R_min + 1))

for q in q_samp:
    ells = ells_all[ells_all != q].astype(np.int64)
    n_ell = len(ells)
    # sample unordered pairs ell < ell'
    pairs = set()
    while len(pairs) < NPAIR_SAMP:
        i, j = rng.integers(0, n_ell, 2)
        if i != j:
            pairs.add((min(i, j), max(i, j)))
    E1, E2, Hh, Hp, W0 = [], [], [], [], []
    for (i, j) in pairs:
        ell, ellp = int(ells[i]), int(ells[j])
        H, Hq = H_of[ell], H_of[ellp]
        c0 = (ell * pow(ellp, -1, q)) % q
        hp = np.concatenate([np.arange(-Hq, 0), np.arange(1, Hq + 1)])
        r = (hp * c0) % q
        r = np.where(r > q // 2, r - q, r)          # signed residue: candidate h
        keep = (np.abs(r) <= H) & (r != 0)
        if not keep.any(): continue
        h = r[keep]; hp_k = hp[keep]
        w0 = h * ellp - hp_k * ell                  # q | w0 by construction
        E1.append(np.full(len(h), ell)); E2.append(np.full(len(h), ellp))
        Hh.append(h); Hp.append(hp_k); W0.append(w0)
    ell_a = np.concatenate(E1).astype(np.float64); ellp_a = np.concatenate(E2).astype(np.float64)
    h_a = np.concatenate(Hh).astype(np.float64);  hp_a = np.concatenate(Hp).astype(np.float64)
    w0_a = np.concatenate(W0).astype(np.float64)
    m_a = ell_a * ellp_a
    n_a = -w0_a / q                                  # j=0: Delta = n/m exactly
    assert np.all(np.abs(w0_a % q) < 1e-9) and np.all(np.abs(w0_a) >= q - 1e-9)
    beta = n_a / m_a
    # F_q(beta) exact (geometric sum)
    Fq = np.exp(1j * np.pi * (q + 1) * beta) * np.sin(np.pi * q * beta) / (q * np.sin(np.pi * beta))
    # per-R signed sums (honest: amplitudes, degrees, phases all move with R)
    S_R = np.zeros(len(Rgrid), dtype=complex)
    for k, R in enumerate(Rgrid):
        term = coeff(h_a, ell_a, R) * np.conj(coeff(hp_a, ellp_a, R)) * Fq
        S_R[k] = term.sum()
    term_bar = coeff(h_a, ell_a, Rbar) * np.conj(coeff(hp_a, ellp_a, Rbar)) * Fq
    S_abs = np.abs(term_bar).sum()
    # rotation count over the sweep & theoretical sinc gain
    trav = (R_max - R_min) * np.abs(w0_a) / (2 * m_a)
    sinc = np.abs(np.sinc((R_max - R_min) * w0_a / (2 * m_a)))   # |avg e(-Rw0/2m)|
    S_theory = (np.abs(term_bar) * sinc).sum()
    w = np.abs(term_bar)
    hist, _ = np.histogram(trav, bins=agg["rot_edges"], weights=w)
    # positively-aligned core: pointwise travel R_max|w0|/(2m) <= 1/6 turn
    core = (R_max * np.abs(w0_a) / (2 * m_a)) <= 1.0 / 6
    core_abs = w[core].sum()
    core_re = np.mean([np.real((coeff(h_a[core], ell_a[core], R) *
                                np.conj(coeff(hp_a[core], ellp_a[core], R)) *
                                Fq[core]).sum()) for R in Rgrid])
    agg["S_abs"] += S_abs; agg["S_fix"] += S_R[len(Rgrid)//2]; agg["S_avgR"] += S_R.mean()
    agg["core_abs"] += core_abs; agg["core_re_avg"] += core_re
    agg["S_theory"] += S_theory; agg["rot_hist"] += hist
    agg["n_coinc"] += len(w0_a)
    agg["min_k"] = min(agg["min_k"], np.abs(w0_a / q).min())
    agg["max_trav"] = max(agg["max_trav"], trav.max())
    print(f"q={q}: n_coinc={len(w0_a)}, S_abs={S_abs:.4f}, |S(Rbar)|={abs(S_R[len(Rgrid)//2]):.4f}, "
          f"|avgR S|={abs(S_R.mean()):.4f}, theory_sinc={S_theory:.4f}, "
          f"core_abs={core_abs:.4f}, core_Re_avgR={core_re:.4f}, max_trav={trav.max():.3f}")

print("\n=== AGGREGATE (6 q, 4000 pairs each) ===")
print(f"coincidences: {agg['n_coinc']}, min |k|=|w0|/q: {agg['min_k']:.0f} (predict >=1), "
      f"max rotations: {agg['max_trav']:.3f} (predict <= ~1.5)")
hist = agg["rot_hist"] / agg["rot_hist"].sum()
print("mass-weighted rotation histogram [0,.125,.25,.5,1,2,inf]:",
      np.array2string(hist, precision=3))
print(f"S_abs (absolute floor)      = {agg['S_abs']:.4f}")
print(f"|S fixed-R| / S_abs         = {abs(agg['S_fix'])/agg['S_abs']:.4f}")
print(f"|avg_R S| / S_abs           = {abs(agg['S_avgR'])/agg['S_abs']:.4f}   <- the lever's yield")
print(f"theory sinc-retained / S_abs= {agg['S_theory']/agg['S_abs']:.4f}")
print(f"aligned-core mass / S_abs   = {agg['core_abs']/agg['S_abs']:.4f}")
print(f"aligned-core Re(avg_R)/S_abs= {agg['core_re_avg']/agg['S_abs']:.4f}  (predict >= ~0.4 x core mass)")
print("VERDICT CHECK: power drop would need |avg_R S|/S_abs ~ x^{-0.1..} ~ 0.16 "
      "AND vanishing core; constant-grade ratio + positive core = lever FAILS as predicted.")
