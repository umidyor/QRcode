#pip install pyqrcode
#pip install pypng

import pyqrcode

text = input("Enter your text: ")
name = input("Enter a desired name for the QRcode>> ")
scale = int(input("Select the size you want for the QRcode>> "))

qrcode = pyqrcode.create(text, error='L', version=10)
qrcode.png(f"{name}.png", scale=scale)
