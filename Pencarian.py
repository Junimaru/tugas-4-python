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

#FUNGSI PENCARIAN#
def cari_buku():
    """ Melakukan seleksi berdasarkan nama buku pada database BUKU """
    while True:
        try:
            buku_cari = inputStr("Masukkan nama buku: ")
            break
        except:
            continue
    import pandas as pd
    cari_buku = "SELECT * FROM buku WHERE nama_buku=%s"
    val = (buku_cari,)
    cursor.execute(cari_buku,val)
    results = cursor.fetchall()
    
    hasil = pd.DataFrame(results, columns = ['id_buku', 'nama_buku', 'kategori', 'stock'])
    print(hasil)
    print("\n\n")