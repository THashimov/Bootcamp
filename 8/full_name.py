name = input("Please enter your full name ")

# Loop until a name is entered in the correct format
while True:
    name.strip()
    if len(name) < 1 :
        print("You haven't entered anything, please try again")
        name = input("Please enter your full name ")
    elif len(name) < 4 :
        print("You have entered less than 4 characters, please ensure you have entered your first name and surname")
        name = input("Please enter your full name ")
    elif len(name) > 25 :
        print("You have entered more than 25 characters, please only enter your first name and surname")
        name = input("Please enter your full name ")
    elif ' ' in name :
        print("Thank you for entering your name")
        break