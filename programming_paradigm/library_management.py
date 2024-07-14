class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        if self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return False
        return True
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, new_book):
        self._books.append(new_book)
        return f"New book added"

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return f'You have successfully checker out "{title}".'
                return f'"{title}" is already checked out.'
        return f'"{title}" is not available in the library.'
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f'You have successfully returned "{title}".'
                return f'"{title}" was not checked out.'
        return f'"{title}" does not belong to this library.'

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f'Title: {book.title}, Author: {book.author}')
        else:
            print("No books are currently available.")
