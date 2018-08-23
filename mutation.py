'''
A mutation class to center the residue-centric presentation scores.

Two ways to create a Mutation object:
1. Through direct peptide input
2. Through the human Ensembl database (this will be implemented later)

Will implement native and MHC-II mutation capabilities as well.
'''

import time
# May want to work around this to avoid the import
from Bio import SeqIO


PATH_TO_ENSEMBL_REF = '/cellar/users/ramarty/Data/hla_ii/' \
                       + 'references/Homo_sapiens.GRCh38.pep.all.fa'
TEMP_DIR = '/cellar/users/ramarty/Data/pypresent/tmp/'
INPUT_FASTA_EXTENSION_I = 10 # class I
INPUT_FASTA_EXTENSION_II = 14 # class II


class Mutation:

    def _get_protein_sequence(self):
        """
        Get the protein sequence from the fasta file
        :return: None
        """
        fasta_sequences = SeqIO.parse(open(self.gene_fasta_file),'fasta')
        sequence = str(fasta_sequences.next().seq)
        return sequence

    def _verify_matching_protein(self):
        """
        Check that old_aa is what it should be
        :return: True if protein matches, False otherwise
        """
        if self.native_aa == None:
            return True
        else:
            if self.sequence[self.residue-1] == self.native_aa:
                return True
            else:
                return False

    # TODO: Only need to create the class II fasta file because it will encompass all class I peptides
    def _create_mutated_input_fasta(self):
        """
        Creating a mutated fasta file for affinity prediction in tmp directory
        :return: None
        """
        # Create output file name


        for y in [INPUT_FASTA_EXTENSION_I, INPUT_FASTA_EXTENSION_II]:
            output_file = '{0}{1}_{2}'.format(TEMP_DIR, self.id, str(time.time()).split('.')[0])
            if y == INPUT_FASTA_EXTENSION_I:
                self.restricted_fasta_fileI = output_file
                mhc_class = 'I'
            else:
                self.restricted_fasta_fileII = output_file
                mhc_class = 'II'
            # Make peptide sequence with mutation and output
            if len(self.sequence) >= self.residue: #(not accurate for random)
                mutated_sequence = self.sequence[:self.residue] \
                                   + self.aa + self.sequence[self.residue+1:]
                # specify start and end
                if (self.residue-1) - y >= 0:
                    start = (self.residue-1) - y
                else:
                    start = -1

                if (self.residue-1) + y <= len(self.sequence)-1:
                    end = (self.residue-1) + y
                else:
                    end = len(self.sequence) - 2

                # Output to tmp file
                with open(output_file, 'w') as f:
                    f.write('>gi {0}\n'.format(self.id))
                    f.write(mutated_sequence[start+1:end+2])
                if y == INPUT_FASTA_EXTENSION_I:
                    self.short_mutated_sequenceI = mutated_sequence[start+1:end+2]
                else:
                    self.short_mutated_sequenceII = mutated_sequence[start+1:end+2]

            else:
                raise Exception('Residue does not exist in the protien.')

    def __init__(self, residue, aa, from_file=True, gene_fasta_file='', gene_sequence='',
                 id='mutationID', native_aa=None, native=False):
        """
        Constructor for direct peptide input
        :return: Object
        """
        # Protein sequence
        if from_file:
            self.gene_fasta_file = gene_fasta_file
            self.sequence = self._get_protein_sequence()
        else:
            self.sequence = gene_sequence

        # Residue number
        self.residue = residue
        # Old AA
        self.native_aa = native_aa
        if self._verify_matching_protein() == False:
            print "Native amino acid does not match given protein."
        # New AA
        self.aa = aa
        # ID
        self.id = id

        # Create prepped output file
        self._create_mutated_input_fasta()

    def get_peptides_containing_residue(self, mhc_class='I'):
        """
        Return the substrings of self.short_mutated_sequence containing the residue
        :return: A list of peptides
        """

        if mhc_class == 'I':
            # Return lengths 8, 9, 10, 11
            peptides = []
            pos = 11
            for kmer in [8,9,10,11]:
                for i in range(len(self.short_mutated_sequenceI) - (kmer-1)):
                    start = i
                    end = i + kmer
                    if pos >= start and pos <= end:
                        peptides.append(self.short_mutated_sequenceI[start:end])

        else: # MHC class II
            # Return lengths 15
            peptides = []
            pos = 15
            for kmer in [15]:
                for i in range(len(self.short_mutated_sequenceII) - (kmer-1)):
                    start = i
                    end = i + kmer
                    if pos >= start and pos <= end:
                        peptides.append(self.short_mutated_sequenceII[start:end])

        return peptides
