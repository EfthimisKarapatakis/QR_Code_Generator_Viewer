# 📱 QR Code Generator and Viewer
This Python script allows users to generate a QR code from a provided URL or text and save it as a PNG image. It also includes functionality to automatically open and display the generated QR code using the default image viewer on your operating system.

## Features:
* User Input: Prompts the user to enter a URL or text that will be encoded into the QR code.
* QR Code Generation: Generates a QR code using the QR code library and saves it as a PNG file.
* Custom Filename: The user can specify the filename for the saved QR code image.
* Cross-Platform Image Display: Attempts to open and display the generated QR code using the default image viewer, supported by the Pillow library (PIL).

## Requirements:
* qrcode
* Pillow (PIL)

## Usage:
1. Run the script.
2. Enter the link or text you want to convert into a QR code.
3. Specify the filename to save the image.
4. The QR code will be generated and saved as a PNG file.
5. The script will attempt to automatically open the generated image in your default image viewer.
