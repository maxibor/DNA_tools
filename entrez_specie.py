#!/usr/bin/env python

import sys
from Bio import Entrez
import re

entrezid = sys.argv[1]
Entrez.email = "yours@email.com"
handle = Entrez.efetch(db="gene", id = entrezid, retmode = "text")

gbf = handle.read()
orga = re.findall(".*\[(.*)\]", gbf)
print(orga)[0]
