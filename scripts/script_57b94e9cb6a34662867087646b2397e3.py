import os
from datetime import datetime

# Define paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
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
invalid_dates = []

# Read the input file
try:
    with open(input_file_path, 'r') as file:
        dates = file.readlines()
except FileNotFoundError:
    print(f"Input file not found: {input_file_path}")
    # Create a blank input file if it doesn't exist
    with open(input_file_path, 'w') as file:
        pass
    dates = []

# Process each date
for date_str in dates:
    date_str = date_str.strip()
    if not date_str:
        continue
    parsed = False
    for date_format in date_formats:
        try:
            date = datetime.strptime(date_str, date_format)
            if date.weekday() == 2:  # 2 corresponds to Wednesday
                wednesday_count += 1
            parsed = True
            break
        except ValueError:
            continue
    if not parsed:
        invalid_dates.append(date_str)

# Write the result to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))

# Log any invalid dates
if invalid_dates:
    print("Invalid date formats encountered:", invalid_dates)