import os
import glob

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs'))
output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs-recent.txt'))

# Get the most recent 10 .log files
log_files = sorted(glob.glob(os.path.join(data_dir, '*.log')), key=os.path.getmtime, reverse=True)[:10]

# Prepare to write the first line of each log file
recent_lines = []

for log_file in log_files:
    try:
        with open(log_file, 'r') as file:
            first_line = file.readline().strip()
            recent_lines.append(first_line)
    except FileNotFoundError:
        print(f"File not found: {log_file}")
    except Exception as e:
        print(f"An error occurred while reading {log_file}: {e}")

# Write the collected lines to the output file
with open(output_file, 'w') as output:
    for line in recent_lines:
        output.write(line + '\n')