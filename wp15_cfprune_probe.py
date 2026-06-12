# WP15-CFPRUNE probe: is the W4.6 j=0 coincidence mass CF-prunable / certificate-sensitive?
# Model of the top cell at x = 1e8 (wp11_w4_probe conventions): P = Q = 2512, R = 16,
# block Lambda = Q. For sampled primes q and pairs (ell, ell'):
#   E1: exact j=0 coincidence count N(ell,ell') and chat-envelope mass vs the lattice
#       mean 4HH'/q resp. ||w||_1 ||w'||_1 / q  (mean-domination test).
#   E2: CF structure: alpha* = (ell' ellbar_q mod q)/q; G = max convergent gap s+/s at
#       s <= H; correlation of per-pair excess with G (premise test: graph IS CF-structured).
#   E3: pruning at thresholds T (the (M3) certificate): pruned mass vs full vs mean.
#   E4: (M1)/(M2*) certification of (p,q) (toy thresholds) vs Mass(q): does
#       certification sparsify the damaging mass? (F1 predicts NO: Mass is p-free.)
#   E5: flatness checks: F_q at coincidences, a_0-phase travel, Dirichlet-lever phase.
import numpy as np
import math, random

random.seed(396)
rng = np.random.default_rng(396)

X = 1e8
L = math.log(X)
Q = int(round(X ** 0.425))          # 2512
P = Q
R = int(round(X ** 0.15))           # 16
LAM = Q                              # bottom (failing) block Lambda = Q

def primes_in(a, b):
    sieve = np.ones(b + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]: sieve[i*i::i] = False
    pr = np.nonzero(sieve)[0]
    return pr[(pr > a) & (pr <= b)]

qs   = primes_in(Q, 2 * Q)
ps   = primes_in(P, 2 * P)
ells = primes_in(LAM, 2 * LAM)
print(f"model x=1e8: Q=P={Q} R={R} Lambda={LAM} L={L:.2f}  "
      f"#q={len(qs)} #ell={len(ells)}")

NQ_SAMPLE, NPAIR, NP_SAMPLE = 8, 1500, 40
q_sample = sorted(int(q) for q in rng.choice(qs, NQ_SAMPLE, replace=False))

def w_env(ell, H):
    """nonnegative chat envelope (wp11 W1 layer): 1/(H+1) + min((R+1)/ell, 1/(pi h))."""
    h = np.arange(1, H + 1)
    return 1.0 / (H + 1) + np.minimum((R + 1) / ell, 1.0 / (np.pi * h))

def cf_denoms(num, den):
    """convergent denominators of num/den (0 < num < den)."""
    a, b = num, den
    s_prev, s = 0, 1            # denominators q_{-1}=0? use standard: q0=1 after first quotient
    dens = []
    # continued fraction of num/den: num/den = [0; a1, a2, ...]
    h0, h1 = 1, 0               # not needed; track denominators only
    k0, k1 = 0, 1               # k_{-1}=1? standard recurrence: k_{-1}=0, k_0=1 for [a0;a1..]
    # do it concretely:
    quots = []
    aa, bb = num, den
    while bb:
        quots.append(aa // bb)
        aa, bb = bb, aa % bb
    # quots[0] = 0 since num < den; denominators k_i: k_{-1}=0, k_0=1
    km1, k = 0, 1
    for j, a_j in enumerate(quots[1:], start=1):
        km1, k = k, a_j * k + km1
        dens.append(k)
    return dens

# ---------------- per-q sweep ------------------------------------------------
print("\n[E1-E3] per-q coincidence mass: full vs mean vs CF-pruned (block Lambda=Q)")
T_GRID = [5, 10, 20, 50]
agg = {"full": [], "mean": [], "cnt_ratio": [], "G": [], "rho": [],
       "pruned": {T: [] for T in T_GRID}, "kept": {T: [] for T in T_GRID},
       "prunedmean": {T: [] for T in T_GRID},
       "Fq_min": 1.0, "phase_max": 0.0, "lever_max": 0.0}
mass_q = {}
for q in q_sample:
    pairs_idx = rng.choice(len(ells), size=(NPAIR, 2))
    full = mean = 0.0
    pruned = {T: 0.0 for T in T_GRID}
    prunedmean = {T: 0.0 for T in T_GRID}
    kept = {T: 0 for T in T_GRID}
    rhos, Gs = [], []
    used = 0
    for i1, i2 in pairs_idx:
        ell, ellp = int(ells[i1]), int(ells[i2])
        if ell == ellp or ell == q or ellp == q: continue
        used += 1
        H  = -(-ell  // (R + 1))
        Hp = -(-ellp // (R + 1))
        c = (ellp * pow(ell, -1, q)) % q
        h = np.arange(1, H + 1)
        r = (h * c) % q
        w  = w_env(ell, H)
        wp = w_env(ellp, Hp)
        # partners h' = r (if <= Hp) and r - q (if >= -Hp); h' != 0 automatic (q prime, h < q)
        m1 = r <= Hp
        m2 = (r - q) >= -Hp
        # counts (ordered, both signs: factor 2)
        Ncoinc = 2 * int(m1.sum() + m2.sum())
        mass   = 2 * (np.dot(w[m1], wp[r[m1] - 1]) + np.dot(w[m2], wp[q - r[m2] - 1]))
        Nmean  = 4.0 * H * Hp / q
        w1, wp1 = 2 * w.sum(), 2 * wp.sum()
        Mmean  = w1 * wp1 / q
        full += mass; mean += Mmean
        rhos.append(Ncoinc / Nmean)
        # CF of alpha* up to H
        dens = cf_denoms(c, q)
        G = 0.0
        for j in range(len(dens) - 1):
            if dens[j] <= H:
                G = max(G, dens[j + 1] / dens[j])
        if dens and dens[0] <= H:           # first gap s=1 -> s+=dens[0]
            G = max(G, dens[0] / 1.0)
        Gs.append(G)
        for T in T_GRID:
            if G <= T:
                pruned[T] += mass; prunedmean[T] += Mmean; kept[T] += 1
        # E5 flatness on a subsample of coincidences
        if used % 200 == 0 and Ncoinc:
            hh = h[m1]
            for hv, rv in zip(hh[:3], r[m1][:3]):
                hpv = int(rv); w0 = hv * ellp - hpv * ell; m = ell * ellp
                delta = -(w0 // q) / m
                Fq = 1.0 if abs(delta) < 1e-15 else abs(math.sin(math.pi * q * delta)
                          / (q * math.sin(math.pi * delta)))
                agg["Fq_min"] = min(agg["Fq_min"], Fq)
                agg["phase_max"] = max(agg["phase_max"], q * abs(delta))
                agg["lever_max"] = max(agg["lever_max"], R * abs(w0) / (2 * m))
    mass_q[q] = (full, mean, used)
    agg["full"].append(full); agg["mean"].append(mean)
    rhos = np.array(rhos); Gs = np.array(Gs)
    agg["rho"].extend(rhos); agg["G"].extend(Gs)
    for T in T_GRID:
        agg["pruned"][T].append(pruned[T]); agg["kept"][T].append(kept[T] / used)
        agg["prunedmean"][T].append(prunedmean[T])
    print(f"  q={q}: pairs={used}  mass_full={full:9.2f}  mass_mean={mean:9.2f}  "
          f"full/mean={full/mean:5.3f}  median(N/Nmean)={np.median(rhos):5.3f}")

full_t, mean_t = sum(agg["full"]), sum(agg["mean"])
print(f"\n  TOTAL: full/mean = {full_t/mean_t:.4f}   "
      f"(mean-domination: excess = {(full_t-mean_t)/mean_t:+.3%} of mean)")

rho = np.array(agg["rho"]); G = np.array(agg["G"])
dec = np.quantile(G, [0.5, 0.9])
lo, hi = rho[G <= dec[0]], rho[G >= dec[1]]
corr = np.corrcoef(np.log(np.maximum(G, 1.0)), rho)[0, 1]
print(f"\n[E2] CF structure: corr(log G, N/Nmean) = {corr:+.3f}; "
      f"mean N/Nmean: G<=med {lo.mean():.3f} vs G>=p90 {hi.mean():.3f}  "
      f"(med G={dec[0]:.1f}, p90 G={dec[1]:.1f}, max G={G.max():.0f})")

print("\n[E3] (M3)-pruning at threshold T: kept pairs, pruned/full, pruned/its-own-mean")
for T in T_GRID:
    pr, prm = sum(agg["pruned"][T]), sum(agg["prunedmean"][T])
    kf = np.mean(agg["kept"][T])
    print(f"  T={T:3d}: kept={kf:6.1%}  pruned/full={pr/full_t:6.3f}  "
          f"pruned/prunedmean={pr/prm:6.3f}  excess removed={(full_t-mean_t-(pr-prm))/mean_t:+.3%}")

print(f"\n[E5] flatness: min F_q at coincidences = {agg['Fq_min']:.5f} (pred 1-O(1/R)); "
      f"max a0-phase travel q|Delta| = {agg['phase_max']:.4f} (pred <= 2/R = {2/R:.3f}); "
      f"max lever phase R|w0|/2m = {agg['lever_max']:.3f}")

# ---------------- E4: (M1)/(M2*) certification vs Mass(q) --------------------
print("\n[E4] certification (toy (M1) tau=8, (M2*) gap<=8 at s<=R, lambda=1) vs Mass(q)")
TAU_M1, TAU_M2 = 8.0, 8.0
cert_mass, all_mass, ncert, nall = 0.0, 0.0, 0, 0
cert_frac_q = {}
for q in q_sample:
    full, meanv, used = mass_q[q]
    p_samp = [int(p) for p in rng.choice(ps, NP_SAMPLE, replace=False) if p != q]
    nc = 0
    for p in p_samp:
        # (M2*): convergent gaps of frac(q/p) below R
        num = q % p
        dens = cf_denoms(num, p)
        ok2 = True
        prev = 1
        for j, s in enumerate(dens):
            if prev <= R and s / prev > TAU_M2: ok2 = False; break
            prev = s
            if prev > R: break
        # (M1): mu with <mu> <= R
        ok1 = True
        beta = (p / q) % 1.0
        for mu in list(range(1, R + 1)) + list(range(p - R, p)):
            amu = min(mu, p - mu)
            th = (mu * q / p - beta) % 1.0
            d = min(th, 1 - th)
            Xmu = min(R, 1 / (2 * d)) if d > 0 else R
            if Xmu / amu > TAU_M1: ok1 = False; break
        certified = ok1 and ok2
        nall += 1; all_mass += full
        if certified: nc += 1; ncert += 1; cert_mass += full
    cert_frac_q[q] = nc / len(p_samp)
print(f"  certified cells: {ncert}/{nall} = {ncert/nall:.1%}")
print(f"  E[Mass | certified] / E[Mass | all] = "
      f"{(cert_mass/max(ncert,1)) / (all_mass/nall):.4f}   (F1 predicts 1.000: p-free mass)")
print("  per-q cert fraction vs mass_full/mass_mean:")
for q in q_sample:
    full, meanv, _ = mass_q[q]
    print(f"    q={q}: cert={cert_frac_q[q]:5.1%}  full/mean={full/meanv:5.3f}")
