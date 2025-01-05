from quantum_defense import post_quantum_key_exchange, post_quantum_encrypt, post_quantum_decrypt

# Example of a secure communication using post-quantum cryptography

def secure_communication(sender_data, receiver_data):
    # Step 1: Key Exchange
    sender_public_key, sender_private_key = post_quantum_key_exchange.generate_keys()
    receiver_public_key, receiver_private_key = post_quantum_key_exchange.generate_keys()

    # Step 2: Encrypt the message using the receiver's public key
    encrypted_message = post_quantum_encrypt.encrypt_message(sender_data, receiver_public_key)
    print(f"Encrypted message: {encrypted_message}")

    # Step 3: Decrypt the message using the receiver's private key
    decrypted_message = post_quantum_decrypt.decrypt_message(encrypted_message, receiver_private_key)
    print(f"Decrypted message: {decrypted_message}")

    # Verify the integrity and authenticity of the message
    if decrypted_message == sender_data:
        print("The message was successfully decrypted and verified.")
    else:
        print("The message verification failed.")

# Example usage
if __name__ == "__main__":
    sender_data = "This is a confidential message."
    receiver_data = "Receiver's data placeholder."

    try:
        secure_communication(sender_data, receiver_data)
    except Exception as e:
        print(f"An error occurred during secure communication: {e}")