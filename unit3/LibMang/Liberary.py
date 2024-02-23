from Book import  Book
class Library:
    total_books = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.total_books_in_library = 0

    def add_book(self, book):
        self.books.append(book)
        self.total_books_in_library += book.num_copies
        Library.total_books += book.num_copies
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    