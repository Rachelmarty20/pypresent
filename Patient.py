class Patient:
    def __init__(self, id='SampleID'):
        '''
        Constructor for this class.
        :return: Object
        '''
        # PatientID
        self.id = id


    def import_hla_types_from_file(self, file_in):
        '''
        Imports patient HLA types from a file
        :param file_in: path to the file with types (new-line separated)
        :return: None
        '''
        self.hla_types = [x.strip() for x in open(file_in).readlines()]


    def import_hla_types_from_list(self, list):
        '''
        Imports patient HLA types from a list
        :param list: List of HLA types
        :return: None
        '''
        self.hla_types = list


    def print_hla_types(self):
        '''
        Prints the HLA types for a patient
        :return: None
        '''
        for hla in self.hla_types:
            print hla

    def get_PHBR(self, mutation):
        '''
        Calculates PHBR score for a specific mutation
        :param mutation: a Mutation instance
        :return: a float (PHBR score)
        '''


    def get_PHBRs(self, mutations):
        '''
        Calculates PHBR scores for a list of mutations
        :param mutations: a list of Mutation instances
        :return: a list of floats (PHBR scores)
        '''