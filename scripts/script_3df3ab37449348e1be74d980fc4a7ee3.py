import os
import requests

# Define paths
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
email_file_path = os.path.join(data_directory, 'email.txt')
output_file_path = os.path.join(data_directory, 'email-sender.txt')

# Check for the existence of the input file
if not os.path.exists(email_file_path):
    print(f"Error: The file {email_file_path} does not exist.")
    # Optionally create a blank file
    open(email_file_path, 'w').close()
    print(f"Created a blank file at {email_file_path}.")
else:
    # Read the email content
    with open(email_file_path, 'r') as file:
        email_content = file.read()

    # Retrieve the API key from environment variables
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
    else:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        # Prepare the data for the LLM
        data = {
            "model": "GPT-4o-Mini",
            "messages": [
                {"role": "user", "content": f"Extract the sender's email address from the following email:\n\n{email_content}"}
            ]
        }

        # Make the API request
        response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=data)

        # Check for a successful response
        if response.status_code == 200:
            result = response.json()
            sender_email = result['choices'][0]['message']['content'].strip()

            # Write the sender's email address to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(sender_email)
            print(f"Extracted sender's email address: {sender_email}")
            print(f"Email address written to {output_file_path}")
        else:
            print(f"Error: Failed to extract email. Status code: {response.status_code}, Response: {response.text}")