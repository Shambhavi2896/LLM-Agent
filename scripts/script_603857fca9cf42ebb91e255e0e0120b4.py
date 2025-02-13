import os
import json

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'contacts.json')
output_file_path = os.path.join(data_dir, 'contacts-sorted.json')

# Function to sort contacts
def sort_contacts(input_path, output_path):
    try:
        # Read contacts from the input file
        with open(input_path, 'r') as file:
            contacts = json.load(file)
        
        # Sort contacts by last_name, then first_name
        sorted_contacts = sorted(contacts, key=lambda x: (x.get('last_name', ''), x.get('first_name', '')))
        
        # Write sorted contacts to the output file
        with open(output_path, 'w') as file:
            json.dump(sorted_contacts, file, indent=4)
        
        print(f"Sorted contacts written to {output_path}")

    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
        # Optionally create an empty output file
        with open(output_path, 'w') as file:
            json.dump([], file)
            print(f"Created an empty output file at {output_path}.")
    except json.JSONDecodeError:
        print(f"Error: The file {input_path} is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the sorting function
sort_contacts(input_file_path, output_file_path)