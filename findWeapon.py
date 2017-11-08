from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def findWeapon(story, storyObj):
    ps = PorterStemmer()
    wl = WordNetLemmatizer()

    weaponFileName = 'weapons.txt'
    weaponsList = []
    with open(weaponFileName) as file:
        for line in file:
            weaponsList.append(line.strip().lower())

    for i in range(len(weaponsList)):
        #if (weaponsList[i])[-1] == 's':
        #weaponsList[i] = ps.stem(weaponsList[i])
        weaponsList[i] = wl.lemmatize(weaponsList[i])

    # if storyObj.id == 'DEV-MUC3-0078':
    #     print('yay')

    storyWords = [i for i in word_tokenize(story)]
    storyWordsStemmed = storyWords.copy()
    for j in range(len(storyWordsStemmed)):
        #if (storyWordsStemmed[j])[-1] == 's':
        #    storyWordsStemmed[j] = ps.stem(storyWordsStemmed[j])
        storyWordsStemmed[j] = wl.lemmatize(storyWordsStemmed[j].lower())

    weaponsDict = {}
    for weapon in weaponsList:
        if weapon in storyWordsStemmed:  # Without using stemming its giving better accuracy.
            wpIndex = storyWordsStemmed.index(weapon);
            wp = storyWords[wpIndex]
            if wp not in weaponsDict:
                weaponsDict[wp] = 1
            else:
                weaponsDict[wp] += 1

    wp = '-'
    if len(weaponsDict) != 0:
        wp = max(weaponsDict, key=weaponsDict.get)
    storyObj.weapon = wp

    #Weapons dictionary has all the wepons talked about in the story.
    candidateSentences = []
    storySentences = [i.lower() for i in sent_tokenize(story)]
    for sentence in storySentences:
        sentence = sentence.replace('\n', ' ').replace('\r', '')
        for key in weaponsDict:
            if key in sentence:
                candidateSentences.append(sentence)

    return candidateSentences
