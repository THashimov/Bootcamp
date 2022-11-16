from Email_class import Email

class Inbox :
    inbox = []
    def __init__(self) :
        self.inbox = []

    # Add email to inbox
    def add_to_inbox(self, email) :
        self.inbox.append(email)

    # Get the length of the inbox 
    def get_count(self) :
        messages = len(self.inbox)
        if messages > 1 :
            print(f"You have {messages} messages in your inbox")
        else :
            print(f"You have {messages} message in your inbox")
    
    # Print the email to terminal and then mark it as read
    def get_email(self, index) :
        self.inbox[index].marks_as_read()
        return self.inbox[index]

    # Iterate over the inbox and check if the email has been read
    def get_unread_emails(self) :
        unread_emails = []
        for i in range(len(self.inbox)) :
            if self.inbox[i].has_been_read :
                continue
            else :
                unread_emails.append(self.inbox[i])
        return unread_emails

    # Iterate over the inbox and check if the email is marked spam
    def get_spam_emails(self) :
        spam = []
        for i in range(len(self.inbox)) :
            if self.inbox[i].is_spam :
                spam.append(self.inbox[i])
        
        return spam

    # Delete an email from inbox 
    def delete(self, email) :
        self.inbox.remove(email)