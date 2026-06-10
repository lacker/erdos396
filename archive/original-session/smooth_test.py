"""
Test the central Tier-A hypothesis directly:
  Witness  <=>  window is sqrt(2n)-smooth  AND  the exponent/carry conditions hold.

We separate two necessary conditions:
  (S) smoothness: every prime factor of every (n-i) is <= sqrt(2n)
  (C) full carry condition (= actual divisibility, our check)

Question: how often does (S) hold but (C) fail?  If (S) almost implies (C),
then problem 396 reduces *almost entirely* to producing smooth windows.
"""
import sys, math
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import carries, factorize_td, check
from collections import Counter

def largest_prime_factor_window(n, K):
    P = 1
    for i in range(K+1):
        x = n - i
        if x <= 1: continue
        for p in factorize_td(x):
            if p > P: P = p
    return P

def scan(K, X):
    smooth = 0          # (S) holds
    witness = 0         # (C) holds
    smooth_and_witness = 0
    smooth_not_witness = 0
    for n in range(K+1, X+1):
        thr = math.isqrt(2*n)
        P = largest_prime_factor_window(n, K)
        S = (P <= thr)
        C = check(n, K)
        if S: smooth += 1
        if C: witness += 1
        if S and C: smooth_and_witness += 1
        if S and not C: smooth_not_witness += 1
    return smooth, witness, smooth_and_witness, smooth_not_witness

for K, X in [(1,100000),(2,200000),(3,300000)]:
    s,w,sw,snw = scan(K,X)
    print(f"K={K}, X={X}:")
    print(f"  sqrt(2n)-smooth windows (S):      {s}")
    print(f"  witnesses (C):                    {w}")
    print(f"  S and C:                          {sw}")
    print(f"  S but NOT C (smooth, still fails): {snw}")
    if s: print(f"  P(C | S) = {sw/s:.4f}")
    if w: print(f"  P(S | C) = {sw/w:.4f}   <- all witnesses smooth? {sw==w}")
    print()
