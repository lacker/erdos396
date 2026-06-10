"""WP8-E3 probe: (A) verify Proposition S reduction exactly;
(B) measure E3 aggregate vs budget at model scale;
(C) measure dispersion ingredients (per-ell Weil-type cancellation on q-average)."""
import math, cmath, random, sys
from sympy import primerange, isprime

random.seed(396)

def smallest_factor_above(a, y):
    # return True if P+(a) > y
    n = a
    f = 2
    while f * f <= n:
        while n % f == 0:
            n //= f
        f += 1
    # n is now the largest prime factor candidate? No: trial division leaves largest prime factor
    return n > y  # n = P+(a) if n>1 else last factor handled

def Pplus_gt(a, y):
    n = a
    p = 2
    big = 1
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            big = max(big, p)
        p += 1
    if n > 1:
        big = max(big, n)
    return big > y

def probe_A(x, u, up, ntrials=40):
    """Exact check of Proposition S."""
    P, Q = x**u, x**up
    R = int(x / (2*P*2*Q) * 4)  # use R = x/(pq) per-pair below instead
    y = (2*x)**(1/3)
    ps = [p for p in primerange(int(P), int(2*P))]
    qs = [q for q in primerange(int(Q), int(2*Q))]
    bad = 0
    for _ in range(ntrials):
        p = random.choice(ps); q = random.choice(qs)
        if p == q: continue
        R = int(x // (p*q))
        a0 = pow(p, -1, q)
        theta = random.random()
        # LHS
        lhs = sum(cmath.exp(2j*math.pi*t*theta) for t in range(0, R+1)
                  if Pplus_gt(a0+q*t, y))
        # RHS: primes ell in (y, a0+qR]
        Amax = a0 + q*R
        rhs = 0
        for ell in primerange(int(y)+1, Amax+1):
            if ell == q:
                continue  # (a0,q)=1 so q never divides a0+qt
            nu = (-a0 * pow(q, -1, ell)) % ell
            if nu <= R:
                rhs += cmath.exp(2j*math.pi*nu*theta)
        if abs(lhs - rhs) > 1e-8:
            bad += 1
            print(f"  MISMATCH p={p} q={q} |diff|={abs(lhs-rhs):.3e}")
    print(f"probe_A x={x:.2e} (u,u')=({u},{up}): {ntrials} trials, mismatches={bad}")

if __name__ == "__main__":
    x = float(sys.argv[1]) if len(sys.argv) > 1 else 2e6
    for (u, up) in [(0.34, 0.34), (0.40, 0.40), (0.34, 0.48), (0.48, 0.34)]:
        probe_A(x, u, up, ntrials=15)
