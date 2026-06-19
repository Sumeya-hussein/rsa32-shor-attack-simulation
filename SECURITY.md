# Security Notes

This project is an **educational simulation** of RSA encryption and Shor's
quantum attack. It is not suitable for production use.

## Intentional Simplifications

| Simplification | Detail |
|---|---|
| 32-bit RSA | Real minimum is 2048-bit |
| Single-character encryption blocks | Textbook RSA, not OAEP padded |
| Simulated quantum environment | No real quantum hardware used |
| Small N=15 for Shor's demo | Standard textbook example for near-term quantum hardware |

## Fixed in v1.1.0

| Fix | Detail |
|---|---|
| Replaced `random` with `secrets` | Now uses CSPRNG for prime generation |
| Null byte ciphertext leakage | Null bytes excluded from encryption |
| Import side effects | `quantum_payload.py` no longer runs on import |
| Unsafe `--real` execution | Real modulus demo now requires explicit `--real` flag |

## Responsible Use

This project exists to demonstrate why post-quantum cryptography matters.
The techniques shown here reflect real theoretical attacks — Shor's algorithm
will eventually break RSA at scale once fault-tolerant quantum computers exist.

For further reading see [NIST Post-Quantum Cryptography Standards](https://csrc.nist.gov/projects/post-quantum-cryptography).
