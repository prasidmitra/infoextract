from nltk.parse.stanford import StanfordDependencyParser
#path_to_jar = 'path_to/stanford-parser-full-2014-08-27/stanford-parser.jar'
#path_to_models_jar = 'path_to/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models.jar'

dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

result = [list(i.triples()) for i in dep_parser.raw_parse('LIMA, 16 JAN 90 (TELEVISION PERUANA) -- [TEXT] TEN TERRORISTS HURLED DYNAMITE STICKS AT U.S.  EMBASSY FACILITIES IN THE MIRAFLORES DISTRICT, CAUSING SERIOUS DAMAGE BUT FORTUNATELY NO CASUALTIES.')]

print(result)