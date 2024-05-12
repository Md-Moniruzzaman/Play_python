from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    # Step 1: Generate a key (keep this secret)
    secret_key = generate_key()
    print(secret_key)

    # Step 2: Encrypt a message
    original_message = "This is a secret message."
    encrypted_message = encrypt_message(original_message, secret_key)

    print(f"Original Message: {original_message}")
    print(f"Encrypted Message: {encrypted_message}")

    # Step 3: Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, secret_key)
    print(f"Decrypted Message: {decrypted_message}")
