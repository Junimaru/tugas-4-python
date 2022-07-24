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


#SHOW DATA PINJAM
def show_pinjam():
    """Menampilkan data pada database PINJAM"""
    import pandas as pd
    show_pinjam = "SELECT * FROM pinjam;"
    cursor.execute(show_pinjam)
    results = cursor.fetchall()

    hasil = pd.DataFrame(results, columns = ['id_user', 'id_buku', 'nama_user', 'nama_buku', 'tgl_pinjam', 'tgl_pengembalian'])
    print(hasil)
    print("\n\n")