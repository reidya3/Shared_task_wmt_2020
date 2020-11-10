from named_entity_recogniser import *


#This is an example of how to use the mask function

IN = "input/train.ende.df.short.tsv"
OUT = "output/masked.tsv"
entities = ["PERSON", "ORG", "PRODUCT", "WORK_OF_ART", "LOC"]

d = mask(IN, OUT, entities)