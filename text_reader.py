import argparse
import os
import re

# Just some OS functions to test
print os.listdir(".")
print os.listdir("/home/tom")

#filename & open
name = "WhatsApp.txt"
fole = open(name, 'r')

# Create empty dictionaries
kady = {}
tommy = {}
Dict = {}

#regex for word
rogex = re.compile('[^a-zA-Z]')

s = raw_input("Lets begin? -- Please press enter")

#read first line
line = fole.readline()

Stats = {}
Stats["total"] = 0

while line:
	
	print "Line: " +line

	L =line.split()

	# Regex for Date : DD/MM/YYY    , 23.12.2017
	m = re.match(r'.*\d+/\d+/\d+.*', line)
	
	if m:
		# if Date found, store date
		date = L[0]	#m.group(0)
		print "Date: " +date

	n = re.search(r'.*\d+:\d+:\d+.*', line)
	if n:
		time = L[1]	#m.group(0)
		print "Time: " +time

	if n and m:
		#print "2: "+L[2]

		#print type(L[2])
		i = L[2].find("Tommy")

		if i>=0:
			sender = 't'
			print "Sender: Tommy"

		i = L[2].find("Kady")
		if i>=0:
			sender = 'k'
			print "Sender: Kady"

		#print "3: "+L[3]

		#LEN = len(L)
		if sender == 'k':
			b = 3
		if sender == 't':
			b = 4

		for x in range(b,len(L) ):
			#print L[x]
			word = L[x].lower()

			#out = rogex.sub('', sling)
			formed = rogex.sub('', word)

			if formed:
				Stats["total"] += 1
				if Dict.has_key(formed):
					Dict[formed]+=1
				else:
					Dict[formed]= 1
	else:
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

print Dict
print Stats["total"]

raw_input("Calculate Charts?")

# CHARTS

fake = { 'tum':10, 'koosh':12 , 'pom':3}
Charts = [ ('.', 0) ]
its = 1

for D in Dict:
	# what is occurence?
	# word
	V = Dict[D]
	tup = (D, V)

	print tup
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

# End