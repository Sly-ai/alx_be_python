class Book:
    def __init__(self, title, author, is_checked_out = False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, Book):
        self.__books.append(Book)

    def list_available_books(self):
        for book in self.__books:
            if not book.is_checked_out:
                print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' was not checked out.")

# library_management.py

library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))

library.list_available_books()


