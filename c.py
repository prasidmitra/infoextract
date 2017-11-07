from nltk.corpus import wordnet as wordnet
from nltk.stem import WordNetLemmatizer

synonyms = []
antonyms = []
wnl = WordNetLemmatizer()

for syn in wordnet.synsets("arson"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(list(set(synonyms)))