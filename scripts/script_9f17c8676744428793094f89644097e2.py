import os
import json
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
email_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Retrieve API key
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
    exit(1)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Read email content
try:
    with open(email_file_path, 'r') as email_file:
        email_content = email_file.read()
except FileNotFoundError:
    print(f"Error: The file {email_file_path} does not exist.")
    # Create an empty email file if it does not exist
    with open(email_file_path, 'w') as email_file:
        email_file.write("")
    exit(1)

# Prepare the request to the LLM
payload = {
    "model": "GPT-4o-Mini",
    "messages": [
        {
            "role": "user",
            "content": f"Extract the sender's email address from the following email content:\n\n{email_content}"
        }
    ]
}

# Call the LLM API
response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=payload)

# Check the response
if response.status_code == 200:
    response_data = response.json()
    email_sender = response_data['choices'][0]['message']['content'].strip()

    # Write the extracted email address to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(email_sender)
else:
    print(f"Error: Unable to fetch data from LLM API. Status code: {response.status_code}, Response: {response.text}")