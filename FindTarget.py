from nltk.parse.stanford import StanfordDependencyParser
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

def FindTarget(story,storyobj):
	sentences = sent_tokenize(story)
	print(sentences)
	for s in sentences:
		s.replace('\n',' ').replace('\r','')
		result = [list(i.triples()) for i in dep_parser.raw_parse(s)]
		print(result)
