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

import printer_lib as Printer

# Instanciate
mail = Gmail()				##Emails = mail_instance.authenticate(NAME, ACCESS_TOKEN)

# & log in
mail.login(NAME, WORD)		# returns TRUE
print "Logged into Gmail as ", NAME		#logger.info("import gmail as "+NAME )

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

def print_oldest_unread():
	# get unread
	unr = get_unread()
	if unr:
		# print oldest
		print_email(unr[0])

def print_most_recent():	# not done
	# get unread
	inb = get_inbox()
	# print oldest
	print_email(inb[0])


def format_decode(ustring):
	return ustring.encode('latin_1')

def format_email(text):
	text = text.replace('&amp', '&')		# & sign
	#
	# remove link addresses
	html = text.find('<http')
	while html > 0:
		htmlEnd = text.find('>', html)
		text = text[:html] + text[htmlEnd+1:]
		html = text.find('<http')
	#
	# remove img placeholders
	img = text.find('[image:')
	while img > 0:
		imgEnd = text.find(']', img)
		text = text[:img] + text[imgEnd+1:]
		img = text.find('[image:')
	#encoded = text.encode('utf-16')
	return text

def print_email(Email):
	Email.fetch()
	subj = format_decode(Email.subject)
	messg = format_email(Email.body)
	date = Email.headers['Received'].split()
	date = " ".join(date[6:-2])
	sender = Email.headers['From'].split()
	sender = sender[1][1:-1]
	Email.read()
	#
	#print sender
	#print date
	#print subj
	#print messg
	#
	Printer.Text(sender, 'ic', 1)
	Printer.Text(date, 'fr', 1)
	Printer.Text(subj, 'bl', 1)
	Printer.Text(messg, 'nl', 0)
	#
	Printer.Nl()
	Printer.Nl()
	#

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


def inbox_loop(Yloop=True):

    snooze = 5
    inbox = get_inbox()

    mark_all_unread(inbox)

    #print "unread"

    while Yloop:
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
