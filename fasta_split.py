#!/usr/bin/env python

import argparse
import numpy as np


def _get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
        prog='fasta_split',
        description='Splitting a fasta file into shorter sequences')
    parser.add_argument('fasta', help="path to input fasta file")
    parser.add_argument(
        '-p',
        default=8,
        help="n parameter for Negative insert length distribution. Default= 8")
    parser.add_argument(
        '-m',
        default=800,
        help="Mode of the negative binomial distribution. Default=800")
    parser.add_argument(
        '-o',
        dest="output",
        default=None,
        help="Output file basename. Default = {basename}.splitted.fa")

    args = parser.parse_args()

    infile = args.fasta
    NBINOM = int(args.p)
    CLEN = int(args.m)
    outfile = args.output

    return(infile, NBINOM, CLEN, outfile)


def get_basename(file_name):
    if ("/") in file_name:
        basename = file_name.split("/")[-1].split(".")[0]
    else:
        basename = file_name.split(".")[0]
    return(basename)


if __name__ == "__main__":
    INFILE, NBINOM, CLEN, OUTFILE = _get_args()

    basename = get_basename(INFILE)
    prob = NBINOM / (NBINOM + CLEN)


    if not OUTFILE:
        OUTFILE = basename + ".splitted.fa"

    fastadict = {}
    split_dict = {}
    with open(INFILE, "r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                seqname = line
                fastadict[seqname] = []
            else:
                fastadict[seqname].append(line)

    for seqname in fastadict:
        i = 0
        seq = fastadict[seqname]
        in_contig = True
        cstart = 0
        while in_contig:
            contig_length = min(len(seq) - cstart, np.random.negative_binomial(NBINOM, prob))
            split_dict[f"{seqname.replace(' ','_')}_{i}_len_{contig_length}"] = seq[cstart:cstart+contig_length]
            cstart += contig_length
            i += 1
            if cstart >= len(seq):
                in_contig = False

    with open(OUTFILE, "w") as fw:
        for seq in split_dict:
            fw.write(seq + "\n")
            fw.write("\n".join(split_dict[seq]) + "\n")
