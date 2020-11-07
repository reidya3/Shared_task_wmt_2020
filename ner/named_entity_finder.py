import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

d={}
#Dictionary to map "EN<xxx>": <entity>
#(example:  {EN001: "Europe"}

FILE = "train_en.txt"
with open(FILE, "r", encoding='Latin-1 Supplement') as f:
	i = 0
	for line in f:
		print(i, end=' ')
		print(line)
		i+=1
	print(i)

#File of source text sentences
'''FILE = "train_en.txt"
with open(FILE, "r") as f:
	i = 1
	for line in f:
		doc=nlp(line)
		for X in doc.ents:
			d["NE{}".format(i)] = X.text
			i+=1
	f.close()
for entry in d:
	print(entry, d[entry])'''