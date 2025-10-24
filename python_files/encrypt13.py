def shift_character(char, key):
    """Shifts a single alphabetic character by the key value."""
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + key) % 26 + base)
    else:
        return char


def encrypt_message(message, key):
    """Encrypts the message using Caesar cipher."""
    encrypted = ""
    for char in message:
        encrypted += shift_character(char, key)
    return encrypted


def main():
    """Main function to run the Caesar cipher program."""
    print("=== Caesar Cipher Encryption ===")
    message = input("Enter a message to encrypt: ")
    key = int(input("Enter a shift key (1-25): "))

    encrypted_text = encrypt_message(message, key)
    
    print("\nOriginal Message:", message)
    print("Encrypted Message:", encrypted_text)


main()
    
