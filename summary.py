import sqlite3
import os.path

con = sqlite3.connect('database.db')
cur = con.cursor()
print('SQLite version:')
print(sqlite3.version)
print('Success!')


#1) A total number of musicians and a list of musicians.
t = cur.execute("SELECT count(*) FROM musician")
t = cur.fetchall()
print(t)
t = cur.execute(" SELECT name from musician")
t = cur.fetchall()
for r in t: print(r)

#2) A total number of albums and a list of albums recorded at Notown.
t = cur.execute("SELECT count(*) FROM album")
t = cur.fetchall()
print(t)
t = cur.execute(" SELECT name from album")
t = cur.fetchall()
for r in t: print(r)
#3) A total number of instruments and a list of instruments at Notown.
t = cur.execute("SELECT count(*) FROM instrument")
t = cur.fetchall()
print(t)
t = cur.execute(" SELECT DISTINCT type from instrument")
t = cur.fetchall()
for r in t: print(r)
#4) A table consists of the name of musicians and the total number of albums written by them.
t = cur.execute(" SELECT M.name, COUNT(*) AS count FROM musician M, musician_album MA, album A WHERE MA.album_id = A.id AND M.ssn = MA.ssn GROUP BY M.ssn")
t = cur.fetchall()
for r in t: print(r)
