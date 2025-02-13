import os
import glob

# Define the paths
logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs'))
output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/logs-recent.txt'))

# Ensure the logs directory exists
if not os.path.exists(logs_dir):
    print(f"Logs directory does not exist: {logs_dir}")
    exit(1)

# Find the 10 most recent .log files
log_files = glob.glob(os.path.join(logs_dir, '*.log'))
log_files.sort(key=os.path.getmtime, reverse=True)
recent_log_files = log_files[:10]

# Prepare to write the first lines to the output file
with open(output_file, 'w') as outfile:
    for log_file in recent_log_files:
        try:
            with open(log_file, 'r') as infile:
                first_line = infile.readline().strip()
                outfile.write(first_line + '\n')
        except Exception as e:
            print(f"Error reading {log_file}: {e}")