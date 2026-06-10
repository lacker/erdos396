# Lemma 0: The Exact Governor Sandwich

**STATUS: PROVED — and fully written (manuscript §3); Lemma 0′ (margins are free) now also PROVED in full (manuscript §15, June 10).** Machine-verified: zero exceptions on 60,000 cases, sampled at $10^9$.

---

## Statement

Let $D_0=\{m:\ m\mid\binom{2m}{m}\}$ (Pomerance's governor set; by Kummer, $m\in D_0$ iff $\kappa_p(m)\ge e$ for every $p^e\|m$, where $\kappa_p(m)=\#\{j:2(m\bmod p^j)\ge p^j\}$), and let $W_1=\{n:\ n(n-1)\mid\binom{2n}{n}\}$. There are margin-modified governor sets $D_0^{(\pm)}$ such that
$$D_0\cap(D_0^{(+)}+1)\ \subseteq\ W_1\ \subseteq\ D_0\cap(D_0^{(-)}+1)$$
holds **exactly** (every $n$, no exceptional set).

## Proof mechanism

$q\mid n-1$ implies $\{(n-1)/q^j\}=\{n/q^j\}-q^{-j}$: the digit data of $n$ at primes of $n-1$ is the digit data of $n-1$ itself shifted by margins of width $q^{-j}$. Tightening (resp. relaxing) the governor carry inequalities by these margins gives $D_0^{(+)}$ (resp. $D_0^{(-)}$). The $n$-side conditions ($p^e\|n$) are direct governor conditions on $n$ with no shift.

## Quantitative facts (measured)

- Margins are nearly free: $|D_0^{(\pm)}\triangle D_0|$ has density $\le 10^{-4}$, measured $\approx 6\times10^{-5}$ at $10^9$; on the 60k verification range $|D_0^{(+)}|=|D_0|$ exactly.
- The lower set captures **98.7%** of $W_1$.
- Ford–Konyagin: $d(D_0)=c_1=0.11424$. Measured pair density at $10^9$: $0.92\,c_1^2$ (finite-scale, converging). $W_1\ni 2,210,460,\dots$

## Consequence

Theorem 1 becomes exactly: *the events $n\in D_0$ and $n-1\in D_0$ are asymptotically independent* — the log-density of $D_0\cap(D_0+1)$ is $c_1^2$. Two fixed sets, one shift, no window bookkeeping, no density-zero error absorption anywhere.
