# Simple-Caeser-Cipher-Program
A college project to learn about concepts of Symmetric Key Cryptography.

Project Overview: Symmetric Key Cryptography with Caesar Cipher & Password Authentication
This Python-based GUI application demonstrates symmetric key cryptography using the Caesar Cipher for encryption and decryption, combined with password authentication using hashing for security. The project simulates how a private key (Caesar Cipher shift value) is generated and securely used for decryption by the receiver.
------------------------------------------------------------------------------------------------------------------

[ Components & Flow ]

1.Password Authentication:

> The user must set and verify a password before accessing encryption and decryption functionality.
> The password is hashed using a secure hashing algorithm to ensure that the original password is not stored or transmitted in plain text.
> Password authentication adds a layer of security, ensuring only authorized users can encrypt or decrypt messages.

2.Caesar Cipher Encryption:

> Once the password is authenticated, the user can encrypt messages using the Caesar Cipher.
> The Caesar Cipher is a simple substitution cipher where each letter in the message is shifted by a certain number of positions (the shift value or private key).
> The user can either manually provide a shift value for encryption or generate a random private key.
> After encryption, the encrypted message is displayed on the GUI.

3.Private Key Generation:

> The system includes a feature to generate a random private key (the Caesar Cipher shift value) and store it in a private_key.json file.
> This private key simulates a symmetric key used to decrypt the encrypted message on the receiver’s end.
> The private key is securely "sent" to the receiver (simulated by saving it to the JSON file).

4.Caesar Cipher Decryption:

> The receiver can decrypt the encrypted message using the private key.
> The private key (shift value) is retrieved from the private_key.json file, and the encrypted message is decrypted using the Caesar Cipher logic.
> The decrypted message is then displayed on the GUI.
------------------------------------------------------------------------------------------------------------------

[ Detailed Working and Logic ]

1. Password Creation & Authentication (in auth.py):

The password system ensures that only authorized users can encrypt or decrypt messages. Here's how it works:

> Password Hashing:
When the user enters a password, it is hashed using a hashing function (e.g., hashlib with a salt).
The hashed password is stored securely, preventing the storage of the raw password.
> Password Verification:
To authenticate, the user must enter the correct password.
The system hashes the entered password again and compares it with the stored hash. If they match, the user is authenticated.

2. Caesar Cipher for Encryption & Decryption (in caesar_cipher.py):

The Caesar Cipher shifts each letter in the message by a specified number of positions (the shift value). This shift value acts as the private key.

Encryption:

> Each character in the message is shifted forward by the shift value.
Example: With a shift of 3, "HELLO" becomes "KHOOR".
Decryption:

> The reverse of encryption. Each character is shifted backward by the same shift value (private key).
Example: With a shift of 3, "KHOOR" becomes "HELLO".

3. Private Key Generation and Storage:

The private key (shift value) is generated randomly and stored in a private_key.json file. This simulates sending the key from the sender to the receiver securely.

> The key is stored as a JSON object for easy retrieval during decryption.
> The receiver uses this key (shift value) to decrypt the message.
> Note : Private Key String can be salted to make it secure but for the sake of simplicity it's just a code element.

4. GUI Flow & Logic (in gui.py):

The GUI is designed using Tkinter and is structured to enable encryption/decryption only after successful password verification.

> Initial State: The encryption and decryption fields are disabled by default until the user sets and verifies the password.
> Password Handling: The user sets a password, which is hashed and stored. Once the password is verified, the encryption/decryption fields are enabled.
> Encryption: The user enters a message and manually provides or generates a shift value to encrypt the message.
> Decryption: The receiver uses the private key from the file to decrypt the encrypted message.
------------------------------------------------------------------------------------------------------------------

[ Key Security Features ]

> Password Hashing: Passwords are never stored in plain text; instead, they are securely hashed.
> Symmetric Encryption: The private key (shift value) used for encryption is the same key used for decryption.
> Private Key Management: The private key is stored securely in a file and must be used by the receiver to decrypt the message.
------------------------------------------------------------------------------------------------------------------

[ Final Flow ]

Step 1: Set and verify the password.
Step 2: Encrypt a message by entering a shift value or generating a private key.
Step 3: Decrypt the message by using the private key stored in private_key.json.

------------------------------------------------------------------------------------------------------------------
This project illustrates the basic principles of symmetric key cryptography with Caesar Cipher, adding authentication via password hashing for security.
