## DNA TOOLS

#### A set of tools for to play with/analyze genomics data

- **random_dna.py** : creates a random sequence of DNA of length K

    usage : `python random_dna.py K`

- **fasta_length.py** : computes the length of DNA sequences in a Fasta file

    usage : `python fasta_length.py file.fa`

- **reverse_complement.py** : computes the revese complement of a DNA sequence

    usage : `python reverse_complement.py CGGGTA`

- **faStats** : compute sequence length of all sequences in a fasta file

    usage : `python faStats file.fa`

- **melting_temp.py** : compute melting temperature of a sequence

    usage : `melting_temp.py DnaSequence`

- **entrez_specie.py** : returns the specie/organism name given an ENTREZ id.

    usage : `python entrez_specie.py 1567`

- **fastq_split.py** : splits a merged paired-end Illumina `{basename}.fastq` (or compressed `fastq.gz`) file in `{basename}.R1.fastq` and `{basename}.R2.fastq`

    usage : `python fastq_split.py paired_end_file.fastq`

- **centrifuge2krona** : converts a [centrifuge](https://github.com/infphilo/centrifuge) output file to a [krona](https://github.com/marbl/Krona/wiki) visualisation using `centrifuge-kreport` and `ktImportTaxonomy`.

    usage : `centrifuge2krona centrifuge_file.out`

- **sam_filter** : filters a sam file on identity percentage and alignment length.

    usage: `sam_filter file.sam`

- **bam_filter** : filters a bam file on identity percentage

    usage: `bam_filter file.bam`

- **filterFastaByLength** : filters a fasta file on sequence length (min and max)

    usage: `filterFastaByLength -min 1 -max 66 file.fa`

- **krakenTometaphlan** : converts a [Kraken] style report to a [Metaphlan] style report

    usage: `krakenTometaphlan -o metaphlan_report.txt kraken_report.txt`

- **consensusMaker** : creates a consensus fasta from a samtools mpileup file

    usage : `consensusMaker -o myconsensus.fa infile.mpileup`

- **bed2coverage** : computes the 10th percentile coverage for each feature in a `BED` file

    usage : `bed2coverage infile.bed`

- **filterFastaByName**: filters a **fasta** file given a list of sequence names

    usage : `filterFastaByName infile.fasta seqnames_to_keep.txt -o outfile.fa`

- **eslfasta2fastq**: Extracts the headers of fasta file formatted by Easel ([hmmer](http://hmmer.org/) toolkit) and get the matching fastq records
-  
    usage : `eslfasta2fastq fasta_input forward.fq -fq2 reverse.fq`

- **parallel_download**: Download files from a list of files (on file per line) in a parallel fashion using multiprocessing, and subprocess calling wget
  
    usage: `parallel_download list_of_files.txt`

- **fasta_split**: Splits fasta sequences in shorter sequences, using a negative binomial distribution
    usage: `python fasta_split.py -m 800 input_sequences.fa`

- **compare_fasta_seqs**: Compare two or more sequences in a fasta file
    usage: `compare_fasta_seqs multifasta.fa`

* * *

#### To add the tools to your command prompt

- **Option 1 :** use aliases in your `~/.bash_profile` or `~/.bashrc`  file to add each tool one by one  (replace `/path/to/DNA_tools/` with the location of the tool)

_example :_

    echo "alias revcom=python /path/to/DNA_tools/reverse_complement.py" >> ~/.bashrc
    source ~/.bashrc

- **Option 2 :** Add all the DNA tools at once to your `$PATH` environment variable (replace `/path/to/` with the location of the `DNA_tools` directory)

_example :_

    echo "export PATH=$PATH:/path/to/DNA_tools/" >> ~/.bashrc
    source ~/.bashrc
