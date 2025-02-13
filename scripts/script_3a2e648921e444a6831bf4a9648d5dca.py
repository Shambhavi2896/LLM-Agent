import os
import requests

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
email_file_path = os.path.join(data_dir, 'email.txt')
output_file_path = os.path.join(data_dir, 'email-sender.txt')

# Check if the email file exists
if not os.path.exists(email_file_path):
    print(f"Error: The file {email_file_path} does not exist.")
    # Create a blank email file if necessary
    with open(email_file_path, 'w') as f:
        f.write("")
    print(f"Created a blank file at {email_file_path}.")
else:
    # Read the email content
    with open(email_file_path, 'r') as file:
        email_content = file.read()

    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('AIPROXY_TOKEN')
    if not openai_api_key:
        print("openai_api_key missing")
    else:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}"
        }

        # Prepare the request data for the LLM
        request_data = {
            "model": "GPT-4o-Mini",
            "messages": [
                {"role": "user", "content": f"Extract the sender's email address from the following email:\n\n{email_content}"}
            ]
        }

        # Call the LLM API
        response = requests.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=request_data)

        if response.status_code == 200:
            response_data = response.json()
            # Extract the email address from the LLM response
            email_sender = response_data['choices'][0]['message']['content'].strip()

            # Write the extracted email address to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(email_sender)
            print(f"Extracted email address written to {output_file_path}.")
        else:
            print(f"Error: Failed to call LLM API. Status code: {response.status_code}, Response: {response.text}")