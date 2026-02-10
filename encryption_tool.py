# This project is created for coursework 
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


print("MESSAGE ENCRYPTION & DECRYPTION TOOL")
print("1. Encrypt Message")
print("2. Decrypt Message")

choice = input("Enter your choice (1 or 2): ")

text = input("Enter your message: ")
key = input("Enter key (letters only): ")

if choice == "1":
    result = encrypt(text, key)
    print("Encrypted Message:", result)
elif choice == "2":
    result = decrypt(text, key)
    print("Decrypted Message:", result)
else:
    print("Invalid choice")




