import os
import json

# Define the data directory
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))
index_file_path = os.path.join(data_directory, 'index.json')

# Initialize the index dictionary
index = {}

# Function to extract H1 titles from a Markdown file
def extract_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()  # Return the title without the '# '
    return None  # Return None if no H1 is found

# Process each Markdown file in the directory
for root, dirs, files in os.walk(data_directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_title(file_path)
            if title:
                # Store the filename without the directory prefix
                index[file] = title

# Write the index to the JSON file
with open(index_file_path, 'w', encoding='utf-8') as index_file:
    json.dump(index, index_file, ensure_ascii=False, indent=4)

print(f"Index created at: {index_file_path}")