import sys
import re
from Template import Template
#import spacy
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from pathlib import Path
from findWeapon import findWeapon

#Change the path to the stanford ner
#st = StanfordNERTagger('/Users/prasidmitra/Downloads/stanford/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/prasidmitra/Downloads/stanford/stanford-ner-2017-06-09/stanford-ner.jar',encoding='utf-8')

ps = PorterStemmer()



# nlp = spacy.load('en')
 




def findIncident(story,obj):
    incidents = ['arson','attack','bombing','kidnapping','robbery']
    incidents_synonyms = []
    for i in range(len(incidents)):
        incidents_synonyms.append(findSynonym(incidents[i]))
    story_words = [ps.stem(i.lower()) for i in word_tokenize(story)]
    score = [0,0,0,0,0]
    for i in range(5):
        for j in incidents_synonyms[i]:
            score[i]+=story_words.count(j)
            #if i == 2:
            #    print(j,story_words.count(j))
    max = 0
    bestindex = 0   
    for i in range(5):
        if i!=1:
            if score[i]>max:
                bestindex = i
                max = score[i]
    if max > 0:
        obj.incident = incidents[bestindex]
    else:
        obj.incident = incidents[1]
          

def findSynonym(word):
    synonyms = []
    antonyms = []

    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return list(set(synonyms))            

def extractInfo(textfile):
    stories=[]
    story_objects=[]
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
        test = findWeapon(stories[i], story_objects[i])
    return story_objects[0]   


    #   Stanford NER Tagger
    #print(st.tag(word_tokenize(stories[0])))   


    # for i in range(len(stories)):
    #   print(story_objects[i].id+'\n----------')
    #   print(ne_chunk(pos_tag(word_tokenize(stories[i])))) 

    # doc = nlp(stories[0])
    # for i in doc.ents:
    #     print(i.label_, i.text)
    # for i in doc:
    #   print(i.text, i.ent_iob,i.ent_type_)   

        
def checkAccuracy():
    
    count  = 0
    filecount = 0
    acc = [0,0,0,0,0,0,0]
    while(count<=1300):
        testfile='./developset/texts/DEV-MUC3-'+str(count).zfill(4)
        ansfile='./developset/answers/DEV-MUC3-'+str(count).zfill(4)+'.anskey'
        if Path(testfile).is_file():
            obj = extractInfo(testfile)

            #incident
            incident_actual = ''

            f = open(ansfile)
            for line in f:
                nline = line.strip().split()
                if nline[0]=='INCIDENT:':
                    incident_actual = nline[1].lower()
                    break
            f.close()

            incident_pred = obj.incident
            if incident_pred == incident_actual:
                acc[1]+=1
            #print (obj.id,incident_pred, incident_actual)
            #filecount+=1

            # weapon
            weapon_actual = ''

            f = open(ansfile)
            for line in f:
                nline = line.strip().split()
                if nline[0] == 'WEAPON:':
                    wpL = ''
                    for i in nline[1:]:
                        wpL += i.lower() + ' '
                    weapon_actual = wpL.strip()
                    break
            f.close()

            weapon_pred = obj.weapon
            if weapon_pred == weapon_actual:
                acc[2] += 1
            print(obj.id, weapon_pred, weapon_actual)
            filecount += 1
        count+=1

    #print('incident accuracy = ', acc[1]/filecount)
    print('weapon accuracy = ', acc[2] / filecount)




def main():
    #args=sys.argv
    #textfile = './developset/texts/DEV-MUC3-0006'
    #textfile = './developset/texts/sample1.txt'
    checkAccuracy()

    #extractInfo(textfile)

if __name__ == '__main__':
    main()