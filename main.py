from entries import input_date , fruit_category , quantity_sold
from storing import logging , delete_table 
import sqlite3

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

conn = sqlite3.connect('loggings.db')

def confirm_entry(entries):
    print("\nPlease review the entered details:")
    for key, value in entries.items():
        print(f"{key}: {value}")
    return input("Is this information correct? (Y/N): ").upper() == 'Y'

def undo_entry(conn):
    cursor = conn.cursor()
    fruit_name = input("Please enter the fruit_name(table) where the entry is found: ")
    fruit_name = ''.join(char for char in fruit_name if char.isalnum()).capitalize()  # Basic sanitization
    entry_id = input("Enter the ID of the entry to delete: ")

    # Check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (fruit_name,))
    if not cursor.fetchone():
        print(f"No such table: {fruit_name}")
        return

    # Fetch and display the entry to be deleted
    select_query = f"SELECT selling_date, quantity_kg, quantity_boxes FROM {fruit_name} WHERE id = ?"
    cursor.execute(select_query, (entry_id,))
    entries = cursor.fetchall()
    if not entries:
        print(f"No entries found for {fruit_name} with id {entry_id}.")
        return

    print(f"Entries for {fruit_name} with ID {entry_id}:")
    for entry in entries:
        print(f"Selling Date: {entry[0]}, Quantity (kg): {entry[1]}, Quantity (boxes): {entry[2]}")

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete entry ID {entry_id} from {fruit_name}? (Y/N): ").upper()
    if confirm != 'Y':
        print("Deletion cancelled.")
        return

    # Delete the entry
    delete_query = f"DELETE FROM {fruit_name} WHERE id = ?"
    cursor.execute(delete_query, (entry_id,))
    conn.commit()
    print(f"Entry with ID {entry_id} has been removed from {fruit_name}.")


def forward():
    conn = sqlite3.connect('loggings.db')
    dollar_rate = 90000

    while True:
        date = input_date()
        fruit_name = fruit_category(all_fruits)
        entries = quantity_sold(date, fruit_name, 'N', dollar_rate)  
        dollar_rate = entries['dollar_rate']
        logging(conn, date, fruit_name, entries)
        while True:
            delete_choice = input("Do you want to delete any entry? (Y/N): ").upper()
            if delete_choice == 'N':
                break  # Exit the deletion loop
            elif delete_choice == 'Y':
                undo_entry(conn)
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        
        while True:
            repeat = input('Log another entry on the SAME DATE? (Y/N): ').upper()
            if repeat == 'N':
                break
            elif repeat == 'Y':
                fruit_name = fruit_category(all_fruits)
                entries = quantity_sold(date, fruit_name, repeat, dollar_rate)
                dollar_rate = entries['dollar_rate']
                logging(conn, date, fruit_name, entries)

                # Ask again for undo after each entry
                if input('Undo this entry? (Y/N): ').upper() == 'Y':
                    undo_entry()
        # Check if the user wants to continue logging for a new date
        if input('Do you want to continue logging for a NEW DATE? (Y/N): ').upper() != 'Y':
            break

    print("Good job, you've logged your sales.")
    print('Have a nice day :)')
    conn.close()

forward()
