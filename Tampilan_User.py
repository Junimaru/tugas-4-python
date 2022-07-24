# In[ ]:
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

#SHOW DATA USER
def show_user():
    """Menampilkan data pada database USER"""
    import pandas as pd
    show_user = "SELECT * FROM user"
    cursor.execute(show_user)
    results = cursor.fetchall()
    
    hasil = pd.DataFrame(results, columns = ['id_user','u_name', 'tgl_lahir', 'pekerjaan', 'alamat'])
    print(hasil)
    print("\n\n")
