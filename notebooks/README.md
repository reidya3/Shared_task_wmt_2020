# noteboks

Folder containing the notebooks 

## Semantic Anaylsis notebook
This notebook details the attempt of trying to find out semanyic categories of the traing/test data of each language pair. I treat every dataset as it own corpus. My first attempt involes topic modelling. Topic Modelling is the process of extracting major themes from a given corpus of text data.

Background Original technique for topic modelling was developed in 1998 by Raghavan, Tamaki and Vempala. Then came the PLSA (Probabilistic Latent Semantic Analysis) in 1998 created by Thomas Hoffman. Most commonly used technique called the was developed in 2002 by Andrew Ng, David Blei and Michael Jordan. Another technique which is an extension of LDA is called the Pachinko Allocation and improves on LDA by modeling correlations between topics in addition to the word correlations which constitute topics. An alternative to LDA is the HLTA (Heirarchical Latent Tree Analysis), which models word co-occurrence using a tree of latent variables and the states of the latent variables, which correspond to soft clusters of documents, are interpreted as topics.

Here, I use LDA and HTLA (Heirarchical Latent Tree Analysis).

## data augementation notebook
This notebook details the process involved in creating 2981 augmenetd data records. They were scraped usin