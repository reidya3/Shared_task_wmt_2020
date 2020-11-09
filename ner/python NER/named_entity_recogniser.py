#Import SpaCy
import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

#Import pandas
import pandas as pd

#Import json
import json

def mask(input_csv, output_csv, entities):
	d = {}
	df = pd.read_csv(input_csv, sep='\t', index_col="index")

	entity_count = 0
	for index, row in df.iterrows():
		line = row.original
		doc=nlp(line)
		for X in doc.ents:
			if X.label_ in entities:

				d[X.text] = value_creator(X.text, entity_count, index, X.start_char, X.end_char)

				before, after = line[:X.start_char], line[X.end_char+1:]

				line = " ".join([before, d[X.text][0], after])
				df.at[index, "original"] = line
				entity_count+=1

	df.to_csv(path_or_buf=output_csv, sep='\t')
	with open('output/mapping.json', 'w') as fp:
		json.dump(d, fp)
	return(d)

def value_creator(text, entity_no, line_no, start, end):
	length = len(text)
	val = ((length -(2+len(str(entity_no)))) * "0") + str(entity_no)
	return("NE{}".format(val),"{}".format(line_no),("{}".format(start), "{}".format(end)))
