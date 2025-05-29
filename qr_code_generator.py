import qrcode
from PIL import Image

# URL to encode
url = "https://kayra-warsaw-web.lovable.app"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image
image_path = "/mnt/data/qr_code_kayra.png"
img.save(image_path)

image_path
