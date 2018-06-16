# Reference : https://earthquake.usgs.gov/

import requests
import datetime

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

resp = requests.get(url)

resp = resp.json()

def info(data):
	cont=1
	for i in data:
		print(cont,"----------------------------------")
		cont+=1
		print(i['properties']['title'])
		print("Magnitude : ",i['properties']['mag'])
		print('Location : ', i['properties']['place'])
		print("Type : ",i['properties']['type'])
		ms = i['properties']['time']
		print(datetime.datetime.fromtimestamp(ms/1000.0))
		print()


if resp['metadata']['count']==0:
	print("No warnings detected")
else:
	print(resp['metadata']['count'])
	info(resp['features'])