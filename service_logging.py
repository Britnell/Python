#	#	#	#	#	#
#	#
#	#		Python Ref with demo functions
#	#
#	#	#	#	#	#

#	#	#	#	#	# Time struct
import time

def format_date(datestring):
	#return date_into_tuple( tweet['date'] )
	return time.strptime(datestring, "%a %b %d %H:%M:%S +0000 %Y")

# takes struct and returns time string for logging
def time_stamp(time_struct):
	return time.strftime("%Y %m %d - %a %H:%M:%S", time_struct )

# takes string from log and returns time as sturct
def read_time_stamp(stamp):
	return time.strptime(stamp, "%Y %m %d - %a %H:%M:%S" )


#	#	#	#	#	#	#
# 	#	#	#	#	#	#		Files
#	#
#from service_logging import *
filepath = "data/service_log.txt"

def log_msg(log_type, text):
	LogFile = open(filepath, 'a')

	stamp = time_stamp( time.localtime() )
	LogFile.write("\n" +stamp +"::"+ log_type +"::" +text)

	LogFile.close()


def log_list():
	LogFile = open(filepath, 'r')

	lines = LogFile.readlines()
	lines.reverse()

	LogFile.close()
	return lines

twitter_tag = 'twitter_log'

def log_twitter(msg='twitter API query'):
	log_msg(twitter_tag, msg)

def last_tweet():
	log = log_list()

	for lines in log:
		line = lines.split("::")
		if len(line) >= 3:
			date = line[0]
			tipe = line[1]
			comment = line[2]

			if tipe == twitter_tag:
				# this was a tweet
				return read_time_stamp( date)

	# after complete loop - if no result :
	return None

def time_diff(now, then):
	# convert to datetime

# Eo File
