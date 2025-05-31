from PIL import Image
import os

# Open the business card image
img = Image.open('/home/ubuntu/alma_landing_page/images/business_card.jpeg')

# Crop the QR code portion with more padding to avoid cutoff
# Adjusting coordinates to capture the full QR code
qr_code = img.crop((760, 60, 1200, 500))

# Save the QR code
qr_code.save('/home/ubuntu/alma_landing_page/images/whatsapp_qr_fixed.png')

print("WhatsApp QR code extracted with improved dimensions and saved successfully!")
