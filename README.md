# Python
Folder for Python based Projects I am running on my Raspberry Pi.

# My Reference Libraries and classes


## 1. [Python_Lib.py](https://github.com/Britnell/Python/blob/master/printer_lib.py)

Reminder file with examples to variable types and associated function.

- String
- Tuples
- Dictionaries
- reading and writing files
- Json


## 2. [Twitter_ref.py](https://github.com/Britnell/Python/blob/master/twitter_ref.py)

Contains
- setup funcitons for twitter
- Functions to search and load profiles
- functions sorting through the Json returned

## 3. [Printer Lib](https://github.com/Britnell/Python/blob/master/printer_lib.py)
This is just an implementation of
Py Thermal Printer : [luopio/py-thermal-printer](https://github.com/luopio/py-thermal-printer)
A python library for the thermal printer available with adafruit, and itself based on Adafruit's Printer library for Arduino : [Github/adafruit/Adafruit-Thermal-Printer-Library](https://github.com/adafruit/Adafruit-Thermal-Printer-Library)

It just takes care of creating an instance of py-thermal-printer and my own functions they way I like to use them in the Twitter example.

## 4. [Gmail_test](https://github.com/Britnell/Python/blob/master/gmail_test.py)
Again, just an implementation of accessing Gmail using
Charlieguo : github.com/charlierguo/gmail


#Projects

## Live Twitter feed - [Twitter Trump](https://github.com/Britnell/Python/blob/master/twitter_trump.py)
This is my first twitter app. It pulls a specified users timeline, checks it for new tweets, stores an up-to-date version of all tweets, and keeps track of unprinted tweets.
I use this to download Donald Drumpf's newest tweets and print them out on my recept printer.

Because Twitter API limits the requests you can make, important for debugging are functions for storing and saving search results, and user-timeline search.

1. Trumps timeline is downloaded
2. History in dict format is loaded from file
3. Timeline is checked for new tweets that are not in history, new tweets are uploaded
4. check if there are unprinted tweets in the History

a. function for marking all tweets as printed.
b. find & print the most recent tweets
c. print most recent X tweets
d. imports twitter and printer libraries for necessary functions

for demo program see functions.
