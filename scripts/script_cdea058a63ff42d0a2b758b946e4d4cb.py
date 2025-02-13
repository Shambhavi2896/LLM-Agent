import os
import sqlite3

# Dynamic path handling
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
db_path = os.path.join(data_dir, 'ticket-sales.db')
output_file_path = os.path.join(data_dir, 'ticket-sales-gold.txt')

# Connect to the SQLite database
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query to calculate total sales for "Gold" ticket type
    query = "SELECT SUM(price * units) FROM tickets WHERE type = ?"
    cursor.execute(query, ('Gold',))
    
    total_sales = cursor.fetchone()[0]
    
    # If total_sales is None, it means no sales were found
    if total_sales is None:
        total_sales = 0.0
    
    # Write the total sales to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"{total_sales:.2f}")
    
except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()