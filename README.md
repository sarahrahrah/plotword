# plotword
Small python package for visualizing word counts in text.

Uses matplotlib

To use:

from plotword import plotwordcounts

newdoc = plotwordcounts.PrepareDocument(text="name_of_document.txt", numofwordsineachchunk = number of words, title="Title for Plot",
                            specificwords=["word1","word2","word3"])



The PrepareDocument class has several arguments.
