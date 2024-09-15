# main.py
from caesar_cipher import encrypt_caesar, decrypt_caesar
from auth import hash_password, verify_password

def main():
    # Step 1: User password authentication
    password = input("Set your password: ")
    hashed_password = hash_password(password)
    print("Password has been hashed and stored!")

    # Verify password
    input_password = input("Enter your password for verification: ")
    if verify_password(input_password, hashed_password):
        print("Password verified successfully!")
    else:
        print("Password verification failed.")
        return

    # Step 2: Caesar Cipher - Encryption/Decryption
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").lower()

    if choice == 'e':
        plaintext = input("Enter message to encrypt: ")
        shift = int(input("Enter shift (key): "))
        encrypted_message = encrypt_caesar(plaintext, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        encrypted_message = input("Enter message to decrypt: ")
        shift = int(input("Enter shift (key): "))
        decrypted_message = decrypt_caesar(encrypted_message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
