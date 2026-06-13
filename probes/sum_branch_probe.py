# Probe: (M1) failures from the SUM branch (upper-half mu) vs DIFFERENCE branch
# at the (1/3,1/3)-corner model. Claim under test (wp8-e1 S1 parenthetical):
# sum branch is "cognate ... applies verbatim". My analysis: tangency at
# mu~lambda*(P/Q)^2 with ||2 sqrt(lambda mu)|| small gives a strip |p - q*sqrt(mu/lam)|
# < ~ q/(lam * L^{B/2}) of failures for EVERY q -- width L^{B/2} larger than
# difference-branch diagonal.
from sympy import primerange
import math

def frac_dist(t):
    return abs(t - round(t))

x = 10**10
u = 1/3.0
P = int(x**u); Q = P
LB = 30.0           # L^B model value
lam = 1
R = x / (P*Q)       # ~ x^{1/3}
M0 = R / LB         # mu-range RL^{-B}

primesP = list(primerange(P, 2*P))
primesQ = [q for q in primesP][:25]   # sample of q's

def fails_via(p, q, branch, mu_max):
    # branch '+': theta = mu*q/p + lam*p/q (upper half, mu=mu_tilde)
    # branch '-': theta = mu*q/p - lam*p/q (lower half)
    # (M1) failure: exists mu <= mu_max with min(R, 1/(2||theta||)) > mu*LB
    # i.e. ||theta|| < 1/(2 mu LB) and R > mu*LB
    best = []
    for mu in range(1, int(mu_max)+1):
        t = mu*q/p + (lam*p/q if branch=='+' else -lam*p/q)
        d = frac_dist(t)
        if d < 1/(2*mu*LB) and R > mu*LB:
            best.append(mu)
            break
    return bool(best)

print(f"P=Q={P}, R={R:.1f}, M0={M0:.1f}, LB={LB}, lam={lam}")
print(f"predicted sum-strip half-width ~ sqrt(P*Q/(2*lam^2*LB)) = {math.sqrt(P*Q/(2*lam*lam*LB)):.1f}")
print(f"predicted diff-diagonal half-width ~ q/(4*lam^2*LB) ... ~ {P/(4*LB):.1f}")
tot_sum, tot_diff, tot_either = 0,0,0
import random
random.seed(7)
qsample = random.sample(primesP, 12)
for q in qsample:
    nsum = ndiff = 0
    # restrict p-scan to a window around q to keep cost down, plus random ps
    for p in primesP:
        if p == q: continue
        if abs(p-q) > 4*math.sqrt(P*Q/LB) and random.random() > 0.02:
            continue
        s = fails_via(p,q,'+',min(M0, 4*lam+10))   # tangency lives at mu ~ lam
        d = fails_via(p,q,'-',min(M0, 4*lam+10))   # same small-mu range for fairness
        nsum += s; ndiff += d
    print(f"q={q}: sum-branch fails(mu<=~4lam) = {nsum},  diff-branch fails(mu<=~4lam) = {ndiff}")
    tot_sum += nsum; tot_diff += ndiff
print(f"TOTALS over {len(qsample)} q: sum={tot_sum}, diff={tot_diff}, ratio={tot_sum/max(tot_diff,1):.1f}")
print("familyA claimed budget per q ~ P*L^{C+1}/L^B  (polylog-small fraction of P/L^B ~",P/LB,")")
