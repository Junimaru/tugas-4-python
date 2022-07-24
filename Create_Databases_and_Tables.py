#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Connect MySQL
import mysql.connector as consql
import sys
from datetime import datetime
from datetime import timedelta
mycon = consql.connect(
    host='localhost',
    user='root', 
    password='ganteng')
if mycon.is_connected():
    print('Berhasil Terhubung ke SQL')
else:
    print('Error saat menghubungkan ke SQL')

#membuat fungsi cursor
cursor = mycon.cursor()


# In[ ]:


#Membuat database lokal
cursor.execute("create database if not exists db_perpus")
print("database berhasil dibuat")
cursor.execute("USE db_perpus")
print("db_perpus berhasil digunakan")


# In[ ]:


# Membuat Tabel USER
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS USER")

# Create table as per requirement
tabel_user = """CREATE TABLE USER (
   id_user INT AUTO_INCREMENT PRIMARY KEY,
   u_name VARCHAR(20),
   tgl_lahir DATE,
   pekerjaan VARCHAR(20),
   alamat VARCHAR(50)
)
"""
cursor.execute(tabel_user)
print("Tabel USER Berhasil ditambahkan")


# In[ ]:


# Membuat Tabel BUKU
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS BUKU")

# Create table as per requirement
tabel_buku = """CREATE TABLE BUKU (
   id_buku VARCHAR(4) NOT NULL,
   nama_buku VARCHAR(20) NOT NULL,
   kategori VARCHAR(20),
   stock INT(1)
)
"""
cursor.execute(tabel_buku)
print("Tabel BUKU Berhasil ditambahkan")


# In[ ]:


# Membuat Tabel Pinjam
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS PINJAM")

# Create table as per requirement
tabel_pinjam = """CREATE TABLE PINJAM (
   id_user INT,
   id_buku INT,
   nama_user VARCHAR(30),
   nama_buku VARCHAR(30),
   tanggal_pinjam DATE,
   tanggal_pengembalian DATE
)
"""
cursor.execute(tabel_pinjam)
print("Tabel PINJAM Berhasil ditambahkan")



