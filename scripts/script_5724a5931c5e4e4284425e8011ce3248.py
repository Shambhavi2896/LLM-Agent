import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Retrieve API key from environment variables
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
else:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Function to extract credit card number from image using LLM
    def extract_credit_card_number(image_path):
        with open(image_path, 'rb') as image_file:
            # Assuming we have an OCR endpoint to extract text from the image
            response = requests.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers=headers, json={
                "model": "GPT-4o-Mini",
                "messages": [{"role": "user", "content": f"Extract credit card numbers from this image."}],
                "files": {"file": image_file}
            })

            if response.status_code == 200:
                return response.json().get('choices')[0]['message']['content'].strip()
            else:
                print("Error in LLM response:", response.text)
                return None

    # Extract the credit card number
    card_number = extract_credit_card_number(image_path)

    # Write the extracted card number to the output file
    if card_number:
        # Remove spaces from the card number
        card_number = card_number.replace(" ", "")
        with open(output_path, 'w') as output_file:
            output_file.write(card_number)
    else:
        print("No credit card number found or an error occurred.")