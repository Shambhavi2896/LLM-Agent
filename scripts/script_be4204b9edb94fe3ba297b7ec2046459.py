import os
from datetime import datetime

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_file_path = os.path.join(data_dir, 'dates.txt')
output_file_path = os.path.join(data_dir, 'dates-wednesdays.txt')

# Initialize the count of Wednesdays
wednesday_count = 0

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

# Read the input file
try:
    with open(input_file_path, 'r') as file:
        for line in file:
            date_str = line.strip()
            for date_format in date_formats:
                try:
                    date_obj = datetime.strptime(date_str, date_format)
                    if date_obj.weekday() == 2:  # Wednesday
                        wednesday_count += 1
                    break  # Exit the format loop on successful parsing
                except ValueError:
                    continue  # Try the next format
            else:
                print(f"Invalid date format encountered: {date_str}")

except FileNotFoundError:
    print(f"Input file not found: {input_file_path}")
    # Create a blank input file if it doesn't exist
    with open(input_file_path, 'w') as file:
        pass

# Write the count of Wednesdays to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))