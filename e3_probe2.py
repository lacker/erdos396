"""WP8-E3 probe 2:
(N2) mu-tail mechanism: full weighted mu-aggregate of |Sigma(theta_mu)| split into
     main (kappa'G), small-mu core, and tail; tail vs sqrt(R) scale.
(N3) core variance: E_q |E(theta_mu)|^2 / diagonal V for small mu.
(N4) corner exponent arithmetic.
"""
import math, random, sys
import numpy as np
from sympy import primerange

random.seed(396)

def Pplus_gt(a, y):
    n = a; p = 2; big = 1
    while p * p <= n:
        if n % p == 0:
            while n % p == 0: n //= p
            big = max(big, p)
        p += 1
    if n > 1: big = max(big, n)
    return big > y

def kappa_prime(y, Amax, q):
    return sum(1.0/ell for ell in primerange(int(y)+1, Amax+1) if ell != q)

def weights_eps(p, q, x, y):
    R = int(x) // (p*q)
    a0 = pow(p, -1, q)
    Amax = a0 + q*R
    om = np.array([1.0 if Pplus_gt(a0+q*t, y) else 0.0 for t in range(R+1)])
    kp = kappa_prime(y, Amax, q)
    return om, kp, R, a0

def probe_N2_N3(x, u, up, lam=1, nq=120, npp=8, mus=(1,2,3,5,10)):
    P, Q = x**u, x**up
    yv = (2*x)**(1/3)
    ps = list(primerange(int(P), int(2*P)))
    qs = list(primerange(int(Q), int(2*Q)))
    random.shuffle(ps); random.shuffle(qs)
    ps = ps[:npp]; qs = qs[:nq]
    print(f"== x={x:.1e} (u,u')=({u},{up}) lam={lam}: P~{int(P)} Q~{int(Q)} "
          f"R~{int(x/(4*P*Q)*4)} y={yv:.0f}, {npp} p x {nq} q ==")
    # N3: for each p, average over q of |E(theta_mu)|^2 vs diagonal V
    for p in ps:
        ratios = {m: [] for m in mus}
        Vs = []
        tail_vals = []   # N2 per (p,q): weighted tail sum, sqrt(R) ref
        main_vals = []
        Rsav = None
        for q in qs:
            if q == p: continue
            om, kp, R, a0 = weights_eps(p, q, x, yv)
            Rsav = R
            eps = om - kp
            V = float(np.sum(eps**2)); Vs.append(V)
            t = np.arange(R+1)
            for m in mus:
                th = (m*q/p - lam*p/q) % 1.0
                Eth = np.sum(eps * np.exp(2j*np.pi*t*th))
                ratios[m].append(abs(Eth)**2 / V)
            # N2 (coarse, FFT over all mu for a subsample of q)
        print(f" p={p}: R={Rsav} mean V={np.mean(Vs):.1f} (~kappa(1-k)R)")
        for m in mus:
            arr = np.array(ratios[m])
            print(f"   mu={m:3d}: E_q|E|^2/V = {arr.mean():.3f}  "
                  f"(median {np.median(arr):.3f}, max {arr.max():.1f}, n={len(arr)})")

def probe_N2_full(x, u, up, lam=1, npairs=6, mu0=12):
    """Full mu-aggregate via FFT: sum_mu (1/<mu>)|Sigma(theta_mu)|, split core/tail/main."""
    P, Q = x**u, x**up
    yv = (2*x)**(1/3)
    ps = list(primerange(int(P), int(2*P)))
    qs = list(primerange(int(Q), int(2*Q)))
    random.shuffle(ps); random.shuffle(qs)
    print(f"== FULL mu-aggregate x={x:.1e} (u,u')=({u},{up}) lam={lam} ==")
    for i in range(npairs):
        p, q = ps[i], qs[i]
        if p == q: continue
        om, kp, R, a0 = weights_eps(p, q, x, yv)
        eps = om - kp
        t = np.arange(R+1)
        beta = (lam*p/q) % 1.0
        pre = np.exp(-2j*np.pi*t*beta)
        # Sigma(theta_mu) for all mu: FFT length p of om*pre zero-padded (exp(+2pi i t mu q/p))
        # theta_mu = mu q/p - beta; e(t theta_mu) = e(t mu q / p) e(-t beta)
        # sum_t w_t e(t mu q/p): index nu = mu*q mod p -> DFT bin nu over Z/p with e(+2pi i t nu/p)
        wfull = np.zeros(p, dtype=complex); wfull[:R+1] = om * pre
        F = np.fft.ifft(wfull) * p   # sum_t w_t e(+2pi i t nu/p)
        efull = np.zeros(p, dtype=complex); efull[:R+1] = eps * pre
        FE = np.fft.ifft(efull) * p
        gfull = np.zeros(p, dtype=complex); gfull[:R+1] = pre
        FG = np.fft.ifft(gfull) * p
        mus = np.arange(1, p)
        nus = (mus * q) % p
        w = 1.0/np.minimum(mus, p-mus)
        S_sig = np.abs(F[nus]); S_E = np.abs(FE[nus]); S_G = np.abs(FG[nus])
        total = float(np.sum(w*S_sig))
        mainp = float(np.sum(w*kp*S_G))
        small = mus[np.minimum(mus, p-mus) <= mu0]
        wS = 1.0/np.minimum(small, p-small)
        core = float(np.sum(wS*np.abs(FE[(small*q) % p])))
        tail = float(np.sum(w*S_E)) - core
        print(f" p={p} q={q} R={R}: total={total:.1f} | main(k'G)={mainp:.1f} "
              f"core(mu<={mu0})={core:.1f} tail={tail:.1f} | R={R} sqrtR={math.sqrt(R):.1f} "
              f"tail/(sqrtR*logx)={tail/(math.sqrt(R)*math.log(x)):.2f}")

def probe_N4():
    corners = [(1/3,1/3),(0.4,0.4),(1/3,1/2),(1/2,1/3)]
    print("== N4 corner exponent arithmetic (strict in open band; boundary noted) ==")
    for (u,up) in corners:
        checks = {
            "u+u'>2/3 (R<y)": u+up > 2/3,
            "u+2u'>1 (beyond-sqrt; A<Q^2)": u+2*up > 1,
            "2u+u'>1 (R<P)": 2*u+up > 1,
            "u+u'<1 (R>=1, m=1 bdry)": u+up < 1,
            "1-u<2/3+ (a<y^2, Prop S)": 1-u <= 2/3,
            "A<Q^2 margin u+2u'-1": round(u+2*up-1, 4),
            "R<P margin 2u+u'-1": round(2*u+up-1, 4),
            "Lambda-range y..A nonempty: 1-u>1/3": 1-u > 1/3,
        }
        print(f" (u,u')=({u:.3f},{up:.3f}): " + "; ".join(f"{k}={v}" for k,v in checks.items()))

if __name__ == "__main__":
    probe_N4()
    x = 2e6
    probe_N2_full(x, 0.36, 0.36, lam=1, npairs=5)
    probe_N3 = probe_N2_N3
    probe_N3(x, 0.36, 0.36, lam=1, nq=100, npp=4)
