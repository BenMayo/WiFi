# in this script we will write some very simple values to an sqlLite DB
import sqlite3
import locationCheck

conn = sqlite3.connect('ex.db')

print locationCheck.lat



   
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE train1(id INTEGER PRIMARY KEY, lat FLOAT,
                       lon FLOAT, timestamp TIMESTAMP, resultText TEXT, resultNum FLOAT)          
                       
''')
conn.commit()