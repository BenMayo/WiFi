# this script is a simple timer, set to run at 5s intervals

import threading

def printit():
  threading.Timer(5.0, printit).start()
  print "do something here"

printit()