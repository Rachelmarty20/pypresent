from allele import Allele
from scoring import single, multi
from affinities import mhcI, mhcII

ALLELES_I = ['HLA-A01:01', 'HLA-A01:01', 'HLA-B07:02', 'HLA-B07:02', 'HLA-C01:02', 'HLA-C01:02']
ALLELES_II = []


class Patient:

    '''
    This class creates a patient object that is defined by its six alleles
    and
    '''

    # TODO: This is currently confusing. Need default options for both classes.
    def __init__(self, alleles_I, alleles_II, id='SampleID'):
        '''
        Constructor from a file or from a list
        :return: Object
        '''
        # PatientID
        self.id = id

        # Get types as Allele objects
        self.hla_I_types = [Allele(a, 'I') for a in alleles_I]
        self.hla_II_types = [Allele(a, 'II') for a in alleles_II]

    def print_hla_types(self):
        '''
        Prints the HLA types for a patient
        :return: None
        '''
        for hla in self.hla_I_types:
            print hla.id
        for hla in self.hla_II_types:
            print hla.id

    def patient_score(self, mutation, mhc_class='I',
                      allele_scoring_function='best_rank',
                      patient_scoring_function='harmonic_mean',
                      software='netMHCpan30'):
        """
        Calculation of a residue centric presentation score for
        a patient
        :param mutation: A mutation object
        :param allele_scoring_function: from scoring.single
        :param patient_scoring_function: from scoring.multi
        :param software: from affinities.mhcI or affinities.mhcII
        :return: a presentation score
        """

        # TODO: speed this up by running all at once
        # Run the affinity prediction
        allele_scores = []
        if mhc_class == 'I':
            types = self.hla_I_types
        else:
            types = self.hla_II_types
        for hla in types:
            if mhc_class == 'I':
                affinity_data_file = mhcI.run_netmhcpan30(hla, mutation)
            elif mhc_class == 'II':
                affinity_data_file = mhcII.run_netmhcIIpan31(hla, mutation)
            else:
                raise Exception('Please select an available software.')

            # Consolidate into a score
            if allele_scoring_function == 'best_rank':
                allele_scores.append(single.best_rank(affinity_data_file, mutation,
                                                      mhc_class=mhc_class))
            elif allele_scoring_function == 'harmonic_mean':
                allele_scores.append(single.harmonic_mean(affinity_data_file, mutation,
                                                          mhc_class=mhc_class))
            else:
                raise Exception('Please select an available single-allelic scoring function.')

        if patient_scoring_function == 'best_rank':
            score = multi.best_rank(allele_scores)
        elif patient_scoring_function == 'harmonic_mean':
            score = multi.harmonic_mean(allele_scores)
        elif patient_scoring_function == 'geometric_mean':
            score = multi.geometric_mean(allele_scores)
        else:
            raise Exception('Please select an available multi-allelic scoring function.')

        return score