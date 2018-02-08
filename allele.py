from scoring import single, multi
from affinities import mhcI, mhcII

class Allele:

    '''
    This class is for all of the functions concerning alleles.

    '''

    def __init__(self, id=None, file_in=''):
        """
        Constructor for this class.
        :param id:
        :param file_in:
        :return:
        """
        # allele
        if id is not None:
            self.id = id
        else:
            try:
                self.id = open(file_in).readline().strip()
            except NameError:
                print("Please specificy an allele name or an input file.")


    # TODO: add a default scoring fuction
    def allele_score(self, mutation, scoring_function, software):
        """
        Calculation of a residue centric presentation score for a single allele
        :param mutation:
        :param scoring_function:
        :param software:
        :return:
        """

        # Run the affinity prediction
        affinity_data_file = mhcI.(self, mutation)

        # Consolidate into a score
        single.best_rank(affinity_data_file, mutation)
