"""
rsa32.py — Toy RSA-32 implementation for educational purposes.
Demonstrates key generation, encryption, and decryption using
16-bit primes and a 32-bit modulus.

NOTE: Not suitable for production use.
"""

import secrets
from math import gcd


def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(bits: int) -> int:
    """Generate a random prime number of the given bit length using CSPRNG."""
    while True:
        candidate = secrets.randbits(bits)
        candidate |= (1 << bits - 1) | 1
        if is_prime(candidate):
            return candidate


def multiplicative_inverse(e: int, phi: int) -> int:
    """Compute the modular multiplicative inverse of e mod phi using the extended Euclidean algorithm."""
    x, y, u, v = 0, 1, 1, 0
    a, b = e, phi
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x % phi


def generate_keys() -> tuple:
    """
    Generate a 32-bit RSA keypair.

    Returns:
        Tuple of (public_key, private_key) where each key is (exponent, modulus)
    """
    p = generate_prime(16)
    q = generate_prime(16)
    while q == p:
        q = generate_prime(16)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))


def pad_message(message: str, block_size: int = 4) -> bytes:
    """
    Pad a message to align to block_size bytes using null bytes.

    Args:
        message: Plaintext string to pad
        block_size: Block alignment size in bytes (default 4)

    Returns:
        Padded bytes object
    """
    padded = message.encode('utf-8')
    while len(padded) % block_size != 0:
        padded += b'\x00'
    return padded


def encrypt(message: str, pub_key: tuple) -> list:
    """
    Encrypt a plaintext string using RSA.
    Null bytes are excluded to prevent ciphertext leakage.

    Args:
        message: Plaintext string (null bytes stripped automatically)
        pub_key: Tuple of (e, n) — the public key

    Returns:
        List of integer ciphertext blocks
    """
    e, n = pub_key
    return [pow(ord(char), e, n) for char in message if char != '\x00']


def decrypt(ciphertext: list, priv_key: tuple) -> str:
    """
    Decrypt a list of RSA ciphertext integers back to plaintext.

    Args:
        ciphertext: List of encrypted integer blocks
        priv_key: Tuple of (d, n) — the private key

    Returns:
        Decrypted plaintext string
    """
    d, n = priv_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext]).rstrip('\x00')


if __name__ == "__main__":
    public_key, private_key = generate_keys()
    message = "HELLO RSA"
    print(f"Public key:  {public_key}")
    print(f"Private key: {private_key}")
    cipher_text = encrypt(message, public_key)
    print(f"Encrypted:   {cipher_text}")
    print(f"Decrypted:   {decrypt(cipher_text, private_key)}")
