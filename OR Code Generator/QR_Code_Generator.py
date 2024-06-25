import qrcode

def generate_qr_code(content, filename):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    print("\t\t\tWelcome to the QR Code Generator!")
    choice = input("Would you like to generate a QR code for a \n\t(1) URL  \n\t(2) Simple Text? \n\nEnter 1 or 2: ")

    if choice == '1':
        url = input("Please enter the URL: ")
        filename = "qrcode_url.png"
        generate_qr_code(url, filename)
        print(f"QR code for the URL has been generated and saved as {filename}.")

    elif choice == '2':
        text = input("Please enter the text: ")
        filename = "qrcode_text.png"
        generate_qr_code(text, filename)
        print(f"QR code for the text has been generated and saved as {filename}.")
        
    else:
        print("Invalid choice. Please run the program again and enter 1 or 2.")