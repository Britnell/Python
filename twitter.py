import twitter_ref as T
import python_lib as P


# load demo search result from file
#
def get_timeline():
	import twitter_ref as T
	import python_lib as P

	timeline = P.read_json('trump.txt')

	return timeline


# Input : History, new timeline
# Output : Update History with new tweets from timeline
def merge_results(Dict, tweets):
	History = Dict

	for tweet in tweets:
		obj = T.get_tweet(tweet)		#get obj

		id = str(obj.ID)			#get ID

		if not History.has_key( id ):		# If not in history
			
			History[id] = (obj, 0)		# put into dict

			# boolean is for printing

	return History


def initialise_twitter():
	# get current profiletime
	timeline = get_timeline()

	# New empty history
	History = {}

	# merge timeline into history
	History = merge_results(History, timeline)
	
	# set history as seen
	for id in History:
		#tweet_obj = History[id][0]
		#printed = History[id][1]
		History[id][1] = 1

	return History

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