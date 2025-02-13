import os
import datetime

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')
input_file_path = os.path.join(data_dir, 'dates.txt')
output_file_path = os.path.join(data_dir, 'wednesday_count.txt')

# Function to count occurrences of Wednesdays
def count_wednesdays(input_path, output_path):
    wednesday_count = 0
    invalid_dates = []

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Input file {input_path} does not exist. Creating an empty file.")
        open(input_path, 'w').close()  # Create an empty file
        return

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

    # Read the input file and process dates
    with open(input_path, 'r') as file:
        for line in file:
            date_str = line.strip()
            for fmt in date_formats:
                try:
                    date_obj = datetime.datetime.strptime(date_str, fmt)
                    if date_obj.weekday() == 2:  # 2 corresponds to Wednesday
                        wednesday_count += 1
                    break
                except ValueError:
                    continue
            else:
                invalid_dates.append(date_str)

    # Write the count of Wednesdays to the output file
    with open(output_path, 'w') as file:
        file.write(f"Count of Wednesdays: {wednesday_count}\n")
        if invalid_dates:
            file.write("Invalid date formats encountered:\n")
            for invalid_date in invalid_dates:
                file.write(f"{invalid_date}\n")

# Execute the function
count_wednesdays(input_file_path, output_file_path)