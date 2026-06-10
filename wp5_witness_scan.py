"""
WP5 diagnosis: witness landscape + coin-model test for the constructive route.

For n <= N compute k(n) = max k with prod_{0<=i<=k}(n-i) | C(2n,n) (capped),
via Kummer digit arithmetic. Then, on the sqrt(2n)-smooth-window population,
test the coin model: P(witness | m band primes in window) ~= c * 2^{-m},
and measure whether witnesses are enriched in band-free (delta<1/3) windows.
Also re-verify the known A375077 witnesses including 101130029.
"""
import numpy as np
from math import comb, isqrt

N = 2_000_000
KCAP = 8

# ---- smallest-prime-factor sieve ----
spf = np.zeros(N + 1, dtype=np.int32)
for p in range(2, isqrt(N) + 1):
    if spf[p] == 0:
        spf[p*p::p] = np.where(spf[p*p::p] == 0, p, spf[p*p::p])
for i in range(2, N + 1):
    if spf[i] == 0:
        spf[i] = i

def factor(m):
    f = {}
    while m > 1:
        p = int(spf[m]); e = 0
        while m % p == 0:
            m //= p; e += 1
        f[p] = e
    return f

def carries(n, p):
    c, q = 0, p
    while q <= 2*n:
        if 2*(n % q) >= q:
            c += 1
        q *= p
    return c

def kmax(n):
    """largest k <= KCAP with prod_{i<=k}(n-i) | C(2n,n)"""
    tot = {}
    kappa = {}
    for k in range(0, KCAP + 1):
        if n - k <= 0: return k - 1
        for p, e in factor(n - k).items():
            tot[p] = tot.get(p, 0) + e
            if p not in kappa:
                kappa[p] = carries(n, p)
            if tot[p] > kappa[p]:
                return k - 1
    return KCAP

# ---- verify known A375077 witnesses (direct, big-int ground truth for small ones) ----
known = {1: 2, 2: 2480, 3: 8178, 4: 45153, 5: 3648841, 6: 7979090, 7: 101130029}
print("verify A375077 witnesses (Kummer check):")
for k, n in known.items():
    ok = True
    tot = {}
    for i in range(k + 1):
        m = n - i
        d = 2
        while d * d <= m:
            while m % d == 0:
                tot[d] = tot.get(d, 0) + 1; m //= d
            d += 1
        if m > 1: tot[m] = tot.get(m, 0) + 1
    ok = all(carries(n, p) >= e for p, e in tot.items())
    extra = ""
    if n <= 3000:
        prod = 1
        for i in range(k + 1): prod *= (n - i)
        extra = f" (bigint: {comb(2*n,n) % prod == 0})"
    print(f"  k={k}: n={n}: {'PASS' if ok else 'FAIL'}{extra}")

# ---- full scan ----
import collections
kcount = collections.Counter()
wit = collections.defaultdict(list)
for n in range(2, N + 1):
    k = kmax(n)
    if k >= 0:
        kcount[k] += 1
        if k >= 2:
            wit[k].append(n)
print(f"\nscan to N={N}: counts of k(n)>=k:")
cum = 0
for k in sorted(kcount, reverse=True):
    cum += kcount[k]
    print(f"  k>={k}: {cum}   (density {cum/N:.2e})")

# ---- coin model on the smooth-window population, k=2 ----
# build window stats for a sample range; band prime = q in ((2n)^{1/3}, sqrt(2n)]
def window_stats(n, k):
    """(is sqrt-smooth, # distinct band primes in window)"""
    m_band = 0
    for i in range(k + 1):
        for p in factor(n - i):
            if p * p > 2 * n:
                return None  # not smooth -> witness impossible
            if p ** 3 > 2 * n:
                m_band += 1
    return m_band

K = 2
rows = collections.Counter(); hits = collections.Counter()
for n in range(1000, N + 1):
    st = window_stats(n, K)
    if st is None: continue
    m = min(st, 9)
    rows[m] += 1
    if kmax(n) >= K:
        hits[m] += 1
print(f"\ncoin-model test, k={K} (smooth windows only): P(witness | m band primes)")
print(f"{'m':>3} {'#windows':>9} {'#witness':>9} {'P':>9} {'P*2^m':>8}")
for m in sorted(rows):
    P = hits[m]/rows[m] if rows[m] else 0
    print(f"{m:>3} {rows[m]:>9} {hits[m]:>9} {P:>9.4f} {P*2**m:>8.3f}")

# band-free enrichment
tot_sm = sum(rows.values()); tot_w = sum(hits.values())
print(f"\nband-free (m=0) share among smooth windows: {rows[0]/tot_sm:.4f}; among witnesses: {(hits[0]/tot_w if tot_w else 0):.4f}")
