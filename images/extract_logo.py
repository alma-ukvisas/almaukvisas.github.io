from PIL import Image
import os

# Open the business card image
img = Image.open('/home/ubuntu/alma_landing_page/images/business_card.jpeg')

# Crop the logo portion (adjust coordinates as needed)
# These coordinates are approximate based on the business card image
logo = img.crop((134, 134, 250, 250))

# Save the logo
logo.save('/home/ubuntu/alma_landing_page/images/alma_logo.png')

print("Logo extracted and saved successfully!")
