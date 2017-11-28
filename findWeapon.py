from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

import spacy
from spacy import displacy

nlp = spacy.load('en')

def findWeapon(story, storyObj):
    ps = PorterStemmer()
    wl = WordNetLemmatizer()

    weaponFileName = 'weapons.txt'
    weaponsList = []
    with open(weaponFileName) as file:
        for line in file:
            weaponsList.append(line.strip().lower())

    # for i in range(len(weaponsList)):
    #     #if (weaponsList[i])[-1] == 's':
    #     #weaponsList[i] = ps.stem(weaponsList[i])
    #     weaponsList[i] = wl.lemmatize(weaponsList[i])

    # if storyObj.id == 'DEV-MUC3-0078':
    #     print('yay')

    storySentences = [i for i in sent_tokenize(story)]
    weaponsDict = {}
    weaponsDictO = {}
    for sentT in storySentences:
        sentWords = [j for j in word_tokenize(sentT)]
        for weapon in weaponsList:
            if weapon.upper() in sentWords:  # Without using stemming its giving better accuracy.
                if weapon.upper() not in weaponsDict:
                    weaponsDict[weapon.upper()] = 1
                else:
                    weaponsDict[weapon.upper()] += 1

    # storySentences = [i for i in sent_tokenize(story)]
    # weaponsDict = {}
    # weaponsDictO = {}
    # for sentT in storySentences:
    #     for weapon in weaponsList:
    #         if weapon.lower() in sentT.lower():
    #             idx = sentT.lower().index(weapon.l.lower())
    #             wp = sentT[idx]
    #             if weapon not in weaponsDict:
    #                 weaponsDict[weapon] = 1
    #             else:
    #                 weaponsDict[weapon] += 1
    #
    #     sentWords = [j for j in word_tokenize(sentT)]
    #     sentWordsLem = sentWords.copy()
    #     for k in range(len(sentWordsLem)):
    #         sentWordsLem[k] = wl.lemmatize(sentWordsLem[k].lower())
    #     for weapon in weaponsList:
    #         if weapon in sentWordsLem:  # Without using stemming its giving better accuracy.
    #             wpIndex = sentWordsLem.index(weapon)
    #             wp = sentWords[wpIndex]
    #             if weapon not in weaponsDict:
    #                 weaponsDict[weapon] = 1
    #                 weaponsDictO[weapon] = wp
    #             else:
    #                 weaponsDict[weapon] += 1





    # storyWords = [i for i in word_tokenize(story)]
    # storyWordsStemmed = storyWords.copy()
    # for j in range(len(storyWordsStemmed)):
    #     #if (storyWordsStemmed[j])[-1] == 's':
    #     #    storyWordsStemmed[j] = ps.stem(storyWordsStemmed[j])
    #     storyWordsStemmed[j] = wl.lemmatize(storyWordsStemmed[j].lower())
    #
    #
    # weaponsDict = {}
    # for weapon in weaponsList:
    #     if weapon in storyWordsStemmed:  # Without using stemming its giving better accuracy.
    #         wpIndex = storyWordsStemmed.index(weapon)
    #         wp = storyWords[wpIndex]
    #         if wp not in weaponsDict:
    #             weaponsDict[wp] = 1
    #         else:
    #             weaponsDict[wp] += 1

    wp = '-'
    if len(weaponsDict) != 0:
        wp = max(weaponsDict, key=weaponsDict.get)
        # for sentT in storySentences:
        #     sentWords = [j for j in word_tokenize(sentT)]
        #     if wp.upper() in sentWords:
        #         doc = nlp(sentT)
        #         for token in doc:
        #             if token.text.lower() == wp.lower():
        #                 print('yay')

    storyObj.weapon = wp

    #Weapons dictionary has all the wepons talked about in the story.
    # candidateSentences = []
    # storySentences = [i.lower() for i in sent_tokenize(story)]
    # for sentence in storySentences:
    #     sentence = sentence.replace('\n', ' ').replace('\r', '')
    #     for key in weaponsDict:
    #         if key in sentence:
    #             candidateSentences.append(sentence)
    #
    # return candidateSentences
