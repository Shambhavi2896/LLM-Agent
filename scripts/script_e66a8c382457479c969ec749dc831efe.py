import os
from datetime import datetime

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'dates.txt')
output_file_path = os.path.join(data_dir, 'dates-wednesdays.txt')

# Function to count Wednesdays
def count_wednesdays(input_file):
    wednesday_count = 0
    invalid_dates = []

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
        with open(input_file, 'r') as file:
            dates = file.readlines()
    except FileNotFoundError:
        print(f"Input file {input_file} not found. Creating an empty file.")
        open(input_file, 'w').close()
        return 0

    # Process each date
    for date_str in dates:
        date_str = date_str.strip()
        parsed = False
        for fmt in date_formats:
            try:
                date_obj = datetime.strptime(date_str, fmt)
                if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                    wednesday_count += 1
                parsed = True
                break
            except ValueError:
                continue
        
        if not parsed:
            invalid_dates.append(date_str)

    # Log invalid dates if any
    if invalid_dates:
        print("Invalid date formats encountered:", invalid_dates)

    return wednesday_count

# Count Wednesdays
wednesday_count = count_wednesdays(input_file_path)

# Write the result to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))