import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Check for the existence of the input file
if not os.path.exists(input_file_path):
    print(f"Input file {input_file_path} does not exist. Creating an empty file.")
    open(input_file_path, 'w').close()

# Read the email content
with open(input_file_path, 'r') as file:
    email_content = file.read()

# Retrieve the API key
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
else:
    print("openai_api_key : ", openai_api_key)

# Define the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Define the payload for the LLM request
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

# Check for a successful response
if response.status_code == 200:
    result = response.json()
    sender_email = result['choices'][0]['message']['content'].strip()

    # Write the sender's email to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(sender_email)
else:
    print(f"Error: {response.status_code} - {response.text}")