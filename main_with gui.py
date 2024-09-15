import tkinter as tk
from tkinter import messagebox
from caesar_cipher import encrypt_caesar, decrypt_caesar
from auth import hash_password, verify_password
import random
import json
import os

# Global variables for password hashing and key storage
hashed_password = None
private_key_file = "private_key.json"

# Function to set password
def set_password():
    global hashed_password
    password = password_entry.get()
    hashed_password = hash_password(password)
    messagebox.showinfo("Password Set", "Password has been hashed and stored.")
    # Enable password verification button
    verify_button.config(state=tk.NORMAL)

# Function to verify password
def verify_user_password():
    input_password = password_entry.get()
    if hashed_password and verify_password(input_password, hashed_password):
        messagebox.showinfo("Success", "Password verified successfully!")
        # Enable the encryption and decryption options once password is verified
        enable_encryption_decryption()
    else:
        messagebox.showerror("Error", "Password verification failed.")
        disable_encryption_decryption()

# Function to enable encryption/decryption fields and buttons
def enable_encryption_decryption():
    message_entry.config(state=tk.NORMAL)
    shift_entry.config(state=tk.NORMAL)
    encrypt_button.config(state=tk.NORMAL)
    decrypt_button.config(state=tk.NORMAL)
    generate_key_button.config(state=tk.NORMAL)

# Function to disable encryption/decryption fields and buttons
def disable_encryption_decryption():
    message_entry.config(state=tk.DISABLED)
    shift_entry.config(state=tk.DISABLED)
    encrypt_button.config(state=tk.DISABLED)
    decrypt_button.config(state=tk.DISABLED)
    generate_key_button.config(state=tk.DISABLED)

# Function to generate and "send" the private key
def generate_private_key():
    shift = random.randint(1, 25)  # Random shift between 1 and 25
    # Save the key in a file or send it through unknown sources
    with open(private_key_file, 'w') as f:
        json.dump({"shift": shift}, f)
    messagebox.showinfo("Key Sent", f"Private key (shift value) has been generated and sent.\nShift: {shift}")

# Function to encrypt message
def encrypt_message():
    plaintext = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = encrypt_caesar(plaintext, shift)
    result_label.config(text=f"Encrypted Message: {encrypted_message}")

# Function to decrypt message using the entered key
def decrypt_message():
    encrypted_message = message_entry.get()
    try:
        if os.path.exists(private_key_file):
            with open(private_key_file, 'r') as f:
                key_data = json.load(f)
            shift = key_data["shift"]
            decrypted_message = decrypt_caesar(encrypted_message, shift)
            result_label.config(text=f"Decrypted Message: {decrypted_message}")
        else:
            messagebox.showerror("Error", "Private key not found!")
    except ValueError:
        messagebox.showerror("Error", "Invalid key or encrypted message.")

# Main GUI window
window = tk.Tk()
window.title("Symmetric Key Cryptography with Caesar Cipher & Authentication")

# Password Input
tk.Label(window, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(window, show="*", width=40)
password_entry.pack()

# Password Set Button
tk.Button(window, text="Set Password", command=set_password).pack(pady=5)

# Password Verification Button (disabled until password is set)
verify_button = tk.Button(window, text="Verify Password", command=verify_user_password, state=tk.DISABLED)
verify_button.pack(pady=5)

# Message Input (disabled until password is verified)
tk.Label(window, text="Enter Message:").pack(pady=5)
message_entry = tk.Entry(window, width=40, state=tk.DISABLED)
message_entry.pack()

# Shift Input for Sender (disabled until password is verified)
tk.Label(window, text="Enter Shift (Key) for Encryption:").pack(pady=5)
shift_entry = tk.Entry(window, width=10, state=tk.DISABLED)
shift_entry.pack()

# Encrypt Button (disabled until password is verified)
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message, state=tk.DISABLED)
encrypt_button.pack(pady=5)

# Generate & Send Key Button (disabled until password is verified)
generate_key_button = tk.Button(window, text="Generate & Send Private Key", command=generate_private_key, state=tk.DISABLED)
generate_key_button.pack(pady=5)

# Decrypt Button (disabled until password is verified)
decrypt_button = tk.Button(window, text="Decrypt with Received Key", command=decrypt_message, state=tk.DISABLED)
decrypt_button.pack(pady=5)

# Result Label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the GUI loop
window.mainloop()
