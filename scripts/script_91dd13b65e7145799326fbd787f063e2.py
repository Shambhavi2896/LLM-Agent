import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
email_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Function to read the email file
def read_email_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

# Function to write the extracted sender email to a file
def write_sender_email(file_path, sender_email):
    with open(file_path, 'w') as file:
        file.write(sender_email)

# Function to extract sender's email using LLM
def extract_sender_email(email_content):
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("Error: openai_api_key missing")
        return None

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": "GPT-4o-Mini",
        "messages": [
            {
                "role": "user",
                "content": f"Extract the sender's email address from the following email content:\n\n{email_content}"
            }
        ]
    }

    response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content'].strip()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Main execution
email_content = read_email_file(email_file_path)
if email_content:
    sender_email = extract_sender_email(email_content)
    if sender_email:
        write_sender_email(output_file_path, sender_email)
    else:
        print("Failed to extract sender's email.")
else:
    print("No email content to process.")