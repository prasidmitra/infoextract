import spacy
nlp = spacy.load('en')
doc = nlp('THE ATTACKS, ACCORDING TO THE REPORTS, TOOK PLACE IN USULUTAN, USULUTAN DEPARTMENT, 110 KM EAST OF THE CAPITAL, AND IN SANTA ELENA WHERE AS OF 0700 CLASHES WERE STILL UNDER WAY.  SANTA ELENA IS LOCATED 119 KM EAST OF THE CAPITAL, AND BOTH CITIES ARE COFFEE REGIONS.')
for i in doc.ents:
    print(i.label_, i.text)
for i in doc:
	print(i.text, i.ent_iob,i.ent_type_)    