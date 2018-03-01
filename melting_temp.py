#!/usr/bin/env python
import sys
#Calculation of sequence melting temperature
#Author : Maxime Borry
#Contact : maxime.borry@gmail.com
#Usage : melting_temp.py sequence

seq = str(sys.argv[1])

def short_formula(dna_seq) :
    dna_seq = dna_seq.upper()
    '''
    Melting temperature calculation for sequence strictly shorter than 14 nucleotides
    '''
    nA = dna_seq.count("A")
    nC = dna_seq.count("C")
    nG = dna_seq.count("G")
    nT = dna_seq.count("T")

    Tm = (nA+nT) * 2 + (nG+nC) * 4
    return(round(Tm,2))

def long_formula (dna_seq) :
    '''
    Melting temperature calculation for sequence strictly longer than 13 nucleotides
    '''
    dna_seq = dna_seq.upper()
    nA = dna_seq.count("A")
    nC = dna_seq.count("C")
    nG = dna_seq.count("G")
    nT = dna_seq.count("T")

    Tm = 64.9 +41*(nG+nC-16.4)/(nA+nT+nG+nC)
    return(round(Tm,2))

if len(seq) < 14 :
    Tm = str(short_formula(seq))
    print ("Sequence : "+seq)
    print ("Melting temperature : "+Tm+" degC")
    print (" Warning : This software doesn't take into account degenarated bases")
    print ("Melting temperature calculated for the following conditions")
    print ("50 nM primer, 50 mM Na+, and pH 7.0")
elif len(seq) > 13 :
    Tm = str(long_formula(seq))
    print ("Sequence : "+seq)
    print ("Melting temperature : "+Tm+" degC")
    print ("Warning : This software doesn't take into account degenarated bases")
    print ("Melting temperature calculated for the following conditions")
    print ("50 nM primer, 50 mM Na+, and pH 7.0")
else :
    print ("Error in sequence, please check your input")
