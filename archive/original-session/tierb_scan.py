"""
Tier B, items 4-6.

(A) Density scan: for each K, count #{n <= X : prod_{i=0..K}(n-i) | C(2n,n)}.
(B) Failure diagnostics: for each failing n, record the 'critical' prime(s):
    the prime p with the largest deficit (need - have), and where it sits
    relative to sqrt(2n). Tests the hypothesis that failures are dominated by a
    single prime p in (~(2n)^{1/2-eps}, sqrt(2n)] dividing some (n-i).
"""
import sys, math
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import carries, factorize_td
from collections import Counter, defaultdict


def diagnose(n, K):
    """Return (ok, fails) with fails = list of (p, need, have, room, e_max)."""
    tot = Counter()
    e_in_factor = defaultdict(int)  # max exponent of p within a single (n-i)
    for i in range(K + 1):
        x = n - i
        if x <= 1:
            continue
        f = factorize_td(x)
        for p, e in f.items():
            tot[p] += e
            if e > e_in_factor[p]:
                e_in_factor[p] = e
    fails = []
    for p, need in tot.items():
        have = carries(n, p)
        if have < need:
            room = 0
            q = p
            while q <= 2 * n:
                room += 1
                q *= p
            fails.append((p, need, have, room, e_in_factor[p]))
    return (len(fails) == 0), fails


def density_scan(K, X):
    cnt = 0
    witnesses = []
    for n in range(K + 1, X + 1):
        ok, _ = diagnose(n, K)
        if ok:
            cnt += 1
            if len(witnesses) < 25:
                witnesses.append(n)
    return cnt, witnesses


def failure_profile(K, X, sample_step=1):
    """Among failing n<=X, classify the dominant failing prime by size band."""
    bands = Counter()
    single_prime_fail = 0
    total_fail = 0
    big_prime_fail = 0  # dominant prime > (2n)^0.4
    for n in range(K + 1, X + 1, sample_step):
        ok, fails = diagnose(n, K)
        if ok:
            continue
        total_fail += 1
        if len(fails) == 1:
            single_prime_fail += 1
        # dominant = largest deficit, tie-break largest prime
        p, need, have, room, emax = max(fails, key=lambda t: (t[1] - t[2], t[0]))
        r = math.log(p) / math.log(2 * n)  # p ~ (2n)^r
        if r < 0.25:
            bands["<0.25"] += 1
        elif r < 0.40:
            bands["0.25-0.40"] += 1
        elif r < 0.50:
            bands["0.40-0.50"] += 1
        else:
            bands[">=0.50"] += 1
        if r >= 0.40:
            big_prime_fail += 1
    return total_fail, single_prime_fail, big_prime_fail, bands


if __name__ == "__main__":
    print("=== Density scan (count of witnesses n <= X) ===")
    for K, X in [(1, 200000), (2, 200000), (3, 200000)]:
        cnt, w = density_scan(K, X)
        print(f"K={K}, X={X}: {cnt} witnesses ({100*cnt/X:.4f}%). first few: {w[:12]}")

    print("\n=== Failure profile: size band of dominant failing prime ===")
    print("(r = log_p / log(2n), so p ~ (2n)^r)")
    for K, X, step in [(2, 200000, 1), (3, 200000, 1), (4, 100000, 1)]:
        tf, sf, bf, bands = failure_profile(K, X, step)
        print(f"K={K}, X={X}: failures={tf}")
        print(f"   single-prime failures: {sf} ({100*sf/tf:.1f}% of failures)")
        print(f"   dominant prime >= (2n)^0.40: {bf} ({100*bf/tf:.1f}%)")
        print(f"   bands: {dict(bands)}")

