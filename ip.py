#Reference : http://freegeoip.net/

import requests

try:
	# look for details of an IP address or hostname

	ipadr=""
	ipadr = input('Enter IP address or hostname : ')
	url = ('http://freegeoip.net/json/'+ipadr)                       # default is requesting system's IP address

	response = requests.get(url)
	response = response.json()

	for key,val in response.items():
		print(key,val)

except Exception as e:
	print(str(e))