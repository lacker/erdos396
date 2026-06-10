"""
Skeleton falsification tests (K1_SKELETON.md section 9), at n ~ [5e8, 2e9].

Band primes of m: p | m with p in ((2n)^{1/3}, sqrt(2n)] -- exactly one carry
slot (j=2). Digit variable xi_p := {n/p^2} in [0,1); success := xi_p >= 1/2.
(For q | n-1 the relevant digit variable is still of n: {n/q^2} = {(n-1)/q^2} + q^{-2};
we record xi'_q := {(n-1)/q^2} per the Lemma 0 reformulation and also the exact
success 2*(n mod q^2) >= q^2.)

Tests:
  T1 (Lemma B): joint anatomy events on (n, n-1) vs product of marginals.
  T2 (marginal digits): uniformity of xi (decile chi^2), success rate ~ 1/2,
      flatness across u = log p/log n.
  T3 (Lemma C, within-side): samples where n has >= 2 band primes:
      P(both succeed) vs product.
  T4 (Lemma D, cross-side): first band prime each side:
      P(both succeed) vs product; also success_n vs anatomy(n-1) conditioning.
  T5 (Theorem 1 decomposition): P(n in D0), P(n-1 in D0+), joint vs product;
      sandwich tightness and margin costs at this scale.
"""
import sys, time, math, json
sys.path.insert(0, "/home/claude/erdos396")
import numpy as np
from divcheck import carries

rng = np.random.default_rng(424242)
A, B = 500_000_000, 2_000_000_000
N = 250_000

t0 = time.time()
PL = int((2 * B) ** 0.5) + 1
sieve = np.ones(PL + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(PL ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
primes = np.nonzero(sieve)[0]
print(f"{len(primes)} primes to {PL}; {time.time()-t0:.0f}s", flush=True)

ns = rng.integers(A, B + 1, N, dtype=np.int64)
X = np.stack([ns, ns - 1], axis=1)
cof = X.copy()
fac = [[{}, {}] for _ in range(N)]
for p in primes:
    p = int(p)
    m = (cof % p) == 0
    if not m.any():
        continue
    rows, cols = np.nonzero(m)
    for r, c in zip(rows.tolist(), cols.tolist()):
        x = int(cof[r, c]); e = 0
        while x % p == 0:
            x //= p; e += 1
        cof[r, c] = x
        fac[r][c][p] = e
print(f"trial division done {time.time()-t0:.0f}s", flush=True)


def full_factors(r, c):
    f = dict(fac[r][c])
    co = int(cof[r, c])
    if co > 1:
        f[co] = f.get(co, 0) + 1
    return f


def governor(m, f, variant):
    """m in D0^(variant) given factorization f. variant in {'std','plus','minus'}."""
    for p, e in f.items():
        cnt = 0
        q = p
        while q <= 2 * m:
            r = m % q
            if variant == 'std':
                ok = 2 * r >= q
            elif variant == 'plus':
                ok = (2 * r >= q) and (r < q - 1)
            else:
                ok = 2 * r >= q - 2
            if ok:
                cnt += 1
            q *= p
        if cnt < e:
            return False
    return True


# ---- collect per-sample data ----
recs = []
for r in range(N):
    n = int(ns[r])
    lo3 = round((2 * n) ** (1 / 3)); hi2 = math.isqrt(2 * n)
    rec = {}
    for c, m in ((0, n), (1, n - 1)):
        f = full_factors(r, c)
        Pp = max(f) if f else 1
        band = sorted([p for p in f if lo3 < p <= hi2], reverse=True)
        # digit data at band primes (digits OF n, per the window condition)
        digs = []
        for p in band:
            p2 = p * p
            rr = n % p2
            digs.append((math.log(p) / math.log(n), rr / p2, 2 * rr >= p2))
        rec[c] = {"f": f, "Pmax": Pp, "smooth": Pp <= hi2, "band": band, "digs": digs}
    rec["D0_n"] = governor(n, rec[0]["f"], 'std')
    rec["D0p_nm1"] = governor(n - 1, rec[1]["f"], 'plus')
    rec["D0_nm1"] = governor(n - 1, rec[1]["f"], 'std')
    rec["D0m_nm1"] = governor(n - 1, rec[1]["f"], 'minus')
    recs.append(rec)
print(f"classification done {time.time()-t0:.0f}s", flush=True)

out = {}

# ---- T1: anatomy independence ----
print("\n== T1: Lemma B (anatomy independence) ==")
events = {
    "smooth(sqrt2n)": lambda s: s["smooth"],
    ">=1 band prime": lambda s: len(s["band"]) >= 1,
    "P+ <= n^0.40":   lambda s: s["Pmax"] <= 0 or s["Pmax"] <= math.exp(0.40 * math.log(2e9)),
}
for name, ev in events.items():
    a = np.array([ev(rec[0]) for rec in recs])
    b = np.array([ev(rec[1]) for rec in recs])
    pj = float(np.mean(a & b)); pa = float(np.mean(a)); pb = float(np.mean(b))
    se = math.sqrt(pj * (1 - pj) / N)
    print(f"  {name:16s}: P(n)={pa:.4f} P(n-1)={pb:.4f} joint={pj:.4f} "
          f"product={pa*pb:.4f} ratio={pj/(pa*pb):.3f} (SE~{se/(pa*pb):.3f})")
    out[f"T1:{name}"] = (pa, pb, pj)

# ---- T2: marginal digit behavior ----
print("\n== T2: digit marginals (band primes, single carry slot) ==")
for c, lbl in ((0, "n-side"), (1, "(n-1)-side")):
    xis = [d[1] for rec in recs for d in rec[c]["digs"]]
    succ = [d[2] for rec in recs for d in rec[c]["digs"]]
    xis = np.array(xis); succ = np.array(succ)
    hist, _ = np.histogram(xis, bins=10, range=(0, 1))
    exp = len(xis) / 10
    chi2 = float(((hist - exp) ** 2 / exp).sum())
    print(f"  {lbl}: #vars={len(xis)}  P(success)={succ.mean():.4f} "
          f"(SE {math.sqrt(0.25/len(succ)):.4f})  decile chi2={chi2:.1f} (df=9, ~16.9 at 5%)")
    # flatness in u
    us = np.array([d[0] for rec in recs for d in rec[c]["digs"]])
    for ulo, uhi in [(0.33, 0.40), (0.40, 0.45), (0.45, 0.52)]:
        m = (us >= ulo) & (us < uhi)
        if m.sum() > 100:
            print(f"     u in [{ulo},{uhi}): P(succ)={succ[m].mean():.4f} (N={m.sum()})")

# ---- T3: within-side joint (Lemma C) ----
print("\n== T3: Lemma C (within-side digit independence) ==")
both = [(rec[0]["digs"][0][2], rec[0]["digs"][1][2]) for rec in recs if len(rec[0]["digs"]) >= 2]
if both:
    a = np.array([x for x, _ in both]); b = np.array([y for _, y in both])
    pj = float(np.mean(a & b)); prod = float(a.mean() * b.mean())
    print(f"  n with >=2 band primes: N={len(both)}  P(both)={pj:.4f} "
          f"product={prod:.4f} ratio={pj/prod:.3f} (SE~{math.sqrt(pj*(1-pj)/len(both))/prod:.3f})")

# ---- T4: cross-side joint (Lemma D core test) ----
print("\n== T4: Lemma D (cross-side digit independence) ==")
pairs = [(rec[0]["digs"][0][2], rec[1]["digs"][0][2]) for rec in recs
         if rec[0]["digs"] and rec[1]["digs"]]
a = np.array([x for x, _ in pairs]); b = np.array([y for _, y in pairs])
pj = float(np.mean(a & b)); prod = float(a.mean() * b.mean())
se = math.sqrt(pj * (1 - pj) / len(pairs))
print(f"  pairs with band prime each side: N={len(pairs)}")
print(f"  P(succ_n)={a.mean():.4f}  P(succ_n-1)={b.mean():.4f}  "
      f"P(both)={pj:.4f}  product={prod:.4f}  ratio={pj/prod:.3f} (SE~{se/prod:.3f})")
# digit success vs OTHER side's anatomy
sn = np.array([rec[0]["digs"][0][2] for rec in recs if rec[0]["digs"]])
oth_smooth = np.array([rec[1]["smooth"] for rec in recs if rec[0]["digs"]])
p_all = sn.mean(); p_cond = sn[oth_smooth].mean()
print(f"  P(succ_n) = {p_all:.4f}  vs  P(succ_n | n-1 smooth) = {p_cond:.4f} "
      f"(N_cond={oth_smooth.sum()}, SE {math.sqrt(0.25/oth_smooth.sum()):.4f})")

# ---- T5: Theorem 1 decomposition + margins ----
print("\n== T5: Theorem 1 quantities at 1e9 scale ==")
d0n = np.array([rec["D0_n"] for rec in recs])
d0pm = np.array([rec["D0p_nm1"] for rec in recs])
d0m = np.array([rec["D0_nm1"] for rec in recs])
d0mm = np.array([rec["D0m_nm1"] for rec in recs])
print(f"  P(n in D0)        = {d0n.mean():.5f}   (FK finite-scale ~0.1238)")
print(f"  P(n-1 in D0)      = {d0m.mean():.5f}")
print(f"  P(n-1 in D0+)     = {d0pm.mean():.5f}   margin cost: {d0m.mean()-d0pm.mean():.5f}")
print(f"  P(n-1 in D0-)     = {d0mm.mean():.5f}   margin gain: {d0mm.mean()-d0m.mean():.5f}")
pj = float(np.mean(d0n & d0pm)); prod = float(d0n.mean() * d0pm.mean())
print(f"  P(n in D0 & n-1 in D0+) = {pj:.5f}  product={prod:.5f}  "
      f"ratio={pj/prod:.3f} (SE~{math.sqrt(pj*(1-pj)/N)/prod:.3f})")
print(f"  c1^2 = {0.11424**2:.5f} (limit prediction)")
print(f"total {time.time()-t0:.0f}s")

