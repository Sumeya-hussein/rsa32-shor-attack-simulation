# RSA-32 & Quantum Attack Demo

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-0.25.0-6929C4?logo=qiskit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)
![Topic](https://img.shields.io/badge/Topic-Post--Quantum%20Cryptography-red)

> **Why this matters:** NIST finalised its first post-quantum cryptography standards in 2024 because quantum computers will eventually break RSA. This project shows *exactly* how — step by step, from key generation to quantum attack — and demonstrates why Quantum Key Distribution (QKD) is the future of secure communication.

---

## What This Project Does

A complete end-to-end demonstration of three interconnected concepts:

1. **Classical RSA-32** — how RSA encryption works at a toy scale (16-bit primes, 32-bit keypair)
2. **Shor's Algorithm** — how a quantum computer can factor the RSA modulus and break the key
3. **QKD as the solution** — why Quantum Key Distribution is resistant to quantum attacks

The narrative follows **Alice and Bob** — two classical endpoints exchanging encrypted messages — before a simulated quantum adversary breaks their encryption using Shor's algorithm.

---

## Sample Output

```bash
# Classical RSA-32 Demo
$ python3 rsa32.py
Public key:  (65537, 2597186087)
Private key: (1857787721, 2597186087)
Encrypted:   [2168329762, 929378014, 1837098201, 1837098201, 775581511, 1223505621, 544041507, 2014454398, 118268784]
Decrypted:   HELLO RSA

# Alice → Bob Communication
$ python3 communication.py
Alice sends:       HELLO BOB!
Encrypted payload: [47307824, 1801068400, 2117272267, 2117272267, 2763884334, 1907958358, 2335389545, 2763884334, 2335389545, 2771420592]
Bob receives:      HELLO BOB!

# Quantum Attack
$ python3 shor_attack.py
[+] Toy demo → factors of 15: [[3, 5]]
[+] RSA key exposed. Private key can now be reconstructed.
[i] Skipping real modulus demo. Run with --real to enable.
```

---

## Features

- **16-bit prime generation** using `secrets` module (CSPRNG) and 32-bit RSA keypair construction
- **Message padding, encryption & decryption** using standard RSA operations
- **Alice ↔ Bob secure channel simulation** — full message lifecycle
- **Quantum payload export** — public modulus and ciphertext passed to the attack module
- **Shor's algorithm demo** on `N = 15` using a local Qiskit simulator
- **Hardware-ready hook** for larger moduli via `--real` flag (see Limitations)
- **Pinned reproducible environment** — exact Qiskit 0.25.x stack
- **SECURITY.md** — documents known simplifications and fixes

---

## Project Structure

```
rsa32-shor-attack-simulation/
├── rsa32.py                # Classical RSA-32 implementation
├── communication.py        # Alice↔Bob secure channel simulation
├── quantum_payload.py      # Exports public modulus & ciphertext for attack
├── shor_attack.py          # Shor's algorithm demo (N=15)
├── requirements_legacy.txt # Pinned Qiskit 0.25.0 environment
├── SECURITY.md             # Security notes and known simplifications
└── README.md
```

---

## Prerequisites

- **Python 3.x** — for classical RSA demos (no external packages needed)
- **Python 3.8** — required for the Qiskit quantum demo
- **Git** — to clone the repo

> Install Python 3.8 via your OS package manager or the [deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) on Ubuntu/Pop!_OS.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sumeya-hussein/rsa32-shor-attack-simulation.git
cd rsa32-shor-attack-simulation
```

### 2. Classical demo

No external dependencies. Just run with your system Python:

```bash
python3 rsa32.py
python3 communication.py
python3 quantum_payload.py
```

### 3. Quantum demo environment

Create and activate a Python 3.8 virtual environment:

```bash
python3.8 -m venv qkd-legacy
source qkd-legacy/bin/activate        # Linux/macOS
# qkd-legacy\Scripts\activate         # Windows
```

Install the pinned Qiskit stack:

```bash
pip install --upgrade pip
pip install -r requirements_legacy.txt --use-deprecated=legacy-resolver
```

---

## Usage

```bash
# Step 1 — Generate RSA-32 keys and encrypt/decrypt a message
python3 rsa32.py

# Step 2 — Simulate Alice → Bob encrypted communication
python3 communication.py

# Step 3 — Export public key data for quantum attack
python3 quantum_payload.py

# Step 4 — Run Shor's algorithm (activate qkd-legacy venv first)
source qkd-legacy/bin/activate
python3 shor_attack.py

# Optional — attempt real 32-bit factoring (WARNING: may take very long)
python3 shor_attack.py --real
deactivate
```

---

## Dependencies

Pinned in `requirements_legacy.txt` for full reproducibility:

```
qiskit==0.25.0
qiskit-terra==0.17.0
qiskit-aer==0.8.0
qiskit-ignis==0.6.0
qiskit-ibmq-provider==0.12.2
qiskit-aqua==0.9.0
```

Padding block size defaults to **4 bytes** in `rsa32.py` — adjustable as needed.

---

## ⚠️ Limitations

This is an **educational simulation**, not a production attack tool. Be aware of the following constraints:

| Limitation | Detail |
|---|---|
| Shor's demo uses `N = 15` | Factoring 3 × 5 is the standard textbook demo for near-term quantum hardware |
| 32-bit RSA factoring not yet possible | Requires ~64 stable, error-corrected logical qubits — beyond current hardware |
| Qiskit 0.25.0 is legacy | Modern Qiskit (1.x) has breaking API changes; migration is a planned future step |
| Simulator only | No real IBM Quantum hardware was used — results are noiseless |
| Prime generation | Uses `secrets.randbits()` — CSPRNG compliant for educational use |

Understanding these limits *is the point*. The gap between `N = 15` and real-world RSA-2048 illustrates exactly why post-quantum cryptography is an active research field today.

---

## What You'll Learn

- How RSA key generation, encryption, and decryption work at a fundamental level
- Why the security of RSA depends entirely on the difficulty of integer factorisation
- How Shor's algorithm achieves polynomial-time factoring on a quantum computer
- Why QKD (e.g. BB84 protocol) is theoretically immune to quantum attacks
- The current gap between quantum theory and practical quantum hardware

---

## Real-World Context

In August 2024, NIST published its first finalised **post-quantum cryptographic standards** (FIPS 203, 204, 205) in direct response to the threat Shor's algorithm poses to RSA and ECC. This project is a hands-on demonstration of exactly the threat model those standards are designed to address.

---

## Changelog

### v1.1.0
- fix: replaced `random` with `secrets` for CSPRNG compliance
- fix: null bytes excluded from encryption to prevent ciphertext leakage
- fix: `quantum_payload.py` wrapped in function to remove import side effects
- fix: `shor_attack.py` requires `--real` flag to attempt 32-bit factoring
- docs: added docstrings and type hints across all modules
- docs: added `SECURITY.md` with known simplifications and fixes
- docs: updated README to reflect real terminal output and new files

---

## Future Work

- [ ] Migrate to Qiskit 1.x API
- [ ] Add BB84 QKD simulation as a secure alternative
- [ ] Demonstrate on IBM Quantum hardware (ibm_nairobi or similar)
- [ ] Extend to ECC (Elliptic Curve Cryptography) attack via quantum algorithms
- [ ] Add visual circuit diagrams for Shor's algorithm steps
- [ ] Add pytest test suite for RSA functions

---

## Contributing

Found a bug or want to extend the demo? Open an issue or submit a pull request. All skill levels welcome — this project is intentionally beginner-readable.

---

## Author

**Sumaya Hussein Ismail**
[LinkedIn](https://www.linkedin.com/in/sumeya-hussein-ismail-0148a0332) · [GitHub](https://github.com/Sumeya-hussein) · [YouTube](https://youtube.com/@sumeya-hussein)

---

## License

MIT License — see [LICENSE](LICENSE) for details.
