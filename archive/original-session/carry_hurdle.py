"""
Among sqrt(2n)-smooth windows (so (S) holds), why does (C) fail?
For each smooth-but-failing n, find the failing prime(s) and characterize them.

Key sub-question: a prime p with p^e || (n-i) needs e carries. For p in
(~(2n)^{1/3}, (2n)^{1/2}], only ONE digit position above the units is available
(since p^2 <= 2n < p^3 roughly), so at most 1 carry -> e must be 1 AND that one
high digit must carry. We measure how often the failure is exactly:
  'a prime p with p^1 || (n-i), p in (~(2n)^{1/3}, sqrt(2n)], whose 2nd base-p
   digit of n is too small to carry'.
"""
import sys, math
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import carries, factorize_td
from collections import Counter

def analyze(K, X):
    medium_single = 0   # failure dominated by single medium prime, exponent 1
    other = 0
    total_smooth_fail = 0
    band = Counter()
    for n in range(K+1, X+1):
        thr = math.isqrt(2*n)
        tot = Counter(); emax = {}
        smooth = True
        for i in range(K+1):
            x = n-i
            if x<=1: continue
            for p,e in factorize_td(x).items():
                tot[p]+=e
                emax[p]=max(emax.get(p,0),e)
                if p>thr: smooth=False
        if not smooth: continue
        fails=[(p,need,carries(n,p)) for p,need in tot.items() if carries(n,p)<need]
        if not fails: continue
        total_smooth_fail += 1
        # dominant failing prime
        p,need,have = max(fails, key=lambda t:(t[1]-t[2],t[0]))
        r = math.log(p)/math.log(2*n)
        if r<0.34: band['<1/3']+=1
        elif r<0.5: band['1/3-1/2']+=1
        else: band['~1/2']+=1
        # is it a single medium prime, exponent 1, deficit exactly 1?
        if len(fails)==1 and tot[p]==1 and (need-have)==1 and r>=0.34:
            medium_single+=1
        else:
            other+=1
    return total_smooth_fail, medium_single, other, band

for K,X in [(1,100000),(2,200000),(3,300000)]:
    tsf,ms,oth,band = analyze(K,X)
    print(f"K={K}, X={X}: smooth-but-failing = {tsf}")
    print(f"   dominant-prime size band: {dict(band)}")
    print(f"   'single medium prime, exp 1, deficit 1' failures: {ms} ({100*ms/tsf:.1f}%)")
    print()
