#	#	#	#	#	#
#	#
#	#		Python Ref with demo functions
#	#
#	#	#	#	#	#	

#	#	#	#	#	#	#		Imports
#	#
#import

import json
import pprint

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
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(docum)


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
# 	#	#	#	#	#	#		
#	#
#	#r

def array_of_tuples():
	ray = [ ('a', 0, 'b', 'd'), (1992, 1993 ), ('green', 'blue', 'red') ]
	print " # Array of tuples : \n", ray

	print "ray[0] : ", ray[0]
	print "ray[1] : ", ray[1]
	print "ray[2] : ", ray[2]




#	#	#	#	#	#	#
# 	#	#	#	#	#	#		Dict
#	#
#	#
def dicts():
	
	Book = {}

	print "type: ", type(Book)
	print "length:  ", len(Book)

	Book["Chapters"] = 1
	Book['entry'] = 4512
	Book['year'] = 1990
	Book['initials'] = 'TB'

	print Book


	if Book.has_key('Chapter'):
		Book['Chapters'] += 1

	print "Added to 'Chapters' = ", Book['Chapters']

	fake = { 'tum':10, 'koosh':12 , 'pom':3}
	print fake


	for index in Book:
		print "index = ", index, ",  entry = ", Book[index]

		tuppel = (index, Book[index] )
		print "tuppel = ", tuppel



#	#	#	#	#	

#	#	#	#	#	Tuples
#	#
#	#

def tuples():

	a = (1,2,3,4,5,6,7,8)
	b = ( 'a', 'B', 39, 'd', 1/2 )

	empty = ()
	one = (1, )

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
#	#
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

	# 12



