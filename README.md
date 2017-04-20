## DNA TOOLS

#### A set of tools for to play with/analyze genomics data
- **random_dna.py** : creates a random sequence of DNA of length K

	usage : `python random_dna.py K`
- **fasta_length.py** : computes the length of DNA sequences in a Fasta file

	usage : `python fasta_length.py file.fa`
- **reverse_complement.py** : computes the revese complement of a DNA sequence

	usage : `python reverse_complement.py CGGGTA`
- **faStats.py** : compute sequence length of all sequences in a fasta file

	usage : `python faStats.py file.fa`

- **melting_temp.py** : compute melting temperature of a sequence

	usage : `melting_temp.py DnaSequence`

- **entrez_specie.py** : returns the specie/organism name given an ENTREZ id.  
	usage : `python entrez_specie.py 1567`


------------

#### To add the tools to your command prompt :
- **Option 1 :** use aliases in your `~/.bash_profile` or `~/.bashrc`  file to add each tool one by one

*example :*
```
echo "alias revcom=python path/to/reverse_complement.py" >> ~/.bash_profile
source ~/.bash_profile
```


- **Option 2 :** Add all the DNA tools at once to your $PATH variable environment variable (replace the location of dna tools directory)

*example :*
```
echo "export PATH=/path/to/dna/tools/directory/:$PATH" >> ~/.bashrc
source ~/.bashrc
```
