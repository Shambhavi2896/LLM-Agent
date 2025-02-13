import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Ensure the API key is available
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
    exit(1)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

def extract_credit_card_number(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    # Make a request to the LLM for text extraction
    response = requests.post(
        "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers=headers,
        json={
            "model": "GPT-4o-Mini",
            "messages": [
                {"role": "user", "content": "Extract credit card number from the provided image."}
            ],
            "files": [
                {"name": "credit_card.png", "content": image_data}
            ]
        }
    )
    
    if response.status_code != 200:
        print("Error in API request:", response.json())
        return None
    
    result = response.json()
    if 'choices' in result and len(result['choices']) > 0:
        return result['choices'][0]['message']['content'].strip()
    return None

# Extract the credit card number
credit_card_number = extract_credit_card_number(image_path)

if credit_card_number:
    # Remove spaces and write to output file
    credit_card_number = credit_card_number.replace(" ", "")
    with open(output_path, 'w') as output_file:
        output_file.write(credit_card_number)
else:
    print("Failed to extract credit card number.")