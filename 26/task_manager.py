#=====importing libraries===========
import task_modification
import user_modification
import generate_report
import stats

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
    all_users = open('26/user.txt', 'r', encoding='UTF-8')
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
        menu_options += "gr - Generate reports\nds - Display statistics\n:"
    else :
        menu_options = menu_options.split("\n")
        menu_options.remove("r - Registering a user")
        menu_options = "\n".join(menu_options)

    menu = input(menu_options).lower()

    # Registering a user
    # Run the create_new_user function to create a user and return the data
    # Run reg_user
    # The reg_user function will add the user and print a success or fail message as well as adding the user if user does not exist
    if menu == 'r':
        if username == "admin" :
            print("\n")
            new_user = user_modification.create_new_user()
            if new_user != False :
                user_modification.reg_user(new_user)
        else:
            print("You have made a wrong choice, Please Try again")

    elif menu == 'a':
        task = task_modification.create_task()
        if task == False :
            print("No task created")
        else :
            task_modification.add_task(task)

    elif menu == 'va':
        stats.view_all()

    elif menu == 'vm':
        stats.view_mine(username)

    elif menu == 'ds' :
        if username == "admin" :
            stats.show_stats()
        else:
            print("You have made a wrong choice, Please Try again")

    elif menu == 'gr' :
        if username == "admin" :
            generate_report.generate_report()
        else:
            print("You have made a wrong choice, Please Try again")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

