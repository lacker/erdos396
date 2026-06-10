import math, cmath, random
from sympy import primerange, isprime

def lq(n, q, q2=None):
    """Fermat quotient ell_q(n) = (n^(q-1)-1)/q mod q, for gcd(n,q)=1."""
    q2 = q2 or q*q
    t = pow(n, q-1, q2)  # = 1 + q*lq mod q^2
    return ((t - 1) // q) % q

print("=== 1. Homomorphism: lq(mn) = lq(m)+lq(n) mod q ===")
for q in [11, 101, 1009]:
    ok = True
    for _ in range(2000):
        m = random.randrange(1, q*q); n = random.randrange(1, q*q)
        if m % q == 0 or n % q == 0: continue
        if lq(m*n % (q*q), q) != (lq(m,q)+lq(n,q)) % q: ok = False; break
    print(f"q={q}: {'PASS' if ok else 'FAIL'}")

print("\n=== 2. lq(1+qu) = -u mod q ===")
for q in [11, 101, 1009]:
    ok = all(lq(1+q*u, q) == (-u) % q for u in range(min(q, 500)))
    print(f"q={q}: {'PASS' if ok else 'FAIL'}")

print("\n=== 3. Orthogonality: sum_lambda chi_lambda(y) = q * 1[y^(q-1)=1 mod q^2] ===")
for q in [11, 31]:
    ok = True
    for _ in range(300):
        y = random.randrange(1, q*q)
        if y % q == 0: continue
        s = sum(cmath.exp(2j*math.pi*lam*lq(y,q)/q) for lam in range(q))
        wief = (pow(y, q-1, q*q) == 1)
        if abs(s - (q if wief else 0)) > 1e-6: ok = False; break
    print(f"q={q}: {'PASS' if ok else 'FAIL'}")

print("\n=== 4. Fiber bound (<= N/q + q) and energy bound E <= N^2/q + qN ===")
print(f"{'q':>6} {'N':>9} {'maxfib':>7} {'N/q+q':>9} {'E':>12} {'N^2/q+qN':>12} {'E/bound':>8}")
for q in [101, 401, 1009]:
    for N in [q, int(q**1.5), q*q, 3*q*q]:
        fib = {}
        for n in range(1, N+1):
            if n % q == 0: continue
            v = lq(n, q); fib[v] = fib.get(v, 0) + 1
        maxfib = max(fib.values()); E = sum(c*c for c in fib.values())
        bound = N*N/q + q*N
        print(f"{q:>6} {N:>9} {maxfib:>7} {N/q+q:>9.1f} {E:>12} {bound:>12.0f} {E/bound:>8.3f}")

print("\n=== 5. RMS over nonzero lambda of |S(lambda)| vs sqrt(qN), N in (q, q^2) ===")
print(f"{'q':>6} {'N':>8} {'RMS|S|':>10} {'sqrt(qN)':>10} {'trivial N':>10} {'saving':>8}")
for q in [101, 401, 1009]:
    for N in [int(q**1.2), int(q**1.5), int(q**1.8)]:
        # S(lam) = sum_{n<=N,(n,q)=1} e(lam*lq(n)/q); compute via fiber counts
        fib = [0]*q
        for n in range(1, N+1):
            if n % q == 0: continue
            fib[lq(n,q)] += 1
        ms = 0.0
        for lam in range(1, q):
            s = sum(fib[v]*cmath.exp(2j*math.pi*lam*v/q) for v in range(q))
            ms += abs(s)**2
        rms = math.sqrt(ms/(q-1))
        print(f"{q:>6} {N:>8} {rms:>10.1f} {math.sqrt(q*N):>10.1f} {N:>10} {N/rms:>8.2f}")

print("\n=== 6. AP linearization: lq(a0 + q*s) = lq(a0) - s*inv(a0) mod q ===")
for q in [101, 1009]:
    ok = True
    for _ in range(500):
        a0 = random.randrange(1, q*q)
        if a0 % q == 0: continue
        s = random.randrange(0, q)
        lhs = lq((a0 + q*s) % (q*q), q)
        rhs = (lq(a0, q) - s * pow(a0, -1, q)) % q
        if lhs != rhs: ok = False; print("FAIL", q, a0, s); break
    print(f"q={q}: {'PASS' if ok else 'FAIL'}")
