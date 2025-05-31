# Extract QR code from business card
from PIL import Image
import os

# Open the business card image
img = Image.open('/home/ubuntu/alma_landing_page/images/business_card.jpeg')

# Crop the QR code portion (adjust coordinates as needed)
qr_code = img.crop((780, 80, 1170, 470))

# Save the QR code
qr_code.save('/home/ubuntu/alma_landing_page/images/whatsapp_qr.png')

print("QR code extracted and saved successfully!")
