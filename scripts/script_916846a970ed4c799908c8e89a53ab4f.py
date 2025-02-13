import os
import json

# Dynamically construct file paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_file_path = os.path.join(data_dir, 'contacts.json')
output_file_path = os.path.join(data_dir, 'contacts-sorted.json')

try:
    # Read the contacts from the input file
    with open(input_file_path, 'r') as infile:
        contacts = json.load(infile)

    # Sort contacts by last_name, then first_name
    sorted_contacts = sorted(contacts, key=lambda x: (x.get('last_name', ''), x.get('first_name', '')))

    # Write the sorted contacts to the output file
    with open(output_file_path, 'w') as outfile:
        json.dump(sorted_contacts, outfile, indent=4)

except FileNotFoundError:
    print(f"Error: The file {input_file_path} does not exist. Please check the file path.")
except json.JSONDecodeError:
    print(f"Error: The file {input_file_path} contains invalid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")