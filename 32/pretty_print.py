# Not scalable at all but I wanted to experiment with printing in a nice way
def pretty_print_all_shoes(table) :

    print("\033[95m" + "\n{:<25} {:<25} {:<25} {:<25} {:<25}\n".format("Country", "Code", "Product", "Cost", "Quantity") + "\033[0m")
    for row in range(len(table)) :
        print("{:<25} {:<25} {:<25} £{:<25} {:<25}".format(table[row][0], table[row][1], table[row][2], table[row][3], table[row][4]))
    
    print()

def pretty_print_value_per_item(table) :

    print("\033[95m" + "\n{:<25} {:<25} {:<25} {:<25} {:<25} {:<25}\n".format("Country", "Code", "Product", "Cost", "Quantity", "Total Value of Stock") + "\033[0m")
    for row in range(len(table)) :
        print("{:<25} {:<25} {:<25} £{:<25} {:<25} £{:<25}".format(table[row][0], table[row][1], table[row][2], table[row][3], table[row][4], table[row][5]))
    
    print()

# Use this to get the data into a table and then we can add any extra data to it
def split_data_into_table(shoe) :
    shoe = [
            str(shoe.get_country()),
            str(shoe.get_code()),
            str(shoe.get_product()),
            str(shoe.get_cost()),
            str(shoe.get_quantity()),
            ]
    return shoe

def show_shoe(table) :
    print("\033[95m" + "\n{:<25} {:<25} {:<25} {:<25} {:<25} {:<25}\n".format("Country", "Code", "Product", "Cost", "Quantity", "On Sale") + "\033[0m")
    for row in range(len(table)) :
        print("{:<25} {:<25} {:<25} £{:<25} {:<25} {:<25}".format(table[row][0], table[row][1], table[row][2], table[row][3], table[row][4], table[row][5]))
    
    print()