from allele import Allele
from scoring import single, multi
from affinities import mhcI, mhcII

class Patient:

    '''
    This class creates a patient object that is defined by its six alleles
    and
    '''

    def __init__(self, alleles, id='SampleID'):
        '''
        Constructor from a file or from a list
        :return: Object
        '''
        # PatientID
        self.id = id

        # Get types as Allele objects
        self.hla_types = [Allele(a) for a in alleles]

    def print_hla_types(self):
        '''
        Prints the HLA types for a patient
        :return: None
        '''
        for hla in self.hla_types:
            print hla.id

    def patient_score(self, mutation, allele_scoring_function='best_rank',
                      patient_scoring_function='best_rank', software='netMHCpan30'):
        """
        Calculation of a residue centric presentation score for
        a patient
        :param mutation: A mutation object
        :param allele_scoring_function: from scoring.single
        :param patient_scoring_function: from scoring.multi
        :param software: from affinities.mhcI or affinities.mhcII
        :return: a presentation score
        """

        # Run the affinity prediction
        allele_scores = []
        for hla in self.hla_types:
            if software == 'netMHCpan30':
                affinity_data_file = mhcI.run_netmhcpan30(hla, mutation)
            else:
                raise Exception('Please select an available software.')

            # Consolidate into a score
            if allele_scoring_function == 'best_rank':
                allele_scores.append(single.best_rank(affinity_data_file, mutation))
            else:
                raise Exception('Please select an available single-allelic scoring function.')

        if patient_scoring_function == 'best_rank':
            score = multi.best_rank(allele_scores)
        else:
            raise Exception('Please select an available multi-allelic scoring function.')

        return score