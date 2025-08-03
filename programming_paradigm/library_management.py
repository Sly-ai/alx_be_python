class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        title = input("which book: ")
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print("Book checked out successfully")
                return
        print(f"Book titled '{title}' is either not in the library or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book titled '{title}' is either not in the library or not checked out.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        for book in available:
            print(f"{book.title} by {book.author}")

Lib = Library()

while True:
    title = input("Please enter Title: ")
    author = input("Please enter Author: ")
    Lib.add_book(Book(title, author))
    print("\nAvailable Books:")
    Lib.list_available_books()
    try_again = input("Add another book? (Y/N): ").lower()
    if try_again == "n":
        break
Lib.check_out_book(title)