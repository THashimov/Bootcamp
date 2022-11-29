import db_class
from book_class import Book
import validation_checks

TABLE_NAME = "ebook_store"

# Create initial books
def create_books(db, ids):
    titles = ["A Tale Of Two Cities", "Harry Potter And The Philosopher's Stone", "The Lion, The Witch And The Wardrobe", "The Lord Of The Rings", "Alice In Wonderland"]
    authors = ["Charles Dickens", "J.K Rowling", "C.S Lewis", "J.R.R Tolkien", "Lewis Carroll"]
    qty = [30, 40, 25, 37, 12]

    
    for i in range(len(titles)):
        book = Book(titles[i], authors[i], qty[i])
        db.insert_into_table(ids[i], book, TABLE_NAME)
        
# Ask user to enter the details of a book to be added to the db
def add_book(db, id):
    book = validation_checks.create_book()
    db.insert_into_table(id, book, TABLE_NAME)

# Get the title, author, qty of the book you want to update
# Update the database
def update_qty(db):
    title_author = validation_checks.get_title_and_author()
    qty = validation_checks.get_qty()
    db.update_qty(title_author, qty, TABLE_NAME)

# Get the title, author, qty of the book you want to update
# Update the database
# Find the id of record in the db and return it so we can delete it from the ids
def delete_book(db):
    title_author = validation_checks.get_title_and_author()
    id = db.get_id(title_author, TABLE_NAME)
    db.remove_record(id, TABLE_NAME)
    return id

def show_all(db):
    db.show_all(TABLE_NAME)
    
def search_for_book(db):
    title_author = validation_checks.get_title_and_author()
    db.show_book(title_author, TABLE_NAME)

ids = [3001, 3002, 3003, 3004, 3005]

# Create database
db = db_class.DB()
db.create_table(TABLE_NAME)
create_books(db, ids)

options = '''

Please select from the following options. Enter a number to make your selection
    1: Add Book
    2: Update Quantity 
    3: Delete Book
    4: Show all books
    5: Search book by title and author
    0: Exit'''

# Check if the choice is an integer, if it is then it is valid and we can call the correct function
while True:
    print(options)
    choice = input().strip()
    if choice == "1":
        id = ids[-1]
        id += 1
        add_book(db, id)
        ids.append(id)
        print("Book Added!\n\n\n")
    elif choice == "2":
        update_qty(db)
        print("Quantity Updated!\n\n\n")
    elif choice == "3":
        id = delete_book(db)
        if id != 0:
            ids.remove(id)
            print("Book Removed!\n\n\n")
        else :
            print("Sorry, there is no such book\n\n\n")
    elif choice == "4":
        show_all(db)
    elif choice == "5":
        search_for_book(db)
    elif choice == "0":
        break
    else:
        print("Please chose from the options above")
