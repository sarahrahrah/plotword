# plotword
plotword is a small python package for visualizing word counts in text. It was made with literary texts in mind for digital humanities projects, but can be used for other large documents, such as legal documents as well. The showplot() function provides a line chart of word counts for specified words over the course of the text.

Uses matplotlib and nltk. 

To use:

from plotword import plotwordcounts

newdoc = plotwordcounts.PrepareDocument(text="name_of_document.txt", numofwordsineachchunk = number of words, title="Title for Plot",
                            specificwords=["word1","word2","word3"])



The PrepareDocument class has several arguments.
