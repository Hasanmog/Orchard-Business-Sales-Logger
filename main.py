from entries import input_date , fruit_category , quantity_sold
from storing import logging , delete_table , undo_entry
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

def undo_last_entry(conn, date, fruit_name):
    cursor = conn.cursor()

    # Query to get all entries for the given fruit and date
    cursor.execute(f"SELECT id, quantity_kg, quantity_boxes FROM {fruit_name} WHERE  selling_date = ?", (date))
    entries = cursor.fetchall()

    if not entries:
        print(f"No entries found for {fruit_name} on {date}.")
        return

    # Display entries
    print(f"Entries for {fruit_name} on {date}:")
    for entry in entries:
        print(f"ID: {entry[0]}, Quantity (kg): {entry[1]}, Quantity (boxes): {entry[2]}")

    # Ask for the ID of the entry to delete
    while True:
        try:
            entry_id = int(input("Enter the ID of the entry to delete: "))
            if any(entry[0] == entry_id for entry in entries):
                break
            else:
                print("Invalid ID. Please enter an ID from the list.")
        except ValueError:
            print("Invalid input. Please enter a numerical ID.")

    # Delete the selected entry
    delete_query = "DELETE FROM loggings WHERE id = ?"
    cursor.execute(delete_query, (entry_id,))
    conn.commit()
    print(f"Entry with ID {entry_id} has been removed.")


def forward():
    conn = sqlite3.connect('loggings.db')
    dollar_rate = 90000

    while True:
        date = input_date()
        fruit_name = fruit_category(all_fruits)
        entries = quantity_sold(date, fruit_name, 'N', dollar_rate)  
        dollar_rate = entries['dollar_rate']
        logging(conn, date, fruit_name, entries)

        # Ask if the user wants to undo the last entry
        if input('Undo this entry? (Y/N): ').upper() == 'Y':
            undo_last_entry(conn, date, fruit_name)
        else:
            while True:
                repeat = input('Log another entry on the SAME DATE? (Y/N): ').upper()
                if repeat in ['Y', 'N']:
                    break
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

            while repeat == 'Y':
                fruit_name = fruit_category(all_fruits)
                entries = quantity_sold(date, fruit_name, repeat, dollar_rate)
                dollar_rate = entries['dollar_rate']
                logging(conn, date, fruit_name, entries)

                # Ask again for undo after each entry
                if input('Undo this entry? (Y/N): ').upper() == 'Y':
                    undo_last_entry(conn, date, fruit_name)
                else:
                    break

        # Check if the user wants to continue logging for a new date
        if input('Do you want to continue logging for a NEW DATE? (Y/N): ').upper() != 'Y':
            break
        more = 'N'
        while more != 'N':
            if input("Is there an entry you would like to remove ? ").upper() == 'Y':
                fruit_name = input('please insert the fruit name')
                entry_id = input("please insert the entry id")
                undo_entry(conn , fruit_name , entry_id)
                more = input('more ? (Y/N) ')

    print("Good job, you've logged your sales.")
    print('Have a nice day :)')
    conn.close()

forward()
