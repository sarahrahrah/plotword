import nltk
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
import math
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from cycler import cycler


class TextCleanandDivisions:

    def __init__(self, text, numofwordsineachchunk, title):
        self.text = text
        self.numofwordsineachchunk = numofwordsineachchunk
        self.title = title
        self.open = self._open()
        self.tokens = self._tokenize()
        self.lower = self._lower()
        self.stem = self._stem()
        self.word_counts = self._count_words()
        self.toklength = self._toklen()
        self.chunks = self._chunks()

    def _open(self):
        with open(self.text) as f:
            s = " ".join([x.strip() for x in f])
        return s
    
    def _tokenize(self):
        return word_tokenize(self.open)

    def _lower(self):
         lower = [x.lower() for x in self.tokens]
         return lower

    def _stem(self):
        ps = PorterStemmer()
        stemmed = [ps.stem(x) for x in self.lower]
        return stemmed
        
    def _count_words(self):
        return Counter(self.tokens)

    def _toklen(self):
        length = len(self.tokens)
        return length

    def _chunks(self):
        length_of_indiv_chunks = self.toklength / self.numofwordsineachchunk
        rounded_up = math.ceil(length_of_indiv_chunks)
        chunksinlist = []
        tokenslist = self.stem
        for i in range(0, rounded_up):
            if len(chunksinlist) < self.numofwordsineachchunk:
                innertokensarray = tokenslist[0:self.numofwordsineachchunk]
                chunksinlist.append(innertokensarray)
                del tokenslist[0:self.numofwordsineachchunk]
            else:
                innertokensarray = tokenslist
                chunksinlist.append(innertokensarray)
        return chunksinlist


class PrepareDocument(TextCleanandDivisions):
    def __init__(self, text, numofwordsineachchunk, title, specificwords):
        super().__init__(text,numofwordsineachchunk, title)
        self.specificwords = specificwords
        self.specificwords_lower_stem = self.specwordslowstem()
        self.specificwordcountsinchucks = self.specificwordcountsinchunks()

    def specwordslowstem(self):
        clean = [x.lower() for x in self.specificwords]
        ps = PorterStemmer()
        stemmed = [ps.stem(x) for x in clean]
        print (stemmed)
        print (clean)
        return stemmed

    def specificwordcountsinchunks(self):
        inchunks = []
        for x in self.specificwords_lower_stem:
            counts = []
            for i in self.chunks:
                count = i.count(x)
                counts.append(count)
            inchunks.append(counts)
        return inchunks

    def showplot(self):
        length = len(self.chunks)
        lenlist = list(range(length))
        c = plt.get_cmap('Set2').colors
        fig, ax = plt.subplots(1,1)
        ax.set_prop_cycle(cycler('color', c))
        for x in self.specificwordcountsinchucks:
            plt.plot(lenlist, x, lw=3)
        plt.legend(self.specificwords)
        plt.ylabel("Number of Occurrences")
        plt.xlabel("Section")
        plt.title("Word Frequencies in " + self.title)
        plt.savefig(self.title +"_wordfreq.png")
        plt.show()
        


