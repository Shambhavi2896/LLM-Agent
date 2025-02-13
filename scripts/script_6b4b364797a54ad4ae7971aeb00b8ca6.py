import os
from datetime import datetime

# Define the input and output file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')

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

def count_wednesdays(file_path):
    wednesday_count = 0
    invalid_dates = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                date_str = line.strip()
                if not date_str:
                    continue  # Skip empty lines
                
                # Try parsing the date with the available formats
                parsed = False
                for fmt in date_formats:
                    try:
                        date = datetime.strptime(date_str, fmt)
                        if date.weekday() == 2:  # 2 corresponds to Wednesday
                            wednesday_count += 1
                        parsed = True
                        break
                    except ValueError:
                        continue
                
                if not parsed:
                    invalid_dates.append(date_str)

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist. Creating a blank file.")
        open(file_path, 'w').close()  # Create a blank file if it doesn't exist

    if invalid_dates:
        print("Invalid date formats encountered:")
        for invalid_date in invalid_dates:
            print(f" - {invalid_date}")

    return wednesday_count

# Count Wednesdays and write the result to the output file
wednesday_count = count_wednesdays(input_file_path)

# Write the count to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))