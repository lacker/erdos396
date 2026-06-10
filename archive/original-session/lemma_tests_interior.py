"""
Sharpest version: restrict to p with p^2 <= n^0.95 (top digit d = n div p^2 >= n^0.05,
so deterministic boundary effects are O(n^-0.05)). Predictions: P(succ) = 1/2 + tiny,
chi2 ~ df, within-side and cross-side ratios = 1.
Also stratified T3: compare joint to product of u-conditional probabilities.
"""
import sys, time, math
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np
rng = np.random.default_rng(616161)
A,B = 500_000_000, 2_000_000_000; N=250_000
t0=time.time()
PL=int((2*B)**0.5)+1
sieve=np.ones(PL+1,dtype=bool); sieve[:2]=False
for p in range(2,int(PL**0.5)+1):
    if sieve[p]: sieve[p*p::p]=False
primes=np.nonzero(sieve)[0]
ns=rng.integers(A,B+1,N,dtype=np.int64)
X=np.stack([ns,ns-1],axis=1); cof=X.copy()
fac=[[{},{}] for _ in range(N)]
for p in primes:
    p=int(p); m=(cof%p)==0
    if not m.any(): continue
    rows,cols=np.nonzero(m)
    for r,c in zip(rows.tolist(),cols.tolist()):
        x=int(cof[r,c]); e=0
        while x%p==0: x//=p; e+=1
        cof[r,c]=x; fac[r][c][p]=e
print(f"factored {time.time()-t0:.0f}s",flush=True)

side=[[],[]]; per=[]
for r in range(N):
    n=int(ns[r]); lo3=round((2*n)**(1/3)); cap=n**0.475   # p^2 <= n^0.95
    samp=[[],[]]
    for c in (0,1):
        f=dict(fac[r][c]); co=int(cof[r,c])
        if co>1: f[co]=f.get(co,0)+1
        for p,e in f.items():
            if lo3 < p <= cap and e==1:
                p2=p*p; rr=n%p2; s=(2*rr>=p2)
                side[c].append((rr/p2,s)); samp[c].append(s)
    per.append(samp)

for c,lbl in ((0,"n-side"),(1,"(n-1)-side")):
    xis=np.array([x for x,_ in side[c]]); su=np.array([s for _,s in side[c]])
    hist,_=np.histogram(xis,bins=10,range=(0,1)); exp=len(xis)/10
    chi2=float(((hist-exp)**2/exp).sum())
    print(f"{lbl}: N={len(xis)} P(succ)={su.mean():.4f} (SE {math.sqrt(.25/len(su)):.4f}) chi2={chi2:.1f} (df=9)")

both=[(s[0][0],s[0][1]) for s in per if len(s[0])>=2]
a=np.array([x for x,_ in both]); b=np.array([y for _,y in both])
pj=float(np.mean(a&b)); prod=float(a.mean()*b.mean())
print(f"within-side interior: N={len(both)} ratio={pj/prod:.3f} (SE~{math.sqrt(pj*(1-pj)/len(both))/prod:.3f})")
pairs=[(s[0][0],s[1][0]) for s in per if s[0] and s[1]]
a=np.array([x for x,_ in pairs]); b=np.array([y for _,y in pairs])
pj=float(np.mean(a&b)); prod=float(a.mean()*b.mean())
print(f"cross-side interior:  N={len(pairs)} ratio={pj/prod:.3f} (SE~{math.sqrt(pj*(1-pj)/len(pairs))/prod:.3f})")
