class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book:Book):
        if book not in self.books:
            self.books.append(book)

    def find_boo(self, title):
        if title in self.books:
            return title
        return "Not found"


