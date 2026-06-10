"""
Test the cornerstone Lemma 0 of the k=1 skeleton.

Definitions:
  D0   = { m : for every prime power p^e || m,  #{j>=1 : {m/p^j} >= 1/2} >= e }
         (= m | C(2m,m), Kummer)
  D0+  = margin-strengthened: #{j : 1/2 <= {m/p^j} < 1 - p^{-j}} >= e
  D0-  = margin-relaxed:      #{j : {m/p^j} >= 1/2 - p^{-j}} >= e

Claimed sandwich (to verify exactly on data):
  (S1)  n in D0  and  n-1 in D0+   ==>   n(n-1) | C(2n,n)     [lower inclusion]
  (S2)  n(n-1) | C(2n,n)           ==>   n in D0 and n-1 in D0-  [upper inclusion]

Mechanism: q | n-1  =>  {n/q^j} = {(n-1)/q^j} + q^{-j} for all j with q^j <= ...
(since n = (n-1)+1 and q^j | ... no wait: exact statement: n/q^j = (n-1)/q^j + q^{-j},
so fractional parts differ by exactly q^{-j} modulo 1, with wraparound iff
{(n-1)/q^j} >= 1 - q^{-j}.)

Also verify densities: D0 vs D0+ vs D0- should be near-identical.
"""
import sys, math
sys.path.insert(0, "/home/claude/erdos396")
from divcheck import factorize_td, check

def carries_variant(m, variant):
    """Check m's own governor condition under margin variant: 'std', 'plus', 'minus'.
    Condition: for each p^e || m, count of qualifying j >= e."""
    if m <= 1:
        return True
    for p, e in factorize_td(m).items():
        cnt = 0
        q = p
        # j ranges over q = p^j <= 2m (carries beyond have {m/p^j} = m/p^j < 1/2)
        while q <= 2*m:
            r = m % q  # {m/q} = r/q
            if variant == 'std':
                ok = 2*r >= q
            elif variant == 'plus':
                ok = (2*r >= q) and (r < q - 1)      # {.} in [1/2, 1 - 1/q^j)
            else:  # minus
                ok = (2*r >= q - 2)                   # {.} >= 1/2 - 1/q^j
            if ok:
                cnt += 1
            q *= p
        if cnt < e:
            return False
    return True

X = 60000
viol_S1 = viol_S2 = 0
cnt = {'D0':0, 'D0p':0, 'D0m':0, 'W1':0, 'S1pred':0}
for n in range(3, X+1):
    w1 = check(n, 1)
    d0_n   = carries_variant(n, 'std')
    d0p_nm1 = carries_variant(n-1, 'plus')
    d0m_nm1 = carries_variant(n-1, 'minus')
    if d0_n: cnt['D0'] += 1
    if carries_variant(n, 'plus'): cnt['D0p'] += 1
    if carries_variant(n, 'minus'): cnt['D0m'] += 1
    if w1: cnt['W1'] += 1
    if d0_n and d0p_nm1:
        cnt['S1pred'] += 1
        if not w1:
            viol_S1 += 1
            if viol_S1 <= 5: print(f"S1 VIOLATION at n={n}")
    if w1 and not (d0_n and d0m_nm1):
        viol_S2 += 1
        if viol_S2 <= 5: print(f"S2 VIOLATION at n={n}")

print(f"\nn <= {X}:")
print(f"  S1 violations: {viol_S1}   S2 violations: {viol_S2}")
print(f"  |D0|={cnt['D0']} ({cnt['D0']/X:.5f})  |D0+|={cnt['D0p']}  |D0-|={cnt['D0m']}")
print(f"  |W1|={cnt['W1']} ({cnt['W1']/X:.5f})")
print(f"  |D0 cap (D0+ +1)| = {cnt['S1pred']} ({cnt['S1pred']/X:.5f})  <- lower bound proxy for W1")
print(f"  sandwich tightness: W1 captured by lower set: {cnt['S1pred']/cnt['W1']:.4f}")
