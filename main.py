```python
import logging
from utils import load_config, log_setup
from cryptography import simulate_quantum_encryption, simulate_quantum_decryption
from network import simulate_network_attack
from data_extraction import extract_sensitive_data

def main():
    # Setup logging
    log_setup()
    
    # Load configuration
    config = load_config()
    
    # Display loaded configuration URLs for reference
    logging.info("Loaded configuration URLs:")
    for key, value in config.items():
        if "url" in key:
            logging.info(f"{key}: {value}")
    
    # Simulate network attack
    simulate_network_attack()
    
    # Extract sensitive data
    extract_sensitive_data()
    
    # Example data to encrypt and decrypt
    example_data = "Hello, Quantum World!"
    logging.info(f"Original data: {example_data}")
    
    # Encrypt data
    encrypted_data = simulate_quantum_encryption(example_data)
    logging.info(f"Encrypted data: {encrypted_data}")
    
    # Decrypt data
    decrypted_data = simulate_quantum_decryption(encrypted_data)
    logging.info(f"Decrypted data: {decrypted_data}")

if __name__ == "__main__":
    main()
```
