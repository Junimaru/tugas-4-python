import mysql.connector as consql
from datetime import datetime
from datetime import timedelta


#Membuat Koneksi ke SQL
mycon = consql.connect(
        host='localhost',
        user='root', 
        password='ganteng')

#membuat cursor
cursor = mycon.cursor()

#menyambungkan ke db_perpus    
cursor.execute("USE db_perpus")


##Definisi INPUTAN

def inputInt(text):
    """membuat inputan harus integer."""
    while True:
        try:
            what = int(input(text))
            return what                # only ever returns a number
        except ValueError:
            print('Oops!  input yang anda masukkan tidak sesuai')

def inputStr(text):
    """membuat inputan harus String."""
    while True:
        try:
            what = str(input(text))
            return what                # only ever returns a str
        except ValueError:
            print('Oops!  input yang anda masukkan tidak sesuai')

            
def upd_buku(buku_pinj,u):
    """membuat fungsi update stock buku apabila buku dipinjam/dikembalikan"""
    ttl_stock = "SELECT stock FROM buku WHERE id_buku=%s;"
    data = (buku_pinj,)
    cursor.execute(ttl_stock,data)
    results = cursor.fetchone()
    hasil = results[0]+u
    upd_stock = "UPDATE buku SET stock=%s where id_buku=%s;"
    cursor.execute(upd_stock,(hasil,buku_pinj))
    mycon.commit()
    print("Update berhasil dieksekusi")
    
    
def hps_peminjam(buku_kemb,id_kemb):
    """membuat fungsi delete user dari list peminjaman setelah buku dikembalikan"""
    hapus = "DELETE FROM pinjam WHERE id_buku=%s AND id_user=%s;"
    val = (buku_kemb,id_kemb)
    cursor.execute(hapus,val)
    mycon.commit()
    print("Daftar Peminjam berhasil dihapus")