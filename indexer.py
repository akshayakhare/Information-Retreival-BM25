from __future__ import division

from itertools import groupby
import json
import sys
__author__ = 'Akshaya'

digit_tuple = ('0','1','2','3','4','5','6','7','8','9')

def contains_Only_Digits(str):
    for i in str:
        if i in digit_tuple:
            continue
        else:
            return False
    return True

# File opens
# CorpusFile = open('H:\IR\Assignment 3\Sample.txt','r')
# CorpusFile = open('H:\IR\Assignment 3\\tccorpus.txt','r')
CorpusFile = open(sys.argv[1],'r')

P  =  CorpusFile.read()

CorpusFile.close()
# File Closes

######## Used For Debugging ##########- Starts
# print "File after being read",P
######## Used For Debugging ##########- Ends

# Splitting the document based on spaces getting each word
words = P.split()

######## Used For Debugging ##########- Starts
# print "list of words from the document", words
######## Used For Debugging ##########- Ends

# Splitting into each doc seperated by #
split_docs=[list(group) for i,
                    group in groupby(words,lambda x: x == '#') if not i]

######## Used For Debugging ##########- Starts
# print "after splitting into each doc",split_docs
######## Used For Debugging ##########- Ends

# putting all strings for a doc in a dictionary of docs
doc_index = {}
for i in split_docs:
    for each in i:
        doc_index[i[0]]=i[1:]

# num_list a temporary list that carries all the only digit values for each doc
num_list=[]

# str list a temporary list which carries all the non-digit values for each doc,
# which will be stored in doc_index eventually
str_list=[]

# Removes all the digit-only strings from the document
for i in doc_index.keys():
    for k in doc_index[i]:
        if contains_Only_Digits(str(k)):
            num_list.append(k)
    for k in doc_index[i]:
            if k not in num_list:
                str_list.append(k)
    doc_index[i] = str_list
    str_list =[]
    num_list = []

######## Used For Debugging ##########- Starts
# print "docindex",doc_index[i]
######## Used For Debugging ##########- Ends

# N contains the total number of documents in the corpus
N = doc_index.__len__()

# total_length contains the sum of all the lengths of a doc
total_length = 0

# Computes the total_length using doc_index
for i in doc_index.keys():
    total_length = total_length + doc_index[i].__len__()

######## Used For Debugging ##########- Starts
# print "N", N
######## Used For Debugging ##########- Ends

# Computest the average length of the document using total_length and N
avg_doc_length = float(total_length/N)

######## Used For Debugging ##########- Starts
# print "avg_doc_length", avg_doc_length
######## Used For Debugging ##########- Ends

# A temporary dictionary that Calculates the particular word freq in each document
word_freq_in_doc = {}

# Contains the list of the term, document and the term frequency in the document
freq_list_tuple = []

# Creates a tuple that contains the term, document and the term frequency
for k,value_lst in doc_index.items():
    for i in value_lst:
        if i not in word_freq_in_doc:
            word_freq_in_doc[i]=1
        else:
            word_freq_in_doc[i]+=1

    for key,val in word_freq_in_doc.items():
        freq_list_tuple.append((key,k,val))

    word_freq_in_doc={}

# The final inverted index which will contain each term and its frequency in all the documents
inv_index = {}

######## Used For Debugging ##########- Starts
# print "tuple length",freq_list_tuple.__len__()
######## Used For Debugging ##########- Ends

# Creates the inverted index using the freq_list_tuple
for i,j,k in freq_list_tuple:
    inv_index.setdefault(i,[]).append((j,k,))

######## Used For Debugging ##########- Starts
# print "inverted index length?",inv_index.__len__()
######## Used For Debugging ##########- Ends

# for key in inv_index.keys():
#     # print "kwy",key
#     if contains_Only_Digits(key):
#         inv_index.pop(key)
#         continue

######## Used For Debugging ##########- Starts
# print "inverted index length? after removing digits",inv_index.__len__()
# print "inverted index???",inv_index
# print (inv_index["current"]).__len__()
######## Used For Debugging ##########- Ends

# fileforInvertedIndex = open('H:\IR\Assignment 3\inverted_index.txt','w')

fileforInvertedIndex = open(sys.argv[2],'w')

json.dump(inv_index,fileforInvertedIndex)

fileforInvertedIndex.close()

######## Used For Debugging ##########- Starts
# print "List of Frequency",freq_list_tuple
######## Used For Debugging ##########- Ends