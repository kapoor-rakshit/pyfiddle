# Reference    : https://wikipedia.readthedocs.io/en/latest/code.html#api
# installation : pip install wikipedia

import wikipedia

try:
	wsearch = wikipedia.search("wipro", results=10, suggestion=True)   # WIKIPEDIA serach, tuple with 10 results and suggestion
	wres = wsearch[0]           # query results as a list
	for i in wres:
		print(i)
	print()
	wsug = wsearch[1]           # suggestions
	if not wsug==None:
		for j in wsug:
			print(j)
	else:
		print("NO suggestions available")

	wsuggest = wikipedia.suggest("wipro")  # suggested Wikipedia title for a query, or None

	try:
		wsum = wikipedia.summary("wipro", sentences=10, auto_suggest=True, redirect=True) # Plain text summary of the page.
		print(wsum)                                                           # auto_suggest and redirect are enabled by default
	except wikipedia.exceptions.DisambiguationError as e :                   # max sentences can be no greater than 10 (default)
		print(e.options)
	except wikipedia.exceptions.PageError:
		print("Page not found. Try again with different query.")

	try:
		wpg = wikipedia.page("virat kohli")                           # Wiki page with title = "title" or the pageid = numpageid
		print(wpg.content)
		print(wpg.categories)
		print(wpg.images)
		print(wpg.links)
		print(wpg.references)
		print(wpg.sections)
		print(wpg.summary)                                           
	except wikipedia.exceptions.DisambiguationError as e:
		print(e.options)
	except wikipedia.exceptions.PageError:
		print("Page not found. Try again with different query.")


	print(wikipedia.languages())        # List all the currently supported language prefixes (usually ISO language code).

	# wikipedia.set_lang(prefix)        # set language, but query must be made in the same lang
	
                                        # requests rate limits
	# wikipedia.set_rate_limiting(rate_limit, min_wait=datetime.timedelta(0, 0, 50000))  

except Exception as e:
	print(str(e))