# in this script we will write some very simple values to an sqlLite DB
import sqlite3
import locationCheck
import seleniumTest

conn = sqlite3.connect('ex.db')

lat = locationCheck.lat
lon = locationCheck.lon
ts = locationCheck.timestampString
timeToLoad = seleniumTest.elapsed_time
  
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO train1 (resultNum, timestamp, lat, lon) VALUES (?,?, ?, ?)''', (timeToLoad,ts, lat, lon))
conn.commit()
