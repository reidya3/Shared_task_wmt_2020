#Import SpaCy
import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

#Instantiate a dictionary
d={}

#List of NE's we want:
named_entity_labels = ["PERSON", "ORG", "PRODUCT"]

FILE = "train_en.txt"
with open(FILE, "r", encoding='utf-8') as f:
    i = 1
    for line in f:
        doc=nlp(line)
        for X in doc.ents:
            if X.label_ in named_entity_labels:
                d[X.text] = "NE{}".format(i)
                i+=1
    f.close()