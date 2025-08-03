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
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                return
        print(f"Book '{title}' was not checked out.")



