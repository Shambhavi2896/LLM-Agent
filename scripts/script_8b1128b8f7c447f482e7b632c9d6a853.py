import os
import json

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))
index_file_path = os.path.join(data_dir, 'index.json')

# Initialize the index dictionary
index = {}

# Function to extract H1 title from a Markdown file
def extract_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()  # Return the title without '# '
    return None  # Return None if no H1 found

# Iterate through all Markdown files in the directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_title(file_path)
            if title:
                # Store the title in the index, using the filename without the path
                index[os.path.relpath(file_path, data_dir)] = title

# Write the index to a JSON file
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)

print(f"Index created at: {index_file_path}")