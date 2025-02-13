import os
import json
import requests

# Constructing paths dynamically
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Retrieve the API key from environment variables
openai_api_key = os.getenv('AIPROXY_TOKEN')
if not openai_api_key:
    print("openai_api_key missing")
else:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Read the email content
    try:
        with open(input_file_path, 'r') as file:
            email_content = file.read()
    except FileNotFoundError:
        print(f"Input file {input_file_path} not found. Creating a blank file.")
        with open(input_file_path, 'w') as file:
            file.write("")
        email_content = ""

    # Prepare the request to the LLM
    prompt = f"Extract the sender's email address from the following email content:\n\n{email_content}"
    data = {
        "model": "GPT-4o-Mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    # Send the request to the LLM
    response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        sender_email = response_data['choices'][0]['message']['content'].strip()
        
        # Write the extracted email address to the output file
        with open(output_file_path, 'w') as file:
            file.write(sender_email)
    else:
        print("Error calling the LLM:", response.status_code, response.text)