#Powered by newsAPI       https://newsapi.org/

import requests
try:
	print("TIMES OF INDIA\n\n")
	url = ('https://newsapi.org/v2/'
		'everything?'                             #all news
		'sources=the-times-of-india'
		'q=modi'                                  #keyword search
		'from=2017-11-1'
		'to=2017-11-30'
		'language=en'
		'sortBy=popularity'
		'&apiKey=--------------your apiKey------------------')  
	response = requests.get(url)
	response = response.json()

	i=1

	for article in response['articles']:
		print(str(i)+". "+article['publishedAt']+"  "+article['title'])
		print(article['description'])
		print()
		i+=1



	print("\n\nNEW SCIENTIST    AND    TIMES OF INDIA\n\n")                          
	url = ('https://newsapi.org/v2/'
		'top-headlines?'                                                              #top headlines             
		'sources=new-scientist,the-times-of-india'                        #multiple sources comma separated                    
		'&apiKey=--------------your apiKey---------------------')
	response = requests.get(url)
	response = response.json()

	i=1

	for article in response['articles']:
		print(str(i)+". "+article['publishedAt']+"  "+article['title'])
		print(article['description'])
		print()
		i+=1

except Exception as e:
	print(str(e))