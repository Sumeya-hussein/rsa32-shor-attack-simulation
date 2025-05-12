from rsa32 import generate_keys, encrypt

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    message = "QUANTUM"
    cipher_text = encrypt(message, public_key)

    payload_for_quantum_attack = {
        "modulus_n": public_key[1],
        "encrypted_message": cipher_text
    }

    print("Payload prepared for quantum attack (Shor's algorithm):")
    print(payload_for_quantum_attack)
