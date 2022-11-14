import task_modification
import validation_checks
import os

# Print a line he full width of the console above and below the text
# Open the file and iterate over each line
# Split each line into a list so we can access the appropriate data
# Print a line the width of the terminal above and below the data
# Check if the username matches the username on the current line we are reading
# If it does, print that line
# If the line does not match the username, don't print it
def view_mine(user) :
    tasks_file = open('26/tasks.txt', 'r+', encoding='UTF-8')
    task_num = "Task number:"
    task = "Task:"
    assigned_to = "Assigned to:"
    date_assigned = "Date assigned:"
    due_date = "Due date:"
    task_completion = "Task complete?"
    desc = "Task description:"
    
    task_nums = []
    
    for line in tasks_file :
        line_data = line.split(",")
        task_nums.append(line_data[0])
        if line_data[1].strip() == user.strip() :
            print(u'\u2500' * os.get_terminal_size().columns)
            print(f"{task_num : <30}{line_data[0].strip() : >}")
            print(f"{task : <30}{line_data[2].strip() : >}")
            print(f"{assigned_to : <30}{line_data[1].strip() : >}")
            print(f"{date_assigned : <30}{line_data[4].strip() : >}")
            print(f"{due_date : <30}{line_data[5].strip() : >}")
            print(f"{task_completion : <30}{line_data[6].strip() : >}")
            print(f"{desc : <30}{line_data[3].strip() : >}")
            print(u'\u2500' * os.get_terminal_size().columns)

    # Check if the task selected matches a task that is assigned to the current user
    # Only run the modification if the task selected is a task that is assigned to the user
    print("Please select a task (by the task number) of enter -1 to go back to main menu")
    while True :
        task_selected = input()
        try :
            int(task_selected)
            break
        except :
            print("Invalid input, please enter a number or -1 to exit")
        
    if validation_checks.does_task_match_user(task_selected, user) :
        task_modification.modify_task(task_selected)
    else :
        print("Sorry, that task is not assigned to you")

    tasks_file.close()

# Print a line he full width of the console above and below the text
# Open the file and iterate over each line
# Split each line into a list so we can access the appropriate data
# Print a line the width of the terminal above and below the data
# Read every line and print the data of each line
def view_all() :
    tasks_file = open('26/tasks.txt', 'r+', encoding='UTF-8')
    task_num = "Task number:"
    task = "Task:"
    assigned_to = "Assigned to:"
    date_assigned = "Date assigned:"
    due_date = "Due date:"
    task_completion = "Task complete?"
    desc = "Task description:"

    for line in tasks_file :
        line_data = line.split(",")
        print(u'\u2500' * os.get_terminal_size().columns)
        print(f"{task_num : <30}{line_data[0].strip() : >}")
        print(f"{task : <30}{line_data[2].strip() : >}")
        print(f"{assigned_to : <30}{line_data[1].strip() : >}")
        print(f"{date_assigned : <30}{line_data[4].strip() : >}")
        print(f"{due_date : <30}{line_data[5].strip() : >}")
        print(f"{task_completion : <30}{line_data[6].strip() : >}")
        print(f"{desc : <30}{line_data[3].strip() : >}")
        print(u'\u2500' * os.get_terminal_size().columns)


    tasks_file.close()

# Open both files
# Iterate over both files and add 1 to each corresponding variable, every time we read a line
def show_stats() :
    all_users = open('26/user.txt', 'r', encoding='UTF-8')
    all_tasks = open('26/tasks.txt', 'r', encoding='UTF-8')
    
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