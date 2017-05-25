import argparse
import os
import re


name = "WhatsApp.txt"
fole = open(name, 'r')

interest = ["love", "sorry", "x", "xx", "xxx"]

# Create empty dictionaries
kady = {}
tommy = {}
Dict = {}

rogex = re.compile('[^a-zA-Z]')		# RegEx for any word, characters only

fake = { 'tum':10, 'koosh':12 , 'pom':3}

Stats = {}
Stats["total"] = 0


s = raw_input("Let's begin? - please press enter")


# read first line, then iterate through lines in while loop
line = fole.readline()

while line:
	raw_input('?')
	print "Line: " +line

	L =line.split()

	# RegEx for date, DD/MM/YYYY
	m = re.match(r'.*\d+/\d+/\d+.*', line)
	#print m.re
	if m:
		date = L[0]	
		#m.group(0)
		print "Date: " +date

	# RegEd for time DD:DD:DD
	n = re.search(r'.*\d+:\d+:\d+.*', line)
	if n:
		time = L[1]	#m.group(0)
		print "Time: " +time

	if n and m:
		# If it contained date & time
		#	 : indentify Username
		
		#print "2: "+L[2]		# print next element
		#print type(L[2])

		i = L[2].find("Tommy")

		if i>=0:
			sender = 't'
			print "Sender: Tommy"

		i = L[2].find("Kady")
		if i>=0:
			sender = 'k'
			print "Sender: Kady"

		#print "3: "+L[3]		#print next element

		# In my example one username has spaces, creating an 
		# extra element before message, hence skip extra element 
		# for username : Tommy G
		#LEN = len(L)
		if sender == 'k':
			b = 3
		if sender == 't':
			b = 4

		# Iterate over remaining element of the Line
		for x in range(b,len(L) ):
			#print L[x]		# print word

			word = L[x].lower()		# make lower case

			#out = rogex.sub('', sling)
			formed = rogex.sub('', word)	# subtract non-letter chars
			
			if formed:
				Stats["total"] += 1
				if Dict.has_key(formed):
					Dict[formed]+=1
				else:
					Dict[formed]= 1
	else:
		# if it does NOT contain date & time : : 
		#
		for w in line:
			#print L[x]
			word = w.lower()

			#out = rogex.sub('', sling)
			formed = rogex.sub('', word)

			if formed:
				Stats["total"] += 1
				if Dict.has_key(formed):
					Dict[formed]+=1
				else:
					Dict[formed]= 1


		
	line = fole.readline()
	# LOOP REPEAT

#print Dict
print Stats["total"]

raw_input("Calculate Charts?")

# CHARTS

Charts = [ ('.', 0) ]
its = 1

for D in Dict:
	# what is occurence?
	# word
	V = Dict[D]
	tup = (D, V)

	#print tup
	# put in charts

	if V >= 10:
		i = 0
		its = len(Charts)
		while i < its :
			# if bigger than element at position x
			# put into position x
			#print Charts[i][0]	#word
			#print Charts[i][1]	# occurence
			if V > Charts[i][1]:
				Charts.insert(i, tup )
				#its += 1  # increase charts
				i = its		# to END loop
			i+=1
			# Eo while


print Charts

"""for c in Charts:
	#t = (Charts[c], c)
	print c
"""

# End