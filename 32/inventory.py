import validation_checks
from Shoe_class import Shoe
import pretty_print

# The list will be used to store a list of objects of shoes.
shoe_list = []

# Create a temporary string which will hold all the file data
# Read the file and find which line the product code is on and write each line to the temp string
# Ask the user how many shoes they'd like to order
# Change the stock value and write it to the temp string
# Carry on writing all the values to the temp string and overwrite the inventory file
# First we user file.seek(0) to index the file at the beginning
# Then we truncate to erase the file
def update_stock(code) :
    file = open("32/inventory.txt", "r+", encoding="UTF-8")
    tmp_string = ""

    for line in file :
        split = line.split(",")
        if split[1] == code :
            print(f"The current stock level is {split[4].strip()}. How many items would you like to order?")
            stock = int(split[4].strip())
            val_to_order = validation_checks.is_valid_int()
            if val_to_order == -1 :
                return
            else :
                stock += val_to_order
                split[4] = str(stock)
                tmp_string += ",".join(split) + "\n"
        else :
            tmp_string += line

    file.seek(0)
    file.truncate()
    file.write(tmp_string)
    file.close()

# Open the inventory file and read it line by line, skipping the first line
# Split the line into a list
# Check the last 2 values in the list are numbers
# Create a shoe object using the values in the list
# Push each obj into shoe_list
def read_shoes_data():
    with open("32/inventory.txt", "r", encoding="UTF-8") as file:
        next(file)
        for line in file :
            line = line.split(",")
            try :
                int(line[-1])
                int(line[-2])
                shoe = Shoe(line[0], line[1], line[2], line[3], line[4])
                shoe_list.append(shoe)
            except :
                continue


# First check if the code is valid
# Then we can iterate over the list and get the shoe data
# Which we can pass into pretty print
def search_shoe():
    print("Please enter a product code")
    while True :
        code = input().upper()
        if code == 'M' :
            break
        elif validation_checks.is_code_valid(code) :
            for i in range(len(shoe_list)) :
                if shoe_list[i].code == code :
                    return shoe_list[i]
            else :
                print("Sorry, there is no product by that code")
                break
        else :
            print("Sorry, that's an invalid code. Code format is SKU followed by numbers")


# Gather all of the data needed to make a new shoe object
# Create a shoe object and push it to the list
# Not really sure what this function is supposed to do so I've decided to create a new shoe and write it to the file
def capture_shoes():
    print("Which country is the shoe in?")
    country = validation_checks.is_string_longer_than_one()
    if country == 'm' :
        return
    print("Please enter the product code")
    code = validation_checks.get_product_code(shoe_list)
    if code == 'm' :
        return
    print("Please enter the product name")
    product = validation_checks.is_string_longer_than_one()
    if product == 'm' :
        return
    print("Please enter the product price")
    cost = validation_checks.is_valid_int()
    if cost == 'm' :
        return
    print("Please enter the quantity of shoes")
    quantity = validation_checks.is_valid_int()    
    if quantity == 'm' :
        return
    shoe = Shoe(country, code, product, cost, quantity)

    with open("32/inventory.txt", "a", encoding="UTF-8") as file :
        shoe = shoe.__str__()
        file.write(shoe)

    shoe_list.append(shoe)

# Iterate over the shoe list and pass the shoe to pretty print to extract all the data
# Now we can create a table by pushing the list from pretty print into table
# Save that to a table and pass it back pretty print
def view_all():
    table = []
    for i in range(len(shoe_list)) :
        shoe_data = pretty_print.split_data_into_table(shoe_list[i])
        table.append(shoe_data)

    pretty_print.pretty_print_all_shoes(table)

# Save the first quantity to a variable
# Save the first product code to a variable
# Iterate over the shoe list and run get quantity on each one
# With every iteration, we can check if the next quantity is less than the previous value
# If it is, we can overwrite the cost and the code
# We can then use this to access the shoe in the list
def re_stock():
    lowest_stock = shoe_list[0].get_quantity()
    lowest_code = shoe_list[0].get_code()

    for i in range(len(shoe_list)) :
        if shoe_list[i].get_quantity() < lowest_stock :
            lowest_stock = shoe_list[i].get_quantity()
            lowest_code = shoe_list[i].get_code()

    update_stock(lowest_code)


# Iterate over the shoe list
# Pass each shoe to pretty print to extract all the data and return a list
# Create a new value which is the total value and push it to the shoe_data before pushing to the table
# Save these to a table and pass it to pretty print
def value_per_item():
    table = []
    for i in range(len(shoe_list)) :
        shoe_data = pretty_print.split_data_into_table(shoe_list[i])
        val_of_stock = int(shoe_data[-1]) * int(shoe_data[-2])
        shoe_data.append(val_of_stock)
        table.append(shoe_data)

    pretty_print.pretty_print_value_per_item(table)
    
# Save the first quantity to a variable
# Iterate over the shoe list and run get quantity on each one
# With every iteration, we can check if the next quantity is higher than the previous value
# If it is, we can save the current shoe object in the shoe variable
# We can then use this to print the data of this shoe
def highest_qty():
    highest_stock = 0
    shoe = shoe_list[0]

    for i in range(len(shoe_list)) :
        if shoe_list[i].get_quantity() > highest_stock :
            highest_stock = shoe_list[i].get_quantity()
            shoe = shoe_list[i]

    table = pretty_print.split_data_into_table(shoe)
    table.append("Yes")
    
    pretty_print.show_shoe([table])

#==========Main Menu=============

# Read al the data from the file into a list upon starting the program
read_shoes_data()

print("Welcome to this sweet inventory manager!")

while True :
    menu_options = '''
Please selecting from the following options

search - Search by code
capture - Add a new shoe to the inventory
view all - View all shoes in stock
re stock = Re stock the shoe of the lowest quantity
value - Show total value of each item
highest - Show item of highest quantity
exit - Quit
m - Return to main menu

'''
    choice = input(menu_options.lower())
    if choice == "search" :
        search_shoe() 
    elif choice == "capture" :
        capture_shoes()
    elif choice == "view all" :
        view_all()
    elif choice == "re stock" :
        re_stock()
    elif choice == "value" :
        value_per_item()
    elif choice == "highest" :
        highest_qty()
    elif choice == "exit" :
        exit()
    else :
        print("Sorry, that was an invalid choice, please try again")