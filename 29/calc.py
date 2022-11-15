import math

# Add x into valid ops incase user uses an x instead of a *
valid_ops = ["+", "-", "*", "/", "^", "x"]

def calculate(file, num1, num2, operator) :
    if operator == '+' :
        calc = round((num1 + num2), 2)
    elif operator == '-' :
        calc = round((num1 - num2), 2)
    elif operator == '*' or operator.lower() == 'x':
        calc = round((num1 * num2), 2)
    elif operator == '/' :
        calc = round((num1 / num2), 2)
    elif operator == '^' :
        calc = round((math.pow(num1, num2)), 2)

    calc = f"{num1} {operator} {num2} = {calc}\n"
    file.write(calc)

# Strip the file and then split it where the . is
# If there is a period, the list will be larger than 1 so we can delete the last item if it is larger than 1
# If it isn't, then we just join it back up and return it
def strip_filename(filename) :
    filename = filename.strip()
    file_list = filename.split(".")
    if len(file_list) > 1 :
        del file_list[-1]
        return "".join(file_list)
    else :
        return "".join(file_list)

# Open file and keep it open until we finish
# Ask the user to enter a number, then another number, followed by an operator
# If the user enters e at any time, break from the loop and quit
# Check the operator against a list of known of operators and run the try block if it is in the list
# Then we can cast the 2 numbers to floats to check if they are indeed numbers
# Do the sum and then write it to the file
def calc_option() :
    calcs_file = open("29/calcs.txt", "w", encoding="UTF-8")
    while True :
        num1 = input("Please enter the first number\n")
        if num1.lower() == 'e' :
            break
        num2 = input("Please enter the second number\n")
        if num2.lower() == 'e' :
            break
        operator = input("Please enter the operator. Hint: + - * / ^\n")
        if operator.lower() == 'e' :
            break

        if operator in valid_ops :
            try :
                num1 = float(num1)
                num2 = float(num2)
                calculate(calcs_file, num1, num2, operator)
                print("Calculation saved!")
            except :
                print("Invalid input, please try again with a number")
        elif operator not in valid_ops :
            print("Sorry, that was an invalid operator, please try again")
        else :
            calcs_file.close()
            break

# Ask the user to enter a filename
# If the file does not exist, print an error message to user and go back to the start of the program
# If file exists, open it and print each line
def read_option() :
    print("Please enter the name of the file you would like to read")
    while True :
        filename = input()
        try :
            filename = strip_filename(filename)
            file = open(f"29/{filename}.txt", "r", encoding="UTF-8")
            print()
            for line in file :
                print(line.strip())
            print()
            break
        except :
            print("Sorry, file does not exist!")
            break

print("Welcome to PyCalc! Type e to exit at anytime")
print("Would you like to carry out a calculation or read all calcs saved from a file?")
while True :
    print("Enter 'calc' to calculate or 'file' to read saved calcs")
    choice = input()
    if choice.lower() != 'e' :
        if choice.lower() == "calc" :
            calc_option()
            continue
        elif choice.lower() == "file" :
            read_option()
            continue
        else :
            print("Invalid input, please try again")
    else :
        break