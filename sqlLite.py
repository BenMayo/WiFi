# in this script we will write some very simple values to an sqlLite DB

import sqlite3

conn = sqlite3.connect('ex.db')
   
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE train1(id INTEGER PRIMARY KEY, lat FLOAT,
                       lon FLOAT, timestamp TIMESTAMP, resultText TEXT, resultNum FLOAT)
''')
conn.commit()