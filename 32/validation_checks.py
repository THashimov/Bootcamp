# Iterate over the shoe list and check if any of the codes in the list match the code we entered
def is_code_in_list(code, shoe_list) :
    for i in range(len(shoe_list)) :
        if shoe_list[i].code == code :
            return True
    else :
        return False

# Check if the first 3 letters of teh code are SKU
# Then check if the next characters can be cast to an int
def is_code_valid(code) :
    if code[0:3] == "SKU" :
        try :
            int(code[3:])
            return True
        except :
            return False
    else :
        return False

# Ensure string is longer than 1 character
def is_string_longer_than_one() :
    while True :
        string = input()
        if len(string) > 0 : 
            return string
        else :
            print("Invalid input. Please try again")

# Check if the code is valid and then check if it is in the list
def get_product_code(shoe_list) :
    while True :
        code = input().upper()
        if is_code_valid(code) :
            if is_code_in_list(code, shoe_list) :
                print("Sorry, code is already assigned to an item")
            else :
                return code
        else : 
            print("Invalid input. All codes start with SKU followed by a sequence of numbers")

def is_valid_int() :
    while True :
        val = input()
        if val.lower() == 'm' :
            return -1
        else :
            try :
                int(val) 
                return int(val)
            except :
                print("Invalid input, please enter a number")