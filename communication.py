"""
communication.py — Simulates an encrypted message exchange between Alice and Bob
using the RSA-32 implementation from rsa32.py.

Educational demonstration only — not suitable for production use.
"""

from rsa32 import generate_keys, encrypt, decrypt, pad_message


def alice_sends(message: str, bob_public_key: tuple) -> list:
    """
    Alice pads and encrypts a message using Bob's public key.

    Args:
        message: Plaintext string to send
        bob_public_key: Bob's RSA public key tuple (e, n)

    Returns:
        List of encrypted integer blocks
    """
    padded_message = pad_message(message)
    cipher = encrypt(padded_message.decode(), bob_public_key)
    return cipher


def bob_receives(cipher: list, bob_private_key: tuple) -> str:
    """
    Bob decrypts a received ciphertext using his private key.

    Args:
        cipher: List of encrypted integer blocks
        bob_private_key: Bob's RSA private key tuple (d, n)

    Returns:
        Decrypted plaintext string
    """
    return decrypt(cipher, bob_private_key)


if __name__ == "__main__":
    public_key, private_key = generate_keys()
    message = "HELLO BOB!"
    print(f"Alice sends:       {message}")
    cipher_payload = alice_sends(message, public_key)
    print(f"Encrypted payload: {cipher_payload}")
    received_payload = bob_receives(cipher_payload, private_key)
    print(f"Bob receives:      {received_payload}")
