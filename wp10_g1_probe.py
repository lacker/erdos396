#!/usr/bin/env python3
"""WP10 G1 probe: sum-branch tangency count (Lemma B+ / S5) verification.

Parts:
  2. Lemma B+ per-(q,nu,lambda) check at the (1/3,1/3)-corner model:
     observed integer count vs predicted, WITH and WITHOUT the tangency
     term T (T must be necessary and sufficient up to absolute constants).
  3. Asymmetric model (u,u')=(0.40,0.36): strip location nu ~ m_* and
     width formula.
  4. Empty corners (0.48,0.34) and (0.34,0.48): no tangency nu <= M_0.
  5. Exponent grid: band inequalities + S5/P exponent <= 0 + budget slack
     for B = max(C+c+4, 2C+2c+10).
  7. Resonance identity (sum branch, exact): |J +- sigma| =
     eta * |s sqrt(t^2-4 lam nu) + lam y| on random live tuples.
"""
import math, random
from fractions import Fraction

def frac_dist(t):
    return abs(t - round(t))

def count_failures(P, Q, q, lam, nu, delta):
    """# integers p in (P,2P] with ||nu q/p + lam p/q|| <= delta (exact loop)."""
    n = 0
    for p in range(P + 1, 2 * P + 1):
        if frac_dist(nu * q / p + lam * p / q) <= delta:
            n += 1
    return n

def predicted(P, Q, q, lam, nu, delta):
    """(main, four_terms, T) of Lemma B+."""
    main = 2 * delta * P
    four = nu * Q / P + lam * P / Q + 1 + delta / (nu * Q / P**2 + lam / Q)
    pstar = q * math.sqrt(nu / lam)
    tstar = 2 * math.sqrt(lam * nu)
    if P / 2 <= pstar <= 4 * P:
        T = q * delta * nu**0.25 * lam**-0.75 / math.sqrt(max(frac_dist(tstar), delta))
    else:
        T = 0.0
    return main, four, T

def part2():
    print("=" * 72)
    print("PART 2: Lemma B+ check, corner model x=1e10, u=u'=1/3, L^B=30")
    x = 10**10
    P = Q = int(x ** (1 / 3.0))
    LB = 30.0
    random.seed(11)
    qs = random.sample(range(Q + 1, 2 * Q + 1), 6)
    worst_with, worst_without, rows = 0.0, 0.0, []
    for lam in (1, 2, 3):
        for q in qs:
            for nu in range(1, 41):
                delta = 1 / (2 * nu * LB)
                obs = count_failures(P, Q, q, lam, nu, delta)
                main, four, T = predicted(P, Q, q, lam, nu, delta)
                r_with = obs / (main + four + T + 5)
                r_without = obs / (main + four + 5)
                if r_with > worst_with:
                    worst_with, ww = r_with, (lam, q, nu, obs, main, four, T)
                if r_without > worst_without:
                    worst_without, wo = r_without, (lam, q, nu, obs, main, four, T)
                if T > 0 and frac_dist(2 * math.sqrt(lam * nu)) <= delta:
                    rows.append((lam, q, nu, obs, main + four, T, obs / max(T, 1e-9)))
    print(f"max obs/(main+four+T+5) = {worst_with:.3f}  at (lam,q,nu,obs,main,four,T)={ww}")
    print(f"max obs/(main+four+5) [NO T] = {worst_without:.3f}  at {wo}")
    print("exact tangencies (||t*||<=delta): lam,q,nu,obs,rest,T,obs/T:")
    for r in rows[:12]:
        print("   ", r)
    print(f"  ({len(rows)} exact-tangency cells total)")

def part3():
    print("=" * 72)
    print("PART 3: asymmetric model x=1e10, (u,u')=(0.40,0.36), L^B=30, lam=1")
    x = 10**10
    P, Q = int(x**0.40), int(x**0.36)
    LB = 30.0
    R = x / (P * Q)
    M0 = R / LB
    mstar = (P / Q) ** 2
    print(f"P={P} Q={Q} R={R:.1f} M0={M0:.2f} m_*={mstar:.2f} "
          f"M_T=[{mstar/16:.2f},{16*mstar:.0f}]")
    lam = 1
    random.seed(5)
    qs = random.sample(range(Q + 1, 2 * Q + 1), 4)
    for q in qs:
        out = []
        for nu in range(1, min(int(M0), 40) + 1):
            delta = 1 / (2 * nu * LB)
            obs = count_failures(P, Q, q, lam, nu, delta)
            main, four, T = predicted(P, Q, q, lam, nu, delta)
            tag = ""
            pstar = q * math.sqrt(nu / lam)
            if P / 2 <= pstar <= 4 * P:
                tag = f" [p*={pstar:.0f} in band-zone, ||t*||={frac_dist(2*math.sqrt(lam*nu)):.3f}, T={T:.0f}]"
            if obs > 2 * (main + four) + 10 or tag:
                out.append(f"  nu={nu}: obs={obs} main={main:.1f} four={four:.1f}{tag}")
        print(f" q={q}:")
        for line in out:
            print(line)

def part4():
    print("=" * 72)
    print("PART 4: corner emptiness")
    x = 10**10
    LB = 30.0
    for (u, up) in [(0.48, 0.34), (0.34, 0.48)]:
        P, Q = int(x**u), int(x**up)
        R = x / (P * Q)
        M0 = R / LB
        mstar = (P / Q) ** 2  # lam=1
        print(f"(u,u')=({u},{up}): P={P} Q={Q} M0={M0:.2f} m_*={mstar:.1f} "
              f"-> tangency range empty: {mstar/16 > M0 or Q > 4*P}")
        # numeric confirmation: scan nu <= M0, all lam <= 3, sample q:
        # is p* ever in [P/2,4P]?
        hits = 0
        for lam in (1, 2, 3):
            for nu in range(1, max(int(M0), 1) + 1):
                for q in (Q + 1, 2 * Q):
                    pstar = q * math.sqrt(nu / lam)
                    if P / 2 <= pstar <= 4 * P:
                        hits += 1
        print(f"   tangency hits over lam<=3, nu<=M0, q in (Q,2Q]: {hits}")
        # and observed counts stay at main-term level (sample):
        if M0 >= 1:
            q = Q + 1
            tot_obs = tot_pred = 0.0
            for nu in range(1, int(M0) + 1):
                delta = 1 / (2 * nu * LB)
                obs = count_failures(P, Q, q, 1, nu, delta)
                main, four, T = predicted(P, Q, q, 1, nu, delta)
                tot_obs += obs
                tot_pred += main + four + T
            print(f"   q={q}, lam=1: sum over nu<=M0: obs={tot_obs:.0f} vs "
                  f"pred(main+four+T)={tot_pred:.0f}")

def part5():
    print("=" * 72)
    print("PART 5: exponent grid checks (closed band, 41x41)")
    bad = []
    n = 40
    for i in range(n + 1):
        for j in range(n + 1):
            u = 1 / 3 + i * (1 / 6) / n
            up = 1 / 3 + j * (1 / 6) / n
            checks = {
                "u+2u'>=1": u + 2 * up >= 1 - 1e-12,
                "2u+u'>=1": 2 * u + up >= 1 - 1e-12,
                "5u+u'>=2": 5 * u + up >= 2 - 1e-12,
                "u'-u<u (Q/P power-small vs P)": up - u < u - 1e-9,
                # S5/P exponents (lambda-free forms):
                "Q<=P: (u+u')/2<=u": (up > u) or ((u + up) / 2 <= u + 1e-12),
                "Q>P: u'+1.5(u-u')<=u": (up <= u) or (up + 1.5 * (u - up) <= u + 1e-12),
            }
            for k, v in checks.items():
                if not v:
                    bad.append((round(u, 4), round(up, 4), k))
    print(f"violations: {len(bad)}")
    for b in bad[:10]:
        print("  ", b)
    # budget slack for B = max(C+c+4, 2C+2c+10): need B/2 >= C+c+3 (+1 spare)
    worst = min(
        max(C + c + 4, 2 * C + 2 * c + 10) / 2 - (C + c + 3)
        for C in range(0, 41) for c in range(0, 41)
    )
    print(f"min over C,c<=40 of B/2-(C+c+3) = {worst}  (>=2 means slack L^2)")
    # (T-exist) emptiness region sample: 3u-u'-1>0 at (0.48,0.34)?
    print(f"3u-u'-1 at (0.48,0.34): {3*0.48-0.34-1:.3f} (>0 -> m_*>M_0, empty)")
    print(f"u'-u at (0.34,0.48): {0.48-0.34:.3f} -> needs 4sqrt(lam)>=x^0.14 (false for lam<=L^C)")

def part7():
    """Exact identity check needs high precision: float64 leaves ~1e-3
    noise when y = ||sc|| is near machine scale (observed); at 50 digits
    the residual is ~1e-38, i.e. the identity is EXACT."""
    print("=" * 72)
    print("PART 7: sum-branch resonance identity, exact check (mpmath, 50 digits)")
    from mpmath import mp, mpf, sqrt as msqrt, floor as mfloor
    mp.dps = 50
    random.seed(3)
    x = 10**10
    P = Q = int(x ** (1 / 3.0))
    LB = mpf(30)
    worst = mpf(0)
    trials = 0
    while trials < 2000:
        lam = random.randint(1, 3)
        nu = random.randint(100, 7000)  # scan regime nu >> m_* = lam
        q = random.randint(Q + 1, 2 * Q)
        Kbar = max(1, nu * Q // P)
        k = random.randint(max(2, Kbar // 2), 2 * Kbar + 2)
        sgn = random.choice((+1, -1))
        delta = 1 / (2 * nu * LB)
        t = k + sgn * delta
        disc = t * t - 4 * lam * nu
        if disc <= 0:
            continue
        c = 2 * nu / (t + msqrt(disc))  # small root (band side), stable form
        if c <= 0:
            continue
        a = c
        h1, k1, h0, k0 = 1, 0, 0, 1  # n/s convergents
        for _ in range(12):
            ai = int(mfloor(a))
            h0, h1 = h1, ai * h1 + h0
            k0, k1 = k1, ai * k1 + k0
            n, s = h1, k1
            if s > 10**5 or n == 0:
                break
            y = s * c - n
            J = nu * s * s - k * s * n + lam * n * n
            sigma = delta * s * n
            # t = k + sgn*delta => lam n^2 - tsn + nu s^2 = J - sgn*sigma
            lhs = abs(J - sgn * sigma)
            rhs = abs(y) * abs(s * msqrt(disc) + lam * y)
            if rhs > mpf("1e-30"):
                worst = max(worst, abs(lhs - rhs) / rhs)
            frac = a - ai
            if frac < mpf("1e-40"):
                break
            a = 1 / frac
        trials += 1
    print(f"max relative error over ~2000 tuples x convergents: {float(worst):.2e}")

if __name__ == "__main__":
    part2()
    part3()
    part4()
    part5()
    part7()
