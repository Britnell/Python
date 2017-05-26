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
#	#
import python_lib as P

from twython import Twython

#APP_KEY = ''
#APP_SECRET = ''

import sys
sys.path.insert(0, '/home/tom/Coding/Dev_Private')

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

# END