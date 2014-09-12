import gps
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
                timeStamp = report.time
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
                lon = report.lon
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
                lat = report.lat
                x = x+1      
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"

# now we have all three variables outside of the GPS function - these print lines are commented out as we don't need them to always run.
# print timeStamp
# print lon
# print lat


# this sql commented out also - this was just testing (it works)
# cursor.execute("""INSERT INTO train1 ('timestamp', 'lat', 'lon') VALUES (?, ?, ?)""", (timeStamp, lon, lat))
# conn.commit()
# conn.close()


