class Book:
    def __init__(self, author,  content: str):
        self.author = author
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return f"----{book.content}-----{book.author}"


class Printer:

    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)