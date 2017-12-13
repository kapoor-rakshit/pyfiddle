#Requires FullContact API Key         http://docs.fullcontact.com/

import requests

usermail = input('Enter email-id to be searched : ')

url = ('https://api.fullcontact.com/v2/person.json?email='+usermail+'&apiKey=-----YOUR API KEY------')
response = requests.get(url)
response = response.json()

if response['status']==200:
	if 'contactInfo' in response.keys():
		print("\nName : "+response['contactInfo']['fullName'])

	if 'demographics' in response.keys() and\
	'locationDeduced' in response['demographics'].keys() and\
	'deducedLocation' in response['demographics']['locationDeduced'].keys():
		print("Location : "+response['demographics']['locationDeduced']['deducedLocation'])

	if 'organizations' in response.keys():
		for place in response['organizations']:
			print(place['name'])
			if 'title' in place.keys():
				print(place['title'])
			if 'startDate' in place.keys():
				print(place['startDate'])
			if 'current' in place.keys():
				if place['current']==True:
					print("Currently working here")
			print()

	if 'chats' in response['contactInfo'].keys():
		for contact in response['contactInfo']['chats']:
			print(contact['client'],contact['handle'])
			print()

	if 'websites' in response['contactInfo'].keys():
		for websites in response['contactInfo']['websites']:
			print(websites['url'])
			print()

	if 'socialProfiles' in response.keys():
		for socprof in response['socialProfiles']:
			print(socprof['typeName'])
			print(socprof['url'])
			print()
else:
	print("Data unavailable right now")