# this script will check the current location and decide if a web test is required
# to start we will do this based just on location, but could also incorporate a time (peak/off peak) element

# the gps posistion and time comes from the gpsTest, so we import that here
import gpsTest

# assign lat lon and timestamp to the variables within gpsTest - this will save us having to reference it throughout the script
lat = gpsTest.lat
lon = gpsTest.lon
timestamp = gpsTest.timeStamp

print lat
print lon
print timestamp