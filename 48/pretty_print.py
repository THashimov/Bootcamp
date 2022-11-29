def pretty_print(books):
    print("\033[95m" + "\n{:<15} {:<55} {:<30} {:<25}\n".format("Id", "Title", "Author", "Quantity") + "\033[0m")

    for i in range(len(books)) :
        print("{:<15} {:<55} {:<30} {:<25}".format(books[i][0], books[i][1], books[i][2], books[i][3]))
    print()