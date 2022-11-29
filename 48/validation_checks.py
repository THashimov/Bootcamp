from book_class import Book

# Get the title and author
# Split them into lists and capitalize each word
# Re join them to a string and return
def get_title_and_author():
    title = input("Please enter the title of the book\n")
    author = input("Please enter the author of the book\n")

    title = title.split()
    author = author.split()

    for i in range(len(title)):
        title[i] = title[i].capitalize()
    
    for i in range(len(author)):
        author[i] = author[i].capitalize()
    
    title = " ".join(title)
    author = " ".join(author)

    return (title, author)

def get_qty():
    print("Please enter the quantity of books")
    while True:
        qty = input()
        try :
            int(qty)
            return qty
        except :
            print("Invalid input, please enter a number")

def create_book():
    title_author = get_title_and_author()    
    print("How many copies do you want to add?")
    qty = get_qty()

    return Book(title_author[0], title_author[1], qty)