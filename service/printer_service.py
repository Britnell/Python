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
import time  # this is only being used as part of the example

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

import time
from gmail import Gmail
from gmail_keys import *
import twitter_trump as trump
import gmail_test as email

#   * * *       Lets beginning
#   *
#   *

# Instanciate
mail = Gmail()				##Emails = mail_instance.authenticate(NAME, ACCESS_TOKEN)

# & log in
mail.login(NAME, WORD)		# returns TRUE
logger.info("import gmail as "+NAME )

def mark_all_unread(inbox):
	for msg in inbox:
		msg.fetch()
		msg.unread()

def mark_all_read(inbox):
	for msg in inbox:
		msg.fetch()
		msg.read()

def get_email(inbox, i=0):
	inbox[i].fetch()
	return inbox[i]

def get_unread(pre_fetch=False):
	inbox = mail.inbox().mail(unread=True, prefetch=pre_fetch)
	return inbox

def get_inbox():
	inbox = mail.inbox().mail()
	# = array of message instances
	# email = inbox[0], etc..
	return inbox

def inbox_demo():
	inbox = mail.inbox()
	# = mailbox.Mailbox instance

	inbox = mail.inbox().mail()
	# = array of message instances

	email = inbox[0]
	# = message.Message instance

	inbox[0].fetch()
	# Returns email.message.Message instance  (?)

	# now
	email = inbox[0]

	print email.subject			# subject
	print email.body			# mail body
	print email.headers			# info's
	print email.headers['Received']		# date

	email.unread()			# to mark unread
	#email.archive()		# archive

snooze = 5
inbox = get_inbox()
logger.info("got inbox")
mark_all_unread(inbox)
logger.info("all unread")
#print "unread"

while True:
	for msg in inbox:
		msg.fetch()
		msg.read()
		#print '.'
		time.sleep(snooze)

	for msg in inbox:
		#msg.fetch()
		msg.unread()
		#print '.'
		time.sleep(snooze)

# End of File
