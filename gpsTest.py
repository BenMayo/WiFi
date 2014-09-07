import gps
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
#         print report
 
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print report.time
        
        try: 
            report = session.next()
            if report['class'] == 'lat':
                if hasattr(report, 'lat'):
                    print report.lat
        
            try: 
                report = session.next()
                if report['class'] == 'lon':
                    if hasattr(report, 'lon'):
                        print report.lat
            finally:
                print 'I think something should go here'