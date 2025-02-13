import os
import json

# Define the directory containing the Markdown files
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))
index_file_path = os.path.join(data_dir, 'index.json')

# Initialize an index dictionary
index = {}

# Function to extract H1 title from a Markdown file
def extract_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()  # Return the title without '# '
    return None  # Return None if no H1 is found

# Find all Markdown files in the directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_title(file_path)
            if title:
                # Map filename without the prefix to its title
                relative_path = os.path.relpath(file_path, data_dir)
                index[relative_path] = title

# Write the index to the JSON file
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)