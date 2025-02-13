import os
from datetime import datetime

# Define the paths
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
input_file_path = os.path.join(data_dir, 'dates.txt')
output_file_path = os.path.join(data_dir, 'dates-wednesdays.txt')

# Function to count Wednesdays
def count_wednesdays(file_path):
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

    try:
        with open(file_path, 'r') as file:
            for line in file:
                date_str = line.strip()
                valid_date = False
                for fmt in date_formats:
                    try:
                        date_obj = datetime.strptime(date_str, fmt)
                        if date_obj.weekday() == 2:  # Wednesday
                            wednesday_count += 1
                        valid_date = True
                        break
                    except ValueError:
                        continue
                if not valid_date:
                    invalid_dates.append(date_str)

    except FileNotFoundError:
        print(f"Input file {file_path} not found. Creating an empty file.")
        open(file_path, 'w').close()
        return 0  # If file is missing, return 0 Wednesdays

    # Log invalid dates if any
    if invalid_dates:
        print(f"Invalid date formats encountered: {invalid_dates}")

    return wednesday_count

# Count the Wednesdays in the input file
wednesday_count = count_wednesdays(input_file_path)

# Write the result to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(str(wednesday_count))