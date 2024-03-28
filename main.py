class Book:
    def __init__(self, name, author, genre, borrowed):
        self.title = name
        self.author = author
        self.genre = genre
        self.borrowed = borrowed

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        print(self.books)
        self.books.append(book)
        print(self.books)

    def borrow_book(self, book):
        print(self.books)
        if len(self.books) != 0:
            for i in range(len(self.books)):
                if self.books[i].title == book.title:
                    self.books.remove(self.books[i])
        print(self.books)

    def return_book(self, book):
        print(self.books)
        self.books.append(book)
        print(self.books)

akobir = Author("Akobir", "UZBEK")
top_books = Book("top books for programming", akobir, "programming", True)
komron_academy = Library()
komron_academy.add_book(top_books)
komron_academy.borrow_book(top_books)
komron_academy.return_book(top_books)
