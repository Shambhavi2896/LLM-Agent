import os
import json

# Define the data directory
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))

# Prepare the index dictionary
index = {}

# Function to extract the first H1 from a Markdown file
def extract_h1_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):  # Check for H1
                return line[2:].strip()  # Return the title without '# '
    return None  # Return None if no H1 found

# Iterate over all files in the data directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_from_md(file_path)
            if title:
                # Store the title in the index
                relative_path = os.path.relpath(file_path, data_dir)
                index[relative_path] = title

# Define the output index file path
index_file_path = os.path.join(data_dir, 'index.json')

# Write the index to a JSON file
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)

print(f"Index created at: {index_file_path}")