def print_name(first_name = 'Sean', last_name = 'Chang'):
    print(first_name, last_name)

#Positional Arguments
print_name('Sean', 'Chang')

#Keyword Arguments
print_name(last_name = 'Chang', first_name = 'Sean')

#Default Arguments
print_name()

#You can make functions take in a dynamic amount of variables with the unpacking operator
#The function will run as many times as there are arguments (records arguments as tuples)
def print_order(*order_items):
    print(order_items)
#Practice with variable arguments
tables = {
        1: {
            'name' : 'Jiho',
            'vip_status' : False,
            'order' : ('Orange Juice', 'Apple Juice')
            },
        2: {},
        3: {},
        4: {},
        5: {},
        6: {},
        7: {},
    }
print(tables)

def assign_table(table_number, name, vip_status = False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for order in order_items:
        print(order)

assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)

#Kwargs are like variable args but instead take in keyword arguments instead
#Kwargs record arguments as a dictionary
def assign_food_items(**order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    print(order_items)
    print(food)
    print(drinks)

#example call
assign_food_items(food = 'Pancakes, Poached Egg', drinks = 'Water')




