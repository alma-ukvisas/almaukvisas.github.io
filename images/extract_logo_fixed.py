from PIL import Image
import os

# Open the business card image
img = Image.open('/home/ubuntu/alma_landing_page/images/business_card.jpeg')

# Crop the logo portion with more padding to avoid cutoff
# Adjusting coordinates to capture more of the logo
logo = img.crop((120, 120, 270, 270))

# Save the logo
logo.save('/home/ubuntu/alma_landing_page/images/alma_logo_fixed.png')

print("Logo extracted with improved dimensions and saved successfully!")
