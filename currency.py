# Reference : https://github.com/ab-anand/Automation-Bots/blob/master/exchange_rates.py

import bs4 as bs
import urllib.request
import datetime

date = datetime.datetime.now().date()

currencycode = input("Enter currency-code : ").upper()

url = "http://www.xe.com/currencytables/?from=" + currencycode + '&date=' + str(date)

sitedata = urllib.request.urlopen(url).read()

soup = bs.BeautifulSoup(sitedata, 'html.parser')

#print(soup.prettify())

table = soup.find('tbody')
header = soup.find_all('th')

#print(table.prettify())
#print(header)

vals = []

vals.append(header[0].text.strip() + " | " + header[1].text.strip() + " | " + header[2].text.strip() + " | " + header[3].text.strip())

rows = table.find_all('tr')
for row in rows:
	cols = row.find_all('td')
	vals.append(cols[0].a.text + " | " + cols[1].text + " | " + cols[2].text + " | " + cols[3].text)

print(*vals,sep="\n")