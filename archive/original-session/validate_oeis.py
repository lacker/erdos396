"""
Reconcile our k with OEIS A375077 indexing, and validate our checker against
the published witness values.

OEIS A375077: a(n) = smallest k such that prod_{i=0..n}(k-i) divides C(2k,k).
That product is (k)(k-1)...(k-n), i.e. n+1 consecutive descending factors.

Our problem 396 uses prod_{i=0..K}(n-i) = n(n-1)...(n-K): K+1 factors.

So A375077's 'n' (number of subtracted indices, top index of i) == our K.
  A375077 a(1) -> K=1, smallest n with n(n-1) | C(2n,n)
  A375077 a(2) -> K=2, smallest n with n(n-1)(n-2) | C(2n,n)
  ...
Published: a(1..7) = 2, 2480, 8178, 45153, 3648841, 7979090, 101130029.

Wait: a(1)=2 means K=1, n=2: 2*1=2 divides C(4,2)=6. Yes (6/2=3). Good.
"""
import sys
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import check, check_brute

oeis = {1: 2, 2: 2480, 3: 8178, 4: 45153, 5: 3648841, 6: 7979090, 7: 101130029}

for K, n in oeis.items():
    # n must satisfy; n-1 (and a few below) must NOT (since n is the *smallest*)
    ok = check(n, K)
    print(f"K={K}: claimed smallest witness n={n}: check={ok}", end="")
    # verify minimality on a small window just below (full minimality is expensive)
    below_clear = all(not check(m, K) for m in range(max(K + 1, n - 50), n))
    print(f", none in [n-50,n) pass: {below_clear}")

# Cross-check the two smallest with big-integer brute force too
for K, n in [(1, 2), (2, 2480)]:
    assert check(n, K) == check_brute(n, K)
print("brute-force agreement on K=1 (n=2) and K=2 (n=2480): OK")

