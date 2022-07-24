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

#SHOW DATA BUKU
def show_buku():
    """Menampilkan data pada database BUKU"""
    import pandas as pd
    show_buku = "SELECT * FROM buku"
    cursor.execute(show_buku)
    results = cursor.fetchall()

    hasil = pd.DataFrame(results, columns = ['id_buku', 'nama_buku', 'kategori', 'stock'])
    print(hasil)
    print("\n\n")