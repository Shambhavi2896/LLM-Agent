import os
import requests

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
image_path = os.path.join(data_dir, 'credit_card.png')
output_path = os.path.join(data_dir, 'credit-card.txt')

# Check if the input image exists
if not os.path.exists(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    # Load the API key from environment variables
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
    else:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        # Prepare the request payload for the LLM
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post('http://aiproxy.sanand.workers.dev/openai/v1/images/extract', headers=headers, files=files)

        if response.status_code == 200:
            # Assuming the response contains the extracted text
            extracted_text = response.json().get('data', '')
            # Remove spaces from the extracted text
            credit_card_number = extracted_text.replace(" ", "")
            
            # Write the credit card number to the output file
            with open(output_path, 'w') as output_file:
                output_file.write(credit_card_number)
        else:
            print(f"Error: Unable to extract text from the image. Status Code: {response.status_code}, Response: {response.text}")