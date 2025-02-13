import os
import glob

# Define the data directory
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs'))
output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs-recent.txt'))

# Get the most recent .log files
log_files = sorted(glob.glob(os.path.join(data_dir, '*.log')), key=os.path.getmtime, reverse=True)[:10]

# Initialize a list to hold the first lines
first_lines = []

# Read the first line of each log file
for log_file in log_files:
    try:
        with open(log_file, 'r') as file:
            first_line = file.readline().strip()
            first_lines.append(first_line)
    except Exception as e:
        print(f"Error reading {log_file}: {e}")

# Write the first lines to the output file
try:
    with open(output_file, 'w') as output:
        for line in first_lines:
            output.write(line + '\n')
except Exception as e:
    print(f"Error writing to {output_file}: {e}")