import os
import requests
from PIL import Image
import pytesseract

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Check if the input image exists
if not os.path.exists(image_path):
    print(f"Error: The input image '{image_path}' does not exist.")
else:
    # Load the image and perform OCR
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)

        # Extract credit card numbers using a regex
        import re
        credit_card_numbers = re.findall(r'\b\d{4}[-]?\d{4}[-]?\d{4}[-]?\d{4}\b', extracted_text)

        # Remove spaces and dashes
        cleaned_numbers = [number.replace('-', '').replace(' ', '') for number in credit_card_numbers]

        # Write the first found number to the output file
        if cleaned_numbers:
            with open(output_path, 'w') as f:
                f.write(cleaned_numbers[0])  # Write the first found number
        else:
            print("No credit card numbers found in the image.")

    except Exception as e:
        print(f"An error occurred during processing: {e}")