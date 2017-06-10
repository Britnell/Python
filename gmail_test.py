#
#
#

# This requires gmail library from Charlie Guo
# https://github.com/charlierguo/gmail
# git clone into same folder as this script


import sys
path=''
sys.path.insert(0,path+'gmail/gmail')		# folder with Gmail library
sys.path.insert(0,path+'../Dev_Private')		# Folder with private API keys

# Import modules
import time
from gmail import Gmail
from gmail_keys import *

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

# End of File
