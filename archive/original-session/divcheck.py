"""
Erdos problem 396 toolkit.

Question: for every k, does there exist n with  prod_{i=0..k} (n-i)  |  C(2n, n) ?

Exact criterion (Kummer 1852):
    v_p(C(2n,n)) = #carries when adding n+n in base p
                 = #{ j >= 1 : 2*(n mod p^j) >= p^j }.
So the divisibility holds iff for every prime p:
    sum_{i=0..k} v_p(n-i)  <=  #{ j >= 1 : 2*(n mod p^j) >= p^j }.

All checks below avoid big-integer binomials entirely (pure digit arithmetic),
except the brute-force verifier used in self-tests.
"""

import math
from collections import Counter


def carries(n: int, p: int) -> int:
    """v_p(C(2n,n)) via Kummer.  Carry out of digit j-1 iff 2*(n mod p^j) >= p^j."""
    c = 0
    q = p
    two_n = 2 * n
    while q <= two_n:
        if 2 * (n % q) >= q:
            c += 1
        q *= p
    return c


def vp(x: int, p: int) -> int:
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e


def factorize_td(x: int):
    """Trial-division factorization, fine for x up to ~10^12 if smooth-ish; use sympy for general big x."""
    f = Counter()
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] += 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        f[x] += 1
    return f


def window_exponents(n: int, k: int, factorizer=factorize_td) -> Counter:
    """Combined prime exponents of prod_{i=0..k}(n-i)."""
    tot = Counter()
    for i in range(k + 1):
        x = n - i
        if x > 1:
            tot.update(factorizer(x))
    return tot


def check(n: int, k: int, factorizer=factorize_td, diagnose=False):
    """
    Exact test of prod_{i=0..k}(n-i) | C(2n,n).
    If diagnose=True, returns (ok, failures) where failures is a list of
    (p, need, have, room) for every failing prime:
        need = v_p(product), have = v_p(C(2n,n)),
        room = number of base-p digit positions j with p^j <= 2n  (i.e. max possible carries).
    """
    if n < k + 1:
        return (False, []) if diagnose else False
    tot = window_exponents(n, k, factorizer)
    fails = []
    for p, need in tot.items():
        have = carries(n, p)
        if have < need:
            if not diagnose:
                return False
            room = 0
            q = p
            while q <= 2 * n:
                room += 1
                q *= p
            fails.append((p, need, have, room))
    if diagnose:
        return (len(fails) == 0), fails
    return True


def check_brute(n: int, k: int) -> bool:
    """Direct big-integer verification."""
    if n < k + 1:
        return False
    prod = 1
    for i in range(k + 1):
        prod *= (n - i)
    return math.comb(2 * n, n) % prod == 0


def legendre_vp_binom(n: int, p: int) -> int:
    """Independent formula: v_p(C(2n,n)) = (2*s_p(n) - s_p(2n))/(p-1)."""
    def digsum(x):
        s = 0
        while x:
            s += x % p
            x //= p
        return s
    return (2 * digsum(n) - digsum(2 * n)) // (p - 1)


if __name__ == "__main__":
    import random
    # Test 1: carries() against Legendre digit-sum formula
    rng = random.Random(396)
    for _ in range(20000):
        n = rng.randrange(1, 10**9)
        p = rng.choice([2, 3, 5, 7, 11, 13, 97, 101, 9973])
        assert carries(n, p) == legendre_vp_binom(n, p), (n, p)
    print("carries() == Legendre formula on 20000 random cases: OK")

    # Test 2: full check() against big-integer brute force
    bad = 0
    for n in range(1, 1201):
        c = math.comb(2 * n, n)
        prod = 1
        for k in range(0, 7):
            if n < k + 1:
                continue
            prod_k = 1
            for i in range(k + 1):
                prod_k *= (n - i)
            assert check(n, k) == (c % prod_k == 0), (n, k)
    print("check() == brute force for all n <= 1200, k <= 6: OK")

