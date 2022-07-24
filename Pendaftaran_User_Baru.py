#!/usr/bin/env python
# coding: utf-8

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

#INSERT DATA USER
def add_user():
    """ Memasukkan data user kemudian data tersebut diinput ke database USER"""
    while True: 
        try: 
            nama_user = inputStr("Masukkan nama user: ")
            tgl_lhr = inputStr("Masukkan tanggal lahir (YYYY-MM-DD): ")
            kerja = inputStr("Pekerjaan: ")
            almt = inputStr("Alamat: ")
            break
        except:
            continue
        
    insert_user = """INSERT INTO USER(u_name, tgl_lahir, pekerjaan, alamat)
                    VALUES (%s, %s, %s, %s)"""
    val_user = (nama_user, tgl_lhr, kerja, almt)

    cursor.execute(insert_user,val_user)
    print("Query Berhasil dieksekusi")
    mycon.commit()
    print("Data berhasil ditambahkan")
    print("\n\n")

