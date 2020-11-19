from named_entity_recogniser2 import mask

#This is an example of how to use the mask function

IN = "input/train.ende.df.short.tsv"
OUT = "output/train.ende.masked.tsv"
JSON = "output/train.ende.mapping.json"
entities = ["PER", "PERSON", "ORG", "ORGANIZATION", "PRODUCT", "WORK_OF_ART", "LOC"]

mask(IN, OUT, JSON, entities)