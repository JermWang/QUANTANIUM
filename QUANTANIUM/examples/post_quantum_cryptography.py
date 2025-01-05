from quantanium_sdk import PostQuantumCrypto

# Example usage of Post-Quantum Cryptography
pqc = PostQuantumCrypto()
message = "Secure this transaction."
secure_message = pqc.encrypt(message)
decrypted_message = pqc.decrypt(secure_message)
print(f"Decrypted Message: {decrypted_message}")