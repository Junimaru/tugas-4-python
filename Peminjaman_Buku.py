import mysql.connector as consql
from datetime import datetime
from datetime import timedelta
from Def_Input import inputStr, inputInt, upd_buku

#Membuat Koneksi ke SQL
mycon = consql.connect(
        host='localhost',
        user='root', 
        password='ganteng')

#membuat cursor
cursor = mycon.cursor()

#menyambungkan ke db_perpus    
cursor.execute("USE db_perpus")

#INSERT DATA PINJAM
def add_pinjam():
    """ Memasukkan data peminjam kemudian data tersebut diinput ke database PINJAM"""
    while True:
        try:
            id_pinj = inputInt("Masukkan id peminjam: ")
            buku_pinj = inputInt("Masukkan id buku: ")
            user_pinj = inputStr("Masukkan Nama Peminjam: ")
            nama_pinj = inputStr("Masukkan Nama Buku: ")
            tgl_pinj = datetime.today()
            tgl_kembali = tgl_pinj + timedelta(days = 7) #Asumsi maksimal 7 hari setelah peminjaman
            break
        except:
            continue

    insert_pinj = """INSERT INTO PINJAM(id_user, id_buku, nama_user, nama_buku, tanggal_pinjam, tanggal_pengembalian)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
    val_pinj = (id_pinj, buku_pinj, user_pinj, nama_pinj, tgl_pinj, tgl_kembali)

    cursor.execute(insert_pinj,val_pinj)
    print("Query Berhasil dieksekusi")
    mycon.commit()
    print("Data berhasil ditambahkan")
    print("\n\n")
    upd_buku(buku_pinj,-1)