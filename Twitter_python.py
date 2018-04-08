'''This code is by Derek Stevens for the use of CCDS and any future student
indending to analyse twitter data'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''list of words I don't think are important feel free to add or remove'''
stops = ['are', 'be', ' ','as', 'and', 'of', 'a', 'to', 'the', 'at', 'is', 'in','was', 'The', 'the', '', 'for', 'on','our', 'all']



''' this will break your csv file into lists of words and a qualitative field,
split the word list into words and combine it with the quant value.
You must specify the index in your csv of your word collum and your qualitative value index.'''

def csvbreaker(filename, wordsidx, qualidx):
    dataset = pd.read_csv(filename)
    words = dataset.iloc[:, wordsidx]
    qual = dataset.iloc[:,qualidx]
    for i in range(len(words)):
        words[i] = words[i].split(" ")
    concat = list()
    for i in range(len(words)-1):
        concat.append([words[i],qual[i]])
    return concat

data = csvbreaker('twitter_data.csv',2,9)



'''takes every word from your twitter data and finds it's association with a metric
to use pass a two dimentional list with the tweet as the first
dimention then the words and metrics in the second'''
def wordimportance(data):
    totals = {}
    for tweet in data:
        for word in tweet[0]:
            if word in stops:
                continue
            elif word not in totals:
                totals[word] = [tweet[1],1]
            else:
                totals[word][0]+=tweet[1]
                totals[word][1]+=1
    sortedtotals = sorted(totals.items(), key = lambda t:t[1][0])
    return sortedtotals

worcount = wordimportance(data)