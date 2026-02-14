# This project is created for coursework 
""" 
Message Encryption and Decryption Tool
Course:Introduction to Programming 
Student:Yunika Parajuli
This program allows users to encrypt and decrypt messages
using a key-based encryption technique.
"""
# Function to encrypt the message 
def encrypt(message, key):
    encrypted = ""
    key = key.lower()
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.islower():
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            encrypted += char

    return encrypted

# Function to decrypt the message 
def decrypt(message, key):
    decrypted = ""
    key = key.lower()
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.islower():
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            decrypted += char

    return decrypted


print("Welcome to the Message Encryption & Decryption Tool")
print("This program allows you to encrypt or decrypt messages.")
print("Please follow the options below:\n")
print("1. Encrypt Message")
print("2. Decrypt Message")

choice = input("Enter your choice (1 or 2): ")

text = input("Enter the message you want to encrypt/decrypt: ")
key = input("Enter key (letters only): ")

if choice == "1":
    result = encrypt(text, key)
    print("Encrypted Message:",result)
elif choice == "2":
    result = decrypt(text, key)
    print("Decrypted Message:", result)
else:
    print("Invalid choice! Please enter 1 for Encrypt or 2 for Decrypt. ")




