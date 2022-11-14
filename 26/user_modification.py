# Create a new user
# Ask for a username
# Check the username is not empty
# Enter a loop and ask for a password, then ask to repeat the password
# If password does not match, ask for a password again and re-run the loop 
# If passwords match, return the username and password in a tuple
def create_new_user() :
    can_save_user = False
    while can_save_user == False :
        print("Please enter a username or press -1 at any time to return to main menu")
        while True :
            username = input()
            if username == '-1' :
                return False
            if len(username) > 0 :
                print("Please enter a password with at least 5 characters")
                break
            else :
                print("Invalid input, please enter a username")
        while True :
            while True :
                pwd = input()
                if pwd == '-1' :
                    return False
                if len(pwd) < 5 :
                    print("Password too short, please try again")
                else :
                    print("Please repeat the password")
                    break
            pwd_repeat = input()
            if pwd == pwd_repeat :
                return (username, pwd)
            else :
                print("Passwords didn't match, please enter a password")

# Open the user.txt file
# Check if the new user already exists
# Use a string literal to split the tuple into the correct format
# If we find a match, print a fail to add message
# Else, add the user and print a success message
def reg_user(new_user) :
    users_file = open('26/user.txt', 'r+', encoding='UTF-8')
    if f"{new_user[0]}, {new_user[1]}" in users_file :
        print("User is already registered!\n")
        users_file.close()
    else :
        users_file.write(f"\n{new_user[0]}, {new_user[1]}")
        users_file.close()
        print("User successfully added\n")