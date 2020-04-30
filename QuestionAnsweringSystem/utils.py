#Functions that will enable to fetch exact answers based on spaCy Matcher & Entity Ruler
import nltk 
import spacy 
from spacy.matcher import PhraseMatcher 
from spacy.matcher import Matcher
from spacy.tokens import Span 
import string

def alsoknownas(sentence):

    from spacy.pipeline import EntityRuler
    nlp = spacy.load('en_core_web_sm', disable = ['ner'])
    rulerAlKnAs = EntityRuler(nlp, overwrite_ents=True)

    answer = sentence
    answer = answer.translate(str.maketrans('','',string.punctuation))

    aka_patterns = [text for text in ('known as', 'nicknamed', 'known mononymously as', 'known professionally as')]

    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    label = ""
    for aka in aka_patterns:
        if aka in answer:
            a=answer.split(aka,1)[-1]
            name = a.split()[0]
            surname1 = a.split()[1]
            surname2 = a.split()[2]
            surname3 = a.split()[3]
            str1 = name
            str2 = name + " " + surname1
            str3 = name + " " + surname1 + " " + surname2 
            str4 = name + " " + surname1 + " " + surname2 + " " + surname3
        
    tokens = nltk.word_tokenize(str4)
    pos = nltk.pos_tag(tokens)

    if (pos[0][1] in {"NNP","NN"} and pos[1][1] not in {"NNP","NN"}):
        label = str1
    if (pos[0][1] in {"NNP","NN"} and pos[1][1] in {"NNP","NN"} and pos[2][1] not in {"NNP","NN"}):
        label = str2
    if (pos[0][1] in {"NNP","NN"} and pos[1][1] in {"NNP","NN"} and pos[2][1] in {"NNP","NN"} and pos[3][1]  not in {"NNP","NN"}):
        label = str3
    if (pos[0][1] in {"NNP","NN"} and pos[1][1] in {"NNP","NN"} and pos[2][1] in {"NNP","NN"} and pos[3][1] in {"NNP","NN"}):
        label = str4

    for aka in aka_patterns:
        rulerAlKnAs.add_patterns([{"label": label, "pattern": aka}])
    rulerAlKnAs.name = 'rulerAlKnAs'
    nlp.add_pipe(rulerAlKnAs)
    doc = nlp(answer)
    for ent in doc.ents:
        return(ent.label_)
       
        
def birthdate(sentence):

    from spacy.pipeline import EntityRuler
    nlp = spacy.load('en_core_web_sm', disable = ['ner'])
    rulerdate = EntityRuler(nlp, overwrite_ents=True)

    answer = sentence

    date_patterns = ['born', 'â€“', '–']
    date = ""

    answer = answer.split('(')[1]     
    if 'â€“' in answer:
        a = answer.split(')')[0]
        day = a.split()[0]
        month = a.split()[1]
        year = a.split()[2]
    if 'born' in answer:
        a = answer.split(')')[0]
        day = a.split()[1]
        month = a.split()[2]
        year = a.split()[3]
    if '–' in answer:
        a = answer.split(')')[0]
        day = a.split()[1]
        month = a.split()[2]
        year = a.split()[3]
    date = day + " " + month + " " + year
      
    label = date

    for date in date_patterns:
        rulerdate.add_patterns([{"label": label, "pattern": date}])
    rulerdate.name = 'rulerdate'
    nlp.add_pipe(rulerdate)
    doc = nlp(answer)
    for ent in doc.ents:
        return(ent.label_)  


def deathday(sentence):
    
    from spacy.pipeline import EntityRuler
    nlp = spacy.load('en_core_web_sm', disable = ['ner'])
    rulerdate = EntityRuler(nlp, overwrite_ents=True)

    answer = sentence

    date_patterns = ['â€“','-']
    date = ""
    day=""
    
    answer = answer.split(')')[0]
    answer = answer.translate(str.maketrans('','',string.punctuation))
    b=[int(s) for s in answer.split() if s.isdigit()]
    a=answer.split(str(b[1]),1)[1]
    if 'â€“' in answer:
        a=a.split('“')[1]
    if '–' in answer:
        a=a.split('–')[1]  
    day = a.split()[0]
    month = a.split()[1]
    year = a.split()[2]
    date = day + " " + month + " " + year
    
    label = date
    return label
                
def nameofperson(sentence):
    from spacy.pipeline import EntityRuler
    nlp = spacy.load('en_core_web_sm', disable = ['ner'])
    rulername = EntityRuler(nlp, overwrite_ents=True)

    answer = sentence
    #answer = answer.translate(str.maketrans('','',string.punctuation))

    answer = answer.split('(')[0]
    answer = answer.split(',')[0]
        
    label = answer

    rulername.add_patterns([{"label": label, "pattern": answer}])
    rulername.name = 'rulername'
    nlp.add_pipe(rulername)
    doc = nlp(answer)
    for ent in doc.ents:
        return(ent.label_)
