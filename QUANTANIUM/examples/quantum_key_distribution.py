from quantum_defense import qkd_protocol, classical_post_processing

# Example of Quantum Key Distribution (QKD) for secure key exchange

def quantum_key_distribution(sender, receiver):
    # Step 1: Initialize QKD protocol
    qkd_session = qkd_protocol.initialize_session(sender, receiver)

    # Step 2: Exchange quantum bits (qubits)
    raw_key_sender, raw_key_receiver = qkd_protocol.exchange_qubits(qkd_session)
    print(f"Raw key (sender): {raw_key_sender}")
    print(f"Raw key (receiver): {raw_key_receiver}")

    # Step 3: Perform classical post-processing
    final_key_sender = classical_post_processing.process_key(raw_key_sender)
    final_key_receiver = classical_post_processing.process_key(raw_key_receiver)

    # Step 4: Verify key integrity
    if final_key_sender == final_key_receiver:
        print("Quantum key distribution successful. Keys match.")
    else:
        print("Key mismatch detected. QKD failed.")

# Example usage
if __name__ == "__main__":
    sender_id = "Alice"
    receiver_id = "Bob"

    try:
        quantum_key_distribution(sender_id, receiver_id)
    except Exception as e:
        print(f"An error occurred during QKD: {e}")