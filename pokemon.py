# Reference : https://github.com/ab-anand/Automation-Bots/blob/master/pokeapi.py

import requests

pokenaam = input().lower()

url = "http://pokeapi.co/api/v2/pokemon/" + pokenaam

resp = requests.get(url)

if resp.ok:
	resp = resp.json()
	print(resp['name'][0].upper() + resp['name'][1:])
	print(resp['id'])
	print(str(resp['height']/10) + " m")
	print(str(resp['weight']/10) + " kg")

	img_url = resp['forms'][0]['url']
	response = requests.get(img_url)
	data = response.json()
	print(data['sprites']['front_default'])
else:
	print("Bad conection, try again later.")