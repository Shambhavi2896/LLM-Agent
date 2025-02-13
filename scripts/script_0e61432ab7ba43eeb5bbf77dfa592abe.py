import os
import glob

# Define the directory for log files and output file
logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs/'))
output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs-recent.txt'))

# Get a list of the 10 most recent .log files
log_files = sorted(glob.glob(os.path.join(logs_dir, '*.log')), key=os.path.getmtime, reverse=True)[:10]

# Prepare to write to the output file
try:
    with open(output_file_path, 'w') as output_file:
        for log_file in log_files:
            with open(log_file, 'r') as file:
                first_line = file.readline().strip()
                output_file.write(first_line + '\n')
except FileNotFoundError:
    print(f"Output file path {output_file_path} could not be created.")
except Exception as e:
    print(f"An error occurred: {e}")