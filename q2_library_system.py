def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book", book_id, "borrowed successfully.")
    else:
        print("Book", book_id, "cannot be borrowed.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book", book_id, "returned successfully.")
    else:
        print("Book", book_id, "was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(book_id, "-", title, "-", author, "-", year)


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Adding 4 books
    add_book(catalog, 1, "Python Basics", "John", 2022)
    add_book(catalog, 2, "Data Science", "Anu", 2023)
    add_book(catalog, 3, "AI Fundamentals", "Ravi", 2024)
    add_book(catalog, 4, "Web Programming", "Meena", 2021)

    # Registering 3 members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)

    # Trying to register the same member again
    register_member(members, 101)

    print("Members:", members)

    # Borrowing 2 books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    print("Borrowed Books:", borrowed_books)

    # Returning 1 book
    return_book(borrowed_books, 1)

    print("Borrowed Books after return:", borrowed_books)

    # Display available books
    show_available(catalog, borrowed_books)


main()