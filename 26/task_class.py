from datetime import date

# Create a task class
# Assign all of teh parameters that get passed by the user
# Assign todays date using datetime module
class Task :
    def __init__(self, username, title, description, due_date) :
        today = date.today()

        self.username = username
        self.title = title
        self.description = description
        self.current_date = today.strftime("%d %b %Y")
        self.due_date = due_date
        self.task_completed = "No"
        self.task_num = 0