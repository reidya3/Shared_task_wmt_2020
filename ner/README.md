# This folder is for Named Entity Recognition

## First attempt

# The idea
1) Extract English source sentences to a file `train_en.txt` (only first 100 for experiment)

2) Use SpaCy to extract **NE**'s and put them in a `dict` as a `key` with their `value` = **NEXXX** (where XXX is an index number)

3) Make sure that the **NEXXX** versions are the same length as original `string`

4) The `dict values` also hold:
	1) The line number that the **NE** appeared in.
	2) The start and end indexes of the **NE** within the sentence (for example, if "Sean" was at the start of a sentence, its position would be (0, 4)) (we put 4 not 3 because it isn't inclusive)

5) We want to now open a new file to write to, I named it `train_en_swapped_ne.txt`.

6) Within the same function, open the `train_en.txt` to read.

7) Loop through lines of `train_en.txt`, match the line number of these lines to the `dict values` for lines.

8) If the line numbers match, find the **NE** by using the `dict values` for start and end.

9) Swap this **NE** with its corresponding **NEXXX**

10) Done.