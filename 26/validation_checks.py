# Check if the username exists 
# Split line into a list
# Check if the first index matched the username
# Return true or false depending on the outcome of the search
def check_if_username_exists(username) :
    users_file = open('26/user.txt', 'r+', encoding='UTF-8')
    for line in users_file :
        line = line.split()
        if f"{username}," == line[0] :
            users_file.close()
            return True
    users_file.close()
    return False



# Iterate over the file and once we find a task that matches the task, change the username
# Once we find the right task, split the line into a list and check if the task is marked complete
# Return true or false
def has_task_been_completed(task):
    tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')

    for line in tasks_file :
        if line[:1] == str(task) :
            split_line = line.split()
            if split_line[len(split_line) - 1] == "No" :
                return False
            else :
                return True
                
    tasks_file.close()


# Check if the month is in the list of valid months, force try block to fail if not
def validate_date_format(date):
    valid_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Now", "Dec"]
    date = date.capitalize()
    date = date.split()
    try :
        int(date[0])
        int(date[2])  
        if date[1].capitalize() not in valid_months :
            int("Force a break from the try")
        return True
    except :
        return False

# Open the file and check the user that the task is assigned to
# If the task matches, split the line into a list and check the second word for a match on the user
def does_task_match_user(task_selected, user) :
    tasks_file = open('26/tasks.txt', 'r', encoding='UTF-8')

    for line in tasks_file :
        if line[:1] == str(task_selected) :
            line = line.split()
            if line[1] == user + "," :
                tasks_file.close()
                return True
            else :
                tasks_file.close()
                return False
            
    tasks_file.close()
    return False