from Email_class import Email
from Inbox_class import Inbox

inbox = Inbox()
user_choice = ""

#ensure the user selects a number that is the correct type and doesn't go out of bounds of the inbox
# In the try block, we try to index the inbox by the index before returning it, if this fails then we are out of bounds
# If user selects 0, force the try block to fail
def which_email() :
    while True :
        index = input()
        try :
            index = int(index) - 1
            email = inbox.get_email(index)
            return email
        except :
            return IndexError


# Ask the user to enter their email address and email content
# Then create a new email instance and push it to the inbox
# Check the email address entered has an "@" and at least one period
def send_email() :
    print("Please enter your email address")
    while True :
        addr = input()
        if "@" in addr and "." in addr :
            break
        else :
            print("Invalid email address, please try again")
    content = input("Please enter the contents of the email you would like to send\n")
    email = Email(addr, content)
    inbox.add_to_inbox(email)
    print("Email sent")

def show_unread_emails() :
    unread_emails = inbox.get_unread_emails()
    for email in unread_emails :
        email.show_email()

def show_spam_emails() :
    spam = inbox.get_spam_emails()
    for email in spam :
        email.show_email()

# After getting the users choice, we check against a list of valid choices
# If the inbox is empty and the choice is valid, we print that the inbox is empty and don't go any further
# Else, the rest of the block will run
while user_choice != "quit":
    number_of_emails = len(inbox.inbox)
    num_of_emails = f"are {number_of_emails} emails" if number_of_emails > 1 else f"is {number_of_emails} email"

    valid_choices = ["read", "mark spam", "inbox", "show unread", "show spam", "delete"]

    user_choice = input("What would you like to do - read/mark spam/send/quit/inbox/show unread/show spam/delete?\n")

    if number_of_emails == 0 and user_choice in valid_choices:
        print("Hooray, your inbox is empty!")
    elif user_choice.lower() == "read" :
        print(f"Which email would you like to read? There {num_of_emails}")
        try :
            email = which_email()
            email.show_email()
        except :
            print("Sorry, you selected an email that doesn't exist") 
    elif user_choice.lower() == "mark spam" :
        print(f"Which email would you like to mark as spam? There {num_of_emails}")
        try :
            email = which_email()
            email.mark_as_spam()
            print("Email successfully marked as spam")
        except :
            print("Sorry, you selected an email that doesn't exist") 
    elif user_choice.lower() == "delete" :
        print(f"Which email would you like to delete? There {num_of_emails}")
        try :
            email = which_email()
            inbox.delete(email)
            print("Email successfully deleted")
        except :
            print("Sorry, you selected an email that doesn't exist") 
    elif user_choice.lower() == "send" :
        send_email()
    elif user_choice.lower() == "inbox" :
        inbox.get_count()
    elif user_choice.lower() == "show unread" :
        show_unread_emails()
    elif user_choice.lower() == "show spam" :
        show_spam_emails()
    elif user_choice.lower() == "quit" :
        print("Goodbye")
    else:
        print("Oops - incorrect input")
