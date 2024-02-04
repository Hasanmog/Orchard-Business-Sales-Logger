import sqlite3
import pandas as pd

table_name = 'Orange Abu Sorra'
db_path = 'Season23_24.db'
excel_path = f'{table_name}.xlsx'

# Create a connection to the SQLite database
conn = sqlite3.connect(db_path)

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_path, engine='openpyxl')

# Export the DataFrame to the SQLite table
# 'replace' to drop the existing table and create a new one
# 'append' to insert new values into the existing table
# 'fail' to do nothing if the table already exists
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Commit any changes and close the connection
conn.commit()
conn.close()

print("Imported!")


