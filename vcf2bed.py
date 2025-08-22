#!/usr/bin/env python3

import pandas as pd
import io
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert VCF to BED format, while accounting for window around indels.")
    parser.add_argument("vcf", help="Input VCF file")
    parser.add_argument("chr_size", help="Chromosome sizes file")
    parser.add_argument("output_bed", help="Output BED file")
    parser.add_argument("--window", type=int, default=20000, help="Window size around indels (default: 20000)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    

    with open(args.vcf, 'r') as file:
        lines = [line for line in file if not line.startswith('##')]

    header_idx = next(i for i, line in enumerate(lines) if line.startswith('#CHROM'))
    header = lines[header_idx].lstrip('#').strip().split('\t')
    records = lines[header_idx + 1:]

    vcf = pd.read_csv(io.StringIO(''.join(records)), sep='\t', names=header)
    sizes = pd.read_csv(args.chr_size, sep='\t', header=None, names=['CHROM', 'SIZE'])

    vcf = vcf.merge(sizes, on='CHROM', how='left')
   
    if not all(col in vcf.columns for col in ["CHROM", "POS", 'REF', 'ALT']):
        raise ValueError("VCF file must contain 'CHROM' and 'POS' columns.")
    
    # Create BED format entries
    bed_dict = {
        "CHROM": [],
        "START": [],
        "END": [],
        "NAME": []
    }
    
    chr = vcf["CHROM"][0]
    pos = max(0, int(vcf["POS"][0]) - 1) # Convert POS to 0-based index
    start = max(0, pos - int(args.window / 2)  )
    chr_size = vcf["SIZE"][0]
    end = min(chr_size, pos + int(args.window / 2))
    for _chr, _pos, _chr_size in zip(vcf["CHROM"][1:], vcf["POS"][1:], vcf["SIZE"][1:]):
        #print(_chr, _pos)
        _pos = int(_pos) - 1  # Convert POS to 0-based index
        if _pos > start and _pos < end and _chr == chr:
            end = min(_chr_size, _pos + int(args.window / 2))
        else:
            bed_dict["CHROM"].append(chr)
            bed_dict["START"].append(start)
            bed_dict["END"].append(end)
            bed_dict["NAME"].append(f"{chr}:{start}-{end}")
            print(f"Adding {chr}:{start}-{end} for {_chr}:{_pos}:to bed_dict")
            start = max(0, _pos - int(args.window / 2))
            end = min(_chr_size, _pos + int(args.window / 2))
            chr = _chr
    bed_dict["CHROM"].append(chr)
    bed_dict["START"].append(start)
    bed_dict["END"].append(end)
    bed_dict["NAME"].append(f"{chr}:{start}-{end}")
    
    with open(args.output_bed, "w") as bed_file:
        for chrom, start, end, name in zip(bed_dict["CHROM"], bed_dict["START"], bed_dict["END"], bed_dict["NAME"]):
            bed_file.write(f"{chrom}\t{start}\t{end}\t{name}\n")

if __name__ == "__main__":
    main()