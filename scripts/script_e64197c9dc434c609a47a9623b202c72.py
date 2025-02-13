import os
import json

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_file_path = os.path.join(data_dir, 'contacts.json')
output_file_path = os.path.join(data_dir, 'contacts-sorted.json')

# Function to sort contacts
def sort_contacts(input_path, output_path):
    try:
        # Read the contacts from the input file
        with open(input_path, 'r') as file:
            contacts = json.load(file)

        # Sort the contacts by last_name then first_name
        sorted_contacts = sorted(contacts, key=lambda x: (x['last_name'], x['first_name']))

        # Write the sorted contacts to the output file
        with open(output_path, 'w') as file:
            json.dump(sorted_contacts, file, indent=4)

        print(f'Successfully sorted contacts and saved to {output_path}')

    except FileNotFoundError:
        print(f'Error: The file {input_path} does not exist. A blank file will be created.')
        with open(input_path, 'w') as file:
            json.dump([], file)  # Create a blank contacts file
    except json.JSONDecodeError:
        print(f'Error: The file {input_path} is not a valid JSON file.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

# Execute the sorting function
sort_contacts(input_file_path, output_file_path)