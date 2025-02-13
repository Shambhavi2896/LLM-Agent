import os
import sqlite3

# Define the paths dynamically
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
db_path = os.path.join(data_directory, 'ticket-sales.db')
output_file_path = os.path.join(data_directory, 'ticket-sales-gold.txt')

# Function to calculate total sales for Gold ticket type
def calculate_gold_ticket_sales(db_path, output_file_path):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Query to sum the sales of Gold ticket type
        cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
        total_sales = cursor.fetchone()[0] or 0  # Default to 0 if no results
        
        # Write the result to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"{total_sales:.2f}")  # Format to two decimal places

        print(f"Total sales for Gold tickets: {total_sales:.2f}")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

# Execute the function
calculate_gold_ticket_sales(db_path, output_file_path)