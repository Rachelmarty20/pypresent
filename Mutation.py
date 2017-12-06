class Mutation:

    def __init__(self, id='mutationID', protein_sequence='', residue=0,
                 old_aa='', new_aa=''):
        '''
        Constructor for this class
        :return: Object
        '''
        # ID
        self.id = id
        # Protein sequence
        self.protein_sequence = protein_sequence
        # Residue number
        self.residue = residue
        # Old AA
        self.old_aa = old_aa
        # New AA
        self.new_aa = new_aa

    def create_native_peptides(self):
        '''

        :return:
        '''

    def get_best_rank(self, allele):
        '''

        :param allele:
        :return:
        '''

