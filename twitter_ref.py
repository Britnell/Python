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


APP_KEY = '3GO6n8qVObX2CgntaqIsL3uX2'
APP_SECRET = 'LFm5QX3is2v8rsAD6WxexlsgRdVDrqaS8VIpDPE6Y3a9MlAKox'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# 			Returns array of statuses
#
def search_statuses(keyword, count=20):
	search = twitter.search(q=keyword, result_type='recent', count=count)
	# , count=15, #default
	# ,	count=100, #max

	# Search json has:
	#	 - search['search_metadata']
	#    - search['statuses']	# array of tweets,
	
	num = len( search['statuses'] )		# default = 15

	return search['statuses']
	

#	Returns array of tweets from profile
def timeline(username, count=20):
	timeline = twitter.get_user_timeline(screen_name=username, count=count)		#
	#default, count=20

	return timeline


def ex_timeline():
	timeline = twitter.get_user_timeline(screen_name='realdonaldtrump')
	#default, count=20

	return timeline


#			Extract info variables from tweet
#
def format_tweet(tweet):
	lens = len(tweet)

	ID = tweet['id']
	text = tweet['text']
	date = tweet['created_at']
	name = tweet['user']['name']
	username = tweet['user']['screen_name']
	link = tweet['source']
	retweet = tweet['retweeted']

	hashtags=[]
	for H in tweet['entities']['hashtags']:
		hashtags.append( H['text'] )
	
	mentions=[]
	for M in tweet['entities']['user_mentions']:
		mentions.append( M['name'] )

	media_URLs=[]
	for N in tweet['entities']['media']:
		media_URLs.append( N['media_url'] )



#			scan searches
#
def search_info(search ):

	text = search['statuses'][0]['text']

	user = search['statuses'][0]['user']['name']

	username = search['statuses'][0]['user']['screen_name']

	link = search['statuses'][0]['source']



# END