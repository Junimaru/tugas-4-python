          
from Pendaftaran_User_Baru import add_user
from Tampilan_User import show_user
from Pendaftaran_Buku_Baru import add_buku
from Peminjaman_Buku import add_pinjam
from Tampilan_Buku import show_buku
from Tampilan_Peminjam import show_pinjam
from Pengembalian import add_kembali
from Pencarian import cari_buku
def main():
    print("""
    ------------LIBRARY MANAGEMENT------------
        1. Pendaftaran User Baru
        2. Pendaftaran Buku Baru
        3. Peminjaman
        4. Tampilkan Daftar Buku
        5. Tampilkan Daftar User
        6. Tampilkan Daftar Peminjam
        7. Cari Buku
        8. Pengembalian
        9. Exit
         """)
    pilihan = input("Masukkan No tugas: ")
    print("-------------------------------")
    if pilihan == "1":
        add_user()
    elif pilihan == "2":
        add_buku()
    elif pilihan == "3":
        add_pinjam()
    elif pilihan == "4":
        show_buku()
    elif pilihan == "5":
        show_user()
    elif pilihan == "6":
        show_pinjam()
    elif pilihan == "7":
        cari_buku()
    elif pilihan == "8":
        add_kembali()
    elif pilihan == "9":
        print("terimakasih")
    else:
        print("Pilihan yang anda masukkan salah")
        main()
main()




