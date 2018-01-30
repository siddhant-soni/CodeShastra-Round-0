import datetime
'''delta_votes=(upvote-dwnvote)

'''
now = datetime.datetime.now()
def sort_newest():
	if models.type=="article":
		return [i for i in models.sort(key= models.time) if i.type=="article"]
	else:
		return [i for i in models.sort(key= models.time) if i.type=="discussion"]

def sort_trending():

	last24= [i for i in models if (now-i.time).seconds<=(24*3600) and (now-i.time).days==0 ]
	return last24.sort(key=(now-last24.time).seconds()

def sort_top():
	return models.sort(key=models.delta_votes)

def sort_comment_new():
	return comment_models.sort(key=comment_models.time)
def sort_comment_top():
	return comment_models.sort(key=comment_models.delta_votes)
