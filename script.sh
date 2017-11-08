pip install --user virtualenv
mkdir venv
#python -m virtualenv venv #for python2.7
python -m virtualenv venv -p /home/rachmani/python3.5/bin/python3.5 #for python3.5
source venv/bin/activate.csh
pip install spacy
python -m spacy download en
#python infoextract.py <textfile>