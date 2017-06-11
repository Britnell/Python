#	#	#	#	#	#
#	#
#	#		Python Ref with demo functions
#	#
#	#	#	#	#	#

#	#	#	#	#	# Time struct
import time, datetime

date_format_log = "%Y %m %d - %a %H:%M:%S"

# returns string format of date
# default : time - now
def time_stamp(stamp = datetime.datetime.now() ):
	return stamp.strftime(date_format_log)

# takes string from log and returns time as sturct
def read_time_stamp(stamp):
	return datetime.datetime.strptime(stamp,  date_format_log)


#	#	#	#	#	#	#
# 	#	#	#	#	#	#		Files
#	#

#from service_logging import *
filepath = "data/service_log.txt"

twitter_tag = 'twitter_log'

def log_msg(log_type, text):
	LogFile = open(filepath, 'a')

	stamp = time_stamp( )
	LogFile.write("\n" +stamp +"::"+ log_type +"::" +text)

	LogFile.close()


def log_list():
	LogFile = open(filepath, 'r')

	lines = LogFile.readlines()
	lines.reverse()

	LogFile.close()
	return lines


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
	t_diff = now-then
	return t_diff



# Eo File
