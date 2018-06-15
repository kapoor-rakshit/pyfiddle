# Reference : https://textgears.com/api/

import requests

text = input()
text = text.replace(' ','+')
url = "https://api.textgears.com/check.php?text=" + text + "&key=DEMO_KEY"
resp = requests.get(url)
resp = resp.json()

if resp['result']:
	for err in resp['errors']:
		print("Error at position : ",err['offset']+1)
		print("Error : ",err['bad'])
		print("Possible corrections are : ")
		for corr in err['better']:
			print(corr)
		print()
else:
	print(resp['description'])