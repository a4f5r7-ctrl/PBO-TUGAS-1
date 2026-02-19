class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)

    def pinjam_buku(self, anggota, buku):
        if buku in self.daftar_buku:
            if buku.status == "tersedia":
                buku.status = "dipinjam"
                anggota.buku_dipinjam.append(buku)
                print(f"{anggota.nama} berhasil meminjam {buku.judul}")
            else:
                print("Buku sedang dipinjam")
        else:
            print("Buku tidak ada di perpustakaan")

    def kembalikan_buku(self, anggota, buku):
        if buku in anggota.buku_dipinjam:
            buku.status = "tersedia"
            anggota.buku_dipinjam.remove(buku)
            print(f"{anggota.nama} berhasil mengembalikan {buku.judul}")
        else:
            print("Buku ini tidak dipinjam oleh anggota tersebut")
