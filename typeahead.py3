'''
program: Type Ahead
author: Chris Batty

This program reads in a file containing lines in the following format: 2,string
It then estimates the next word that will follow the string based on the n-gram probability.
For this program we use a hardcoded corpus that may be found towards the bottom of the file.
'''
def ngram(dictList, n, string):
	'''
	Calculates an ngram probabilty.
	wordCounts - dictionary containing all words found in our corpus.  Values are their total counts.
	dictList - a list containing our corpus
	n - the n value of our n-gram
	string - the string we are using to search for our n-gram.
	'''
	resultsList = []
	stringCount = 0

	# loop through and find all instances of our string, note the word that follows
	for ind,word in enumerate(dictList):
		tempStr = " ".join(dictList[ind:ind+n-1])
		if(string == tempStr):
			stringCount += 1
			found = False
			for entry in resultsList:
				if str(dictList[ind+n-1]) == entry[0]:
					entry[1] += 1
					found = True
			if found == False:
				resultsList.append([str(dictList[ind+n-1]), 1])
	for res in resultsList:
		res[1] = (res[1]/stringCount)
	return resultsList

def outputResp(resp):
	'''
	Formats and prints the output.
	'''
	total = 0
	for entry in resp:
		total+=entry[1]
	for i,out in enumerate(resp):
		if i+1 == len(resp):
			print(out[0]+ ",%.3f" % out[1])
		else:
			print(out[0]+ ",%.3f" % out[1], end=";")
	return

import sys

f = open(sys.argv[1], "r")
fileList = f.readlines()

dictionaryText = "Mary had a little lamb its fleece was white as snow; And everywhere that Mary went, the lamb was sure to go It followed her to school one day, which was against the rule; It made the children laugh and play, to see a lamb at school. And so the teacher turned it out, but still it lingered near, And waited patiently about till Mary did appear. \"Why does the lamb love Mary so?\" the eager children cry; \"Why, Mary loves the lamb, you know\" the teacher did reply."
dictionaryList = dictionaryText.replace("\"", "").replace(',', "").replace('?', "").replace("!", "").replace(".", "").replace(";", "").split(' ')

for line in fileList:
	command = line.replace('\n','').split(',')
	resp = ngram(dictionaryList, int(command[0]), command[1])
	# handle sorting
	resp.sort(key=lambda poss:poss[0], reverse=False) # secondary sort alphabetically
	resp.sort(key=lambda p:p[1], reverse=True) # primary sort by value
	outputResp(resp)
