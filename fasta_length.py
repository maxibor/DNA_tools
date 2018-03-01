#!/usr/bin/env python


import sys

def fasta_len_count (file) :
	"""
	Counts length of sequences in fasta
	"""
	mylen = 0
	fasta_handle = open(file, "r")
	for line in fasta_handle :
		line = line.rstrip()
		try :
			if line[0] != ">" :
				mylen += len(line)
		except IndexError :
			continue
    	fasta_handle.close()
	return int(mylen)

print fasta_len_count(sys.argv[1])
