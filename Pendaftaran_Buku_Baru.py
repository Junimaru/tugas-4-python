import mysql.connector as consql
from datetime import datetime
from datetime import timedelta
from Def_Input import inputStr, inputInt

#Membuat Koneksi ke SQL
mycon = consql.connect(
        host='localhost',
        user='root', 
        password='ganteng')

#membuat cursor
cursor = mycon.cursor()

#menyambungkan ke db_perpus    
cursor.execute("USE db_perpus")

#INSERT DATA BUKU
def add_buku():
    """ Memasukkan data buku kemudian data tersebut diinput ke database BUKU"""
    while True:
        try:
            kode_buku = inputInt("Masukkan kode buku: ")
            nama_buku = inputStr("Masukkan nama buku: ")
            kat_buku = inputStr("Masukkan kategori buku: ")
            stok_buku = inputInt("Stok buku: ")
            break
        except:
            continue

    insert_buku = """INSERT INTO BUKU(id_buku, nama_buku, kategori, stock)
                   VALUES (%s, %s, %s, %s)"""
    val_buku = (kode_buku, nama_buku, kat_buku, stok_buku)

    cursor.execute(insert_buku,val_buku)
    print("Query Berhasil dieksekusi")
    mycon.commit()
    print("Data berhasil ditambahkan")
    print("\n\n")