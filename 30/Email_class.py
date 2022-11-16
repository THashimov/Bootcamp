import os 

# Create a class and set the types to ensure we don't get a type mixup when instantiating 
class Email :
    has_been_read = bool
    email_contents = str
    is_spam = bool
    from_address = str

    def __init__(self, addr, content) :
        self.from_address = addr
        self.has_been_read = False
        self.is_spam = False
        self.email_contents = content

    def marks_as_read(self) :
        self.has_been_read = True

    def mark_as_spam(self) :
        self.is_spam = True

    # Check if message is spam and change string depending on the value of self.spam
    def show_email(self) :
        spam_message = "is" if self.is_spam else "is not"
        has_been_read = "has" if self.has_been_read else "has not"
        print(u'\u2500' * os.get_terminal_size().columns)
        print(f"Email sent from {self.from_address}")
        print(f"Email {spam_message} Spam")
        print(f"Email {has_been_read} been read\n")
        print(self.email_contents)
        print(u'\u2500' * os.get_terminal_size().columns)
