import os
import glob

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
logs_dir = os.path.join(data_dir, 'logs')
output_file = os.path.join(logs_dir, 'logs-recent.txt')

# Ensure the output file exists
if not os.path.exists(output_file):
    open(output_file, 'w').close()

# Find the 10 most recent .log files
log_files = sorted(glob.glob(os.path.join(logs_dir, '*.log')), key=os.path.getmtime, reverse=True)[:10]

# Read the first line of each log file and write to the output file
with open(output_file, 'w') as outfile:
    for log_file in log_files:
        try:
            with open(log_file, 'r') as infile:
                first_line = infile.readline().strip()
                outfile.write(first_line + '\n')
        except Exception as e:
            print(f"Error reading {log_file}: {e}")