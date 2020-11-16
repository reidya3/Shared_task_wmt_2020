from named_entity_recogniser import mask

#This is an example of how to use the mask function

IN = "input/dev.ende.df.short.tsv"
OUT = "output/dev_masked.tsv"
entities = ["PER", "PERSON", "ORG", "PRODUCT", "WORK_OF_ART", "LOC"]

d = mask(IN, OUT, entities)