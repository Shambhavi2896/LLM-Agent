import os
from datetime import datetime

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_file_path = os.path.join(data_dir, 'dates.txt')
output_file_path = os.path.join(data_dir, 'dates-wednesdays.txt')

# List of possible date formats
date_formats = [
    "%Y-%m-%d",
    "%d-%b-%Y",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d",
    "%b %d, %Y",
    "%d %B %Y",
    "%B %d, %Y",
    "%d.%m.%Y",
    "%m-%d-%Y",
    "%A, %B %d, %Y",
    "%I:%M %p, %d-%b-%Y"
]

# Initialize the count of Wednesdays
wednesday_count = 0

# Try to read the input file
try:
    with open(input_file_path, 'r') as file:
        dates = file.readlines()
except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found. Creating a blank file.")
    open(input_file_path, 'w').close()
    dates = []

# Process each date
for date_str in dates:
    date_str = date_str.strip()
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                wednesday_count += 1
            break  # Stop trying formats if one is successful
        except ValueError:
            continue  # Try the next format

# Write the count of Wednesdays to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))