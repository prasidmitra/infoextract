from nltk.corpus import wordnet as wordnet
from nltk.stem import WordNetLemmatizer

synonyms = []
antonyms = []
wnl = WordNetLemmatizer()

for syn in wordnet.synsets("kidnaps"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

for i in synonyms:
	print(wnl.lemmatize(i),i)