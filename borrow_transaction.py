from book import Book
from member import Member
from staff import Staff

class BorrowTransaction:
    def __init__(self, book: Book, member: Member, staff: Staff, borrow_date: str):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False

    def borrow_book(self) -> None:
        if not self.book.is_borrowed:
            self.book.borrow()
            self.member.borrowed_books.append(self)
            print(f"Buku '{self.book.title}' berhasil dipinjam oleh {self.member.name}")
        else:
            print("Buku sudah dipinjam")

    def return_book(self) -> None:
        if not self.returned:
            self.book.return_book()
            self.returned = True
            print(f"Buku '{self.book.title}' berhasil dikembalikan")
        else:
            print("Buku sudah dikembalikan sebelumnya")