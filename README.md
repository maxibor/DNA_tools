##DNA TOOLS

####A set of tools for to play with/analyze genomics data
- **random_dna.py** : creates a random sequence of DNA of length K 

	usage : `python random_dna.py K`
- **fasta_length.py** : computes the length of DNA sequences in a Fasta file
	
	usage : `python fasta_length.py file.fa`
- **reverse_complement.py** : computes the revese complement of a DNA sequence

	usage : `python reverse_complement.py CGGGTA`

-
	
To add the tools to your command prompt, use aliases in your `~/.bash_profile` file

``` 
alias revcom="python path/to/reverse_complement.py"
alias fasta_len="python path/to/fasta_length.py"
```

Save it and reload it with `source .bash_profile`

Now you can access the DNA tools from any location in the terminal, for example :

```
betsy:~ Maxime$ revcom CGGGTA
TACCCG
```