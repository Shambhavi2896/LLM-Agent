import os
import requests

# Define file paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
email_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Retrieve OpenAI API key
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
else:
    print("openai_api_key : ", openai_api_key)

# Read email content
try:
    with open(email_file_path, 'r') as email_file:
        email_content = email_file.read()
except FileNotFoundError:
    print(f"Error: The file {email_file_path} does not exist.")
    email_content = ""

# Prepare the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Prepare the payload for the LLM
payload = {
    "model": "GPT-4o-Mini",
    "messages": [
        {
            "role": "user",
            "content": f"Extract the sender's email address from the following email message:\n\n{email_content}"
        }
    ]
}

# Make the API call to extract the sender's email address
if email_content:
    response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        sender_email = response_data['choices'][0]['message']['content'].strip()

        # Write the extracted email address to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(sender_email)
    else:
        print(f"Error: Failed to retrieve data from the LLM. Status code: {response.status_code}")
else:
    # Create an empty output file if the email content is not available
    with open(output_file_path, 'w') as output_file:
        output_file.write("")