import os
import json

# Define the data directory
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))

# Initialize the index dictionary
index = {}

# Function to extract the first H1 heading from a Markdown file
def extract_h1_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()  # Return the title without the '# ' prefix
    return None  # Return None if no H1 is found

# Iterate through all files in the data directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_from_md(file_path)
            if title:
                # Map the filename (without the data directory prefix) to its title
                relative_path = os.path.relpath(file_path, data_dir)
                index[relative_path] = title

# Write the index to a JSON file
index_file_path = os.path.join(data_dir, 'index.json')
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)