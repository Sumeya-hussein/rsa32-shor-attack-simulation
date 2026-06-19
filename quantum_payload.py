"""
quantum_payload.py — Generates an RSA-32 keypair and encrypts a sample message
to produce a payload for Shor's algorithm attack demonstration.

Educational demonstration only — not suitable for production use.
"""

from rsa32 import generate_keys, encrypt


def generate_quantum_payload() -> dict:
    """
    Generate a fresh RSA-32 keypair and encrypt a sample message.
    Wrapped in a function to avoid side effects on import.

    Returns:
        Dict containing the public modulus and encrypted message
    """
    public_key, _ = generate_keys()
    n = public_key[1]
    cipher = encrypt("QUANTUM", public_key)
    return {
        "modulus_n": n,
        "encrypted_message": cipher
    }


payload_for_quantum_attack = generate_quantum_payload()


if __name__ == "__main__":
    print("Payload prepared for quantum attack (Shor's algorithm):")
    print(f"  Modulus n:         {payload_for_quantum_attack['modulus_n']}")
    print(f"  Encrypted message: {payload_for_quantum_attack['encrypted_message']}")
