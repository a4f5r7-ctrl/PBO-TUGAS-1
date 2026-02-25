class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self) -> None:
        self.is_borrowed = True

    def return_book(self) -> None:
        self.is_borrowed = False