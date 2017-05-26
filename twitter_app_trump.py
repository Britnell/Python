import twitter_ref as T
import python_lib as P


# load demo search result from file
#    twitter API limits to 15 actions per day...
#
def get_demo_timeline():
	import twitter_ref as T
	import python_lib as P

	timeline = P.read_json('twitter_trump.txt')

	return timeline


# Input : current History dict;		 new timeline
# Returns : Updated History dict with new tweets from timeline
# 
def merge_results(History, TimeLine):
	# timeL = array of tweet.json's

	for json in TimeLine:
		tweet = T.tweet_as_dict(json)	# turn json into dict

		ID = str(tweet['id'])			#get ID

		if not History.has_key( ID ):		# If not in history
			# when adding new tweet, automatically printed = 0
			History[ID] = tweet		# put into dict

	return History  	# return appended History


def get_first_twitter():
	# get current profiletime
	timeline = get_demo_timeline()
	#timeline = get_timeline_trump()

	# New empty history
	History = {}

	# merge timeline into history
	History = merge_results(History, timeline)
	
	# set history as seen
	for ID in History:
		# mark as printed
		History[ID]['printed'] = 1

	return History



def store_history(dict):
	P.write_json('twitter_history.txt', dict)

def get_history():
	return P.read_json('twitter_history.txt')


def store_dict( dict, filename):
	P.write_json(filename,  dict)

def get_dict( filename):
	return P.read_json(filename)


# History printer
def unprinted_tweet(History):
	unprinted = []

	for tweet in History:
		if History[tweet]['printed'] is 0:
			# Print tweet
			unprinted.append( History[tweet] )
	
	return unprinted


def date_into_tuple(datestring):
	#date = ( dd, mm, yyyy, hh, mm )

	date = datestring.split()

	Months = {
	'Jan': 1,	'Feb': 2,
	'Mar': 3,	'Apr': 4,
	'May': 5,	'Jun': 6,
	'Jul': 7,	'Aug': 8,
	'Sep': 9,	'Oct': 10,
	'Nov': 11,	'Dec': 12
	}

	month = date[1]
	day = date[2]
	year = date[5]

	time = date[3].split(':')

	hour = time[0]
	minute = time[1]

	day = int(day)
	year = int(year)
	hour = int(hour)
	minute = int(minute)

	month = Months[month]

	# return tuple
	return ( day, month, year, hour, minute )




# End of File