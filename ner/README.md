# This folder is devote to Named Entity Recognition

## First attempt

# The idea
1) Extract English source sentences to a file `train_en.txt` (only first 100 for experiment)

2) Add named entites of type `PERSON` , `ORGANISATION`, and `PRODUCT` in `train_en.txt` to a dictionary corresponding to a **NEXXX**. (For example: `{NE1: Google, NE2: Sean}` etc)

3) Replace NE's in the source with its **NEXXX** value.

4) Run translator as normal

5) In target text, revert **NEXXX** back to original word.

6) Done.
