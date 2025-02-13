import os
import json

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'contacts.json')
output_file_path = os.path.join(data_dir, 'contacts-sorted.json')

# Function to sort contacts
def sort_contacts(input_file, output_file):
    try:
        # Load contacts from JSON file
        with open(input_file, 'r') as file:
            contacts = json.load(file)

        # Sort contacts by last_name, then first_name
        sorted_contacts = sorted(contacts, key=lambda x: (x.get('last_name', ''), x.get('first_name', '')))

        # Write sorted contacts to output file
        with open(output_file, 'w') as file:
            json.dump(sorted_contacts, file, indent=4)

        print(f"Sorted contacts written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        # Optionally create an empty output file
        with open(output_file, 'w') as file:
            json.dump([], file)
            print(f"Created empty file {output_file}")
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the sorting function
sort_contacts(input_file_path, output_file_path)