#!/usr/bin/env python

# This requires gmail library from Charlie Guo
# https://github.com/charlierguo/gmail
# git clone into same folder as this script

# *
# *
# *
#	* * * * * * * * * * * *      		 	Logging
import logging
import logging.handlers
import argparse
import sys

# Defaults
LOG_FILENAME = "/tmp/printer_service.log"
LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG" or "WARNING"

# Define and parse command line arguments
parser = argparse.ArgumentParser(description="My first Python service")
parser.add_argument("-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

# If the log file is specified on the command line then override the default
args = parser.parse_args()
if args.log:
        LOG_FILENAME = args.log

# Configure logging to log to a file, making a new file at midnight and keeping the last 3 day's data
# Give the logger a unique name (good practice)
logger = logging.getLogger(__name__)
# Set the log level to LOG_LEVEL
logger.setLevel(LOG_LEVEL)
# Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
# Format each log message like this
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
# Attach the formatter to the handler
handler.setFormatter(formatter)
# Attach the handler to the logger
logger.addHandler(handler)

# Make a class we can use to capture stdout and sterr in the log
class MyLogger(object):
        def __init__(self, logger, level):
                """Needs a logger and a logger level."""
                self.logger = logger
                self.level = level

        def write(self, message):
                # Only log if there is a message (not just a new line)
                if message.rstrip() != "":
                        self.logger.log(self.level, message.rstrip())

# Replace stdout with logging to file at INFO level
sys.stdout = MyLogger(logger, logging.INFO)
# Replace stderr with logging to file at ERROR level
sys.stderr = MyLogger(logger, logging.ERROR)

# *
# *
# *
# * * * * * * * * * * * * * * * * * *            Paths

# File, Project and relative paths
import os
try:
	SELF_PATH = os.path.dirname(os.path.abspath(__file__))
except NameError:
	SELF_PATH = os.path.abspath('.')

def parent_dir(Path, it=1):
	for x in range(it):
		Path = Path[:Path.rfind('/')]
	return Path

PROJ_PATH = parent_dir(SELF_PATH)
logger.info("python path "+SELF_PATH +"python dir: "+PROJ_PATH)

# Add paths to sys.path for import
import sys
sys.path.insert(0,PROJ_PATH +'/gmail/gmail')		# folder with Gmail library
sys.path.insert(0,parent_dir(PROJ_PATH) +'/Dev_Private')		# Folder with private API keys

#   * * *       Imports
#
#

import twitter_trump as Trump
import gmail_test as email
import service_logging as Log

#   * * *       Lets beginning
#   *
#   *
import datetime, time
twitter_interval = 20

def twitter_service():

	#check elapsed time
	time_now = datetime.datetime.now()

	last_check = Log.last_tweet()

	elapsed = time_now - last_check
	minutes = elapsed.seconds / 60

	# could do something for first check of the day

	# if more than 30 mins past
	if minutes >= twitter_interval:
		# update history
		Trump.update_timeline()

		# log twitter search
		Log.log_twitter()

		# print new tweet if there is one
		Trump.update_print_newest()


#   * * *       Lets beginning
#   *
#   *
Looping = True
mins5 = 60 * 5

while Looping:
    # every 5 mimnutes wake up and check:

    #check email for unprinted
    # & print
    
    twitter_service()

    time.sleep(mins5)       # sleep 5 mins



    #


# End of File
