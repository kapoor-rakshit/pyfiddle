# Reference    : https://pypi.python.org/pypi/wolframalpha
# installation : pip install wolframalpha

import wolframalpha

app_id = '----your api key----'         # get yours from     http://www.wolframalpha.com/

client = wolframalpha.Client(app_id)

res = client.query('cos(60) + sin(45)')

print(next(res.results).text)