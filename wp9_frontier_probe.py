"""WP9 frontier probe: pair correlation of congruence roots at small fixed mu,
on a realistic (q, ell)-population, with the hard sub-range Lambda in (Q, Q^{3/2}]
isolated; plus a Shape-K-single probe (Kloosterman sums over primes ell to
composite modulus q1*q2 with random numerators) in the same range.

Object (Incarnation R, E3-dagger): for fixed mu, lambda,
  S_{p,q} = sum_{ell prime in range, ell != q, nu_ell <= R} e(nu_ell * theta_mu),
  nu_ell = (-a0 * qbar) mod ell, a0 = p^{-1} mod q, theta_mu = mu q/p - lambda p/q.
Square-root cancellation <=> E_q |S|^2 ~ E_q n  (n = #terms = diagonal).
"""
import math, random, cmath
import numpy as np
from sympy import primerange

random.seed(396)

def roots_sum(p, q, x, ell_list, mu, lam):
    R = int(x) // (p * q)
    a0 = pow(p, -1, q)
    th = (mu * q / p - lam * p / q) % 1.0
    S = 0j
    n = 0
    for ell in ell_list:
        if ell == q:
            continue
        nu = (-a0 * pow(q, -1, ell)) % ell
        if nu <= R:
            S += cmath.exp(2j * math.pi * nu * th)
            n += 1
    return S, n, R

def probe_pair_correlation(x=2e7, u=0.34, up=0.36, lam=1, mus=(1, 2, 3, 5),
                           nq=160, npp=6):
    P, Q = x ** u, x ** up
    y = (2 * x) ** (1 / 3)
    Qhi = Q ** 1.5
    A = x ** (1 - u)
    print(f"== pair correlation: x={x:.0e} (u,u')=({u},{up}) lam={lam}")
    print(f"   P~{P:.0f} Q~{Q:.0f} y~{y:.0f} Q^1.5~{Qhi:.0f} A~{A:.0f} R=x^{1-u-up:.2f}")
    ps = [pp for pp in primerange(int(P), int(2 * P))]
    qs = [qq for qq in primerange(int(Q), int(2 * Q))]
    random.shuffle(ps); random.shuffle(qs)
    ps, qs = ps[:npp], qs[:nq]
    ranges = {
        "easy (y, 2Q]":     [l for l in primerange(int(y), int(2 * Q) + 1)],
        "HARD (2Q, Q^1.5]": [l for l in primerange(int(2 * Q) + 1, int(Qhi) + 1)],
        "top (Q^1.5, A]":   [l for l in primerange(int(Qhi) + 1, int(A) + 1)],
    }
    for rname, ell_list in ranges.items():
        print(f" --- range {rname}: {len(ell_list)} primes ---")
        for mu in mus:
            rows = []
            for p in ps:
                S2s, ns = [], []
                for q in qs:
                    if q == p:
                        continue
                    S, n, R = roots_sum(p, q, x, ell_list, mu, lam)
                    if n > 0:
                        S2s.append(abs(S) ** 2)
                        ns.append(n)
                S2s, ns = np.array(S2s), np.array(ns)
                ratio = S2s.mean() / ns.mean()          # E|S|^2 / diagonal
                offdiag = (S2s.mean() - ns.mean()) / ns.mean()
                rows.append((p, ns.mean(), ratio, offdiag,
                             np.median(S2s / ns), (S2s / ns).max()))
            agg = np.array([[r[2], r[3]] for r in rows])
            print(f"  mu={mu}: per-p ratio E_q|S|^2/E_q n = "
                  f"{', '.join(f'{r[2]:.2f}' for r in rows)}")
            print(f"         mean ratio {agg[:,0].mean():.3f}  "
                  f"mean offdiag/diag {agg[:,1].mean():+.3f}  "
                  f"mean n {np.mean([r[1] for r in rows]):.1f}")

def probe_K_single(x=2e7, up=0.36, npairs=40):
    """Shape K-single: W(Lam) = sum_{ell<=Lam prime} e(n * inv(ell) mod q'),
    q' = q1*q2 ~ Q^2 squarefree, random numerators n; hard range
    Lam in (q'^{1/2}, q'^{3/4}]."""
    Q = x ** up
    qs = [qq for qq in primerange(int(Q), int(2 * Q))]
    random.shuffle(qs)
    print(f"== Shape K-single: modulus q'=q1q2~{Q*Q*2:.0f}, prime variable ell")
    exps = (0.55, 0.65, 0.75)
    stats = {e: [] for e in exps}
    for i in range(npairs):
        q1, q2 = random.sample(qs, 2)
        qp = q1 * q2
        n = random.randrange(1, qp)
        while math.gcd(n, qp) != 1:
            n = random.randrange(1, qp)
        for e in exps:
            Lam = int(qp ** e)
            W = 0j
            cnt = 0
            for ell in primerange(2, Lam + 1):
                if qp % ell == 0:
                    continue
                W += cmath.exp(2j * math.pi * ((n * pow(ell, -1, qp)) % qp) / qp)
                cnt += 1
            stats[e].append(abs(W) / math.sqrt(cnt))
    for e in exps:
        arr = np.array(stats[e])
        print(f"  Lam=q'^{e}: |W|/sqrt(pi(Lam)) mean {arr.mean():.2f} "
              f"median {np.median(arr):.2f} max {arr.max():.2f}   "
              f"(1.0 = exact square-root cancellation)")

def probe_hard_only(x=2e8, u=0.34, up=0.36, lam=1, mus=(1, 2, 3, 5),
                    nq=200, npp=6):
    """Larger-scale run, hard sub-range only."""
    P, Q = x ** u, x ** up
    Qhi = Q ** 1.5
    print(f"== HARD-range only, larger scale: x={x:.0e} P~{P:.0f} Q~{Q:.0f} "
          f"Q^1.5~{Qhi:.0f} R=x^{1-u-up:.2f}")
    ps = [pp for pp in primerange(int(P), int(2 * P))]
    qs = [qq for qq in primerange(int(Q), int(2 * Q))]
    random.shuffle(ps); random.shuffle(qs)
    ps, qs = ps[:npp], qs[:nq]
    ell_list = [l for l in primerange(int(2 * Q) + 1, int(Qhi) + 1)]
    print(f"   {len(ell_list)} primes in (2Q, Q^1.5]")
    for mu in mus:
        ratios, offs, nbar = [], [], []
        for p in ps:
            S2s, ns = [], []
            for q in qs:
                if q == p:
                    continue
                S, n, R = roots_sum(p, q, x, ell_list, mu, lam)
                if n > 0:
                    S2s.append(abs(S) ** 2); ns.append(n)
            S2s, ns = np.array(S2s), np.array(ns)
            ratios.append(S2s.mean() / ns.mean())
            offs.append((S2s.mean() - ns.mean()) / ns.mean())
            nbar.append(ns.mean())
        print(f"  mu={mu}: ratios {', '.join(f'{r:.2f}' for r in ratios)} | "
              f"mean {np.mean(ratios):.3f} offdiag {np.mean(offs):+.3f} "
              f"n~{np.mean(nbar):.0f}")

if __name__ == "__main__":
    probe_pair_correlation()
    probe_K_single()
    probe_hard_only()
