# import indexer
from __future__ import division
from math import log
from operator import itemgetter
import json
import sys
__author__ = 'Akshaya'


k1=1.2
b=0.75
k2=100
b_complement = 1-b

# Terms needed for computing BM25 score
##k1 = 10, b = 0.75 & k2 = 100
##n=number of docs containing term i
##N= Total number of documents in the collection
##doc_length is the length of the document
##avg_doc_length is the average document length
##term_freq is the frequency of term i in the doc under consideration.


# inv_index_file = open('H:\IR\Assignment 3\inverted_index.txt','r')
inv_index_file = open(sys.argv[1],'r')

inv_index = json.load(inv_index_file)

inv_index_file.close()

# Stores the length of each document
doc_index = {}

# To Calculate length of each document based on the inv_index values
for i in inv_index.keys():
    for j in inv_index[i]:

        ######## Used For Debugging ##########- Starts
        # print "here?",j[0]
        ######## Used For Debugging ##########- Ends

        if j[0] not in doc_index.keys():
            doc_index[j[0]] = j[1]
        else:
            doc_index[j[0]] += j[1]

# N contains the total number of documents in the corpus
N = doc_index.__len__()

######## Used For Debugging ##########- Starts
# print "N",N
######## Used For Debugging ##########- Ends

# total_length contains the sum of all the lengths of a doc
total_length = 0

# Computes the total_length using doc_index
for i in doc_index.keys():
    total_length = total_length + doc_index[i]

######## Used For Debugging ##########- Starts
# print "total_length",total_length
######## Used For Debugging ##########- Ends

# Computest the average length of the document using total_length and N
avg_doc_length = float(total_length/N)

# query_file = open('H:\IR\Assignment 3\queries.txt','r')
query_file = open(sys.argv[2],'r')
query_list  =  query_file.readlines()
query_file.close()

# The number of documents which need to be present on the output
# max_doc_result = 100
max_doc_result = int(sys.argv[3])

query_list = [i.strip('\n') for i in query_list]


######## Used For Debugging ##########- Starts
# print "inv_index",inv_index.__len__()
# print "avg_doc_length",avg_doc_length
# print "N",N
# print query_list
######## Used For Debugging ##########- Ends


##Function to calculate the BM25 score for each term in the query.
# qf -> the frequency of term i in the query.
# tf -> Term Frequency
# r -> the number of relevant documents indexed by this term, for this case it is 0
# R -> the total number of relevant documents, for this case it is 0
# b_complement -> 1-b
def calculate_BM25(r,R,n,N,avg_doc_length,doc_length,tf,qf):
    K = k1*((b*(doc_length/avg_doc_length)) + b_complement)
    term_score = 0
    term_score += log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))
    term_score *= ((k1+1)*tf)/(K + tf)
    term_score *= ((k2+1)*qf)/(k2 + qf)
    return term_score



# file_results = open('H:\IR\Assignment 3\\results.txt','w')
file_results = open(sys.argv[4],'w')

# Contains the list of the scores for each query
q_score_result_list = []

# Gives the id for which query the loop is currently in progress
query_id = 1

# Provides the final output
for i in query_list:

    # temporary variable which contains the dictionary of doc-id and its score
    q_score = {}
    # Temporary variable which contains the value for the inv_index key
    val_dict = {}
    # contains individual words from the query
    words_in_query = i.split()
    for j in words_in_query:

        # The below loop calculates the word frequency in the given query
        qf = 0
        for k in words_in_query:
            if j == k:
                qf += 1

        if j in inv_index.keys():
            val = inv_index[j]
            val_dict = dict(val)
            val_dict_len = val_dict.__len__()

            # Calculates the score for each term and then adds it to the socre for each document
            for doc_id,term_freq in val_dict.items():
                doc_length = doc_index[doc_id]
                term_score = calculate_BM25(0,0,val_dict_len,N,avg_doc_length,doc_length,term_freq,qf)

                if doc_id not in q_score:
                        q_score[doc_id]=term_score
                else:
                        q_score[doc_id]+=term_score

    q_score_result_list.append(q_score)
    q_score = {}

    # Sorts the docs according to BM25 score and stores the top 100 of them
    for i in q_score_result_list:
        sorted_docs = sorted(i.items(),key=itemgetter(1),reverse=True)
        doc_rank = 1

        for doc_id,term_score in sorted_docs:

            if doc_rank > max_doc_result:
                break
            file_results.write(str(query_id)+ " " + "Q0"+ " " +str(doc_id).rjust(4)+ " "
                               +str(doc_rank).rjust(3)+ " " + str(term_score).rjust(13)+ " " +"System-AK\n")
            doc_rank+=1

        sorted_docs = []

    query_id += 1

file_results.close()

######## Used For Debugging ##########- Starts
# print q_score_result_list.__len__()
######## Used For Debugging ##########- Ends