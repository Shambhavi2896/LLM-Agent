import os
import requests
from PIL import Image
import pytesseract

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Ensure the output file exists
if not os.path.exists(output_path):
    with open(output_path, 'w') as f:
        pass

# Function to extract text from an image
def extract_text_from_image(image_path):
    try:
        # Open the image
        img = Image.open(image_path)
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None

# Function to call the LLM for credit card extraction
def extract_credit_card_number(text):
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
        return None

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Prepare the payload for the API call
    payload = {
        "model": "GPT-4o-Mini",
        "messages": [
            {"role": "user", "content": f"Extract the credit card number from the following text: {text}"}
        ]
    }

    # Make the API call
    response = requests.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        print(f"Error in API call: {response.status_code} - {response.text}")
        return None

# Extract text from image
extracted_text = extract_text_from_image(image_path)

if extracted_text:
    # Extract credit card number using LLM
    credit_card_number = extract_credit_card_number(extracted_text)

    if credit_card_number:
        # Remove spaces
        credit_card_number = credit_card_number.replace(" ", "")
        # Write the credit card number to the output file
        with open(output_path, 'w') as f:
            f.write(credit_card_number)
    else:
        print("No credit card number extracted.")
else:
    print("Failed to extract text from the image.")