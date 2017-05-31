# This requires gmail library from Charlie Guo
# https://github.com/charlierguo/gmail
# git clone into same folder as this script

import sys

sys.path.insert(0,'gmail/gmail')		# folder with Gmail library
sys.path.insert(0,'../Dev_Private')		# Folder with private API keys

from gmail import Gmail
from gmail_keys import *

from printer_lib import *

mail = Gmail()

##Emails = mail_instance.authenticate(NAME, ACCESS_TOKEN)

mail.login(NAME, WORD)
# returns TRUE


def get_email(inbox, i=0):
	inbox[i].fetch()
	return inbox[i]


def get_unread(pre_fetch=False):
	inbox = mail.inbox().mail(unread=True, prefetch=pre_fetch)

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

def print_mail(email, limit=200):
	# subject is unistring
	subject = email.subject.encode('utf-16')
	# mail is... normal?
	mail = email.body[:limit]

	date = email.headers['Received']
	date = " ".join(date[2:6])
	
	#print subject,"\n",date,"\n",mail,
	#Nl()
	Text(subject, 'bc', 1)
	Text(date, 'fr', 1)

	Text(mail)

	Nl()
	Nl()


Headers = """
	Delivered-To
	From
	Return-Path
	ARC-Seal
	To
	Message-ID
	X-Received
	X-Google-DKIM-Signature
	ARC-Authentication-Results
	ARC-Message-Signature
	Date
	X-Notifications
	Received
	Received-SPF
	Authentication-Results
	X-Account-Notification-Type
	MIME-Version
	X-Gm-Message-State
	DKIM-Signature
	Content-Type
	Feedback-ID
	Subject
	"""
# Eo-File