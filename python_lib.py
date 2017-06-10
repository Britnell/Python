#	#	#	#	#	#
#	#
#	#		Python Ref with demo functions
#	#
#	#	#	#	#	#



#	#	#	#	#
#
#	#	#	#	#		Regular Expressions
import re

def regexs():
	RE_word = re.compile(r'[^a-zA-Z]')
	RE_date = r'.*\d+/\d+/\d+.*'
	RE_time = r'.*\d+:\d+:\d+.*'
	match = re.match(RE_date, line)


#	#	#	#	#
#
#	#	#	#	#		system.path
import sys, os

def paths(path):
	sys.path.insert(0, path)
	#sys.path.append(path)
	#then import module_name

	# prints current dir / path of terminal
	print os.path.abspath('./')

	# list files / folder in current directory
	print os.listdir(".")

	# list /path/path/
	print os.listdir("/home/tom")


#	#	#	#	#	#	#		Json
#	#
# http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

import json
import pprint as PrettyP

PPP = PrettyP.PrettyPrinter(indent=4)

def write_json(filename, jason):
	with open(filename, 'w') as outfile:
		json.dump(jason, outfile)


def append_json(filename, jason):
	with open(filename, 'a') as outfile:
		json.dump(jason, outfile)


def read_json(filename ):
	with open(filename) as json_file:
		data = json.load(json_file)
		return data


def pprint(docum):
	PPP.pprint(docum)


#	#	#	#	#	#	#
# 	#	#	#	#	#	#		Files
#	#
#	#
def write_file():
	filename = "filetest.txt"
	file = open(filename, 'w')
	file.write("Hello world. ")
	file.write("Now we're talkin'\n")
	file.write("a=128\n")
	file.write("(1,2,3,4,5,6,7)\n#tag")
	file.close()

def read_file():
	filename = "filetest.txt"
	file = open(filename, 'r')

	#file.read(5)		gets 5 characters
	word = file.read(5)
	print " # first 5 chars : ", word

	#file.read()	gets full content
	entire = file.read()
	print " # entire : ", entire

	file.seek(0)	#rewind to beginning

	#file.readline()	reads one line until line break
	#file.readlines()		reads all lines and returns them as list
	lines = file.readlines()
	print " # loop through list of lines : "
	# > you can for loop throug list
	for l in lines:
		print l

	file.seek(0)	#rewind to beginning

	#  You can for loop through file, it assumes as readlines() list
	print " # loop through file : "
	for line in file:
		print line



#	#	#	#	#	#	#
# 	#	#	#	#	#	#		Dict
#	#
#	#
def dicts():

	Book = {}

	print "type: ", type(Book)
	print "length:  ", len(Book)

	Book = {
		'a': 1,
		'b': 2,
	}

	Book["Chapters"] = 1
	Book['entry'] = 4512
	Book['year'] = 1990
	Book['initials'] = 'TB'

	print "~Print dict: ", Book
	print "~PRetty print: "
	pprint(Book)

	print "~keys() : ", Book.keys()



	if Book.has_key('Chapter'):
		Book['Chapters'] += 1

	print "~Added to 'Chapters' = ", Book['Chapters']

	print "~Loop through"
	for index in Book:
		print index, ":  ", Book[index]

		tuppel = (index, Book[index] )
		print "~tuppel : ", tuppel


	# get RANDOM first element:
	iterate = iter(Book)
	print next(iterate)

	list_of_keys = Book.list()

	return Book


#	#	#	#	#

#	#	#	#	#			Lists

#	#

#	#
def lists():
	list1 = ['bits', 'bobs', 1,	2,	3]

	#slicing
	print list1[0]
	print list1[2:4]

	# list_of_tuples
	ray = [ ('a', 0, 'b', 'd'), (1992, 1993 ), ('green', 'blue', 'red') ]
	print " # List of tuples : \n", ray

	print "ray[0] : ", ray[0]
	print "ray[1] : ", ray[1]
	print "ray[2] : ", ray[2]



#	#	#	#	#

#	#	#	#	#			Tuples
#	#
#	#
#	https://www.tutorialspoint.com/python/python_tuples.htm
#	TUPLES 		CANT	 BE 	CHANGED
#
def tuples():

	a = (1,2,3,4,5,6,7,8)
	b = ( 'a', 'B', 39, 'd', 1/2 )

	empty = ()
	one = (1, )

	## ! !!!!!!!!!!!!!!!!!!!!
	# print a[1] works
	# BUUUUUUUUT
	# a[1] = X
	# DOES NOT WORK
	#
	print "type: ", type(a), ", ", type(empty)
	print "len: ", len(a),",  ", len(empty)


	print "(1,2,3) + (4,5,6) = ", (1,2,3) + (4,5,6)
	# (1,2,3...6)

	print "3 in (1,2,3) : ", 3 in (1,2,3)
	# True

	print "~for x in b:"
	for x in b:
		print x,","
		#a, B, 39, d, 0,5

#	#	#	#	#	#	#
#	#	#	#	#	#	#	Strings
#	#
#	https://www.tutorialspoint.com/python/python_strings.htm
def strings():

	a = "There once was one"
	b = 'DD'

	print a
	print "length: ", len(a)
	print "indexing [0] =  ",a[0]
	print "Slicing, [1:5] =   ",a[1:5]

	c = a.join(b)
	print "add by .join()  = ", c
	c = a+b
	print "add by +  = ", c

	c = str( 125 )
	print "Convert int : ", c


	print "boolean : ", 'i' in "teamwork"

	print "Find in a = ", a
	print "a.find('on') = ", a.find("on")

	print "a.find('on', 10) = ", a.find("on", 10)

	print "a.find('me') = ", a.find("me")
	#returns index or -1

	print "a.rfind('on')", a.rfind('on')

	print "Split: ", a.split()

	# Unicode


	#st = 'pnts'
	#print type(st), st

	#uni = u'pnts'
	#print type(uni), uni

	# string = encoded uni
	#st.encode('latin_1')

	# uni = decoded strong
	#uni.decode('latin_1')
