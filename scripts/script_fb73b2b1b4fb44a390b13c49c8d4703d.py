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
    print(f"Error: The input file {image_path} does not exist.")
    exit(1)

# Function to extract text from the image using OCR
def extract_text_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return None

# Function to validate credit card number using Luhn's algorithm
def is_valid_credit_card(number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    return (sum(odd_digits) + sum(sum(digits_of(d * 2)) for d in even_digits)) % 10 == 0

# Function to extract credit card number from text
def extract_credit_card_number(text):
    # Find all sequences of digits that could be credit card numbers
    potential_numbers = ''.join(filter(str.isdigit, text)).split()
    for number in potential_numbers:
        if is_valid_credit_card(number):
            return number
    return None

# Extract text from the image
extracted_text = extract_text_from_image(image_path)

# Check if text extraction was successful
if extracted_text is None:
    print("Error: Could not extract text from the image.")
    exit(1)

# Extract credit card number from the text
credit_card_number = extract_credit_card_number(extracted_text)

# Check if a valid credit card number was found
if credit_card_number is None:
    print("Error: No valid credit card number found in the image.")
    exit(1)

# Write the credit card number to the output file without spaces
with open(output_path, 'w') as output_file:
    output_file.write(credit_card_number)

print(f"Credit card number extracted and saved to {output_path}.")