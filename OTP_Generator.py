import random


class OTPGenerator:
    def __init__(self, length=6):
        self.length = length

    def generate_otp(self):
        """Generate a random OTP with the specified length."""
        otp = ''.join(random.choices('0123456789', k=self.length))
        return otp

    def save_otp_to_file(self, otp, filename='otp.txt'):
        """Save the generated OTP to a file."""
        with open(filename, 'w') as file:
            file.write(f"Your OTP: {otp}\n")
        print(f"OTP saved to {filename}")


def main():
    print("Welcome to the OTP Generator!")

    # User input for OTP settings
    length = int(input("Enter the desired length of the OTP (default is 6): ") or 6)

    # Generate and display the OTP
    generator = OTPGenerator(length)
    otp = generator.generate_otp()
    print(f"Generated OTP: {otp}")

    # Optionally save the OTP to a file
    save_to_file = input("Would you like to save the OTP to a file? (Y/N) ").strip().lower()
    if save_to_file == 'y':
        filename = input("Enter the filename (default is 'otp.txt'): ").strip() or 'otp.txt'
        generator.save_otp_to_file(otp, filename)


if __name__ == "__main__":
    main()
