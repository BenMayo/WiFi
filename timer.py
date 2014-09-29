# this script is a simple timer, set to run at 5s intervals
# this will run all of the time, and fire other processes at given intervals
import seleniumTest
import threading



import time
def executeSomething():
    while True:
#         execfile ("seleniumTest.py")
        print 'hello'
        time.sleep(10)

# while True:
#     executeSomething()
# def printit():
#     threading.Timer(120.0, printit).start()
# execfile ("seleniumTest.py")
# printit()