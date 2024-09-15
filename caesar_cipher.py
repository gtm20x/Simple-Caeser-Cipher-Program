# caesar_cipher.py
def encrypt_caesar(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep special characters unchanged
    return result

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)  # Decrypt by shifting backwards
