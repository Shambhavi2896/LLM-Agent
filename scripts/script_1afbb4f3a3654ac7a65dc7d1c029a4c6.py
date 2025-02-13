import os
import json

# Define the directory containing the Markdown files
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))
index_file_path = os.path.join(data_directory, 'index.json')

# Initialize an empty dictionary to hold the index
index = {}

# Function to extract the first H1 title from a Markdown file
def extract_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()  # Return the title without the '# ' prefix
    return None  # Return None if no H1 title is found

# Walk through the data directory to find all .md files
for root, dirs, files in os.walk(data_directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_title(file_path)
            if title:
                # Store the filename (relative to data_directory) and its title
                relative_path = os.path.relpath(file_path, data_directory)
                index[relative_path] = title

# Write the index to the index.json file
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)

print(f"Index created at: {index_file_path}")