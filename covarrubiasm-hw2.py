#Covarrubias, Michael 09-14-2018   
#Homework 2
#I worked on this alone :(


from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Create a geolocator object to access geo data using Nominatum
geolocator = Nominatim()

# A query address
#query = '1314 chavez st, las vegas, nm'
query = input("Enter First location, I guess? ")
query2 = input("Enter Second locatioin, bruh? ")

# Build/retrieve a geopy Location object with a query address
location = geolocator.geocode(query)
location2 = geolocator.geocode(query2)

# Access the latitude and longitude from location object
first =(location.latitude, location.longitude)
print(first)
second =(location2.latitude, location2.longitude)
print(second)

# Get the geodesic distance using the lat and long coordinates above
distance = geodesic(first,second).miles

#print results i guess
print("Distance between %s and %s is %f miles" % (location, location2, distance))
