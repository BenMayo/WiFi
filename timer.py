# this script is a simple timer, set to run at 5s intervals
# this will run all of the time, and fire other processes at given intervals
import seleniumTest

import threading

def printit():
  threading.Timer(20.0, printit).start()
execfile ("seleniumTest.py")
printit()