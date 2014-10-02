import gps
import sqlite3

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

x = 0
y = 0
z = 0
while x<1 and y <1 and z<1:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                timeStamp = report.time
                x = x+1
            elif hasattr(report, 'lon'):
                lon = report.lon
                y = y+1
            elif hasattr(report, 'lat'):
                lat = report.lat
                z = z+1 
            
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"

print lat
