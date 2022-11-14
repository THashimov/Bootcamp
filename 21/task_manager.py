#=====importing libraries===========
from task_class import Task 
import os

# Create a new user
# Ask for a username
# Check the username is not empty
# Enter a loop and ask for a password, then ask to repeat the password
# If password does not match, ask for a password again and re-run the loop 
# If passwords match, return the username and password in a tuple
def create_new_user() :
    can_save_user = False
    while can_save_user == False :
        print("Please enter a username or press m at any time to return to main menu")
        while True :
            username = input()
            if username.upper() == 'M' :
                return False
            if len(username) > 0 :
                print("Please enter a password with at least 5 characters")
                break
            else :
                print("Invalid input, please enter a username")
        while True :
            while True :
                pwd = input()
                if pwd.upper() == 'M' :
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
def add_user_to_db(new_user) :
    users_file = open('21/user.txt', 'r+', encoding='UTF-8')
    if f"{new_user[0]}, {new_user[1]}" in users_file :
        print("User is already registered!\n")
        users_file.close()
    else :
        users_file.write(f"\n{new_user[0]}, {new_user[1]}")
        users_file.close()
        print("User successfully added\n")

# Check if the username exists 
# Return true or false depending on the outcome of the search
def check_if_username_exists(username) :
    users_file = open('21/user.txt', 'r+', encoding='UTF-8')
    for line in users_file :
        username_in_file = line.split()[0]
        if f"{username}," == username_in_file :
            users_file.close()
            return True
    users_file.close()
    return False


# Add a task to the tasks file
# Format a string from the Task class 
# Check if the task already exists
# We need to remove the first character when doing the check to ensure it doesn't match the \n 
# Else, write that string to the file
def add_task_to_db(Task) :
    tasks_file = open('21/tasks.txt', 'r+', encoding='UTF-8')
    formatted_string = f"\n{Task.username}, {Task.title}, {Task.description}, {Task.current_date}, {Task.due_date}, {Task.task_completed}"
    if formatted_string[1:] in tasks_file :
        print("Task already exists for this user!")
        tasks_file.close()
    else :
        tasks_file.write(formatted_string)
        tasks_file.close()
        print("Task added successfully\n\n")

# Ask for a username
# Check if the username exists
# If it doesn't, print a message and give the option to return to main menu so the user can be added
# If user does exist, ask for the title of the task, description of task and the due date
# When checking the date, we split the due date into a list then try casting the day and year into ints. Then we check the length of the month. If everything passes, we have a valid date and we can break
# Create an object with all the data
# Pass the object into add_task_to_db
def create_task() :
    print("Please enter the username of the person this task is assigned to or press m at any time to return to main menu")
    while True :
        username = input()
        if username.upper() == 'M' :
            return False
        if check_if_username_exists(username) :
            print("Please enter the title of the task")
            while True :
                title = input()
                if title.upper() == 'M' :
                    return False
                if len(title) < 1 :
                    print("Title is empty, please enter a valid title")
                else :
                    break
            print("Please enter a description of the task")
            while True :
                desc = input()
                if desc.upper() == 'M' :
                    return False
                if len(desc) < 1 :
                    print("Description is empty, please enter a valid description")
                else :
                    break
            print("Please enter the due date of the task in the following format: dd mon yyyy")
            while True :
                due_date = input()
                if due_date.upper() == 'M' :
                    return False
                date = due_date.split()
                try :
                    int(date[0]) 
                    int(date[2]) 
                    if len(date[1]) != 3 :
                        int("Force the try block to fail")
                    else :
                        break
                except :
                    print("Invalid format, please try again. Hint: dd mon yyyy")
            return Task(username, title, desc, due_date)
        else :
            print("Sorry, user does not exist. Please try again or press m to return to main menu")
    
# Print a line he full width of the console above and below the text
# Open the file and iterate over each line
# Split each line into a list so we can access the appropriate data
# Print a line the width of the terminal above and below the data
# If we pass a username, we check if the username matches the username on the current line we are reading
# If it does, print that line
# If the line does not match the username, don't print it
# If the username is "all", print all tasks
def view_all_tasks(user) :
    tasks_file = open('21/tasks.txt', 'r+', encoding='UTF-8')
    task = "Task:"
    assigned_to = "Assigned to:"
    date_assigned = "Date assigned:"
    due_date = "Due date:"
    task_completion = "Task complete?"
    desc = "Task description:"

    
    for line in tasks_file :
        line_data = line.split(",")
        if user != "all" :
            if line_data[0] == user :
                print(u'\u2500' * os.get_terminal_size().columns)
                print(f"{task : <30}{line_data[1].strip() : >}")
                print(f"{assigned_to : <30}{line_data[0].strip() : >}")
                print(f"{date_assigned : <30}{line_data[3].strip() : >}")
                print(f"{due_date : <30}{line_data[4].strip() : >}")
                print(f"{task_completion : <30}{line_data[5].strip() : >}")
                print(f"{desc : <30}{line_data[2].strip() : >}")
                print(u'\u2500' * os.get_terminal_size().columns)
        else :
            print(u'\u2500' * os.get_terminal_size().columns)
            print(f"{task : <30}{line_data[1].strip() : >}")
            print(f"{assigned_to : <30}{line_data[0].strip() : >}")
            print(f"{date_assigned : <30}{line_data[3].strip() : >}")
            print(f"{due_date : <30}{line_data[4].strip() : >}")
            print(f"{task_completion : <30}{line_data[5].strip() : >}")
            print(f"{desc : <30}{line_data[2].strip() : >}")
            print(u'\u2500' * os.get_terminal_size().columns)


    tasks_file.close()



# Open both files
# Iterate over both files and add 1 to each corresponding variable, every time we read a line
def show_stats() :
    all_users = open('21/user.txt', 'r', encoding='UTF-8')
    all_tasks = open('21/tasks.txt', 'r', encoding='UTF-8')
    
    total_tasks = 0
    total_users = 0

    for line in all_users :
        total_users += 1
    for line in all_tasks :
        total_tasks += 1


    print(u'\u2500' * os.get_terminal_size().columns)
    print(f"{'Number of users' : <30}{'Number of tasks' : >}")
    print(f"{total_users : <30}{total_tasks : >}")
    print(u'\u2500' * os.get_terminal_size().columns)

#====Login Section====

# Ask for username 
# Ask for password
# Open the user.txt file
# Iterate over every line and check if line matches the username and password
# Break if true, keep loping if false
print("Please enter you username")
can_login = False
while can_login == False :
    username = input() 
    pwd = input("Please enter your password\n") 
    all_users = open('21/user.txt', 'r', encoding='UTF-8')
    for line in all_users :
        if line.strip() == f"{username}, {pwd}" :
            print("Login successful\n")
            can_login = True
            pwd_correct = True
            all_users.close()
            break
    else :
        print("Sorry, that is the incorrect username or password. Please enter your username")

while True:
    # Create a menu options 
    # If the user is admin, add a new option of display statistics
    # If user is not admin, do not add new option and delete the option to register a user
    # Then get the users choice and make it lower case
    menu_options = '''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
'''

    if username == "admin" :
        menu_options += "ds - Display statistics\n:"
    else :
        menu_options = menu_options.split("\n")
        menu_options.remove("r - Registering a user")
        menu_options = "\n".join(menu_options)

    menu = input(menu_options).lower()

    # Registering a user
    # Run the create_new_user function to create a user and return the data
    # Run add_user_to_db
    # The add_user_to_db function will add the user and print a success or fail message as well as adding the user if user does not exist
    if menu == 'r':
        if username == "admin" :
            print("\n")
            new_user = create_new_user()
            if new_user != False :
                add_user_to_db(new_user)
        else :
            print("Sorry, only admin can register new users")

    elif menu == 'a':
        task = create_task()
        if task == False :
            pass
        else :
            add_task_to_db(task)

    elif menu == 'va':
        view_all_tasks("all")

    elif menu == 'vm':
        view_all_tasks(username)

    elif menu == 'ds' :
        show_stats()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")