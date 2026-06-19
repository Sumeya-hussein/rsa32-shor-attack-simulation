"""
shor_attack.py — Demonstrates Shor's quantum factoring algorithm using Qiskit.
Factors N=15 as a toy demo, with an optional hook for the real RSA-32 modulus.

Requires the qkd-legacy virtual environment (Python 3.8 + Qiskit 0.25.0).
Educational demonstration only — not suitable for production use.
"""

import sys
from qiskit import Aer
from qiskit.aqua.algorithms import Shor
from qiskit.utils import QuantumInstance
from quantum_payload import payload_for_quantum_attack


def toy_demo() -> QuantumInstance:
    """
    Run Shor's algorithm on N=15 (3x5) as a toy demonstration.
    This is the standard textbook example for near-term quantum hardware.

    Returns:
        QuantumInstance used for the simulation (reusable for real_demo)
    """
    N = 15
    qi = QuantumInstance(Aer.get_backend("aer_simulator"))
    shor = Shor(N)
    result = shor.run(quantum_instance=qi)
    factors = result.get('factors') or result.get('factors_list')
    print(f"[+] Toy demo → factors of {N}: {factors}")
    print(f"[+] RSA key exposed. Private key can now be reconstructed.")
    return qi


def real_demo(qi: QuantumInstance) -> None:
    """
    Attempt to factor the real RSA-32 modulus from quantum_payload.py.

    WARNING: This may run for a very long time or crash on a local simulator.
    32-bit factoring requires ~64 stable logical qubits — beyond current hardware.
    Run with --real flag to enable.

    Args:
        qi: QuantumInstance from toy_demo()
    """
    rsa_N = payload_for_quantum_attack["modulus_n"]
    print(f"\n[!] Attempting to factor real RSA-32 modulus: {rsa_N}")
    print(f"[!] Warning: this may take a very long time on a simulator.")
    shor = Shor(rsa_N)
    result = shor.run(quantum_instance=qi)
    print(f"[+] Factors: {result.get('factors')}")


if __name__ == "__main__":
    qi = toy_demo()
    if "--real" in sys.argv:
        real_demo(qi)
    else:
        print("\n[i] Skipping real modulus demo.")
        print("[i] Run with --real flag to attempt 32-bit factoring.")
