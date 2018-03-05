#!/usr/bin/env python

from numpy import random as npr
import matplotlib.pyplot as plt

import argparse

def _get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
    prog='MetaBenReadSim',
    description='Metagenomic Benchmarking Read Simulator for ancient DNA')
    parser.add_argument('infile', help="path to reference fasta file")
    parser.add_argument(
    '-n',
    default=1000,
    help="Number of reads to simulate. Default = 1000")
    parser.add_argument(
    '-readlen',
    default=76,
    help="Average read length. Default = 76")
    parser.add_argument(
    '-inserlen',
    default=47,
    help="Average insert length. Default = 47")
    parser.add_argument(
    '-lendev',
    default=10,
    help="Insert length standard deviation. Default = 10")
    parser.add_argument(
    '-fa',
    default="AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG",
    help="Forward adaptor. Default = AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG")
    parser.add_argument(
    '-ra',
    default="AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
    help="Reverse adaptor. Default = AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT")
    parser.add_argument(
    '-o',
    default=None,
    help="Output file basename. Default = ./{basename}.*")

    args = parser.parse_args()

    infile = args.infile
    nread = int(args.n)
    readlen = int(args.readlen)
    inserlen = int(args.inserlen)
    lendev = int(args.lendev)
    a1 = args.fa
    a2 = args.ra
    outfile= args.o

    return(infile, nread, readlen, inserlen, lendev, a1, a2, outfile)

def get_basename(file_name):
    if ("/") in file_name:
        basename = file_name.split("/")[-1].split(".")[0]
    else:
        basename = file_name.split(".")[0]
    return(basename)

def reverse_complement(dna) :
    dna = dna.upper()
    '''
    Reverse complement a DNA string
    '''
    dna = dna[::-1]
    revcom = []
    complement = {"A" : "T", "T" : "A" , "G" : "C" , "C" : "G"}
    for letter in dna :
        for key in complement.keys() :
            if letter == key :
                revcom.append(complement[key])

    return "".join(revcom)

def read_fasta (file_name):
    """
    READS FASTA FILE, RETURNS SEQUENCE AS STRING
    INPUT:
        file_name(string): path to fasta file
    OUPUT:
        result(string): all of the sequences in fasta file, concatenated
    """
    result = ""
    with open(file_name, "r") as f:
        for line in f:
            if not line.startswith(">"):
                line = line.rstrip()
                result = result+line
    return([result, len(result)])

def random_insert(read_fasta_out, insert_lengths, read_length, minlen):
    genome = read_fasta_out[0]
    genome_length = read_fasta_out[1]
    result = []
    for i in insert_lengths:
        if i >= minlen:
            insert_start = npr.randint(0, genome_length-read_length)
            insert_end = insert_start + i + 1
            insert = genome[insert_start:insert_end]
            result.append(insert)
    return(result)

def complement_read(all_inserts, adaptor, read_length):
    result = []
    for insert in all_inserts:
        inlen = len(insert)
        if inlen < read_length:
            diff = read_length - inlen
            to_add = adaptor[0:diff]
            read = insert+to_add
        elif inlen == read_length:
            read = insert
        elif inlen > read_length:
            read = insert[0:read_length]
        result.append(read)
    return(result)

def write_fastq(all_reads, basename, orientation, read_length, outfile):
    if not outfile:
        with open(basename+"."+str(orientation)+".fastq", "w") as fw:
            for read in all_reads:
                fw.write("@"+basename+"\n")
                fw.write(read+"\n")
                fw.write("+\n")
                fw.write("d"*read_length+"\n")
    else:
        with open(outfile+"."+str(orientation)+".fastq", "w") as fw:
            for read in all_reads:
                fw.write("@"+basename+"\n")
                fw.write(read+"\n")
                fw.write("+\n")
                fw.write("d"*read_length+"\n")


def run_read_simulation(INFILE, NREAD, READLEN, INSERLEN, LENDEV, A1, A2, OUTFILE, MINLENGTH):
    print("INFILE", INFILE)
    print("NREAD", NREAD)
    print("READLEN", READLEN)
    print("INSERLEN", INSERLEN)
    print("LENDEV", LENDEV)
    print("A1", A1)
    print("A2", A2)
    print("OUTFILE", OUTFILE)

    basename = get_basename(INFILE)

    insert_lengths = [int(n) for n in npr.normal(INSERLEN, LENDEV, NREAD)]
    all_inserts = random_insert(read_fasta(INFILE), insert_lengths, READLEN, MINLENGTH)
    fwd_inserts = all_inserts
    rev_inserts = [reverse_complement(i) for i in all_inserts]
    fwd_reads = complement_read(fwd_inserts, A1, READLEN)
    rev_reads = complement_read(rev_inserts, A2, READLEN)

    write_fastq(fwd_reads, basename, 1, READLEN, OUTFILE)
    write_fastq(rev_reads, basename, 2, READLEN, OUTFILE)

if __name__ == "__main__":
    INFILE, NREAD, READLEN, INSERLEN, LENDEV, A1, A2, OUTFILE = _get_args()
    MINLENGTH = 20

    run_read_simulation(INFILE, NREAD, READLEN, INSERLEN, LENDEV, A1, A2, OUTFILE, MINLENGTH)
