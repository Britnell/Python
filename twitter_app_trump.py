import twitter_ref as T
import python_lib as P


# load demo search result from file
#    twitter API limits to 15 actions per day...
#
def get_demo_timeline():
	import twitter_ref as T
	import python_lib as P

	timeline = P.read_json('data/twitter_trump.txt')

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
	P.write_json('data/twitter_history.txt', dict)

def get_history():
	return P.read_json('data/twitter_history.txt')


def store_dict( dict, filename):
	P.write_json(filename,  dict)

def get_dict( filename):
	return P.read_json(filename)


def get_any_tweet(tweets):
	ID = next(iter(tweets) )
	return tweets[ID]


# History printer
def get_unprinted(History):
	unprinted = []

	for tweet in History:
		if History[tweet]['printed'] is 0:
			# Print tweet
			unprinted.append( History[tweet] )
	
	return unprinted

def print_unprinted(History):
	for un in get_unprinted(History):
		un['printed'] = 1
		# print_tweet un['text']

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


def get_date(tweet):
	return date_into_tuple( tweet['date'] )


def greater_smaller_equal(a, b):
	if a > b:
		return 'a'
	elif a < b:
		return 'b'
	else:
		return '='

def compare_dates(A, B):
	#date = ( dd, mm, yyyy, hh, mm )
	#         0   1   2     3   4
	winner = ''

	year = greater_smaller_equal( A[2], B[2] )

	if year is '=':
		month = greater_smaller_equal( A[1], B[1] )
		if month is '=':
			day = greater_smaller_equal( A[0], B[0] )
			if day is '=':
				hour = greater_smaller_equal( A[3], B[3] )
				if hour is '=':
					minu = greater_smaller_equal( A[4], B[4] )
					winner = minu
				else:
					winner = hour
			else:
				winner = day
		else:
			winner = month
	else:
		winner = year

	return winner


def most_recent(Tweets):
	# get any date for loop
	twit = get_any_tweet(Tweets) 
	recent = get_date(twit)
	recent_ID = twit['id']

	for ID in Tweets:
		date = get_date( Tweets[ID] )
		result = compare_dates(recent, date)
		
		if result is 'b':
			recent = date
			recent_ID = ID

	return Tweets[recent_ID]

def update_timeline():
	# get current profiletime
	timeline = get_timeline_trump()			#timeline = get_demo_timeline()

	# Read stored History from file
	history = get_history()

	# merge timeline into history
	updated = merge_results(gistory, timeline)

	print_unprinted( update)

	# save new history to file
	store_history(updated)


def format_tweet(tweet):
	text = tweet['text']

	text = text.replace('&amp', '&')

	html = text.find('http://')
	if html > 0:
		text = text[:html]
		
	htmls = text.find('https://')
	if htmls >0:
		text = text[:htmls]

	return text
#	'&amp' = &
#	remote http://... 


# End of File