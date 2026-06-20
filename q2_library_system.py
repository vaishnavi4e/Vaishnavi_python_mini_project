def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed.")
    else:
        print("Book unavailable.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned.")
    else:
        print("Book not borrowed.")


def register_member(members, member_id):
    before = len(members)
    members.add(member_id)

    if len(members) == before:
        print("Duplicate member ignored.")
    else:
        print(f"Member {member_id} registered.")


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(book_id, details)


def main():
    catalog = {}

    borrowed_books = []

    members = set()

    add_book(catalog, 101, "Python Basics", "John", 2020)
    add_book(catalog, 102, "Data Science", "Alice", 2021)
    add_book(catalog, 103, "AI Fundamentals", "Bob", 2022)
    add_book(catalog, 104, "Machine Learning", "David", 2023)

    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")

    register_member(members, "M001")

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    return_book(borrowed_books, 101)

    show_available(catalog, borrowed_books)


main()