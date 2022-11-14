# Open task_overview file or create if there isn't one
# Open the file containing all of the tasks
# Count the number of lines in the tasks_file to get how many tasks have been created
# Check if the line has more than 2 characters in it to skip any empty lines
def task_overview() :
    task_overview = open('26/task_overview.txt', 'w+', encoding='UTF-8')
    tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')

    num_of_tasks = 0

    for line in tasks_file :
        num_of_tasks += 1
    pass


def user_overview() :
    pass

def generate_report() :
    pass