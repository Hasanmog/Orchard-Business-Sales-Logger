from entries import input_date , fruit_category , quantity_sold
import sqlite3 

conn = sqlite3.connect('loggings.db')
cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS sales(
    selling_date TEXT , 
    fruit_name  TEXT ,
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
cursor.execute(create_table)
conn.commit()

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


def insert_data_db(connection , selling_date ,fruit_name, quantity_kg , quantity_box , average_kg_per_box,
                    total_price_ll , total_price_dollar , price_per_kg_ll , 
                   price_per_kg_dollar , price_per_box_ll , price_per_box_dollar):
    
    # connection = sqlite3.connect('loggings.db')
    cursor = connection.cursor()
    
    SQL = '''
    INSERT INTO sales (selling_date, fruit_name, quantity_kg, quantity_boxes, average_kg_per_box,
                       total_price_ll, total_price_dollar, price_per_kg_dollar, price_per_kg_ll,
                       price_per_box_ll, price_per_box_dollar)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    cursor.execute(SQL , (selling_date ,fruit_name, quantity_kg , quantity_box , average_kg_per_box,
                 total_price_ll , total_price_dollar , price_per_kg_ll , 
                   price_per_kg_dollar , price_per_box_ll , price_per_box_dollar))
    connection.commit()

date = input_date()
fruit_name = fruit_category(all_fruits)
quantities = quantity_sold(date , fruit_name)

selling_date = quantities['selling_date']
fruit_name = quantities['fruit_name']
quantity_kg = quantities['quantity_kg']
quantity_box = quantities['quantity_box']
average_kg_per_box = quantities['average_kg_per_box']
total_price_ll = quantities['total_price_ll']
total_price_dollar = quantities['total_price_dollar']
price_per_kg_ll = quantities['price_per_kg_ll']
price_per_kg_dollar = quantities['price_per_kg_dollar']
price_per_box_ll = quantities['price_per_box_ll']
price_per_box_dollar = quantities['price_per_box_dollar']

insert_data_db(conn , selling_date ,fruit_name, quantity_kg , quantity_box , average_kg_per_box,
                    total_price_ll , total_price_dollar , price_per_kg_ll , 
                   price_per_kg_dollar , price_per_box_ll , price_per_box_dollar)

conn.close()