from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer


import spacy
nlp = spacy.load('en')
ps = PorterStemmer()

seedwords = ['attack','attacked','bomb','bombed','grenade','destroyed','destroy']

def FindOrg(story,storyobj):
    sentences = sent_tokenize(story)
    index =0
    for s in sentences:
        flag =0
        count=0
        for word in seedwords:
            sentence_words = [ps.stem(i.lower()) for i in word_tokenize(s)]
            if word in sentence_words:
                count=1
                flag = 1
                break
        if flag==1:
            break
        index +=1    
    if count == 0:
        storyobj.indiv='-'
    else:
        s = sentences[index]
        doc=nlp(s)
        text = ''
        for token in doc:
            if token.dep_ == 'nsubj':
                text=token.text
                break
        noun_phrases=[np.text for np in doc.noun_chunks]
        if len(text)>0:    
            for i in noun_phrases:
                np_split = i.split()
                if text in np_split:
                    storyobj.indiv=i.upper()
                    break
        else:
            storyobj.indiv=noun_phrases[-1].upper() 