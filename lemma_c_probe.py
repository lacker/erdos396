"""
Lemma C diagnosis probe.

C's hardest configuration: n = p1*p2*a with TWO band primes. The joint slot-2
digit conditions are {n/p1^2} = {p2*a/p1} >= 1/2 and {n/p2^2} = {p1*a/p2} >= 1/2,
with a <= R = x/(p1 p2) far shorter than p1*p2 (thin progressions: joint
residues cannot equidistribute per-pair; only the ensemble can).

Note the phases: detecting the joint condition uses e(a*(h*p2/p1 + k*p1/p2)),
i.e. theta_{h,k} = (h p2^2 + k p1^2)/(p1 p2) -- EXACTLY the two-frequency
phases of the D-dagger machinery (manuscript Sec 6-8) with (mu,lambda,q,p) ->
(h,-k,p2,p1) and the same R. This probe measures:

  (1) the centered joint-digit sums against 1-bounded multiplicative weights
      g(n-1) in {1, liouville, chi_3}: Lemma C predicts square-root
      cancellation on ensemble average (z = O(1));
  (2) the per-pair thin-progression bias (the known ~4% within-side effect)
      and its behavior on ensemble average;
  (3) resonant pairs (p2/p1 near sqrt(h/k)): major arcs, counted not bounded
      -- same dichotomy as D-dagger.
"""
import numpy as np, math
from sympy import primerange

x = 10**8
SMALLP = [int(p) for p in primerange(2, int(x**0.5) + 1)]

def batch_liouville(vals):
    """liouville for an int64 array (vals <= x), vectorized trial division"""
    m = vals.astype(np.int64).copy()
    om = np.zeros(len(m), dtype=np.int32)
    for p in SMALLP:
        if p * p > x: break
        while True:
            dv = (m % p) == 0
            if not dv.any(): break
            m[dv] //= p
            om[dv] += 1
    om += (m > 1).astype(np.int32)          # residual prime > sqrt(x)
    return np.where(om % 2 == 0, 1.0, -1.0)

def chi3(vals):
    r = vals % 3
    return np.where(r == 0, 0.0, np.where(r == 1, 1.0, -1.0))

BLO = int(round((2*x)**(1/3)))
print(f"x={x:.0e}  band floor ~ {BLO}, sqrt(2x) ~ {int((2*x)**0.5)}")

def run(tag, P1, P2):
    p1s = [int(p) for p in primerange(*P1)]
    p2s = [int(p) for p in primerange(*P2)]
    agg = {"1": [0.0, 0.0], "liou": [0.0, 0.0], "chi3": [0.0, 0.0]}
    perpair_z, biases = [], []
    npairs = 0
    for p1 in p1s:
        for p2 in p2s:
            if p2 <= p1: continue
            R = x // (p1 * p2)
            if R < 30: continue
            npairs += 1
            a = np.arange(1, R + 1, dtype=np.int64)
            a = a[(a % p1 != 0) & (a % p2 != 0)]
            d1 = ((p2 * a) % p1) >= (p1 + 1)//2
            d2 = ((p1 * a) % p2) >= (p2 + 1)//2
            w = (d1.astype(float) - 0.5) * (d2.astype(float) - 0.5)
            n1 = p1 * p2 * a - 1
            biases.append(float((d1 & d2).mean() - d1.mean()*d2.mean()))
            sw2 = float(np.sum(w * w))
            perpair_z.append(abs(float(np.sum(w)))/math.sqrt(sw2) if sw2 > 0 else 0.0)
            for name, gv in (("1", None), ("liou", batch_liouville(n1)), ("chi3", chi3(n1))):
                wg = w if gv is None else w * gv
                agg[name][0] += float(np.sum(wg))
                agg[name][1] += float(np.sum(wg * wg))
    print(f"\n--- {tag}: {npairs} pairs ---")
    print(f" per-pair z: median={np.median(perpair_z):.2f} 90pct={np.percentile(perpair_z,90):.2f} max={max(perpair_z):.2f}")
    print(f" thin-progression bias: mean over pairs of [P(joint)-P1*P2] = {np.mean(biases):+.5f}  (rms {np.std(biases):.4f})")
    for name, (T, s2) in agg.items():
        z = abs(T)/math.sqrt(s2) if s2 > 0 else float('nan')
        print(f" ensemble z  [g={name:>4}]: {z:.2f}")

run("generic: p1~620-700, p2~950-1150", (620, 700), (950, 1150))
run("resonant: p2/p1 near 1 (h/k=1 curve)", (800, 880), (881, 960))
run("wide ratio: p1~600-660, p2~1800-2100", (600, 660), (1800, 2100))
