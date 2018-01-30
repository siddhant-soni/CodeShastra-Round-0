def search_articles(string):
	search_results=[]
	for i in Articles:
		if string in i.title:
			search_results.append(i)
	#search_results.sort(key=lambda x:x.title.split(' ').index(string))
	return search_results

def search_questions(string):
	search_results=[]
	for i in Questions:
		if string in i.question:
			search_results.append(i)
	#search_results.sort(key=lambda x:x.title.split(' ').index(string))
	return search_results
