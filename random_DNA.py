from __future__ import division

'''
random DNA string generator
'''
from random import *
from collections import Counter
import sys
try :
    length = int(sys.argv[1])
    mydna = []
    for i in range(0, length) :
        random_letter = random()
        if random_letter < 0.25 :
            mydna.append("A")
        elif random_letter >= 0.25 and random_letter < 0.5 :
            mydna.append("T")
        elif random_letter >= 0.5 and random_letter < 0.75 :
            mydna.append("G")
        else :
            mydna.append ("C")

    print "".join(mydna)
    stats = Counter(mydna)
    print "-Statistics-"
    for key in stats.keys() :
        print str(key)+ ":"+str(int(((stats[key])/length)*100))+"%"
except IndexError :
    print "Please specify the length of your desired random DNA molecule. \npython random_DNA.py YourLength"
except ValueError :
    print "Please enter a valid value for the length."
