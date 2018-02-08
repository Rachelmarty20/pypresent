'''
A mutation class to center the residue-centric presentation scores.

Two ways to create a Mutation object:
1. Through direct peptide input
2. Through the human Ensembl database (this will be implemented later)

Will implement native and MHC-II mutation capabilities as well.
'''

import time
from Bio import SeqIO


PATH_TO_ENSEMBL_REF = '/cellar/users/ramarty/Data/hla_ii/' \
                       + 'references/Homo_sapiens.GRCh38.pep.all.fa'
TEMP_DIR = '/cellar/users/ramarty/Data/pypresent/tmp'
INPUT_FASTA_LENGTH = 21 # this is only for class I


class Mutation:

    def _get_protein_sequence(self):
        """
        Get the protein sequence from the fasta file
        :return: None
        """
        fasta_sequences = SeqIO.parse(open(self.gene_fasta_file),'fasta')
        sequence = fasta_sequences.next().seq.tostring()
        return sequence

    def _verify_matching_protein(self, native_aa):
        """
        Check that old_aa is what it should be
        :return: True if protein matches, False otherwise
        """

    def _create_mutated_input_fasta(self, MHC_class='I'):
        """
        Creating a mutated fasta file for affinity prediction in tmp directory
        :return: None
        """
        # Create output file name
        output_file = '{0}{1}_{2}'.format(TEMP_DIR, self.id, str(time.time()).split('.')[0])
        self.restricted_fasta_file = output_file

        # TODO: make this account for both classes
        y = 10 # this will need to get updated
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
            self.short_mutated_sequence = mutated_sequence[start+1:end+2]

        else:
            raise Exception('Residue does not exist in the protien.')

    def __init__(self, gene_fasta_file, residue, aa, id='mutationID',
                 native_aa=None, native=False):
        """
        Constructor for direct peptide input
        :return: Object
        """
        # Protein sequence
        self.gene_fasta_file = gene_fasta_file
        # Residue number
        self.residue = residue
        # New AA
        self.aa = aa
        # ID
        self.id = id

        # Get sequence
        self.sequence = self._get_protein_sequence()

        # Create prepped output file
        self._create_mutated_input_fasta()

    def get_peptides_containing_residue(self, MHC_class='I'):
        """
        Return the substrings of self.short_mutated_sequence containing the residue
        :return: A list of peptides
        """

        if MHC_class == 'I':
            # Return lengths 8, 9, 10, 11
            None

        else:
            # Return lengths 15
            None
