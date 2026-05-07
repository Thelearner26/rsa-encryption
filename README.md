# RSA Encryption — From Scratch

## What Is This?
A Python implementation of RSA encryption built entirely from 
scratch using number theory — no cryptography libraries. 
Demonstrates 2300 years of mathematics executing in milliseconds.

## The Mathematics

### The Core Asymmetry
Multiplying two large primes p and q takes milliseconds. 
Factoring n = p×q back into p and q is computationally 
impossible — the foundation of RSA security.

### Euler's Totient
φ(n) = (p-1)(q-1) counts numbers coprime to n. 
Euler proved a^φ(n) ≡ 1 (mod n) — the theorem 
guaranteeing RSA decryption always recovers the original message.

### Why Decryption Works
Since e×d ≡ 1 mod φ(n), we have ed = k×φ(n) + 1.
Therefore x^ed = x × (x^φ(n))^k ≡ x × 1 = x (mod n).

## Versions

### V1 — Pure RSA
Implements complete RSA from scratch — key generation 
using Euclidean algorithm, encryption and decryption 
using modular exponentiation. Encrypts and decrypts numbers.

### V2 — Text Encryption
Extends V1 to handle real text messages — ASCII encoding 
bridges human language and mathematics. Any string encrypted 
and perfectly recovered.

### V3 — Sieve Generated Keys
Uses primes from the Sieve of Eratosthenes — the same sieve 
built for the Goldbach Conjecture project. Primes generated 
to explore a 282 year old conjecture becoming cryptographic 
keys for a 1977 encryption algorithm.

## Mathematical Ancestry

| Mathematician | Year | Contribution |
|---|---|---|
| Euclid | 300 BC | Euclidean algorithm, unique prime factorisation |
| Fermat | 1640 | a^(p-1) ≡ 1 mod p for prime p |
| Euler | 1763 | Generalised Fermat using φ(n) |
| Rivest, Shamir, Adleman | 1977 | Assembled into RSA |

## Connection To Other Projects
- **Goldbach Conjecture** — same prime sieve generates RSA keys
- **Riemann Hypothesis** — prime distribution controls prime availability

## Libraries Used
- No external libraries — pure Python mathematics only

## What I Learned
- Euclidean and Extended Euclidean algorithms
- Euler's totient function and Fermat's Little Theorem
- Why ed ≡ 1 mod φ(n) guarantees decryption
- Modular exponentiation
- ASCII encoding bridging language and mathematics

## Resources
- Computerphile — Public Key Cryptography
- Computerphile — Prime Numbers and RSA
- Numberphile — Encryption and HUGE numbers
