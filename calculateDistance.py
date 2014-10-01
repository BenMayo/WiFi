from math import *
lat1 = 50.171
lon1 = 3.52
lat2 = 51.0
lon2 = 4.0

R = 6371
x = (lon2 - lon1) * cos( 0.5*(lat2+lat1) )
y = lat2 - lat1
d = R * sqrt( x*x + y*y )

print d


