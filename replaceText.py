import re

#text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

text = open('./TextDir/madlib.txt','r')

substext = open('./TextDir/textforsubs.txt','r').readlines()
subjectre,verbre,nounre,adjactivere = substext[0].split(',')

matchRE = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB',re.I)

for textline in text.readlines():
    mo = matchRE.findall(textline)
    if mo is not None:
        for moRE  in mo:
            if moRE.lower() == 'adjective':
                subRE = re.compile(moRE)
                textline = subRE.sub(adjactivere,textline)
            elif moRE.lower() == 'noun':
                subRE = re.compile(moRE)
                textline = subRE.sub(nounre, textline)
            elif moRE.lower() == 'adverb':
                subRE = re.compile(moRE)
                textline = subRE.sub(verbre, textline)
    print(textline)