pip install --user virtualenv
if [ -d './venv' ]; then
	mkdir venv
	#python -m virtualenv venv #for python2.7
	python -m virtualenv venv -p /home/rachmani/python3.5/bin/python3.5
	source venv/bin/activate
	pip install nltk
	pip install spacy
	python -m spacy download en
	python requirements.py
	python infoextract.py "/home/u1143744/NLPPRojects/infoextract/developset/texts.txt"
	deactivate
else
	source venv/bin/activate
	pip install nltk
	pip install spacy
	python -m spacy download en
	python requirements.py
	python infoextract.py "/home/u1143744/NLPPRojects/infoextract/developset/texts.txt"
	deactivate
fi
