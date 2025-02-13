import os
import glob

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs'))
output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs-recent.txt'))

# Get the most recent 10 log files
log_files = sorted(glob.glob(os.path.join(data_dir, '*.log')), key=os.path.getmtime, reverse=True)[:10]

# Prepare to write the first line of each log file to the output file
with open(output_file_path, 'w') as output_file:
    for log_file in log_files:
        try:
            with open(log_file, 'r') as file:
                first_line = file.readline().strip()
                output_file.write(f"{first_line}\n")
        except Exception as e:
            print(f"Error reading {log_file}: {e}")