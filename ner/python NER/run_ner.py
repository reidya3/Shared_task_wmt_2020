from named_entity_recogniser2 import mask

#This is an example of how to use the mask function

IN = "input/dev.roen.df.short.tsv"
OUT = "output/masked-levenshtein-1/dev.roen.masked.tsv"
JSON = "output/masked-levenshtein-1/dev.roen.mapping.json"
entities = ["PER", "PERSON", "ORG", "ORGANIZATION", "PRODUCT", "WORK_OF_ART", "LOC"]

mask(IN, OUT, JSON, entities, "roen")