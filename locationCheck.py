# this script will check the current location and decide if a web test is required
# to start we will do this based just on location, but could also incorporate a time (peak/off peak) element

# the gps posistion and time comes from the gpsTest, so we import that here
import gpsTest
import WGS84toBNG

# assign lat lon and timestamp to the variables within gpsTest - this will save us having to reference it throughout the script
lat = gpsTest.lat
lon = gpsTest.lon
timestampString = gpsTest.timeStamp
timestampString = timestampString.replace(" ", "")
# the timestamp is currently a string in a bit of a strange format - let's break it down a bit into component parts, and then as a actual timestamp
time = timestampString[11:-5]
date = timestampString[:10]

# now get the locations in east and north (British National Grid - this will be much easier to work with)
east = WGS84toBNG.east
north = WGS84toBNG.north

# define peak and offpeak times

print lat
print lon
print time
print date
print east
print north



# define a bounding box
