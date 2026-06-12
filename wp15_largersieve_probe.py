"""WP15-LARGERSIEVE probe. Model x=1e8 (wp11_w4_probe conventions):
Q = P = 2512, R = 16, block Lambda = Q (ell in (Lambda, 2Lambda]).
Verifies: (S1) v-support S_V/q = 1 - o(1) (fibers are MANY);
(S2) fiber energy Sum|m_v|^2 = diag + coincidence mass, q-stable;
(S3) prime-sampled energy E_p|U(pbar_q)|^2 << fiber energy (the D3 gap);
(S4) zero collisions: r_q(v) <= 1 (larger-sieve primitive empty);
(S5) Parseval: full-period mean |U~|^2 = fiber energy.
"""
import numpy as np

X = 1e8
Q = P = 2512
R = 16
LAM = Q  # Lambda = Q block


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i:: i] = False
    return np.nonzero(s)[0]


PR = sieve(4 * Q + 10)
ells = PR[(PR > LAM) & (PR <= 2 * LAM)]
ps = PR[(PR > P) & (PR <= 2 * P)]
qs = [int(q) for q in PR[(PR > Q) & (PR <= 2 * Q)]][:8]  # first 8 primes q ~ Q

print(f"N_Lambda={len(ells)}  N_P={len(ps)}  #q={len(qs)}  R={R}")
print(f"{'q':>6} {'S_V/q':>7} {'diag':>8} {'fibE':>9} {'fullE':>9} "
      f"{'sampE':>8} {'samp/fibE':>9} {'maxr':>4}")

agg = []
for q in qs:
    m = np.zeros(q, dtype=complex)
    diag = 0.0
    for ell in ells:
        if ell == q:
            continue
        H = -(-ell // (R + 1))  # ceil
        linv = pow(int(ell), -1, q)
        h = np.arange(1, H + 1)
        # exact sharp-window coefficient c_h = e(-hR/2ell) sin(pi h(R+1)/ell)/(ell sin(pi h/ell))
        amp = np.sin(np.pi * h * (R + 1) / ell) / (ell * np.sin(np.pi * h / ell))
        c = np.exp(-2j * np.pi * h * R / (2 * ell)) * amp
        v = (h * linv) % q
        np.add.at(m, v, c)            # +h
        np.add.at(m, (q - v) % q, np.conj(c))  # -h (c_{-h} = conj(c_h))
        diag += 2 * np.sum(amp ** 2)
    fibE = np.sum(np.abs(m) ** 2)
    SV = np.count_nonzero(np.abs(m) > 1e-15) / q
    # full period via FFT: U~(a) = sum_v m_v e(av/q)
    U = np.fft.ifft(m) * q
    fullE = np.mean(np.abs(U) ** 2)
    # prime-sampled: a0 = pbar_q
    a0 = np.array([pow(int(p), -1, q) for p in ps if p % q])
    sampE = np.mean(np.abs(U[a0]) ** 2)
    # collisions
    maxr = np.max(np.bincount(a0, minlength=q))
    agg.append((SV, sampE / fibE))
    print(f"{q:>6} {SV:>7.4f} {diag:>8.2f} {fibE:>9.2f} {fullE:>9.2f} "
          f"{sampE:>8.2f} {sampE/fibE:>9.4f} {maxr:>4}")

SVm = np.mean([a[0] for a in agg])
rat = np.mean([a[1] for a in agg])
print(f"\nmean S_V/q = {SVm:.4f}  (claim: 1 - o(1); occupancy #T_lin/q >> 1)")
print(f"mean sampled/fiber-energy = {rat:.4f}  (D3 gap: truth far below the "
      f"fiber-energy floor that ANY weight-uniform sieve bound must pay)")
