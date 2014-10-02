import gps
import sqlite3

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

x = 0
while x<3:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                timeStamp = report.time
                x = x+1
            elif hasattr(report, 'lon'):
                lon = report.lon
                x = x+1
                print lon
            elif hasattr(report, 'lat'):
                lat = report.lat
                x = x+1 
                print lat

            
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
        
print lon
