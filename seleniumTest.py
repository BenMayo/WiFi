from selenium import webdriver
import time
import datetime
import sqlite3

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://www.bbc.co.uk"

mydriver = webdriver.Firefox()
start_time = time.time()
mydriver.get(baseurl)
end_time = time.time()
timestamp = datetime.datetime.utcnow()
elapsed_time = end_time - start_time
print("Elapsed time was %g seconds" % (end_time - start_time))
mydriver.quit()

conn = sqlite3.connect('ex.db')
   
cursor = conn.cursor()
cursor.execute('''
    INSERT INTO train1 (resultNum, timestamp) VALUES (?,?)''', (elapsed_time,timestamp))

conn.commit()