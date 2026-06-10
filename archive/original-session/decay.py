"""
How does witness density decay with K, and does it stabilize (suggesting positive
density for each fixed K)? We estimate density in a high window via sampling.
"""
import sys, math, random
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import check

rng = random.Random(2024)
def est_density(K, lo, hi, samples):
    hit=0
    for _ in range(samples):
        n=rng.randrange(lo,hi)
        if check(n,K): hit+=1
    return hit/samples

print("Estimated witness density by K and magnitude window:")
print(f"{'K':>2} {'~10^4':>10} {'~10^5':>10} {'~10^6':>10}")
for K in range(1,7):
    d4=est_density(K, 5000, 20000, 60000)
    d5=est_density(K, 50000, 200000, 60000)
    d6=est_density(K, 500000, 2000000, 40000)
    print(f"{K:>2} {d4:>10.5f} {d5:>10.5f} {d6:>10.5f}")
