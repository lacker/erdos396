# Proposition: The Deep Large Sieve for Fermat-Quotient Characters

**STATUS: PROVED.** Re-derived and numerically verified June 9, 2026. (Originally derived in the cut-off session, where the writeup was destroyed; this document is the durable record.) Formal LaTeX writeup: pending (WP4).

---

## Definitions and identities (all numerically verified)

Let $q$ be an odd prime. For $\gcd(n,q)=1$ the **Fermat quotient** is
$$\ell_q(n)\;\equiv\;\frac{n^{q-1}-1}{q}\pmod q .$$
It depends only on $n\bmod q^2$ and is a surjective homomorphism $(\mathbb{Z}/q^2)^*\to(\mathbb{Z}/q,+)$:
$$\ell_q(mn)=\ell_q(m)+\ell_q(n), \qquad \ell_q(1+qu)\equiv -u \pmod q .$$
Its kernel is the **Teichmüller subgroup** $T_q$ (the $(q-1)$-th roots of unity mod $q^2$, $|T_q|=q-1$). The **depth-1 characters** are $\chi_\lambda(n)=e(\lambda\,\ell_q(n)/q)$, $\lambda\in\mathbb{Z}/q$: exactly the characters of $(\mathbb{Z}/q^2)^*$ trivial on $T_q$; for $\lambda\ne0$ the conductor is $q^2$. Orthogonality over $\lambda$ is a Wieferich-type condition:
$$\sum_{\lambda\bmod q}\chi_\lambda(y)\;=\;q\cdot\mathbf{1}\!\left[y^{\,q-1}\equiv 1 \pmod{q^2}\right].$$

## Proposition 1 (fiber bound)

For any $N\ge 1$ and any $v\in\mathbb{Z}/q$:
$$\#\{n\le N:\ (n,q)=1,\ \ell_q(n)=v\}\;\le\;(q-1)\Big(\Big\lfloor\frac{N}{q^2}\Big\rfloor+1\Big)\;\le\;\frac{N}{q}+q .$$
*Proof.* $\ell_q$ is constant on residue classes mod $q^2$; exactly $q-1$ classes (one coset of $T_q$) take the value $v$; each class meets $[1,N]$ in at most $\lfloor N/q^2\rfloor+1$ points. $\square$

## Proposition 2 (Teichmüller energy / Wieferich-pair count)

$$E(N;q):=\#\{(n_1,n_2)\in[1,N]^2:\ (n_1n_2,q)=1,\ n_1^{q-1}\equiv n_2^{q-1}\ (\mathrm{mod}\ q^2)\}\;\le\;\frac{N^2}{q}+qN .$$
*Proof.* The condition is $\ell_q(n_1)=\ell_q(n_2)$, so $E=\sum_v f_v^2$ with $f_v$ the fiber counts; $E\le(\max_v f_v)\sum_v f_v\le(N/q+q)\cdot N$. $\square$

## Theorem 3 (deep large sieve, single modulus)

For any complex weights $(a_n)_{n\le N}$ supported on $(n,q)=1$:
$$\sum_{\lambda\bmod q}\Big|\sum_{n\le N}a_n\,\chi_\lambda(n)\Big|^2\;\le\;(N+q^2)\,\|a\|_2^2 .$$
*Proof.* Orthogonality gives the left side $=q\sum_v|A_v|^2$ with $A_v=\sum_{\ell_q(n)=v}a_n$; Cauchy–Schwarz within each fiber and Proposition 1 give $\sum_v|A_v|^2\le(N/q+q)\|a\|_2^2$. $\square$

*Remark.* The family has $q$ characters of conductor $q^2$; $(N+q^2)$ is the natural conductor-limited analogue of the classical $(N+Q^2)$ and is optimal for $N\ge q^2$.

## Corollary 4 (per-character RMS; nontriviality range)

For $a$ the indicator of an $N$-segment and $N\le q^2$:
$$\Big(\frac{1}{q-1}\sum_{\lambda\ne 0}|S(\lambda)|^2\Big)^{1/2}\;\ll\;\sqrt{qN},$$
a saving of $\sqrt{N/q}$ over the trivial bound $N$ — **nontrivial whenever $N>q^{1+\varepsilon}$**. (For $N>q^2$ the RMS bound is $N/\sqrt q$.)

## Corollary 5 (crude $q$-average)

Summing Theorem 3 over primes $q\sim Q$: total mean square over the family $\{(q,\lambda):\lambda\ne0\}$ (size $\asymp Q^2/\log Q$) is $\ll(N^2+Q^3N)/\log Q$; per-character RMS $\ll N/Q+\sqrt{QN}$. **No cross-moduli gain yet** — this just sums the single-$q$ bounds. The genuine open strengthening (the program's flagged main theoretical question) is a tailored $(q,\lambda)$-averaged sieve exploiting cross-moduli Wieferich-pair counting: for fixed $n_1\ne n_2$, the primes $q$ with $q^2\mid n_1^{q-1}-n_2^{q-1}$ should be very sparse (Wieferich heuristics), far below what fixed-$q$ counting sees.

## Corollary 6 (AP-restricted version)

For $a$ supported on $n\equiv 1\ (\mathrm{mod}\ q)$, the fibers are **single** residue classes mod $q^2$ (since $\ell_q(1+qu)=-u$), so
$$\sum_{\lambda\bmod q}\Big|\sum_n a_n\chi_\lambda(n)\Big|^2\;\le\;\Big(\frac{N}{q}+q\Big)\|a\|_2^2 ,$$
equivalently the classical additive large sieve in the coordinate $u=(n-1)/q$.

## Application to Estimate D\* (parameter conclusions; details in lemma-D doc)

With band parameters $p=x^u$, $q=x^{u'}$, $u,u'\in(1/3,1/2)$:
- **$a$-side** (length $N_a=x^{1-u}$): always in the nontrivial range ($u'<1/2<1-u$); unconditional saving $x^{(1-u-u')/2}$ after Cauchy–Schwarz in $p$.
- **$p$-side** (length $x^u$): nontrivial only when $u>u'$ — half the band.
- **Caveats:** these are per-$\lambda$ *mean* bounds; the $\lambda$-sum carries weights $\sum_\lambda|c_\lambda|\asymp\log q$, and the congruence $pa\equiv1\ (q)$ couples the variables. Whether the savings survive the full bookkeeping is exactly WP1.4's numerology table.

## Numerical verification (June 9)

All identities PASS (q up to 1009, randomized). Energy bound: $E/(N^2/q+qN)\le 0.75$ across $q\in\{101,401,1009\}$, $N$ up to $3q^2$, approaching the bound at $N\asymp q^2$ as the proof structure predicts. Observed RMS of $|S(\lambda)|$ over initial segments is **far below** the proven $\sqrt{qN}$ (e.g. $q=1009$, $N=255272$: observed $356$ vs guaranteed $16049$ vs trivial $255272$) — consistent with square-root cancellation for structured sequences and with the conditional framing that Estimate D\* is true with room to spare. Script: `verify_dls.py`.
