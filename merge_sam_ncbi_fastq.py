import sys

fastq = sys.argv[1]
sam = sys.argv[2]

def get_basename(samfile_name):
    if ("/") in samfile_name:
        basename = samfile_name.split("/")[-1].split(".")[0]
    else:
        basename = samfile_name.split(".")[0]
    return(basename)

seqdata = {}
with open(fastq, "r") as f1:
    for line in f1:
        print(line)
        line = line.rstrip()
        if line.startswith("@SRR"):
            seqname = line
            seqdata[seqname] = []
        else:
            seqdata[seqname].append(line)

basename = get_basename(sam)

with open(basename+".rg.sam", "w") as f3:
    with open(sam,"r") as f2:
        for line in f2:
            line = line.rstrip()
            splitline = line.split("\t")
            rname = splitline[0]
            for akey in seqdata.keys():
                if rname in akey:
                    #print("\t".join(splitline))
                    f3.write("".join(akey.split()[1:-1])+" "+"\t".join(splitline[1:])+"\n")
