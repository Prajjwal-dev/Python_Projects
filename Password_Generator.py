import random
import string


class PasswordGenerator:
    def __init__(self, length=12, use_special_chars=True):
        self.length = length
        self.use_special_chars = use_special_chars
        self.characters = string.ascii_letters + string.digits
        if use_special_chars:
            self.characters += string.punctuation

    def generate_password(self):
        """Generate a random password."""
        return ''.join(random.choice(self.characters) for _ in range(self.length))

    def save_password_to_file(self, password, filename='password.txt'):
        """Save the generated password to a file."""
        with open(filename, 'w') as file:
            file.write(password)
        print(f"Password saved to {filename}")


def main():
    print("Welcome to the Password Generator!")

    # User input for password settings
    length = int(input("Enter the desired length of the password: "))
    use_special_chars = input("Include special characters (Y/N)? ").strip().lower() == 'y'

    # Generate and display the password
    generator = PasswordGenerator(length, use_special_chars)
    password = generator.generate_password()
    print(f"Generated Password: {password}")

    # Optionally save the password to a file
    save_to_file = input("Would you like to save the password to a file? (Y/N) ").strip().lower()
    if save_to_file == 'y':
        filename = input("Enter the filename (default is 'password.txt'): ").strip() or 'password.txt'
        generator.save_password_to_file(password, filename)


if __name__ == "__main__":
    main()
