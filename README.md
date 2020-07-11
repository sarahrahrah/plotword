# plotword
**plotword** is a small python package for visualizing word counts in text. It was made with :books: literary texts :books: in mind for digital humanities projects, but can be used for other large documents, such as legal documents as well. Its showplot() function provides a line chart of word counts for specified words over the course of the text.

Dependencies are **matplotlib** and **nltk**, which must be installed for it to work. 

How to use:

from plotword import plotwordcounts

newdoc = plotwordcounts.PrepareDocument(text="name_of_document.txt", numofwordsineachchunk = number of words, title="Title for Plot",
                            specificwords=["word1","word2","word3"])



The PrepareDocument class has several arguments:

text - accesses the .txt file with the entire text

numofwordsineachchunk - the number of words by which to subdivide the text into individual chunks 

title - the title to appear on the plot

specificwords - the words for which to plot the word counts for over the course of the text

Sample output:

!["War and Peace" example](/images/wandp_wordfreq.png)


!["Sense and Sensibility one](/images/sands_wordfreq1.png)

!["Sense and Sensibility two](/images/sands_wordfreq2.png)
