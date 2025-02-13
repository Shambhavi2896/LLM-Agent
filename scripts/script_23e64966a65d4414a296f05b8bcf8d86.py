import os
import json
import requests
from PIL import Image
import pytesseract

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_image_path = os.path.join(data_dir, 'credit_card.png')
output_text_path = os.path.join(data_dir, 'credit-card.txt')

# Ensure the output file exists
if not os.path.exists(output_text_path):
    with open(output_text_path, 'w') as f:
        f.write('')  # Create a blank file if it doesn't exist

# Function to extract text from image
def extract_text_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None

# Function to call LLM for credit card extraction
def extract_credit_card_number(text):
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
        return None
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Prepare the data for the API call
    payload = {
        "model": "GPT-4o-Mini",
        "messages": [{"role": "user", "content": f"Extract the credit card number from the following text: {text}"}]
    }

    # Call the LLM API
    try:
        response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip().replace(" ", "")
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return None

# Main processing
if __name__ == "__main__":
    # Step 1: Extract text from image
    extracted_text = extract_text_from_image(input_image_path)
    if extracted_text:
        # Step 2: Extract credit card number using LLM
        credit_card_number = extract_credit_card_number(extracted_text)
        if credit_card_number:
            # Step 3: Write the credit card number to the output file
            with open(output_text_path, 'w') as output_file:
                output_file.write(credit_card_number)
                print(f"Credit card number extracted and written to {output_text_path}")
        else:
            print("No credit card number found.")
    else:
        print("Failed to extract text from the image.")