class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out


    def __str__(self):
        return f"{self.title} by {self.author})"
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f"You have checked out '{book.title}'."
        return f"'{title}' is not available for checkout."
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f"You have returned '{book.title}'."
        return f"'{title}' was not checked out."
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            return "No books available."
        return "\n".join(str(book) for book in available_books)