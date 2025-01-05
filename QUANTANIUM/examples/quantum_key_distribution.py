from quantanium_sdk import QuantumKeyDistribution

# Example usage of Quantum Key Distribution (QKD)
qkd = QuantumKeyDistribution()
key = qkd.generate_key()
print(f"Quantum Key: {key}")