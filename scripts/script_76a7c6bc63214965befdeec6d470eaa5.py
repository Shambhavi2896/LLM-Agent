import os
from datetime import datetime

# Define paths
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_directory, 'dates.txt')
output_file_path = os.path.join(data_directory, 'dates-wednesdays.txt')

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

# Initialize Wednesday count
wednesday_count = 0
invalid_dates = []

# Read the dates from the input file
try:
    with open(input_file_path, 'r') as file:
        dates = file.readlines()
except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found. Creating an empty file.")
    open(input_file_path, 'w').close()
    dates = []

# Process each date
for date_str in dates:
    date_str = date_str.strip()
    if not date_str:
        continue
    date_parsed = False
    for fmt in date_formats:
        try:
            date = datetime.strptime(date_str, fmt)
            if date.weekday() == 2:  # 2 corresponds to Wednesday
                wednesday_count += 1
            date_parsed = True
            break
        except ValueError:
            continue
    if not date_parsed:
        invalid_dates.append(date_str)

# Write the count of Wednesdays to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))

# Log any invalid date formats encountered
if invalid_dates:
    print("Invalid date formats encountered:", invalid_dates)