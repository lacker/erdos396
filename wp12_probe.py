"""WP12 probe: second moment of the C-dagger-single-lb(g0) object at model scale.

Object: V_p(h) = sum_{m<=M} g0(pm-1) e(hm/p),  M = floor((x+1)/p), p in top cell.
g0(n) = 1 iff P1(n) in (x^a1, x^a2], P1^2 does not divide n, P2(n) <= x^{3/10}.
Top cell (a1,a2) = (0.40, 0.45) (eta = 0.05).

Measured (all with empirical-mean centering gt = g - G/M):
  Z1(p,h) = |Vt_p(h)|^2 / (G(1-kap))      -- per-harmonic, Bernoulli-normalized
  Z2(p)   = p*sum_c At(c)^2 / ((p-1) G(1-kap))
          = avg over all h != 0 of Z1     -- exact identity (checked)
Square-root cancellation with margin <=> Z = O(1)-ish, stable in x, thin tails.
Controls: random permutation of the same fiber (destroys arithmetic structure).

Run: .venv/bin/python wp12_probe.py
"""
import numpy as np
import sys, time

rng = np.random.default_rng(396)

def spf_sieve(N):
    spf = np.zeros(N + 1, dtype=np.int32)
    spf[0] = spf[1] = 1
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == 0:
            spf[i] = i
            sl = spf[i * i::i]
            sl[sl == 0] = i
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx.astype(np.int32)
    return spf

def factor_stats(ns, spf):
    """Return P1 (largest prime factor), mult1 (its multiplicity),
    P2 (second largest distinct prime factor) for each n in ns."""
    cur = ns.astype(np.int64).copy()
    P1 = np.zeros(len(ns), dtype=np.int64)
    M1 = np.zeros(len(ns), dtype=np.int64)
    P2 = np.zeros(len(ns), dtype=np.int64)
    act = cur > 1
    while act.any():
        ai = np.nonzero(act)[0]
        f = spf[cur[ai]].astype(np.int64)
        same = f == P1[ai]
        M1[ai[same]] += 1
        nw = ai[~same]
        P2[nw] = P1[nw]
        P1[nw] = f[~same]
        M1[nw] = 1
        cur[ai] //= f
        act[ai] = cur[ai] > 1
    return P1, M1, P2

def primes_in(lo, hi, spf):
    cand = np.arange(int(lo) + 1, int(hi) + 1)
    return cand[spf[cand] == cand]

def run_cell(x, spf, u1, u2, tag, nprime=40, hs=(1, 2, 3, 4, 5, 6, 7, 8)):
    a1, a2, fr = 0.40, 0.45, 0.30          # g0 parameters (fixed, global x)
    cl, ch, yc = x ** a1, x ** a2, x ** fr
    ps = primes_in(x ** u1, x ** u2, spf)
    if len(ps) > nprime:
        ps = ps[np.linspace(0, len(ps) - 1, nprime).astype(int)]
    Z1s, Z2s, kaps, Z2perm = [], [], [], []
    ident_ok = True
    for p in ps:
        p = int(p)
        M = int((x + 1) // p)
        m = np.arange(1, M + 1, dtype=np.int64)
        ns = p * m - 1
        P1, M1, P2 = factor_stats(ns, spf)
        g = ((P1 > cl) & (P1 <= ch) & (M1 == 1) & (P2 <= yc)).astype(float)
        G = g.sum()
        if G < 30:
            continue
        kap = G / M
        gt = g - kap
        norm = G * (1 - kap)
        # per-harmonic
        ph = 2j * np.pi * (m % p) / p
        for h in hs:
            V = np.sum(gt * np.exp(h * ph))
            Z1s.append(abs(V) ** 2 / norm)
        # full-h variance via class counts (exact orthogonality)
        At = np.bincount((m % p).astype(int), weights=gt, minlength=p)
        Z2 = p * np.sum(At ** 2) / ((p - 1) * norm)
        Z2s.append(Z2); kaps.append(kap)
        # identity check (h=3): V from raw sum == DFT of class sums
        V3 = np.sum(gt * np.exp(3 * ph))
        V3b = np.sum(At * np.exp(2j * np.pi * 3 * np.arange(p) / p))
        if abs(V3 - V3b) > 1e-6 * (1 + abs(V3)):
            ident_ok = False
        # permutation control
        gp = rng.permutation(gt)
        Ap = np.bincount((m % p).astype(int), weights=gp, minlength=p)
        Z2perm.append(p * np.sum(Ap ** 2) / ((p - 1) * norm))
    Z1s, Z2s, Z2perm = map(np.array, (Z1s, Z2s, Z2perm))
    print(f"x={x:.1e} cell={tag} #p={len(Z2s)} kappa={np.mean(kaps):.4f} | "
          f"Z1 mean/med/max={Z1s.mean():.2f}/{np.median(Z1s):.2f}/{Z1s.max():.1f} | "
          f"Z2 mean/med/max={Z2s.mean():.3f}/{np.median(Z2s):.3f}/{Z2s.max():.2f} | "
          f"tail Z2>1.5,>3: {np.mean(Z2s>1.5):.3f},{np.mean(Z2s>3):.3f} | "
          f"perm Z2 mean={Z2perm.mean():.3f} | ident={'OK' if ident_ok else 'FAIL'}")
    return Z1s, Z2s

def main():
    print("== WP12 numerics: second moment of V_p(h), g0 = cell-prime x friable ==")
    for x in (1_000_000, 4_000_000, 16_000_000):
        t0 = time.time()
        spf = spf_sieve(x)
        run_cell(x, spf, 0.40, 0.45, "top(0.40,0.45)")
        if x == 16_000_000:
            run_cell(x, spf, 0.34, 0.36, "low(0.34,0.36)")
        print(f"   [{time.time()-t0:.0f}s]")
    print()
    print("== exponent self-checks (top cell, u = 1/2 - eta) ==")
    for eta in (0.05, 0.02):
        u = 0.5 - eta
        # route 1a: Lemma alpha verbatim (max-form): bound exp = max(3u, 1) + 1; target 3/2+eta... wait target = 1.5+eta? budget exponent:
        tgt = 1 + (1 - u) + u - 0  # P*(x/P)^2 / ... = x^{2-u}; with P/L normalizers: exponent 2-u
        tgt = 2 - u  # Sigma_p |V_p|^2 target exponent (= 3/2+eta)
        r1a = max(3 * u, 1.0, min(1 + u / 2, 0.5 + 2 * u)) + 1.0
        r1b = max(3 * u, 1.0, min(1 + u / 2, 0.5 + 2 * u)) + 1.0 - u
        r1c = 1.0 + 1.0 - u  # (1/P)*N*||g0||^2
        # route 2: room exponent in Var_p target vs truth
        room2 = (2 - 3 * u) - (1 - u)          # = 1-2u = 2 eta
        # route 2 per-term bilinear (unrestricted benchmark): VW = (1-u-?)...
        VW = u + (1 - u)  # q'' ~ x^{u}, s' ~ x^{1-u}: product x^1... cell q''~x^{0.45-ish}, s'~x^{0.55}
        Vopt = VW / 2
        bil = VW / 2 + max(0.0, Vopt - u) / 2 + max(0.0, (VW - Vopt) - u) / 2 + u / 2
        per_term_deficit = bil - (1 - u)       # error vs main x^{1-u} per (p,k)
        # route 3: diagonal room, quadruple saturation
        diag_room = tgt - 1.0
        quad = u + 2 * (1 - u)                 # P * (x/P)^2 -> exact budget scale
        print(f" eta={eta}: target exp Sigma_p|V|^2 = {tgt:.3f}")
        print(f"   route1a (alpha max-form) bound exp {r1a:.3f}  deficit x^{r1a-tgt:.3f}  [claim 1-4eta={1-4*eta:.3f}]")
        print(f"   route1b (coset+BZ family) bound exp {r1b:.3f}  deficit x^{r1b-tgt:.3f}  [claim 1/2-3eta={0.5-3*eta:.3f}]")
        print(f"   route1c (ideal thin sieve) bound exp {r1c:.3f}  deficit x^{r1c-tgt:.3f}  [saturation: 0]")
        print(f"   route2 Var_p room exp = {room2:.3f} [claim 2eta={2*eta:.3f}]; "
              f"GS margin for bare q''-AP: {20/39 - u:.4f}")
        print(f"   route2 per-(p,k) fiber-Fourier bilinear: bound x^{bil:.3f} vs main x^{1-u:.3f}: deficit x^{per_term_deficit:.3f}")
        print(f"   route3 diagonal room x^{diag_room:.3f}; quadruple count exp {quad:.3f} = target+{quad-tgt:.3f} (polylog-saturation)")

if __name__ == "__main__":
    main()
