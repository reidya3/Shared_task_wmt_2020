# This folder is for our Named Entity Finder python script.

---
## named_entity_recogniser.py


### Contents

1) `mask` function. 
Function parameters:
	mask(input_tsv, output_tsv, entities)

`input_tsv` is the .tsv containing the source text you want to mask.
`output_tsv` is the name of the file you would like to write to.
`entities` is a list of the labels you would like to mask.

**NOTE:** This function also produces a **mapping.json** file containing the `dictionary`.

2) `value_creator` function.

This function is called by `mask`. It creates the correct **NEXXX** value for a a given **key** (named entity)

---

## run_ner.py


This is an example usage of `named_entity_recogniser.py`

---

## Jupyter notebook

**NOTE:** For some reason, the same script fails on jupyter notebook. Not sure why.