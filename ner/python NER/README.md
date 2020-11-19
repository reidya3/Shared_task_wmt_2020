# This folder is for our Named Entity Finder python script.

---
## named_entity_recogniser.py

### Contents

`mask` function. <br>
Function parameters:<br>
	**mask(input_tsv, output_tsv, entities)**<br>

`input_tsv` is the .tsv containing the text you want to mask.<br>
`output_tsv` is the name of the file you would like to write to.<br>
`entities` is a list of the labels you would like to mask.<br>

**NOTE:** This function also produces a **mapping.json** file containing the `dictionary`.<br>

---

## run_ner.py


This is an example usage of `named_entity_recogniser.py`<br>

Make sure you select the right **input** and **output**.

---