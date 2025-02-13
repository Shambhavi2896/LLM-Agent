import os
from datetime import datetime

# Define the paths
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
input_file_path = os.path.join(data_directory, 'dates.txt')
output_file_path = os.path.join(data_directory, 'dates-wednesdays.txt')

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

    try:
        with open(input_file, 'r') as file:
            for line in file:
                date_str = line.strip()
                valid_date = False
                for fmt in date_formats:
                    try:
                        date_obj = datetime.strptime(date_str, fmt)
                        if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                            wednesday_count += 1
                        valid_date = True
                        break
                    except ValueError:
                        continue
                
                if not valid_date:
                    invalid_dates.append(date_str)

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found. Creating a blank file.")
        with open(input_file, 'w') as file:
            file.write("")  # Create an empty file if it doesn't exist
        return

    # Write the count of Wednesdays to the output file
    with open(output_file, 'w') as output_file:
        output_file.write(str(wednesday_count))

    # Log any invalid dates encountered
    if invalid_dates:
        print("Invalid date formats encountered:", invalid_dates)

# Execute the function
count_wednesdays(input_file_path)