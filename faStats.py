#!/usr/bin/env python

from Bio import SeqIO
import sys
# import matplotlib as mpl ##These two lines are needed
# mpl.use('Agg') # to plot without a X server running.
# import matplotlib.pyplot as plt
from collections import Counter

# Author : Maxime Borry
# Contact : maxime.borry@gmail.com
# Usage : faStats file.fa
# Summary : Computes sequences length statistics of a fasta file

def maxprint(elem, maxcount):
    return(int(elem/maxcount*80))

def getmax(thecounter):
    themax = 0
    for elem in sorted(list(set(thecounter.elements()))):
        if thecounter[elem] > themax:
            themax = thecounter[elem]
    return(themax)

seq_length = []
filename = sys.argv[1]
filename_short = filename.split(".")[0]
print ("Loading fasta file...")
for seq_record in SeqIO.parse(filename, "fasta"):
    seq_length.append(len(seq_record.seq))
cnt = Counter(seq_length)
themax = getmax(cnt)
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print (filename+" fasta file statistics : ")
print ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("Number of sequences: "+str(len(seq_length)))
print ("Average sequence length : "+str(sum(seq_length)/len(seq_length)))
print ("Max sequence length : "+str(max(seq_length)))
print ("Min sequence length : "+str(min(seq_length)))
print ("Distribution of sequence lengths")
for elem in sorted(list(set(cnt.elements()))):
    print("{0:6}".format(elem), "-", "{0:6}".format(cnt[elem]),  "|", "*"*maxprint(cnt[elem], themax ),)

# print ("Histogram of sequences length saved in "+filename_short+"_seq_len_distrib.png")
# print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# plt.hist(seq_length,color = "green")
# plt.ylabel("Number of sequences")
# plt.xlabel("Length of sequences")
# plt.title("Sequence length distribution in "+filename)
# plt.savefig(filename_short+"_seq_len_distrib.png")
