import os
import json

# Define the data directory
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/docs'))

# Initialize an index dictionary
index = {}

# Function to extract the first H1 title from a Markdown file
def extract_h1_title(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('# '):
                    return line[2:].strip()  # Return the title without the '# '
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

# Find all Markdown files in the data directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            title = extract_h1_title(file_path)
            if title:
                # Store the filename without the prefix and its title
                relative_path = os.path.relpath(file_path, data_dir)
                index[relative_path] = title

# Create the index file
index_file_path = os.path.join(data_dir, 'index.json')
try:
    with open(index_file_path, 'w', encoding='utf-8') as index_file:
        json.dump(index, index_file, indent=4)
    print(f"Index file created at: {index_file_path}")
except Exception as e:
    print(f"Error writing index file: {e}")