import validation_checks
from task_class import Task 

# Check if the task can be changed
# Ask the user which user they would like to assign the task to
# Check if the username exists
# If it does, iterate over the file until we find the line which matches with the task number
# Change the user to the new user
# Write all the data back to the file
def change_user_of_task(task):
    if validation_checks.has_task_been_completed(task) != True:
        print("Please enter the user you would like to assign the task to")
        while True :
            user = input()
            if user == "-1" :
                break
            if validation_checks.check_if_username_exists(user) :
                tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')
                modified_content = []

                for line in tasks_file :
                    if line[:1] == str(task) :
                        split_line = line.split()
                        split_line[1] = user.lower() + ","
                        modified_content.append(" ".join(split_line) + "\n")
                    else :
                        modified_content.append(line)

                tasks_file.close()
                tasks_file = open('26/tasks.txt', 'w', encoding='UTF-8')

                for line in modified_content :
                    tasks_file.write(line)

                tasks_file.close()
                print(f"Task now assigned to {user}")
                break
            else :
                print("Sorry, user does not exists, please try again")
    else :
        print("Sorry, task cannot be modified as it is already complete")

# If user choses to edit the task, they can change who the task was assigned to or the due date. This is only allowed if the task is marked as incomplete
# We need to find the task by using the number
# Open the file and read the file until we find the line starting with the task 
# Iterate over each line in the file saving the whole line read into a list
# If we find the line which corresponds to the task number, modify the string we save to the list
# Go to the last index of the list and change it to a yes
# Join the list back up and push it to the modified content list
# Close the file and re-open it, in write only mode, to overwrite the old file
# Write the new data to the file
# This seems pretty inefficient but I couldn't find a way to open a file and modify a line without writing to the whole file, not very scalable!
def set_task_to_complete(task) :
    if validation_checks.has_task_been_completed(task) != True :
        tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')
        modified_content = []

        for line in tasks_file :
            if line[:1] == str(task) :
                split_line = line.split()
                if split_line[len(split_line) - 1] == "No" :
                    split_line[len(split_line) -1 ] = "Yes"
                modified_content.append(" ".join(split_line) + "\n")
            else :
                modified_content.append(line)

        tasks_file.close()
        tasks_file = open('26/tasks.txt', 'w', encoding='UTF-8')

        for line in modified_content :
            tasks_file.write(line)

        tasks_file.close()

        print("Task has been marked complete")
    else :
        print("Task already complete")

# Add a task to the tasks file
# Format a string from the Task class 
# Check if the task already exists
# Check the first char of the last line so the next task we enter is allocated a higher number than the previous task
# Increment the last number and assign it to the new task
# We need to remove the first character when doing the check to ensure it doesn't match the \n 
# Else, write that string to the file
def add_task(Task) :
    tasks_file = open('26/tasks.txt', 'r+', encoding='UTF-8')
    num_of_last_task = 0
    for line in tasks_file :
        num_of_last_task = int(line[:1])
    num_of_last_task += 1
    formatted_string = f"\n{str(num_of_last_task)}, {Task.username}, {Task.title}, {Task.description}, {Task.current_date}, {Task.due_date}, {Task.task_completed}"
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
# Pass the object into add_task
def create_task() :
    print("Please enter the username of the person this task is assigned to or press -1 at any time to return to main menu")
    while True :
        username = input()
        if username == '-1' :
            return False
        if validation_checks.check_if_username_exists(username) :
            print("Please enter the title of the task")
            while True :
                title = input()
                if title == '-1' :
                    return False
                if len(title) < 1 :
                    print("Title is empty, please enter a valid title")
                else :
                    break
            print("Please enter a description of the task")
            while True :
                desc = input()
                if desc == '-1' :
                    return False
                if len(desc) < 1 :
                    print("Description is empty, please enter a valid description")
                else :
                    break
            print("Please enter the due date of the task in the following format: dd mon yyyy")
            while True :
                due_date = input()
                if due_date == '-1' :
                    return False
                if validation_checks.validate_date_format(due_date) :
                    return Task(username, title, desc, due_date)
                else :
                    print("Invalid format, please try again. Hint: dd mon yyyy")
        else :
            print("Sorry, user does not exist. Please try again or press -1 to return to main menu")

# Modify the task selected
# Ask user if they want to mark the task as complete or edit the task
def modify_task(task):
    print("Would you like to mark task complete? Select with Y or N")
    while True :
        choice = input()
        if choice.upper() == 'Y' :
            set_task_to_complete(task)
            break
        elif choice.upper() == 'N' :
            break
        else :
            print("Invalid input, please enter Y or N")
    
    print("Would you like to change who the task is assigned to? Select with Y or N")
    while True :
        choice = input()
        if choice.upper() == 'Y' :
            change_user_of_task(task)
            break
        elif choice.upper() == 'N' :
            break
        else :
            print("Invalid input, please enter Y or N")

    print("Would you like to change the due date of the task? Select with Y or N")
    while True :
        choice = input()
        if choice.upper() == 'Y' :
            change_due_date(task)
            break
        elif choice.upper() == 'N' :
            break
        else :
            print("Invalid input, please enter Y or N")

# Open the file and read each line until we find the right task number
# Once we find the right task number, we can ask the user to input a date
# If date is valid, capitalize the date and ensure we push with a space
# Split the line into a list, modify the date and then write to file
def change_due_date(task):
    if validation_checks.has_task_been_completed(task) != True:
        print("What would you like the new due date to be? Please use dd mon yyyy")
        while True :
            date = input()

            if validation_checks.validate_date_format(date) and validation_checks.is_date_in_the_future(date):
                date = date.split()
                date[1] = date[1].capitalize()
                date = " ".join(date)
                tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')
                modified_content = []

                for line in tasks_file :
                    if line[:1] == str(task) :
                        split_line = line.split(",")
                        split_line[5] = " " + date
                        line = ",".join(split_line)
                        modified_content.append(line)
                    else :
                        modified_content.append(line)

                tasks_file.close()
                tasks_file = open('26/tasks.txt', 'w', encoding='UTF-8')

                for line in modified_content :
                    tasks_file.write(line)

                tasks_file.close()
                print("Due date changed")
                break
            else :
                print("Invalid format, please enter a date using dd mon yyyy")
    else :
        print("Sorry, task cannot be modified as it is already complete")