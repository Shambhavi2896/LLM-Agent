import os
import sqlite3

# Define the path to the database and the output file
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/ticket-sales.db'))
output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/ticket-sales-gold.txt'))

# Connect to the SQLite database
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to calculate total sales for "Gold" ticket type
    cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = ?", ("Gold",))
    total_sales = cursor.fetchone()[0]

    # If total_sales is None, set it to 0
    if total_sales is None:
        total_sales = 0

    # Write the total sales to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"{total_sales}\n")

    print("Total sales for Gold tickets written to:", output_file_path)

except sqlite3.Error as e:
    print("Database error:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    if conn:
        conn.close()