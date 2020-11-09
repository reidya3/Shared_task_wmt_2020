from named_entity_recogniser import *

IN = "train.ende.df.short.tsv"
OUT = "masked.tsv"
entities = ["PERSON", "ORG", "PRODUCT", "WORK_OF_ART", "LOC"]

d = mask(IN, OUT, entities)