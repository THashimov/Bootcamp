import validation_checks
import os

# Count the number of lines in the tasks_file to get how many tasks have been created
# Check if the line has more than 2 characters in it to skip any empty lines
def get_total_num_of_tasks() :
    tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')

    num_of_tasks = 0

    for line in tasks_file :
        if len(line) > 2 :
            num_of_tasks += 1
        else :
            continue

    tasks_file.close()

    return num_of_tasks

# Find how many tasks are assigned to this user
# Find how many assigned tasks have been completed
# Find how many tasks are overdue
def get_tasks_for_user(user) :
    tasks_file = open('26/tasks.txt', 'r+', encoding='UTF-8')

    tasks_assigned = 0
    tasks_completed = 0
    tasks_overdue = 0

    for line in tasks_file :
        line = line.split(",")
        if line[1].strip() == user :
            tasks_assigned += 1
            if validation_checks.has_task_been_completed(line[0]) :
                tasks_completed += 1
            elif validation_checks.is_task_overdue(line[5]) :
                tasks_overdue += 1
            else :
                continue
        
    return (tasks_assigned, tasks_completed, tasks_overdue)


# Open task_overview file or create if there isn't one
# Open the file containing all of the tasks
# Check if task on the current line has been completed and change the appropriate variable
# If the current task is not complete, check if it's overdue 
# Calculate percentages
# Format the data and write it to the file
def generate_task_overview() :
    task_overview = open('26/task_overview.txt', 'w+', encoding='UTF-8')
    tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')

    num_of_tasks = get_total_num_of_tasks()
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    for line in tasks_file :
        split_line = line.split(",")
        if validation_checks.has_task_been_completed(line[:1]) :
            completed_tasks += 1
        else :
            if validation_checks.is_task_overdue(split_line[5]) :
                overdue_tasks += 1

            incomplete_tasks += 1 
    
    percentage_incomplete = int((incomplete_tasks/num_of_tasks) * 100)
    percentage_overdue = int((overdue_tasks/num_of_tasks) * 100)

    formatted_string = f'''Total tasks: {num_of_tasks}
Total number of completed tasks: {completed_tasks}
Total number of incomplete tasks: {incomplete_tasks}
Total number of overdue tasks: {overdue_tasks}
Percentage of incomplete tasks: {percentage_incomplete}%
Percentage of overdue tasks: {percentage_overdue}%
'''

    task_overview.write(formatted_string)
    tasks_file.close()
    task_overview.close()

def calc_percentages(user_tasks) :
    tasks_completed = 0
    tasks_to_complete = 0
    tasks_overdue = 0

    if user_tasks[1] > 0 :
        tasks_completed = int((user_tasks[1] / user_tasks[0]))
        tasks_to_complete = 100 - tasks_completed
    else :
        tasks_completed = 0
        tasks_to_complete = 100

    if user_tasks[2] > 0 :
        tasks_overdue = int((user_tasks[2] / user_tasks[0]))
    else :
        tasks_overdue = 0

    return (tasks_completed, tasks_to_complete, tasks_overdue)


# Read users file 
# Iterate over the line and each line of len > 2, add one to total users
# Get the total number of tasks
# Get data for each user
# Find all the tasks that are assigned to the current user
# Calculate percentages and push all data to a list
# Iterate over the list and pull out the information, formatting it into a string and then writing it to the file
def generate_user_overview() :
    users_overview = open('26/users_overview.txt', 'w+', encoding='UTF-8')
    users_file = open('26/user.txt', 'r', encoding='UTF-8')

    total_users = 0
    num_of_tasks = get_total_num_of_tasks()
    break_line = u'\u2500' * os.get_terminal_size().columns

    num_of_tasks_for_user = 0
    percentage_of_tasks_for_user = 0
    percentage_completed_by_user = 0
    percentage_to_be_completed_by_user = 0
    percentage_of_overdue_tasks_per_user = 0

    formatted_str = f'''
{break_line}
Number of users generated: {total_users}
Number of tasks generated: {num_of_tasks}
{break_line}
'''

    users_overview.write(formatted_str)

    for line in users_file :
        if len(line) > 2 :
            total_users += 1
        else :
            continue
        user = line.split(",")[0]
        user_tasks = get_tasks_for_user(user)
        num_of_tasks_for_user = user_tasks[0]
        percentages = calc_percentages(user_tasks)
        percentage_of_tasks_for_user = int((num_of_tasks_for_user/num_of_tasks) * 100)
        percentage_completed_by_user = int(percentages[0])
        percentage_to_be_completed_by_user = int(percentages[1])
        percentage_of_overdue_tasks_per_user = int(percentages[2])

        formatted_str = f'''
{break_line}
Number of tasks assigned to {user}: {num_of_tasks_for_user}
Percentage of tasks assigned to {user}: {percentage_of_tasks_for_user}%
Tasks completed by {user}: {percentage_completed_by_user}%
Tasks to be completed by {user}: {percentage_to_be_completed_by_user}%
Tasks overdue for {user}: {percentage_of_overdue_tasks_per_user}%
{break_line}
'''
        users_overview.write(formatted_str)

    users_overview.close()
    users_file.close()

# Ask user if they want to se the user overview or the tasks overview
# Open the file and read the data in the file, printing it to the console 
def show_report() :
    print("Would you like to see the users overview? Select with Y or N")
    while True :
        choice = input()
        if choice.upper() == 'Y' :
            users_overview = open('26/users_overview.txt', 'r', encoding='UTF-8')

            for line in users_overview :
                print(line.strip())
                
            users_overview.close()
            break
        elif choice.upper() == 'N' :
            break
        else :
            print("Invalid input, please select with Y or N")

    print("Would you like to see the tasks overview? Select with Y or N")
    while True :
        choice = input()
        if choice.upper() == 'Y' :
            task_overview = open('26/task_overview.txt', 'r', encoding='UTF-8')
            print("\n")        
            print(u'\u2500' * os.get_terminal_size().columns)

            for line in task_overview :
                print(line.strip())

            print(u'\u2500' * os.get_terminal_size().columns)
            task_overview.close()
            break
        elif choice.upper() == 'N' :
            break
        else :
            print("Invalid input, please select with Y or N")

def generate_report() :
    generate_task_overview()
    generate_user_overview()
    show_report()