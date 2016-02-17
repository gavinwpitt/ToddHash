"""
ToddHash.py

A program that generates a fake git log titled 'revisions.txt'
Inspired and designed after Todd Wellman's signature hashing method in his faked revisions.txt
"""

import sys
import random
from datetime import datetime
from calendar import weekday

###GLOBAL VARIABLE FOR CURRENT DAY
today = datetime.now()
"""
readFile(fileName)

reads in a file and returns all the methods of that file.
Currently only handles .py files.
@param: fileName - file to be read by function
return-A list of method methodNames
"""
def readFile(fileName):
	methodNames = []
	for line in open(fileName):
		nextWord = False
		words = line.strip().split()
		for i in range(0,len(words)-1):
			if(words[i] == "def"):
				methodName = words[i+1].strip(':')
				methodNames.append(methodName)			

	return methodNames

def toddHash():
	lettersAndNumbers = "0123456789abcdefghijklmnopqrstuvwxyz"
	hashString = ""
	for i in range(0, 40):
		hashString += random.choice(lettersAndNumbers)
	return hashString

def translateDate(date):
	dateArray = date.split("/")
	month = dateArray[0]
	if(month == 1):
		month = "Jan"
	if(month == 2):
		month = "Feb"
	if(month == 3):
		month = "Mar"
	if(month == 4):
		month = "Apr"
	if(month == 5):
		month = "May"
	if(month == 6):
		month = "Jun"
	if(month == 7):
		month = "Jul"
	if(month == 8):
		month = "Aug"
	if(month == 9):
		month = "Sep"
	if(month == 10):
		month = "Oct"
	if(month == 11):
		month = "Nov"
	if(month == 12):
		month = "Dec"

	day = weekday(int(dateArray[2]), int(dateArray[0]), int(dateArray[1]))

	return str(day) + month + dateArray[1]

"""
Hash format:
commit (toddHash())
Author (Author)
Date(system time?)
Commit Message (i.e. initial commit)

"""
def generateHash(methodNames, authorName, email, date, currentCommit, finalCommit):
	if(currentCommit == 0):
		print("Commit " + toddHash())
		print("Author: " + authorName + " <" + email + ">")
		print("Date: " + date + " 5:00:00 " + str(today.year)) #NOT DONE
		print(" ") #newLine
		print("Initial Commit")
		print(" ") #newLine
		return

	if(currentCommit == finalCommit):
		print("Commit " + toddHash())
		print("Author: " + authorName + " <" + email + ">")
		print("Date: " + date + " 5:00:00 " + str(today.year)) #NOT DONE
		print(" ") #newLine
		print("Final Commit")
		print(" ") #newLine
		return

	print("Commit " + toddHash())
	print("Author: " + authorName + " <" + email + ">")
	print("Date: " + date + " 5:00:00 " + str(today.year)) #NOT DONE
	print(" ") #newLine
	print("Modified " + random.choice(methodNames)) #should be varying message
	print(" ") #newLine
	return



def main():
	#IF USER INPUT IS TAKEN, STDOUT CANNOT BE PIPED TO WHATEVER.txt
	#USER INPUT SHOULD NOT BE TAKEN COMMAND LINE ARGUMENTS SHOULD BE USED.

	#Get User Input
	filename = input("Enter the file name (example.py): ")
	name = input("Name to sign commit log: ")
	email = input("Email for commit log: ")
	startdate = input("Start Date for commit log (MM/DD/YY): ")
	enddate = input("End Date (MM/DD/YY): ")
	numberOfCommits = input("Number of Commits: ")

	#translate User Input
	methodNames = readFile(filename)
	startdate = translateDate(startdate)
	endDateTime = translateDate(enddate)

	
	#print(hashString)

	for i in range(0, int(numberOfCommits)):
		if(i == 0):
			generateHash(methodNames, name, email, startdate, i, numberOfCommits)
		elif(i == numberOfCommits):
			generateHash(methodNames, name, email, enddate, i, numberOfCommits)
		else:
			generateHash(methodNames, name, email, "Thu Feb 11", i, numberOfCommits)



main()