import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
email_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Ensure the output file exists
if not os.path.exists(email_file_path):
    with open(email_file_path, 'w') as f:
        f.write("")  # Create a blank email file if it doesn't exist

# Read the email content
with open(email_file_path, 'r') as file:
    email_content = file.read()

# Get OpenAI API key from environment variables
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
else:
    # Prepare the request for the LLM
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

    # Call the LLM API
    response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        sender_email = response_data['choices'][0]['message']['content'].strip()

        # Write the extracted email address to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(sender_email)
    else:
        print("Error:", response.text)