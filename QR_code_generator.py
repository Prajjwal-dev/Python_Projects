import qrcode


class QRCodeGenerator:
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def generate_qr_code(self, data, filename):
        """Generate a QR code and save it as an image file."""
        self.qr.add_data(data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill='black', back_color='white')
        img.save(filename)
        print(f"QR Code saved as '{filename}'.")


def menu():
    """Display the menu and handle user choices."""
    qr_generator = QRCodeGenerator()

    while True:
        print("\nQR Code Generator Menu:")
        print("1. Generate QR Code")
        print("2. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                data = input("Enter the data to encode in the QR code: ")
                filename = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")
                qr_generator.generate_qr_code(data, filename)
            case "2":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 2.")


if __name__ == "__main__":
    menu()
