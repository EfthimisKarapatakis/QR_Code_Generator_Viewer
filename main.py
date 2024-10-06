import os
import qrcode
from PIL import Image  # Pillow module to handle images

# Get the link from the user
link = str(input("Enter the link here: "))

# Generate the QR code and save it as a PNG file
img = qrcode.make(link)
name = str(input("Enter file name here: "))
img.save(f"{name}.png", "PNG")

# Cross-platform approach to open/display the image
try:
    img = Image.open("qr.png")
    img.show()  # This will display the image in the default image viewer
except Exception as e:
    print(f"Unable to display image: {e}")
