from nltk import wordpunct_tokenize, pos_tag #punkt (Punkt Tokenizer Models) ; averaged_perceptron_tagger (Tagger)
from nltk.stem.wordnet import WordNetLemmatizer #wordnet (WordNet)
from math import log
import re

class Category:

	numCategories = 0

	def __init__(self, category, tokens = []):
		self.category = category
		self.tokens = tokens
		self.freqToken = {}
		self.count = 1
		self.totalToken = 0

	def train(self):
		self.totalToken = len(self.tokens)
		for token in self.tokens:
			if token not in self.freqToken:
				self.freqToken[token] = 1
			else:
				self.freqToken[token] = self.freqToken[token] + 1

	def getTokenCount(self, token):
		if token not in self.freqToken:
			return 0
		else:
			return self.freqToken[token]

	def getTotalTokenCount(self):
		return self.totalToken
			
	def addTokens(self, newTokens):
		self.tokens.extend(newTokens)

	def getSelfCount(self):
		return self.count

	def incCount(self):
		self.count = self.count + 1

	def printTokens(self):
		print(self.tokens)

	def printDict(self):
		print(self.freqToken)

	def printCount(self):
		print(self.count)

def cleanTokens(tokens):
	toLook= ['CD']
	stemmer = WordNetLemmatizer()
	tags = pos_tag(tokens)
	i = 0
	while i < len(tokens):
		if tags[i][1] in toLook:
			if tags[i][1] == 'CD':
				tokens[i] = ' NUMBER '	
		tokens[i] = stemmer.lemmatize(tokens[i])
		i = i + 1
	return tokens

def cleanText(text):
	text.replace('US Navy', 'military')
	text.replace('US Army', 'military')
	text.replace('army', 'military')
	text.replace('U.S', 'UnitedStates')
	text.replace('U.N', 'UnitedNations')
	text.replace('US', 'UnitedStates')
	text.replace('UN', 'UnitedNations')
	text.replace('United States', 'UnitedStates')
	text.replace('United Nations', 'UnitedNations')
	text.replace('AIDS', 'disease')
	text.replace('HIV', 'disease')
	text.replace('Pentagon', 'military')
	text = re.sub(r'\$[0-9]+(\.[0-9][0-9]|\b)', ' MONEY ' , text)
	text = re.sub(r'(January|Jan\.|February|Feb\.|March|Mar\.|April|Apr\.|May|June|Jun\.|July|Jul\.|August|Aug\.|September|Sep\.|Sept\.|October|Oct\.|November|Nov\.|December|Dec\.) [0-9]([0-9]|\b)', ' DATE ', text)
	text = re.sub(r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)', ' DAY ', text)
	text = re.sub(r'[Tt]housand(s|\b)', ' BIGNUMBER ', text)
	text = re.sub(r'[Mm]illion(s|\b)', ' BIGNUMBER ', text)
	text = re.sub(r'[0-9]{4}', ' YEAR ', text)
	text = re.sub(r'\b.+%', ' PERCENTAGE ' , text)
	return text	

def labelInput(string):
	
	corpusName = input(string)

	try:
		f = open(corpusName, 'r')
	except:
		print ("Error: File not found. Exiting...")
		exit()

	filesList = []

	for line in f:
		filesList.append(line.split())

	f.close()
	
	return filesList

def tokenizeTextFromFile(fileLocation):
	try:
		f = open(fileLocation, 'r')
	except:
		print('{0} not found, pretending nothing happened...'.format(fileLocation))
		return None
	text = f.read()
	text = cleanTokens(wordpunct_tokenize(cleanText(text)))
	return text

filesList = labelInput('Enter name of training set: ')

categoryList = {}

for data in filesList:
	category = data[1]
	text = tokenizeTextFromFile(data[0])
	if text == None:
		continue
	if category not in categoryList:
		categoryList[category] = Category(category, text)
		Category.numCategories = Category.numCategories + 1
	else:
		categoryList[category].addTokens(text)
		categoryList[category].incCount()

for category, count in categoryList.items():
	count.train()

#end of training. Begin test....

def categorizeText(docTokens, categoryList):
	categoryProb = []
	for category, item in categoryList.items():
		PofC = log(item.getSelfCount() / item.numCategories)
		PofTgivenC = 0
		for token in docTokens:
			tempP = item.getTokenCount(token)
			if tempP == 0:
				tempP = 0.05
			PofTgivenC = PofTgivenC + log(tempP/item.getTotalTokenCount()) 
		categoryProb.append([category, PofC + PofTgivenC])
	categoryProb = sorted(categoryProb, key = lambda x: x[1])
	return categoryProb[len(categoryProb)-1][0]

outputName = input('Enter name of output file: ')

outputFile = open(outputName, 'w+')

filesList = labelInput('Enter name of test set: ')


for data in filesList:
	name = data[0]
	text = tokenizeTextFromFile(name)
	if text == None:
		print('Cannot open file....')
		continue
	category = categorizeText(text, categoryList)
	outputFile.write('{0} {1}\n'.format(name, category))

outputFile.close()

