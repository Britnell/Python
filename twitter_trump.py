#
#
#

import twitter_ref as T
import python_lib as P
from printer_lib import *


# load demo search result from file
#    twitter API limits to 15 actions per day...
#
def get_demo_timeline():

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
	#timeline = get_demo_timeline()
	timeline = get_timeline_trump()

	# New empty history
	History = {}

	# merge timeline into history
	History = merge_results(History, timeline)

	# set history as seen
	for ID in History:
		# mark all as printed, to save paper
		History[ID]['printed'] = 1

	return History



def store_history(Dict):
	P.write_json('data/twitter_history.txt', Dict)


def get_history():
	return P.read_json('data/twitter_history.txt')

def store_timeline(Dict):
	P.write_json('data/twitter_timeline.txt', Dict)

def read_timeline():
	return P.read_json('data/twitter_timeline.txt')


# History printer
def get_unprinted(History):
	unprinted = []

	for tweet in History:
		if History[tweet]['printed'] is 0:
			# Print tweet
			unprinted.append( History[tweet] )

	return unprinted


def print_unprinted(History):
	for tweet in get_unprinted(History):
		print_tweet( tweet )
		History[str(tweet['id'])]['printed'] = 1


def most_recent(Tweets):
	# get any date for loop
	twit = T.get_tweet(Tweets)
	recent = T.get_date(twit)
	recent_ID = twit['id']

	for ID in reversed(Tweets):
		date = T.get_date( Tweets[ID] )
		result = T.compare_dates(recent, date)

		if result is 'b':
			recent = date
			recent_ID = ID

	return Tweets[recent_ID]


def print_recent():
	Tweets = get_history()

	# get most recent tweet
	recent = most_recent(Tweets)

	# print it
	print_tweet( recent)


def update_timeline():
	# get current profiletime
	timeline = T.get_timeline_trump()
	#timeline = get_demo_timeline()
	store_timeline(timeline)

	# Read stored History from file
	history = get_history()

	# merge timeline into history
	updated = merge_results(history, timeline)

	print_unprinted( updated)

	# save new history to file
	store_history(updated)


def print_tweet(tweet):
	text = T.format_tweet( tweet )
	text = text[2:]

	user = '@' +tweet['username']

	date = tweet['date'].split()	# split date
	date = " ".join(date[:4])	# take first 4 elements

	Text(user, 'bc', 0)
	Text(date, 'fr')
	Text(text)

	Nl()
	Nl()


# End of File
