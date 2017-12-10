# In spaces with curvature, straight lines are replaced by geodesics. 
# Geodesics on the sphere are circles on the sphere whose centers coincide with the center of the sphere,called great circles.
# distance measured along the surface of the sphere (as opposed to a straight line through the sphere's interior).

#Requirements ---  pip install geopy

from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from geopy.distance import great_circle

geolocator = Nominatim()

location1 = geolocator.geocode("lawrence road amritsar")
location2 = geolocator.geocode("pap jalandhar")
print(location1.address)

print(location1.latitude, location1.longitude)

print(location1.raw)

print()

coordinates_location = geolocator.reverse("52.05659, 89.6398")      # reverse() Method....Address from coordinates
print(coordinates_location.address)

print(coordinates_location.latitude,coordinates_location.longitude)

print(coordinates_location.raw)

                                                                   # Distance...Vincenty and Great Circle distance calculation
loc1coordinates=(location1.latitude,location1.longitude)
loc2coordinates=(location2.latitude,location2.longitude)

print(vincenty(loc2coordinates,loc1coordinates).kilometers)

print(great_circle(loc1coordinates,loc2coordinates).kilometers)