#	#
#	#
#	#	#	#	#	#	#
#
#	#	#			Twython
#	
#	
#	#	#	Basic Usage - 
#	https://twython.readthedocs.io/en/latest/usage/basic_usage.html
#
#	#	#	Advanced Usage - 
#	https://twython.readthedocs.io/en/latest/usage/advanced_usage.html#advanced-usage
#
#	#		Twitter API
#
#	#	#	search
#	https://twython.readthedocs.io/en/latest/usage/advanced_usage.html#advanced-usage
#
#	#	#	user_timeline
#	https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#
#	#

import python_lib as P

from twython import Twython

import sys

sys.path.insert(0, '../Dev_Private')

from twitter_keys import APP_KEY, APP_SECRET

# Manual import of variables
#APP_KEY = twitter_keys.APP_KEY
#APP_SECRET = twitter_keys.APP_SECRET



twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


# 			Returns array of statuses
#
def twitter_search(keyword, count=20):
	search = twitter.search(q=keyword, result_type='recent', count=count)
	# , count=15, #default
	# ,	count=100, #max

	# Search json has:
	#	 - search['search_metadata']
	#    - search['statuses']	# array of tweets,
	
	num = len( search['statuses'] )		# default = 15

	return search['statuses']
	

#	Returns array of tweets from profile
def get_timeline(username, count=20):
	timeline = twitter.get_user_timeline(screen_name=username, count=count)		#
	#default, count=20

	return timeline


def get_timeline_trump():
	timeline = twitter.get_user_timeline(screen_name='realdonaldtrump')
	#default, count=20

	return timeline



#		Turns tweet json into Dict with relevant info
# 
def tweet_as_dict(tweet):
	Tweet = {}

	Tweet['id'] = tweet['id']
	Tweet['text'] = tweet['text']
	Tweet['date'] = tweet['created_at']
	Tweet['name'] = tweet['user']['name']
	Tweet['username'] = tweet['user']['screen_name']
	Tweet['link'] = tweet['source']
	Tweet['retweet'] = tweet['retweeted']

	Tweet['hashtags']=[]
	for H in tweet['entities']['hashtags']:
		Tweet['hashtags'].append( H['text'] )
	Tweet['no_hashtags'] = len( Tweet['hashtags'] )

	Tweet['mentions']=[]
	for M in tweet['entities']['user_mentions']:
		Tweet['mentions'].append( M['name'] )
	Tweet['no_mentions'] = len( Tweet['mentions'] )

	Tweet['media_URLs']=[]	
	if tweet['entities'].has_key('media'):
		for N in tweet['entities']['media']:
			Tweet['media_URLs'].append( N['media_url'] )

	Tweet['no_URLs'] = len( Tweet['media_URLs'] )

	Tweet['printed'] = 0

	return Tweet


def store_dict( dict, filename):
	P.write_json(filename,  dict)

def get_dict( filename):
	return P.read_json(filename)


def get_tweet(tweets):
	ID = next(iter(tweets) )
	return tweets[ID]


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


def format_tweet(tweet):
	text = tweet['text']

	# & sign
	#text = text.replace('&amp', '&')

	# remove link at the end of tweet
	html = text.find('http://')
	if html > 0:
		text = text[:html]

	htmls = text.find('https://')
	if htmls >0:
		text = text[:htmls]

	encoded = text.encode('utf-16')

	return encoded
#	'&amp' = &
#	remote http://... 

# END