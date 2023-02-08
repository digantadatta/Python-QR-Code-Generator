import qrcode as qr
img= qr.make("This is a test image and will be displayed as QRCode")
img.save("Google_Link_Code.png")
