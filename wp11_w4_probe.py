# WP11 W4 probe: signed tuple-aggregate vs random model; fiber counts; Farey spacing.
# Model of the top cell at x = 1e8: P = Q = x^0.425, R = x^0.15, A = x^0.575.
# E1: sharp-window block variance, signed off-diagonal vs Bernoulli diagonal.
# E2: linear signed aggregate U (Fejer-surrogate coefficients, same envelope
#     class as Vaaler -- surrogate, NOT a majorant) vs ||c||_2 (random model)
#     vs ||c||_1 (absolute chain).
# E3: fiber count (W4.2) and kernel q-average (W4.3) vs proved bounds.
# E4: pair-level Farey family: multiplicity, support, min-gap scales.
import numpy as np
from fractions import Fraction
import random, math

random.seed(396)
rng = np.random.default_rng(396)

X = 1e8
L = math.log(X)
Q = int(round(X ** 0.425))          # 2512
P = Q
R = int(round(X ** 0.15))           # 16
A = int(round(X ** 0.575))          # 39811
print(f"model x=1e8: Q=P={Q} R={R} A={A} L={L:.2f}")

def primes_in(a, b):
    sieve = np.ones(b + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]: sieve[i*i::i] = False
    pr = np.nonzero(sieve)[0]
    return pr[(pr > a) & (pr <= b)]

qs = primes_in(Q, 2 * Q)
ps = primes_in(P, 2 * P)
print(f"#primes q~(Q,2Q]: {len(qs)}, N_Q/(Q/L)={len(qs)*L/Q:.2f}")

blocks = {"Q": Q, "4Q": 4 * Q, "A/2": A // 2}
block_ells = {name: primes_in(Lam, 2 * Lam) for name, Lam in blocks.items()}
for name, Lam in blocks.items():
    print(f"block {name}: Lambda={Lam}, N_Lambda={len(block_ells[name])}")

# precompute per-ell Fejer-surrogate coefficients c_h, h=1..H (c_{-h}=conj)
coef = {}
for name, Lam in blocks.items():
    per = []
    for ell in block_ells[name]:
        H = -(-ell // (R + 1))          # ceil
        h = np.arange(1, H + 1)
        hat1 = np.exp(-1j * np.pi * h * R / ell) * np.sin(np.pi * h * (R + 1) / ell) \
               / (ell * np.sin(np.pi * h / ell))
        c = (1 - h / (H + 1)) * hat1
        per.append((int(ell), h, c))
    coef[name] = per

# ---------------- E1 + E2 over shared (p,q) samples -----------------------
M1, M2 = 300, 48
samples = []
while len(samples) < M1:
    p = int(random.choice(ps)); q = int(random.choice(qs))
    if p != q: samples.append((p, q))

print("\n[E1] sharp-window variance: signed off-diagonal vs Bernoulli diagonal")
for name, Lam in blocks.items():
    ells = block_ells[name]
    v = (R + 1) / ells
    diag_pred = float(np.sum(v * (1 - v)))
    D2s, emp_diags = [], []
    for (p, q) in samples:
        a0 = pow(p, -1, q)
        nus = np.array([(-a0 * pow(q, -1, int(ell))) % int(ell)
                        for ell in ells if ell != q], dtype=float)
        vv = (R + 1) / np.array([ell for ell in ells if ell != q], dtype=float)
        d = (nus <= R).astype(float) - vv
        D2s.append(float(np.sum(d)) ** 2)
        emp_diags.append(float(np.sum(d * d)))
    ED2, Ediag = np.mean(D2s), np.mean(emp_diags)
    se = np.std(D2s) / math.sqrt(M1)
    print(f"  {name:>3}: E D^2 = {ED2:8.3f} (+-{se:.3f})  emp.diag = {Ediag:8.3f} "
          f"pred.diag = {diag_pred:8.3f}  signed off-diag = {ED2 - Ediag:+8.3f} "
          f"(ratio E D^2/diag = {ED2 / Ediag:.3f})")

print("\n[E2] linear signed aggregate U (Fejer surrogate) vs masses")
for name, Lam in blocks.items():
    per = coef[name]
    l2sq = sum(2 * float(np.sum(np.abs(c) ** 2)) for (_, _, c) in per)
    l1 = sum(2 * float(np.sum(np.abs(c))) for (_, _, c) in per)
    Tlin = sum(2 * len(hh) for (_, hh, _) in per)
    Us = []
    for (p, q) in samples[:M2]:
        a0 = pow(p, -1, q)
        tot = 0.0
        for (ell, h, c) in per:
            if ell == q: continue
            nu = (-a0 * pow(q, -1, ell)) % ell
            ph = np.exp(2j * np.pi * h * nu / ell)
            tot += 2 * float(np.real(np.sum(c * ph)))
        Us.append(tot)
    Us = np.array(Us)
    rms = float(np.sqrt(np.mean(Us ** 2)))
    print(f"  {name:>3}: #T_lin={Tlin:7d}  rms|U| = {rms:7.3f}  ||c||_2 = {math.sqrt(l2sq):7.3f}"
          f"  ratio = {rms / math.sqrt(l2sq):5.2f}   ||c||_1 = {l1:9.1f}"
          f"  (absolute chain pays ||c||_1/||c||_2 = {l1 / math.sqrt(l2sq):8.1f})")

# ---------------- E3 fiber counts / kernel average ------------------------
print("\n[E3] fiber count (W4.2) and kernel q-average (W4.3), block Lambda=Q")
ells = block_ells["Q"]
npairs = 1500
Ks = range(0, 6)
counts = {k: [] for k in Ks}
kernel_avgs = []
for _ in range(npairs):
    ell, ellp = (int(v) for v in rng.choice(ells, size=2, replace=False))
    H1, H2 = -(-ell // (R + 1)), -(-ellp // (R + 1))
    h = random.choice([-1, 1]) * random.randint(1, H1)
    hp = random.choice([-1, 1]) * random.randint(1, H2)
    m = ell * ellp
    cnt = {k: 0 for k in Ks}
    ker = 0.0
    for q in qs:
        q = int(q)
        if q == ell or q == ellp: continue
        n = (-(h * pow(q, -1, ell) * ellp - hp * pow(q, -1, ellp) * ell)) % m
        dist = min(n, m - n) / m
        for k in Ks:
            if dist < (1 << k) / q: cnt[k] += 1
        ker += min(1.0, 1.0 / (2 * q * dist)) if dist > 0 else 1.0
    for k in Ks: counts[k].append(cnt[k])
    kernel_avgs.append(ker / len(qs))
for k in Ks:
    arr = np.array(counts[k])
    print(f"  k={k}: mean #q with ||Delta||<2^k/q = {arr.mean():7.4f}  "
          f"max = {arr.max():3d}   (W4.2) bound 2^(k+4) = {1 << (k + 4)}")
ka = np.array(kernel_avgs)
bound = 4.4 * L ** 2 / Q
print(f"  kernel q-avg: mean = {ka.mean():.5f}  max = {ka.max():.5f}  "
      f"(W4.3) bound c8 L^2/Q = {bound:.5f}")

# ---------------- E4 pair-level Farey spacing ------------------------------
print("\n[E4] pair-level family theta = h1/ell1 + h2/ell2, small model")
L0, R0 = 100, 10
ells0 = [int(v) for v in primes_in(L0, 2 * L0)]
pts = {}
for e1 in ells0:
    H1 = -(-e1 // (R0 + 1))
    for e2 in ells0:
        if e2 == e1: continue
        H2 = -(-e2 // (R0 + 1))
        m = e1 * e2
        for h1 in range(-H1, H1 + 1):
            if h1 == 0: continue
            for h2 in range(-H2, H2 + 1):
                if h2 == 0: continue
                hs = (h1 * e2 + h2 * e1) % m
                key = (hs, m)             # lowest terms: (h*,m)=1 guaranteed
                pts[key] = pts.get(key, 0) + 1
ntup = sum(pts.values()); mults = np.array(list(pts.values()))
print(f"  Lambda0={L0} R0={R0}: tuples={ntup}, distinct pts={len(pts)}, "
      f"multiplicity: min={mults.min()} max={mults.max()} "
      f"(claim: exactly 2)  energy/2#tuples = {np.sum(mults**2)/(2*ntup):.4f}")
thetas = sorted(Fraction(hs, m) for (hs, m) in pts.keys())
gaps = [thetas[i + 1] - thetas[i] for i in range(len(thetas) - 1)]
ming = min(gaps)
sup = max(min(float(t), 1 - float(t)) for t in thetas)
mean_gap = (float(thetas[-1] - thetas[0])) / len(gaps)
print(f"  support: max dist from 0 = {sup:.5f} vs 2/(R0+1)+2/L0 = {2/(R0+1)+2/L0:.5f}")
print(f"  min gap = {float(ming):.3e} = 1/{int(1/float(ming))}; "
      f"1/(16 Lam^4) = {1/(16*L0**4):.3e}; 1/(4 Lam^2) = {1/(4*L0**2):.3e}; "
      f"mean gap = {mean_gap:.3e}")
same_m_min = min((g for g, t in zip(gaps, thetas) if True), default=None)
# scale ratio: min gap in units of the cross-denominator floor
print(f"  min gap x 16 Lam^4 = {float(ming) * 16 * L0 ** 4:.2f} (O(1) <=> floor attained)")
