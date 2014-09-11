# in this script we will write some very simple values to an sqlLite DB

import sqlite3

conn = sqlite3.connect('ex.db')
print "Opened database successfully";



# 



# db = sqlite3.connect('/home/pi/Desktop/Wifi/ex')
# 
# cursor = db.cursor()
# cursor.execute('''
#     CREATE TABLE train1(id INTEGER PRIMARY KEY, lat FLOAT,
#                        lon FLOAT, timestamp TIMESTAMP, resultText TEXT, resultNum FLOAT)
# ''')
# db.commit()