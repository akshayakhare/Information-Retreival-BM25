# BM25
Implementation of BM25 algorithm to rank documents

Steps for running the program:
---------------------------------------------------------------------------------------------------------------------------
1. Install Python if not already installed from https://www.python.org/downloads/  version 2.7.10
2. The file 'indexer.py' creates an inverted index
3. The file 'BM25.py' creates a file which shows the top ranked documents based on the set of queries given
4. 'indexer.py' takes two arguments, first a corpus file (sample-> "tccorpus.txt") and an output file (sample-> "index.out")
5. 'BM25.py' takes four arguments, first the inverted index file (sample-> "index.out"), second the query file(sample-> "query.txt"), third the max number of documents to be shown for each query to be shown in the final(sample -> 100)  and an output file (sample-> "results.eval")
6. While running both the files, proper number of arguments and proper values should be given else the program will fail

References:
----------------------------------------------------------------------------------------------------------------------------
http://stackoverflow.com/-> Helping out for various logic and syntax issues in python
https://www.python.org/doc/


******************************************************************************************************
The implementation description is given in 
"Implementation_Technique.txt"

******************************************************************************************************
The sample corpus file is being sent as
"tccorpus.txt"

******************************************************************************************************
The inverted index for the given corpus file is stored in 
"index.out"

******************************************************************************************************
The list of queries on which BM25 has to be implemented for finding ranked documents
"queries.txt"

******************************************************************************************************
The final result with the documents in sorted order for each query
"results.eval"
