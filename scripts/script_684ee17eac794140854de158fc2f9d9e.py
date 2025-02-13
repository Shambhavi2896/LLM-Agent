import os
import glob

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs'))
output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs-recent.txt'))

# Get the most recent .log files
log_files = glob.glob(os.path.join(data_dir, '*.log'))
log_files.sort(key=os.path.getmtime, reverse=True)

# Prepare to write the first lines to the output file
recent_lines = []
for log_file in log_files[:10]:  # Get the 10 most recent files
    try:
        with open(log_file, 'r') as file:
            first_line = file.readline().strip()
            recent_lines.append(first_line)
    except FileNotFoundError:
        print(f"File not found: {log_file}")
    except Exception as e:
        print(f"Error reading {log_file}: {e}")

# Write the collected lines to the output file
with open(output_file_path, 'w') as output_file:
    for line in recent_lines:
        output_file.write(line + '\n')