import json, sys, ast, pandas as pd
author_hits = []
question_hits = []
ans_hits = []
comm_hits = []
tag_hits = []
matches = []

def match(type):
	if type == "Q":
		for i in question_hits:
			for j in author_hits:
				if i == j:
					matches.append(i)
	if type == "A":
		for i in ans_hits:
			for j in author_hits:
				if i ==j:
					matches.append(i)					
	if type == "C":
		for i in comm_hits:
			for j in author_hits:
				if i == j:
					matches.append(i)
	if type == "T":
		for i in tag_hits:
			for j in author_hits:
				if i==j:
					matches.append(i)
					


def findauthor(word, author):

	for i in range(0, len(index[word]['authors'])):
		if author == index[word]['authors'][i]:
			author_hits.append(i)

def findquest(word):
	
	for i in range(0, len(index[word]['types'])):
		if "question" == index[word]['types'][i]:
			question_hits.append(i)
			
def findans(word):
	
	for i in range(0, len(index[word]['types'])):
		if "answer" == index[word]['types'][i]:
			ans_hits.append(i)	

def findcomm(word):
			
	for i in range(0, len(index[word]['types'])):
		if "comment" == index[word]['types'][i]:
			comm_hits.append(i)			

def findtag(word):

	for i in range(0, len(index[word]['types'])):
		if "tag" == index[word]['types'][i]:
			tag_hits.append(i)	
	
with open('index2.txt', 'rb') as fp:
	#index = json.load(fp)
	
	index = ast.literal_eval((fp.read()))
	
	quit = False;
	
	while quit == False:
		word = raw_input("Enter the word you would like to search\t")
		type = raw_input("Search among Questions(Q), Answers(A), Comments(C), Tags(T), All(E)\t")
		author = raw_input("If you would like to search words from a particular author provide they're author ID, otherwise hit ENTER\t")
		
		print word, type, author
		print "\n"
		
		
		if author != '' and type == "E":
			try:
				index[word]
				findauthor(word, author)
				author_hits[0]
				print "word, node id, type, author id"
				for i in author_hits:
					print word, index[word]['nodes'][i], index[word]['types'][i], index[word]['authors'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "The author id {0} was not found!".format(author)
		
		elif author != '' and type == "Q":
			try:
				index[word]
				findauthor(word, author)
				findquest(word)
				author_hits[0]
				match(type)
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "The author id {0} was not found!".format(author)
			try:
				matches[0]
				print "word, node id, author id, type"
				for i in matches:
					#print i
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except IndexError:
				print "There appears to be no questions for the given author {0} containing the word {1}".format(author, word)

		elif author == '' and type == "Q":
			try:
				index[word]
				findquest(word)
				question_hits[0]
				print "word, node id, author id, type"
				for i in question_hits:
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				author_hits = []
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "questions containing the word {0} were not found!".format(word)				

		elif author != '' and type == "A":
			try:
				index[word]
				findauthor(word, author)
				findans(word)
				author_hits[0]
				match(type)
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "The author id {0} was not found!".format(author)
			try:
				matches[0]
				print "word, node id, author id, type"
				for i in matches:
					#print i
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except IndexError:
				print "There appears to be no answers for the given author {0} containing the word {1}".format(author, word)
							

		elif author == '' and type == "A":
			try:
				index[word]
				findans(word)
				ans_hits[0]
				print "word, node id, author id, type"
				for i in ans_hits:
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "answers containing the word {0} were not found!".format(word)			
				


		elif author != '' and type == "C":
			try:
				index[word]
				findauthor(word, author)
				findcomm(word)
				author_hits[0]
				match(type)
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "The author id {0} was not found!".format(author)
			try:
				matches[0]
				print "word, node id, author id, type"
				for i in matches:
					#print i
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except IndexError:
				print "There appears to be no comments for the given author {0} containing the word {1}".format(author, word)
				

		elif author == '' and type == "C":
			try:
				index[word]
				findcomm(word)
				comm_hits[0]
				print "word, node id, author id, type"
				for i in comm_hits:
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "comments containing the word {0} were not found!".format(word)						
				
				
		elif author != '' and type == "T":
			try:
				index[word]
				findauthor(word, author)
				findtag(word)
				author_hits[0]
				match(type)
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "The author id {0} was not found!".format(author)
			try:
				matches[0]
				print "word, node id, author id, type"
				for i in matches:
					#print i
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except IndexError:
				print "There appears to be no tags for the given author {0} containing the word {1}".format(author, word)
				

		elif author == '' and type == "T":
			try:
				index[word]
				findtag(word)
				tag_hits[0]
				print "word, node id, author id, type"
				for i in tag_hits:
					print word, index[word]['nodes'][i], index[word]['authors'][i], index[word]['types'][i]
				matches = []
				author_hits = []
				question_hits = []
				ans_hits = []
				comm_hits = []
				tag_hits = []
			except KeyError:
				print "The word {0} was not found!".format(word)
			except IndexError:
				print "tags containing the word {0} were not found!".format(word)	
		
		
		elif author == '' and type == "E":
			try:
				print str(word), index[word]
			except KeyError:
				print "The word {0} was not found!".format(word)
				
		else:
			print "You incorrectly chose options... Please try again"
		
		ans = raw_input("Continue (Y/N)")
		if ans == "Y":
			continue
		else:
			quit = True;
		foundauthor = []
		

	
