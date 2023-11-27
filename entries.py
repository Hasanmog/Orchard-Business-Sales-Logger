from datetime import datetime 

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

# function to get the selling date of one recipt
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_date():
    print('Setting Selling Date:')
    print('------------------------') 
    date = input('Selling Date (DD-MM-YY):')
    while True :
        try:
            user_date = datetime.strptime(date, "%d-%m-%Y")
            print(f"You entered: {user_date}")
        except ValueError:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
        return user_date

# function for getting the fruit name for a logging       
def fruit_category(all_fruits):
    indices = []
    print('Fruit Pick:')
    for idx,fruit in enumerate(all_fruits):
        indices.append(idx)
        print(f'{idx} : {fruit} ')
    
    fruit_index = int(input('Type the number corresponding to the fruit sold:'))
    while fruit_index not in indices :
        print("Invalid fruit number , please try again")  
        fruit_index = int(input('Type the number corresponding to the fruit sold:'))
    fruit_name = all_fruits[fruit_index]
    return fruit_name

 # get the quantity sold for a fruit type in kg and boxes(sanade2)       
def quantity_sold(user_date , fruit_name):
    print(f'please insert the quantity sold for {fruit_name} according to the following:')
    
    quantity_kg = get_positive_float('In kg: ')
    quantity_box = get_positive_int('In boxes: ') 
    if quantity_box == 0:
        average_kg_per_box = 0
        print("No boxes sold.")
    else:
        average_kg_per_box = quantity_kg / quantity_box
        print(f"In Average, each box contains {average_kg_per_box:,.2f} kg")

    print('Now, for the selling price:')
    
    
    dollar_rate = int(input(f'insert the market dollar rate on {user_date}:'))
    price = int(input("price for the quantity sold in Lebanese Pounds (L.L):"))
    price_in_dollar = price / dollar_rate
    
    if quantity_kg > 0:
        price_per_kg_ll = price / quantity_kg
        price_per_kg_dollar = price_in_dollar / quantity_kg
    else:
        price_per_kg_ll = 0
        price_per_kg_dollar = 0

    if quantity_box > 0:
        price_per_box_ll = price / quantity_box
        price_per_box_dollar = price_in_dollar / quantity_box
    else:
        price_per_box_ll = 0
        price_per_box_dollar = 0
        
    entries_summary = {
        "selling_date" : user_date ,
        "fruit_name" : fruit_name ,
        "quantity_kg": quantity_kg,
        "quantity_box": quantity_box,
        "average_kg_per_box": average_kg_per_box,
        "dollar_rate": dollar_rate,
        "total_price_ll": price,
        "total_price_dollar": price_in_dollar,
        "price_per_kg_ll": price_per_kg_ll,
        "price_per_kg_dollar": price_per_kg_dollar,
        "price_per_box_ll": price_per_box_ll,
        "price_per_box_dollar": price_per_box_dollar
    }
    print("Sales Summary:")
    print("---------------")
    print(f"Selling Date : {entries_summary['selling_date']}")
    print(f"Quantity Sold (kg): {entries_summary['quantity_kg']} kg")
    print(f"Quantity Sold (boxes): {entries_summary['quantity_box']} boxes")
    print(f"Average Weight per Box: {entries_summary['average_kg_per_box']} kg")
    print(f"Market Dollar Rate: {entries_summary['dollar_rate']:,} L.L/$")
    print(f"Total Price (L.L): {entries_summary['total_price_ll']:,} L.L")
    print(f"Total Price ($): ${entries_summary['total_price_dollar']:,.2f}")
    print(f"Price per kg (L.L): {entries_summary['price_per_kg_ll']:,} L.L")
    print(f"Price per kg ($): ${entries_summary['price_per_kg_dollar']:,.2f}")
    print(f"Price per Box (L.L): {entries_summary['price_per_box_ll']:,} L.L")
    print(f"Price per Box ($): ${entries_summary['price_per_box_dollar']:,.2f}")
    return entries_summary


# date = input_date()
# fruit_name = fruit_category(all_fruits)
# quantities = quantity_sold(date , fruit_name)