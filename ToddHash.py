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
				methodName2 = ""
				for char in methodName:
					if ( char == "(" ):
						break
					else:
						methodName2 += char
				methodNames.append(methodName2)			

	return methodNames
"""
Generates random string of characters.
Used in the commit creating function
@param - None
@return 40 char string of a faked hash 
"""
def toddHash():
	lettersAndNumbers = "0123456789abcdefghijklmnopqrstuvwxyz"
	hashString = ""
	for i in range(0, 40):
		hashString += random.choice(lettersAndNumbers)
	return hashString

"""
Translates date from dd/mm/yy Format into
Day Mon ## format
@param date: string in dd/mm/yy format
@returns string of date in translated form.
"""
def translateDate(date):
	dateArray = date.split("/")
	month = int(dateArray[0])

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

	if (day == 0):
		day = "Mon"
	if (day == 1):
		day = "Tue"
	if (day == 2):
		day = "Wed"
	if (day == 3):
		day = "Thu"
	if (day == 4):
		day = "Fri"
	if (day == 5):
		day = "Sat"
	if (day == 6):
		day = "Sun"

	return str(day) + " " + month + " " + dateArray[1]

"""
Commmit format:
commit (toddHash())
Author (Author)
Date(given dates)
Commit Message (i.e. initial commit)

This function prints out the commits.
Prints it out in stack format (initial commit at bottom, final commit on top).

@param - methodNames: List of strings that represent Method Names from given file.
@param - authorName: Takes in author of file
@param - email: takes in email to be forged to git log
@param - currentCommit - takes in value of current commit
@param - finalCommit: takes in value of the final commit (total nubmer of commits supplied)
returns nothing
"""
def generateHash(methodNames, authorName, email, date, currentCommit, finalCommit):
	if(currentCommit == finalCommit):
		print("Commit " + toddHash())
		print("Author: " + authorName + " <" + email + ">")
		print(translateDate(date)) #NOT DONE
		print(" ") #newLine
		print("Initial Commit")
		print(" ") #newLine
		return

	if(currentCommit == 0):
		print("Commit " + toddHash())
		print("Author: " + authorName + " <" + email + ">")
		print(translateDate(date)) #NOT DONE
		print(" ") #newLine
		print("Final Commit")
		print(" ") #newLine
		return

	print("Commit " + toddHash())
	print("Author: " + authorName + " <" + email + ">")
	print(translateDate(date)) #NOT DONE
	print(" ") #newLine
	print("Modified " + random.choice(methodNames)) #should be varying message
	print(" ") #newLine
	return


"""
Main function that runs program.
Takes in user arguments, and prints a usage case if there are no command line arguments.
Runs readFile which returns a list of method names.
Runs for loop in range of desired commits that
@param - none except program arguments
@return - none, but prints faked hashs to stdout
"""
def main():
	#IF USER INPUT IS TAKEN, STDOUT CANNOT BE PIPED TO W)HATEVER.txt
	#USER INPUT SHOULD NOT BE TAKEN COMMAND LINE ARGUMENTS SHOULD BE USED.

	#functionality statement
	if(len(sys.argv) == 1 or sys.argv[1] == "-h"):
		print("The Todd Hash Prints a faked git revisions log to stdout")
		print("Run via Command Line Arguments. Example:")
		print("python3 toddHash.py 'filename' 'your name' 'email' 'startdate' 'enddate' 'numberOfCommits'")
		return

	#Get User Input
	filename = sys.argv[1]
	name = sys.argv[2] + " " + sys.argv[3]
	email = sys.argv[4]
	startdate = sys.argv[5]
	enddate = sys.argv[6]
	numberOfCommits = sys.argv[7]
	#get List of method names from given file.
	methodNames = readFile(filename)

	


	
	#print(hashString)

	for i in range(0, int(numberOfCommits)):
			generateHash(methodNames, name, email, startdate, i, int(numberOfCommits) - 1)



main()