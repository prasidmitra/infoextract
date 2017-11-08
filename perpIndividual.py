from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize

def perpIndividual(inFile):
    st = StanfordNERTagger('D:\PythonProjects\StanfordParser\stanford-ner-2017-06-09\classifiers\english.all.3class.distsim.crf.ser.gz',
					   'D:\PythonProjects\StanfordParser\stanford-ner-2017-06-09\stanford-ner.jar',
					   encoding='utf-8')
    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)

    print(classified_text)


if __name__ == '__main__':
    perpIndividual('test')

