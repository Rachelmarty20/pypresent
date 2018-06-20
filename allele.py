from scoring import single
from affinities import mhcI, mhcII

class Allele:

    '''
    This class is for all of the functions concerning alleles.

    '''

    def __init__(self, id=None, mhc_class=None, file_in=''):
        """
        Constructor for this class.
        :param id:
        :param file_in:
        :return:
        """
        # allele
        if (id is not None) and (mhc_class is not None):
            # TODO: add appropriate formatting or check (ex. HLA-C14:09)
            self.id = id
            self.mhc_class = mhc_class
        else:
            try:
                self.id = open(file_in).readline().strip()
                self.id = id
                self.mhc_class = mhc_class
            except NameError:
                print("Please specificy an allele name or an input file.")


    def allele_score(self, mutation, scoring_function='best_rank'):
        """
        Calculation of a residue centric presentation score for
        a single allele
        :param mutation:
        :param scoring_function: the scoring function used to
                consolidate the affinities
        :param software: the software used to call the affinities
        :return: score
        """

        # Run the affinity prediction
        if self.mhc_class == 'I':
            software = 'netMHCpan30'
            affinity_data_file = mhcI.run_netmhcpan30(self, mutation)
        elif self.mhc_class == 'II':
            software = 'netMHCIIpan31'
            affinity_data_file = mhcII.run_netmhcIIpan31(self, mutation)
        else:
            raise Exception('Please select a class with an available software.')

        # Consolidate into a score
        if scoring_function == 'best_rank':
            score = single.best_rank(affinity_data_file, mutation, mhc_class=self.mhc_class)
        else:
            raise Exception('Please select an available scoring function.')

        return score