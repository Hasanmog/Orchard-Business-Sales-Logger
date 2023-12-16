# Python provides several libraries that can help convert an SQLite database to an Excel sheet.
# We'll use 'pandas' for data manipulation and 'openpyxl' to create an Excel file.
# First, ensure you have these libraries installed. If not, you can install them using pip:
# pip install pandas openpyxl

import sqlite3
import pandas as pd

all_fruits = [
    'Lemon',
    'Avocado',
    'Orange Abu Sorra',
    'Orange Valencia',
    'Clementine',
    'Pomelo' ,
    'Orange Moro',
    'Orange Shamoute'
]

table_name = 'Clementine'
# Path to the SQLite database
db_path = 'Season23_24.db'
# Path where the Excel file will be saved
excel_path = f'{table_name}.xlsx'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Assuming you want to export a table named 'my_table' from the SQLite database

# Read the data from SQLite into a pandas DataFrame
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

# Close the SQLite connection
conn.close()

# Write the data to an Excel file
df.to_excel(excel_path, index=False, engine='openpyxl')

# The Excel file is saved at the specified path
excel_path

print("Converted!")