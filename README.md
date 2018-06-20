PyPresent
========
Quantified patient MHC presentation

Author: Rachel Marty <br>

Introduction
--------


Requirements 
---------
PyPresent uses the following software:

1. [NetMHCpan-3.0](http://www.cbs.dtu.dk/services/NetMHCpan-3.0/)
2. [NetMHCIIpan-3.1](http://www.cbs.dtu.dk/services/NetMHCIIpan-3.1/)

*Licensed only for academic use*

And the following Python modules:

1. [Pandas](https://pandas.pydata.org/)
2. [Scipy](https://www.scipy.org/)
3. [Bio](https://biopython.org/)

*[Anaconda](https://www.anaconda.com/download) makes downloading the python modules easy*

Setup 
---------
1. Clone repository locally.
2. Download NetMHCpan and NetMHCIIpan. 
3. Add paths.
4. Download python modules. 


Inputs needed for scores
------
###Single-Allelic Score (Best Rank)
* MHC-I/MHC-II allele
* Mutation information:
	* Gene sequence - *string or fasta file*
	* Residue position
	* New amino acid

###Multi-Allellic Score (PHBR)
* All MHC-I/MHC-II alleles
* Mutation information:
	* Gene sequence
	* Residue position
	* New amino acid

Test examples
------
See example_usage.ipyn

Contact
------
ramarty [at] ucsd.edu

Citation
------
[Marty, Rachel, et al. "MHC-I genotype restricts the oncogenic mutational landscape." Cell 171.6 (2017): 1272-1283.] (https://www.cell.com/cell/fulltext/S0092-8674(17)31144-3)
