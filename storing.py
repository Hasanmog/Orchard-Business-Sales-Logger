from entries import input_date , fruit_category , quantity_sold
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

def undo_entry(conn , table_name , entry_id):
    cursor = conn.cursor()
    delete = f'''
    DELETE FROM {table_name} WHERE id = ?
    '''
    cursor.execute(delete , (entry_id))
    conn.commit()
    
def delete_table(conn , table_name):
    table_name = table_name.capitalize()
    cursor = conn.cursor()
    delete = f'''
    DROP TABLE {table_name}
    '''
    cursor.execute(delete)
    conn.commit()

def logging(conn , selling_date ,fruit_name , entries):   
    #explain arguments ....
    #.......................
    #connection to database
    
    cursor = conn.cursor()
    
    safe_fruit_name = ''.join(char for char in fruit_name if char.isalnum())  # Basic sanitization
    # It removes any characters from fruit_name that are not alphanumeric.
    quantity_kg = entries['quantity_kg']
    quantity_box = entries['quantity_box']
    average_kg_per_box = entries['average_kg_per_box']
    total_price_ll = entries['total_price_ll']
    total_price_dollar = entries['total_price_dollar']
    price_per_kg_ll = entries['price_per_kg_ll']
    price_per_kg_dollar = entries['price_per_kg_dollar']
    price_per_box_ll = entries['price_per_box_ll']
    price_per_box_dollar = entries['price_per_box_dollar']
    
    table = f"""
    CREATE TABLE IF NOT EXISTS {safe_fruit_name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        selling_date TEXT , 
        quantity_kg INTEGER ,
        quantity_boxes REAL , 
        average_kg_per_box INTEGER,
        total_price_ll  INTEGER , 
        total_price_dollar INTEGER , 
        price_per_kg_dollar INTEGER,
        price_per_kg_ll INTEGER,
        price_per_box_ll INTEGER,
        price_per_box_dollar Integer
    ) 
    """
    cursor.execute(table)
   
    insert_log = f'''
    INSERT INTO {safe_fruit_name} (selling_date, quantity_kg, quantity_boxes, average_kg_per_box,
                       total_price_ll, total_price_dollar, price_per_kg_dollar, price_per_kg_ll,
                       price_per_box_ll, price_per_box_dollar)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_log , (selling_date ,quantity_kg , quantity_box , average_kg_per_box,
                                 total_price_ll, total_price_dollar , price_per_kg_ll,
                                 price_per_kg_dollar , price_per_box_ll , price_per_box_dollar))
    conn.commit()
    
# conn = sqlite3.connect('loggings.db')
# delete_table(conn , 'Avocado')