"""
ToddHash.py

A program that generates a fake git log titled 'revisions.txt'
Inspired and designed after Todd Wellman's signature hashing method in his faked revisions.txt
"""

import sys
import random

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
				print(methodName)
				methodNames.append(methodName)			

	return methodNames

def toddHash():
	lettersAndNumbers = "0123456789abcdefghijklmnopqrstuvwxyz"
	hashString = ""
	for i in range(0, 40):
		hashString += random.choice(lettersAndNumbers)
	return hashString

def generateHash(methodName)s:

def main():
	methodNames = readFile(sys.argv[1])
	for method in methodNames:
		print(method)
	hashString = toddHash()
	print(hashString)


main()