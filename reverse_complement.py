import sys

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

print (reverse_complement(sys.argv[1]))
