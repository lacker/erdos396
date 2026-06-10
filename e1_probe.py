"""
E1 diagnosis probe (WP4 follow-up; manuscript Hypothesis E1).

For fixed (q, lambda, mu), Lemma `branch count' gives
  N_q(mu,lam,delta) = #{p prime in (P,2P]: ||mu q/p - lam p/q|| <= delta}
                    = 2 delta Npr + E_q,   |E_q| << mu Q/P + lam P/Q + 1.
E1 needs the SIGNED q-average of sum_mu E_q(mu,lam,delta_mu) to be small
(the worst-case absolute sum is genuinely too big near u=u'=1/3).

This probe measures, at model scale, both the signed and absolute averages,
in the two band geometries (P > Q and P < Q).
"""
import numpy as np
from sympy import primerange

LB = 50.0          # the L^B level in delta_mu = 1/(2 mu L^B)
MUMAX = 30
LAMS = [1, 2]

def run(tag, Plo, Phi, Qlo, Qhi, nq):
    ps = np.array(list(primerange(Plo, Phi)), dtype=np.float64)
    qs = [int(q) for q in primerange(Qlo, Qhi)][:nq]
    Npr = len(ps)
    print(f"\n=== {tag}: p in ({Plo},{Phi}) [{Npr} primes], q: {len(qs)} primes in ({Qlo},{Qhi}) ===")
    mus = np.arange(1, MUMAX+1, dtype=np.float64)
    deltas = 1.0/(2.0*mus*LB)
    for lam in LAMS:
        E = np.zeros((len(qs), MUMAX))
        for i, q in enumerate(qs):
            th = mus[:, None]*(q/ps)[None, :] - lam*(ps/q)[None, :]
            d = np.abs(th - np.round(th))
            cnt = (d <= deltas[:, None]).sum(axis=1)
            E[i, :] = cnt - 2.0*deltas*Npr
        sum_mu = E.sum(axis=1)                       # per-q signed aggregate over mu
        worst = (mus*np.mean(qs)/np.mean(ps) + lam*np.mean(ps)/np.mean(qs) + 1).sum()
        print(f" lam={lam}:  signed avg_q sum_mu E_q = {sum_mu.mean():+8.3f}   "
              f"avg_q |sum_mu E_q| = {np.abs(sum_mu).mean():8.3f}   "
              f"avg_q sum_mu |E_q| = {np.abs(E).sum(axis=1).mean():8.3f}")
        print(f"          per-q std = {sum_mu.std():.3f}   theoretical worst-case bound sum_mu(muQ/P+lamP/Q+1) = {worst:.1f}")
        print(f"          main term sum_mu 2 delta_mu Npr = {(2*deltas*Npr).sum():.2f}")

run("geometry u>u' (P/Q ~ 6)", 20000, 40000, 5000, 5900, 60)
run("geometry u<u' (P/Q ~ 1/12)", 1500, 3000, 24000, 30000, 60)
