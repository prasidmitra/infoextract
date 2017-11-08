from nltk.parse.stanford import StanfordDependencyParser
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tag import StanfordNERTagger
from nltk.stem import PorterStemmer

import spacy
nlp = spacy.load('en')
ps = PorterStemmer()

seedwords = ['attack','attacked','bomb','bombed','grenade','destroyed','destroy']

#dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
#st = StanfordNERTagger('/Users/prasidmitra/Downloads/stanford/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/prasidmitra/Downloads/stanford/stanford-ner-2017-06-09/stanford-ner.jar',encoding='utf-8')
def FindTarget(story,storyobj):
    sentences = sent_tokenize(story)
    index =0
    for s in sentences:
        # s.replace('\n',' ').replace('\r','')
        # doc = nlp(s)
        # print('*********')
        # noun_phrases=[np.text for np in doc.noun_chunks]
        # depend = [token.text+' '+token.dep_ for token in doc]
        # print(noun_phrases)
        # print('*********')
        # print(depend)
        # print('*********')
        # print(st.tag(word_tokenize(s)))
        # print('____________________________________________')
        # result = [list(i.triples()) for i in dep_parser.raw_parse(s)]
        # print(result)
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
        storyobj.target='-'
    else:
        s = sentences[index]
        doc=nlp(s)
        text = ''
        for token in doc:
            if token.dep_ == 'dobj':
                text=token.text
                break
        noun_phrases=[np.text for np in doc.noun_chunks]
        if len(text)>0:    
            for i in noun_phrases:
                np_split = i.split()
                if text in np_split:
                    storyobj.target=i.upper()
                    break
        else:
            storyobj.target=noun_phrases[-1].upper()            

                            

