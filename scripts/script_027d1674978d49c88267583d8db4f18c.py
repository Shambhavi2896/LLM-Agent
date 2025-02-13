import os
import json

# Define file paths
input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/contacts.json')
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/contacts-sorted.json')

# Function to sort contacts
def sort_contacts(input_path, output_path):
    try:
        # Read the contacts from the input file
        with open(input_path, 'r') as infile:
            contacts = json.load(infile)
        
        # Sort contacts by last_name and then by first_name
        sorted_contacts = sorted(contacts, key=lambda x: (x.get('last_name', ''), x.get('first_name', '')))
        
        # Write the sorted contacts to the output file
        with open(output_path, 'w') as outfile:
            json.dump(sorted_contacts, outfile, indent=4)
        
        print(f"Sorted contacts have been written to {output_path}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
        # Optionally, create an empty contacts.json if it does not exist
        with open(input_path, 'w') as infile:
            json.dump([], infile)
            print(f"Created an empty contacts file at {input_path}.")
    except json.JSONDecodeError:
        print(f"Error: The file {input_path} is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the sorting function
sort_contacts(input_file_path, output_file_path)