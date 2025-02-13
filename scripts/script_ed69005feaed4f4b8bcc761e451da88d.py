import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Check if the image exists
if not os.path.exists(image_path):
    print(f"Error: The image file {image_path} does not exist.")
else:
    # Read the image file to send to the LLM
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Retrieve the API key from environment variables
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
    else:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        # Prepare the request to the LLM for text extraction
        json_data = {
            "model": "GPT-4o-Mini",
            "messages": [
                {
                    "role": "user",
                    "content": "Extract the credit card number from the provided image."
                }
            ],
            "files": {
                "image": image_data
            }
        }

        # Send the request to the LLM
        response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=json_data)

        # Check the response status
        if response.status_code == 200:
            result = response.json()
            credit_card_number = result.get('choices')[0].get('message').get('content').strip()

            # Remove spaces from the credit card number
            credit_card_number = credit_card_number.replace(" ", "")

            # Write the extracted number to the output file
            with open(output_path, 'w') as output_file:
                output_file.write(credit_card_number)
            print(f"Credit card number extracted and saved to {output_path}.")
        else:
            print(f"Error: Failed to extract credit card number. Status code: {response.status_code}, Response: {response.text}")