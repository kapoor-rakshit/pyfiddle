#In publishing and graphic design, placeholder text is commonly used to demonstrate the elements 
#of a document or visual presentation, such as font, typography, and layout.

#Reference : https://loripsum.net/

"""
(integer) - The number of paragraphs to generate.
short, medium, long, verylong - The average length of a paragraph.
decorate - Add bold, italic and marked text.
link - Add links.
ul - Add unordered lists.
ol - Add numbered lists.
dl - Add description lists.
bq - Add blockquotes.
code - Add code samples.
headers - Add headers.
allcaps - Use ALL CAPS.
prude - Prude version.
plaintext - Return plain text, no HTML."""

import requests

url = ('https://loripsum.net/api/10/short/decorate/plaintext')

response = requests.get(url)
response = response.text

print(response)