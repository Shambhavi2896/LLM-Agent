import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    # Load API key from environment variable
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
    else:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        # Prepare the request to the LLM for text extraction from image
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            extracted_text = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
            # Process the extracted text to find the credit card number
            credit_card_number = ''.join(extracted_text.split())  # Remove spaces
            
            # Write the credit card number to the output file
            with open(output_path, 'w') as output_file:
                output_file.write(credit_card_number)
        else:
            print(f"Error: Failed to extract text from image. Status code: {response.status_code}, Response: {response.text}")