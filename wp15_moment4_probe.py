# WP15 probe: 4th moment of the centered root-count D_Lambda vs the (eta R)^4
# budget, against the 2nd moment vs (eta R)^2. Model of the top cell at
# x = 1e8 (wp11_w4_probe.py conventions): P = Q = x^0.425, R = x^0.15.
# M1: arithmetic E D^2, E D^4 (sharp window), kurtosis ratio E D^4/(3(E D^2)^2),
#     vs the uniform-nu random model and the independent-Bernoulli prediction.
# M2: per-tuple kernel q-average for genuinely-4-linked tuples (4 distinct
#     ells) vs 2-linked pairs: does the coincidence measure gain anything
#     from arity? (W4.3-species, one CRT constraint either way.)
import numpy as np
import random, math

random.seed(396)
rng = np.random.default_rng(396)

X = 1e8
L = math.log(X)
Q = int(round(X ** 0.425)); P = Q
R = int(round(X ** 0.15))
A = int(round(X ** 0.575))
etaR = 0.05 * X ** 0.15
print(f"model x=1e8: Q=P={Q} R={R} A={A} L={L:.2f}  (eta R)^2={etaR**2:.3f} (eta R)^4={etaR**4:.3f}")

def primes_in(a, b):
    sieve = np.ones(b + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]: sieve[i*i::i] = False
    pr = np.nonzero(sieve)[0]
    return pr[(pr > a) & (pr <= b)]

qs = primes_in(Q, 2 * Q)
ps = primes_in(P, 2 * P)
blocks = {"Q": Q, "4Q": 4 * Q, "A/2": A // 2}
block_ells = {nm: primes_in(Lam, 2 * Lam) for nm, Lam in blocks.items()}

M1 = 2000
samples = []
while len(samples) < M1:
    p = int(random.choice(ps)); q = int(random.choice(qs))
    if p != q: samples.append((p, q))

# precompute qbar_ell arrays per distinct q, per block
qset = sorted({q for (_, q) in samples})
qbar = {}
for nm, ells in block_ells.items():
    for q in qset:
        qbar[(nm, q)] = np.array([pow(q, -1, int(e)) if e != q else -1 for e in ells],
                                 dtype=np.int64)

print("\n[M1] moments of sharp-window D_Lambda: arithmetic vs random model")
print("     (kappa := E D^4 / (3 (E D^2)^2); Bernoulli pred for indep. model)")
for nm, Lam in blocks.items():
    ells = block_ells[nm].astype(np.int64)
    v = (R + 1) / ells
    V_pred = float(np.sum(v * (1 - v)))
    c4_pred = float(np.sum(v * (1 - v) * (1 - 6 * v * (1 - v))))
    D4_pred = 3 * V_pred ** 2 + c4_pred
    D2s, D4s = [], []
    for (p, q) in samples:
        a0 = pow(p, -1, q)
        qb = qbar[(nm, q)]
        ok = qb >= 0
        nus = (-a0 * qb[ok]) % ells[ok]
        d = float(np.sum((nus <= R).astype(float) - v[ok]))
        D2s.append(d * d); D4s.append(d ** 4)
    # uniform random model, same ell set
    rD2s, rD4s = [], []
    for _ in range(M1):
        nus = (rng.random(len(ells)) * ells).astype(np.int64)
        d = float(np.sum((nus <= R).astype(float) - v))
        rD2s.append(d * d); rD4s.append(d ** 4)
    ED2, ED4 = np.mean(D2s), np.mean(D4s)
    rED2, rED4 = np.mean(rD2s), np.mean(rD4s)
    se4 = np.std(D4s) / math.sqrt(M1)
    print(f"  {nm:>3}: arith E D^2={ED2:7.3f}  E D^4={ED4:8.2f} (+-{se4:.2f})"
          f"  kappa={ED4/(3*ED2**2):5.2f} | rand E D^2={rED2:7.3f} E D^4={rED4:8.2f}"
          f" kappa={rED4/(3*rED2**2):5.2f} | Bern pred V={V_pred:.3f} D4={D4_pred:.2f}")
print(f"  toy budgets: (eta R)^2={etaR**2:.3f}, (eta R)^4={etaR**4:.3f} "
      f"(L-factors dominate at x=1e8; exponent arithmetic is the real comparison)")
print(f"  exponent room (real scale): 2nd level budget x^0.30 vs truth x^0.15 -> room x^0.15;")
print(f"                              4th level budget x^0.60 vs truth 3V^2 = x^0.30 -> room x^0.30")

print("\n[M2] kernel q-average E_q min(1,1/(2q||Theta||)): 2-linked vs 4-linked, block Q")
ells = block_ells["Q"]
H = lambda ell: -(-ell // (R + 1))
qarr = qs.astype(np.int64)
qbarQ = {}
def qb_of(ell):
    if ell not in qbarQ:
        qbarQ[ell] = np.array([pow(int(q), -1, int(ell)) if q != ell else 0 for q in qarr],
                              dtype=np.int64)
    return qbarQ[ell]
def kernel_avg(ell_list, h_list):
    # Theta_q = -sum h_i qbar_{ell_i}/ell_i mod 1; vectorized over q
    th = np.zeros(len(qarr))
    for ell, h in zip(ell_list, h_list):
        th += h * qb_of(ell) / ell
    th = th % 1.0
    dist = np.minimum(th, 1 - th)
    return float(np.mean(np.minimum(1.0, 1.0 / (2 * qarr * np.maximum(dist, 1e-300)))))
n_t = 800
k2, k4 = [], []
for _ in range(n_t):
    e1, e2 = (int(v) for v in rng.choice(ells, size=2, replace=False))
    h1 = rng.integers(1, H(e1) + 1) * rng.choice([-1, 1])
    h2 = rng.integers(1, H(e2) + 1) * rng.choice([-1, 1])
    k2.append(kernel_avg([e1, e2], [h1, -h2]))
    e = [int(v) for v in rng.choice(ells, size=4, replace=False)]
    h = [int(rng.integers(1, H(ei) + 1)) * int(rng.choice([-1, 1])) for ei in e]
    k4.append(kernel_avg(e, [h[0], h[1], -h[2], -h[3]]))
c8b = 4.4 * L ** 2 / Q
print(f"  2-linked: mean={np.mean(k2):.5f} max={np.max(k2):.5f}  (W4.3 bound c_8 L^2/Q={c8b:.4f})")
print(f"  4-linked: mean={np.mean(k4):.5f} max={np.max(k4):.5f}  (extended bound 2c_8 L^2/Q={2*c8b:.4f})")
print(f"  ratio 4-linked/2-linked mean = {np.mean(k4)/np.mean(k2):.3f} "
      f"(arity buys NO extra 1/Q iff ratio ~ 1)")
print(f"  reference 1/Q grade: 6/Q = {6/Q:.5f}")
