#Import SpaCy
import spacy
from spacy import displacy
from collections import Counter

#Import pandas
import pandas as pd

#Import regex
import regex

#Import json
import json

def mask(input_csv, output_csv, output_json, entities, lang):
#Set up dict & dataframe
    d = {}
    df = pd.read_csv(input_csv, sep='\t', index_col="index")

    if lang == "roen":
        source_nlp = spacy.load("ro_core_news_sm")
    else:
        source_nlp = spacy.load("en_core_web_sm")

    entity_count = 0
    for index, row in df.iterrows():
        line1, line2 = row.original, row.translation
        source = source_nlp(line1)
        source_adjust, target_adjust = 0, 0
        
#mask source:
        for X in source.ents:
            if X.label_ in entities:
                if X.text not in d:
                    d[X.text] = "NE{}".format(entity_count)
                start, end = X.start_char-source_adjust, X.end_char-source_adjust
                line1 = "".join([line1[:start],d[X.text],line1[end:]])
                source_adjust=len(X.text)-len(d[X.text])
                entity_count+=1
  
#Find NE from source in target and mask:
                entity = "".join(["(?b)" + "(", X.text, ")", "{0<=s<=5,0<=d<=5}"])
                re = regex.search(entity, line2)
                if re:
                    d[X.text] = "NE{}".format(entity_count)
                    t_start, t_end = re.span()[0]-target_adjust, re.span()[1]-target_adjust
                    line2 = "".join([line2[0:re.span()[0]], d[X.text], line2[re.span()[1]:]])
                    target_adjust=(re.span()[1]-re.span()[0])-len(d[X.text])
                    entity_count+=1


#Replace row with masked version:
        df.at[index,"original"]=line1
        df.at[index,"translation"]=line2
#Export dict to json:
    df.to_csv(path_or_buf=output_csv, sep='\t')
    with open(output_json, 'w') as fp:
        json.dump(d, fp)