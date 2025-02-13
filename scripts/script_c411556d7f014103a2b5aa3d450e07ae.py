import os
from datetime import datetime

# Define the input and output file paths
input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'dates.txt')
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'dates-wednesdays.txt')

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

wednesday_count = 0
invalid_dates = []

# Read the input file
try:
    with open(input_file_path, 'r') as file:
        dates = file.readlines()
except FileNotFoundError:
    print(f"Input file not found: {input_file_path}")
    # Create a blank file if it doesn't exist
    open(input_file_path, 'w').close()
    dates = []

# Process each date
for date_str in dates:
    date_str = date_str.strip()
    if not date_str:
        continue  # Skip empty lines
    found = False
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                wednesday_count += 1
            found = True
            break
        except ValueError:
            continue
    if not found:
        invalid_dates.append(date_str)

# Write the count of Wednesdays to the output file
with open(output_file_path, 'w') as file:
    file.write(str(wednesday_count))

# Log invalid date formats if any
if invalid_dates:
    print("Invalid date formats encountered:")
    for invalid_date in invalid_dates:
        print(invalid_date)