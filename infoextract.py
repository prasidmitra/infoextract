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
from FindTarget import FindTarget
from FindVictim import FindVictim
from FindPerp import FindPerp

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
    maxFreq = 0
    bestindex = 0   
    for i in range(5):
        if i != 1:
            if score[i]>maxFreq:
                bestindex = i
                maxFreq = score[i]
    if maxFreq > 0:
        obj.incident = incidents[bestindex].upper()
    else:
        obj.incident = incidents[1].upper()
          

def findSynonym(word):
    synonyms = []
    antonyms = []

    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return list(set(synonyms))            

def extractInfo(inTextFile):
    stories = []
    story_objects = []
    with open(inTextFile) as inputFile:
        text = ""
        for line in inputFile:
            p = re.match('^((DEV-MUC3|TST1-MUC3|TST2-MUC4)-[0-9]{4})',line)
            if p:
                if len(text) != 0:
                    stories.append(text)
                    text = ""
                obj = Template(p.group(),'-','-','-','-','-','-')
                story_objects.append(obj)

            else:
                text += line.replace('\n', ' ').replace('\r', '')
    if len(text)!= 0:
        stories.append(text)

    for i in range(len(stories)):
        findIncident(stories[i],story_objects[i])
        test = findWeapon(stories[i], story_objects[i])
        FindTarget(stories[i], story_objects[i])
        FindVictim(stories[i],story_objects[i])
        FindPerp(stories[i],story_objects[i])


    return story_objects   


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

        
def checkAccuracy(inTextFile):
    storyObjects = extractInfo(inTextFile)
    if not storyObjects:
        print('No stories found. Somewthing is wrong!')
        return

    with open('output.txt', 'w') as outFile:
        for storyT in storyObjects:
            outFile.write('ID:' + '  ' + storyT.id + '\n')
            outFile.write('INCIDENT:' + '  ' + storyT.incident + '\n')
            outFile.write('WEAPON:' + '  ' + storyT.weapon + '\n')
            outFile.write('PERP INDIV:' + '  ' + storyT.indiv + '\n')
            outFile.write('PERP ORG:' + '  ' + storyT.org + '\n')
            outFile.write('TARGET:' + '  ' + storyT.target + '\n')
            outFile.write('VICTIM:' + '  ' + storyT.victim + '\n')
            outFile.write('\n')
    outFile.close()

    #count = 0
    #filecount = 0
    #acc = [0, 0, 0, 0, 0, 0, 0]
    # while(count<=1300):
    #     testfile='./developset/texts/DEV-MUC3-'+str(count).zfill(4)
    #     ansfile='./developset/answers/DEV-MUC3-'+str(count).zfill(4)+'.anskey'
    #     if Path(testfile).is_file():
    #         obj = extractInfo(testfile)
    #
    #         #incident
    #         incident_actual = ''
    #
    #         f = open(ansfile)
    #         for line in f:
    #             nline = line.strip().split()
    #             if nline[0]=='INCIDENT:':
    #                 incident_actual = nline[1].lower()
    #                 break
    #         f.close()
    #
    #         incident_pred = obj.incident
    #         if incident_pred == incident_actual:
    #             acc[1]+=1
    #         #print (obj.id,incident_pred, incident_actual)
    #         #filecount+=1
    #
    #         # weapon
    #         weapon_actual = ''
    #
    #         f = open(ansfile)
    #         for line in f:
    #             nline = line.strip().split()
    #             if nline[0] == 'WEAPON:':
    #                 wpL = ''
    #                 for i in nline[1:]:
    #                     wpL += i.lower() + ' '
    #                 weapon_actual = wpL.strip()
    #                 break
    #         f.close()
    #
    #         weapon_pred = obj.weapon
    #         if weapon_pred == weapon_actual:
    #             acc[2] += 1
    #         print(obj.id, weapon_pred, weapon_actual)
    #         filecount += 1
    #     count+=1
    #
    # print('incident accuracy = ', acc[1]/filecount)
    # print('weapon accuracy = ', acc[2] / filecount)


def main():
    args = sys.argv
    if len(args) == 2:
        checkAccuracy(args[1])
    else:
        print('Wrong number of arguments specified!.')

if __name__ == '__main__':
    main()
