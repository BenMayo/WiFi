import gpsimport
import sqlite3

conn = sqlite3.connect('ex.db')
cursor = conn.cursor()


# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

x = 0

while x<1:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                cursor.execute("insert into train1 values '%s'" % report.time)
                print report.time
        session = None
        print "GPSD has terminated"
        x = x+1      
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"

x = 0
while x<1:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                print report.lon
                x = x+1      
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"

x = 0
while x<1:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat'):
                print report.lat
                x = x+1      
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"


