import os
import json

# Define the paths dynamically
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'contacts.json')
output_file_path = os.path.join(data_dir, 'contacts-sorted.json')

# Function to sort contacts
def sort_contacts(input_path, output_path):
    try:
        with open(input_path, 'r') as file:
            contacts = json.load(file)

        # Sort contacts by last_name, then first_name
        sorted_contacts = sorted(contacts, key=lambda x: (x['last_name'], x['first_name']))

        # Write the sorted contacts to the output file
        with open(output_path, 'w') as file:
            json.dump(sorted_contacts, file, indent=4)

        print(f"Contacts sorted and written to {output_path}")

    except FileNotFoundError:
        print(f"Input file not found: {input_path}")
        # Optionally create an empty contacts.json file
        with open(input_path, 'w') as file:
            json.dump([], file)
            print(f"Created empty contacts file at {input_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {input_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the sorting function
sort_contacts(input_file_path, output_file_path)