import mysql.connector as consql
from datetime import datetime
from datetime import timedelta
from Def_Input import inputStr, inputInt, upd_buku, hps_peminjam

#Membuat Koneksi ke SQL
mycon = consql.connect(
        host='localhost',
        user='root', 
        password='ganteng')

#membuat cursor
cursor = mycon.cursor()

#menyambungkan ke db_perpus    
cursor.execute("USE db_perpus")

#INSERT DATA KEMBALI
def add_kembali():
    """ Memasukkan data buku kemudian menambah stock buku pada database BUKU dan Mengurangi list peminjam pada database PINJAM"""
    while True:
        try:
            id_kemb = inputInt("Masukkan id peminjam: ")
            buku_kemb = inputInt("Masukkan id buku: ")
            break
        except:
            continue
    print("Query Berhasil dieksekusi")
    mycon.commit()
    print("\n\n")
    upd_buku(buku_kemb,1)
    hps_peminjam(buku_kemb,id_kemb)
    print("Query Berhasil dieksekusi")