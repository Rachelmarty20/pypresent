'''
Calls affinity prediction tools for MHC-I

All output should be in the form of a dataframe with the following columns:
peptide, rank

'''

import os
import time
import pandas as pd

NETMHCIIPAN31_PATH = '/cellar/users/ramarty/programs/netMHCIIpan-3.1/netMHCIIpan'
TEMP_DIR = '/cellar/users/ramarty/Data/pypresent/tmp/'


def run_netmhcIIpan31(allele, mutation):
    """
    To run netMHCIIpan3.1 and return a cleaned dataframe
    :param allele: an Allele object
    :param mutation: a Mutation object
    :return: A cleaned output dataframe path
    """
    # create unique identifier
    raw_affinities_file = '{0}raw_affinities.{1}_{2}'.format(TEMP_DIR, mutation.id,
                                                         str(time.time()).split('.')[0])

    # Run command
    cmd = '{0} -a {1} -f {2} -xls -xlsfile {3}'.format(NETMHCIIPAN31_PATH,
                                                                   allele.id,
                                                                   mutation.restricted_fasta_fileII,
                                                                    raw_affinities_file)
    os.system(cmd)

    # Alter output file
    df = pd.read_csv(raw_affinities_file, sep='\t',
               header=1)
    df = df[['Peptide', 'Rank']]

    # Save re-formatted output file
    formatted_affinities_file = '{0}formatted_affinities.{1}_{2}'.format(TEMP_DIR, mutation.id,
                                                         str(time.time()).split('.')[0])
    df.to_csv(formatted_affinities_file)
    return formatted_affinities_file