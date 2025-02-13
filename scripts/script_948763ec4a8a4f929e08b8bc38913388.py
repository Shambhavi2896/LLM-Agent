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

# Read the input file
try:
    with open(input_file_path, 'r') as file:
        dates = file.readlines()
except FileNotFoundError:
    print(f"Input file {input_file_path} not found. Creating a blank file.")
    open(input_file_path, 'w').close()
    dates = []

# Process each date
for date_str in dates:
    date_str = date_str.strip()
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                wednesday_count += 1
            break  # Exit the loop if date is successfully parsed
        except ValueError:
            continue  # Try the next format if the current one fails

# Write the count to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))