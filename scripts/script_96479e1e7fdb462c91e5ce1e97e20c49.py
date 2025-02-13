import os
import json

# Define the path to the data directory
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs/'))
index_file_path = os.path.join(data_dir, 'index.json')

# Initialize the index dictionary
index = {}

# Function to extract H1 title from a markdown file
def extract_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):  # Check for H1
                return line[2:].strip()  # Remove '# ' and return the title
    return None  # Return None if no H1 is found

# Find all markdown files in the data directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_title(file_path)
            if title:
                # Store the filename without the path and its corresponding title
                index[os.path.relpath(file_path, data_dir)] = title

# Write the index to the JSON file
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)