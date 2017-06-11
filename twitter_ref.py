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

import sys, time

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
	timeline = twitter.get_user_timeline(screen_name='realdonaldtrump', result_type='recent')
	#default, count=20

	return timeline

def print_timeline(timeline, tag):
	for tx in timeline:
		tweet = tweet_as_dict(tx)
		print tweet[tag]

def print_history(history,tag):
	for ID in history:
		print history[ID][tag]

	#print dates of history

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


date_format_tweet = "%a %b %d %H:%M:%S +0000 %Y"

#returns python.time struct
def get_date(tweet):
	#return date_into_tuple( tweet['date'] )
	as_string = tweet['date']
	return datetime.datetime.strptime(as_string,  date_format_tweet)
	#previously used python.time but can not compute time difference
	#return time.strptime(as_string, "%a %b %d %H:%M:%S +0000 %Y")

def format_datetime(datestring):
	return datetime.datetime.strptime(datestring,  date_format_tweet)
	#return time.strptime(datestring, "%a %b %d %H:%M:%S +0000 %Y")

# takes time str from tweet and returns time.time-struct
def format_time(datestring):
	return time.strptime(datestring, date_format_tweet)


def greater_smaller_equal(a, b):
	if a > b:
		return 'a'
	elif a < b:
		return 'b'
	else:
		return '='


def compare_dates(tweet1, tweet2):

	# get each date string
	date1= tweet1['date']
	date2= tweet2['date']

	# turn string into time.time struct
	date1 = format_time(date1)
	date2 = format_time(date2)

	#loop = len(dateA)
	winner = ''

	for d in range( 9 ):
		ratio = greater_smaller_equal( date1[d], date2[d] )
		if not ratio is '=':
			# there is a winner
			winner = ratio
			break

	# now winner A or B
	if winner is 'a':
		return tweet1
	elif winner is 'b':
		return tweet2
	else:
		return tweet1


def format_text(text):
	#	'&amp' = &
	#	remote http://...

	text = text.replace('&amp', '&')		# & sign

	# remove link at the end of tweet
	html = text.find('http://')
	if html > 0:
		text = text[:html]

	htmls = text.find('https://')
	if htmls >0:
		text = text[:htmls]

	encoded = text.encode('utf-16')

	return encoded


# END
