import os
import json
import requests

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Check for the API key
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
else:
    # Read the email content
    if not os.path.exists(input_file_path):
        print(f"Input file '{input_file_path}' does not exist. Creating a blank file.")
        with open(input_file_path, 'w') as f:
            f.write("")  # Create a blank file
    else:
        with open(input_file_path, 'r') as f:
            email_content = f.read()

    # Prepare the request to the LLM
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "GPT-4o-Mini",
        "messages": [
            {
                "role": "user",
                "content": f"Extract the sender's email address from the following email content:\n\n{email_content}"
            }
        ]
    }

    # Call the LLM
    response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        sender_email = response_data['choices'][0]['message']['content'].strip()

        # Write the extracted email address to the output file
        with open(output_file_path, 'w') as f:
            f.write(sender_email)
    else:
        print(f"Error: {response.status_code} - {response.text}")