__author__ = 'Akshaya'

neg_file = open('H:/IR/Assignment 6/1576_neg.txt','r')
pos_file = open('H:/IR/Assignment 6/1198_pos.txt','r')

neg_test_list = neg_file.readlines()
pos_test_list = pos_file.readlines()

fileOfLinks = open('H:/IR/Assignment 2/In-Links-Sample.txt','r')
P  =  set(fileOfLinks.readlines())
print P

print "neg_test_list",neg_test_list
neg_file.close()
pos_file.close()

