"""
Tier C item 8: the n = m^2 family for K=1.
Claim from the plan: n=m^2 makes the smoothness obstruction vanish identically,
because n=m^2 has P(n)<=m<=sqrt(n)<sqrt(2n), and n-1=(m-1)(m+1) factors into two
pieces ~sqrt(n). So (S) is 'free' and only the carry conditions remain.

Test: among n=m^2, what fraction are K=1 witnesses? Compare to the global
~1.1% witness density. If much higher, the square family is a strong construction
seed. Also: do witnesses among squares have a clean characterization?
"""
import sys, math
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import check, carries, factorize_td

# (a) Are all n=m^2 automatically smooth windows for K=1?
def window_smooth(n,K):
    thr=math.isqrt(2*n)
    for i in range(K+1):
        x=n-i
        if x<=1: continue
        for p in factorize_td(x):
            if p>thr: return False
    return True

sq_total=0; sq_smooth=0; sq_witness=0; sq_smooth_examples=[]; not_smooth=[]
for m in range(2, 2000):
    n=m*m
    sq_total+=1
    s=window_smooth(n,1)
    if s: sq_smooth+=1
    else: not_smooth.append(m)
    if check(n,1):
        sq_witness+=1
        if len(sq_smooth_examples)<20: sq_smooth_examples.append(m)

print(f"n=m^2 for m in [2,2000): total={sq_total}")
print(f"  smooth K=1 windows: {sq_smooth} ({100*sq_smooth/sq_total:.1f}%)")
print(f"  witnesses (K=1):    {sq_witness} ({100*sq_witness/sq_total:.2f}%)  vs global ~1.1%")
print(f"  m with witness n=m^2 (first 20): {sq_smooth_examples}")
print(f"  m where window NOT smooth (first 15): {not_smooth[:15]}")

# (b) why do non-smooth ones occur? m+1 or m-1 could have a prime factor > sqrt(2)*m
# largest prime factor of (m-1)(m+1) vs threshold sqrt(2n)=sqrt(2)*m
print("\nNon-smooth squares fail because m-1 or m+1 has a large prime factor:")
for m in not_smooth[:8]:
    n=m*m; thr=math.isqrt(2*n)
    fm=factorize_td(m-1); fp=factorize_td(m+1)
    print(f"  m={m}: m-1={m-1}={dict(fm)}, m+1={m+1}={dict(fp)}, thr=sqrt(2n)={thr}")
