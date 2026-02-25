from book import Book
from member import Member
from staff import Staff
from borrow_transaction import BorrowTransaction

# Membuat objek
book1 = Book("Python Dasar", "Andi", "12345")
member1 = Member("Ahmad", "M01")
staff1 = Staff("Budi", "S01")

# Membuat transaksi
transaction1 = BorrowTransaction(book1, member1, staff1, "24-02-2026")

# Proses peminjaman
transaction1.borrow_book()

# Coba pinjam lagi (harus gagal)
transaction1.borrow_book()

# Proses pengembalian
transaction1.return_book()