#Import SpaCy
import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("de_core_news_sm")

#Import pandas
import pandas as pd

#Import json
import json

def mask(input_csv, output_csv, entities):
	d = {}
	df = pd.read_csv(input_csv, sep='\t', index_col="index")

	entity_count = 0
	for index, row in df.iterrows():
		line = row.translation
		doc = nlp(line)
		adjust = 0
		for X in doc.ents:
			if X.label_ in entities:
				if X.text not in d:
					d[X.text] = "NE{}".format(entity_count)

				start, end = X.start_char-adjust, X.end_char-adjust

				line = "".join([line[:start],d[X.text],line[end:]])

				adjust=len(X.text)-len(d[X.text])

				entity_count+=1

		df.at[index,"translation"]=line

			
	df.to_csv(path_or_buf=output_csv, sep='\t')
	with open('output/dev_mapping.json', 'w') as fp:
		json.dump(d, fp)
	return(d)
