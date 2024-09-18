#write extension as well in giving input
import os

def encrypt(text, shift):
    """Encrypt the given text using a Caesar cipher."""
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text, shift):
    """Decrypt the given text using a Caesar cipher."""
    return encrypt(text, -shift)

def encrypt_file(input_file, shift):
    """Encrypt a .txt file and save as .env file."""
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        encrypted_text = encrypt(text, shift)
        output_file = os.path.splitext(input_file)[0] + ".env"
        with open(output_file, 'w') as file:
            file.write(encrypted_text)
        print(f"File encrypted and saved as {output_file}.")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")

def decrypt_file(input_file, shift):
    """Decrypt a .env file and save as .txt file."""
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        decrypted_text = decrypt(text, shift)
        output_file = os.path.splitext(input_file)[0] + ".txt"
        with open(output_file, 'w') as file:
            file.write(decrypted_text)
        print(f"File decrypted and saved as {output_file}.")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")

def main():
    """Main function to handle encryption and decryption for files."""
    print("Simple Encryption/Decryption Tool for .txt to .env and vice versa")
    choice = input("Choose an option:\n1. Encrypt a .txt file to .env\n2. Decrypt a .env file to .txt\nChoice: ")

    if choice == '1':
        input_file = input("Enter the input .txt file path: ")
        shift = int(input("Enter the shift value: "))
        encrypt_file(input_file, shift)
    elif choice == '2':
        input_file = input("Enter the input .env file path: ")
        shift = int(input("Enter the shift value: "))
        decrypt_file(input_file, shift)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
