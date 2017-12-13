#Reference :  http://freegeoip.net/
#          :  https://pypi.python.org/pypi/timezonefinder   Python library to look up timezone from lat / long offline
#          :  https://pypi.python.org/pypi/pytz             World timezone definitions

import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
import datetime

try:
	geolocator = Nominatim()

	place = input('Enter city name : ')

	loc = geolocator.geocode(place)

	tf = TimezoneFinder()
	timezone = tf.timezone_at(lat=loc.latitude,lng=loc.longitude)

	time = datetime.datetime.now(pytz.timezone(timezone))
	print("Location :",loc.address,str(time).split('.')[0])


# look for details of an IP address
	ipadr=""
	ipadr = input('Enter IP address for location : ')
	url = ('http://freegeoip.net/json/'+ipadr)                       # default is requesting system's IP address

	response = requests.get(url)
	response = response.json()

	for key,val in response.items():
		print(key,val)
except Exception as e:
	print(str(e))