import sqlite3
import pretty_print

class DB:
    def __init__(self):
        self.db = sqlite3.connect("python_db")
        self.cursor = self.db.cursor()

    # Create a table if the table does not exist
    def create_table(self, name):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name} ("id" INT PRIMARY KEY, "title" VARCHAR(255), "author" VARCHAR(255), "qty" INT)''')

        self.db.commit()

    # Insert book into table
    def insert_into_table(self, id, book, name):
        self.cursor.execute(f'''INSERT OR IGNORE INTO {name}
                                VALUES(?, ?, ?, ?)''', (id, book.title, book.author, book.qty))

        self.db.commit()


    # Update book quantity
    def update_qty(self, title_author, qty, name):
        self.cursor.execute(f'''UPDATE {name}
                    SET qty = "{qty}"
                    WHERE title = "{title_author[0]}"
                    AND author = "{title_author[1]}"''')

        self.db.commit()

    # Get id
    def get_id(self, title_author, name):
        self.cursor.execute(f'''SELECT * FROM {name} WHERE title = "{title_author[0]}" AND author = "{title_author[1]}"''')
        book = self.cursor.fetchone()
        if book != None :
            return book[0]
        else :
            return 0

    # Delete record
    def remove_record(self, id, name):
        self.cursor.execute(f'''DELETE  from {name}
                    WHERE id = "{id}" ''')

        self.db.commit()


    # Show all books in list
    # Fetch all the books in the db
    # Push the book tuples into an array
    # We can then pass this into pretty print and print the books
    def show_all(self, name):
        book_table = []
        self.cursor.execute(f'''SELECT * FROM {name}''')
        books = self.cursor.fetchall()
        for book in books:
            book_table.append(book)

        pretty_print.pretty_print(book_table)
        
    def show_book(self, title_author, name):
        book_table = []
        self.cursor.execute(f'''SELECT * FROM {name} WHERE title = "{title_author[0]}" AND author = "{title_author[1]}"''')
        books = self.cursor.fetchall()
        for book in books:
            book_table.append(book)

        pretty_print.pretty_print(book_table)