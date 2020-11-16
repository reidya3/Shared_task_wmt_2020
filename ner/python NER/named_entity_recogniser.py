#Import SpaCy
import spacy
from spacy import displacy
from collections import Counter
source_nlp = spacy.load("en_core_web_sm")
target_nlp = spacy.load("de_core_news_sm")

#Import pandas
import pandas as pd

#Import json
import json

def mask(input_csv, output_csv, entities):
	d = {}
	df = pd.read_csv(input_csv, sep='\t', index_col="index")

	entity_count = 0
	for index, row in df.iterrows():
		line1, line2 = row.original, row.translation
		source, target = source_nlp(line1), target_nlp(line2)
		source_adjust, target_adjust = 0, 0

#mask source
		for X in source.ents:
			if X.label_ in entities:
				if X.text not in d:
					d[X.text] = "NE{}".format(entity_count)
				start, end = X.start_char-source_adjust, X.end_char-source_adjust
				line1 = "".join([line1[:start],d[X.text],line1[end:]])
				source_adjust=len(X.text)-len(d[X.text])
				entity_count+=1
#mask target
		for Y in target.ents:
			if Y.label_ in entities:
				if Y.text not in d:
					d[Y.text] = "NE{}".format(entity_count)
				start, end = Y.start_char-target_adjust, Y.end_char-target_adjust
				line2 = "".join([line2[:start],d[Y.text],line2[end:]])
				target_adjust=len(Y.text)-len(d[Y.text])
				entity_count+=1
		df.at[index,"original"]=line1
		df.at[index, "translation"]=line2
			
#Export dict to json
	df.to_csv(path_or_buf=output_csv, sep='\t')
	with open('output/dev_mapping.json', 'w') as fp:
		json.dump(d, fp)
	return(d)
