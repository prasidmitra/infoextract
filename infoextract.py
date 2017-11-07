import sys
import re
from Template import Template
#import spacy
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/Users/prasidmitra/Downloads/stanford/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/prasidmitra/Downloads/stanford/stanford-ner-2017-06-09/stanford-ner.jar',encoding='utf-8')

ps = PorterStemmer()



# nlp = spacy.load('en')
 


stories=[]
story_objects=[]

def findIncident(story,obj):
	incidents = ['arson','attack','bombing','kidnapping','robbery']
	incidents_synonyms = []
	for i in range(len(incidents)):
		incidents_synonyms.append(findSynonym(incidents[i]))
	story_words = word_tokenize(story)
	for 

def findSynonym(word):
	synonyms = []
	antonyms = []

	for syn in wn.synsets(word):
	    for l in syn.lemmas():
	        synonyms.append(l.name())
	        if l.antonyms():
	            antonyms.append(l.antonyms()[0].name())
	return synonyms            

def extractInfo(textfile):
	f = open(textfile,'r')
	text = ""
	for line in f:
		p = re.match('^((DEV-MUC3|TST1-MUC3|TST2-MUC4)-[0-9]{4})',line)
		if p:
			if len(text)!=0:
				stories.append(text)
				text=""
			obj = Template(p.group(),'','','','','','')
			story_objects.append(obj)

		else: 
			text += line
	if len(text)!=0:
		stories.append(text)

	for i in range(len(stories)):
		findIncident(stories[i],story_objects[i])


	#   Stanford NER Tagger
	#print(st.tag(word_tokenize(stories[0])))	


	# for i in range(len(stories)):
	# 	print(story_objects[i].id+'\n----------')
	# 	print(ne_chunk(pos_tag(word_tokenize(stories[i]))))	

	# doc = nlp(stories[0])
	# for i in doc.ents:
	#     print(i.label_, i.text)
	# for i in doc:
	# 	print(i.text, i.ent_iob,i.ent_type_)   

		



def main():
	#args=sys.argv
	#textfile = './developset/texts/DEV-MUC3-0006'
	textfile = './developset/texts/sample.txt'

	extractInfo(textfile)

if __name__ == '__main__':
	main()