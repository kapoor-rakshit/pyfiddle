# Reference : http://thesaurus.altervista.org/

import requests

word = input("Enter word : ")
print()
url = "http://thesaurus.altervista.org/thesaurus/v1?word=" + word + "&language=en_US&key=test_only&output=json"

resp = requests.get(url)
resp = resp.json()

for i in resp['response']:
	print(i['list']['synonyms'])
	print()