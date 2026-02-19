from buku import Buku
from anggota import Anggota
from perpustakaan import Perpustakaan

# Membuat perpustakaan
perpus = Perpustakaan("Perpustakaan Kota")

# Membuat buku
buku1 = Buku("Matematika", "Budi")
print(buku1)
buku2 = Buku("Fisika", "Andi")

# Membuat anggota
anggota1 = Anggota("Ahmad", "155")

# Menambahkan buku & anggota ke perpustakaan
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_anggota(anggota1)

# Proses peminjaman
perpus.pinjam_buku(anggota1, buku1)

# Proses pengembalian
perpus.kembalikan_buku(anggota1, buku1)
