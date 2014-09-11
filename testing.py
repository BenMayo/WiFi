# this is just a place to hack about with any code - anything in this file is liable to be deleted

import sqlite3

conn = sqlite3.connect('ex.db')
cursor = conn.cursor()

report.time = '00:00:00 01/12/200'

cursor.execute("insert into train1 values '%s'" % report.time)

