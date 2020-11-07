#This folder is devote to Named Entity Recognition

##First attempt

#The idea
1) Extract English source sentences to a file `train_en.txt` (only first 100 for experiment)

2) Add named entites of type `person` , `organisation`, and `product` in `train_en.txt` to a dictionary corresponding to a **NEXXX**. (For example: `{NE1: Google, NE2: Sean}` etc)

3) Replace NE's in the source with its **NEXXX** value.

4) Run translator as normal

5) In target text, revert **NEXXX** back to original word.

6) Done.

#The Problem (I think)
All language characters, (a to z, 0 to 9, special characters, áé... etc) have a unicode representation. There are various different encoding formats, some contain characters that others do not.<br>
I believe the source text is of various different encodings. And so, to read the file using one encoding, for example `utf-8`, will result in an error somewhere for a sentence of encoding `latin-1`.<br>
The same happens but in reverse if you use `latin-1` instead.

#The Solution (Maybe)
I transfered 100 lines to `train_en.txt` using the unix command line. Maybe this affected the encoding? I will try use pandas to extract the first 100 lines instead.