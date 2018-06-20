PyPresent
========
Quantified patient MHC presentation

Author: Rachel Marty <br>

Introduction
--------
PyPresent has been developed to improve the reproducibility of MHC-I and MHC-II presentation scores as seen in (Marty et al. 2017). It is a wrapper that is build around netMHCpan and netMHCIIpan. Users can get residue-centric presentation by single alleles and multi-allelic patients.

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
3. Update paths for NetMHCpan, NetMHCIIpan and a temporary directory in the config.py file.
4. Download python modules. 
5. Run example_usage.ipynb. The scores should be as follows:
	* HLA-A01:01 - 0.25
	* DRB1_1114 - 46.0
	* Patient MHCI - 1.810..
	* Patient MHCII - 5.379..

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
See example_usage.ipynb

Contact
------
ramarty [at] ucsd.edu

Citation
------
[Marty, Rachel, et al. "MHC-I genotype restricts the oncogenic mutational landscape." Cell 171.6 (2017): 1272-1283.] (https://www.cell.com/cell/fulltext/S0092-8674(17)31144-3)
