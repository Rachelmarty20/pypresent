'''
Calls affinity prediction tools for MHC-I

All output should be in the form of a dataframe with the following columns:
peptide, rank

'''

import os
import time
import string
import random
import pandas as pd

import config

NETMHCIIPAN31_PATH, TEMP_DIR = config.setup_MHCII()

def run_netmhcIIpan31(allele, mutation):
    """
    To run netMHCIIpan3.1 and return a cleaned dataframe
    :param allele: an Allele object
    :param mutation: a Mutation object
    :return: A cleaned output dataframe path
    """
    # create unique identifier
    raw_identifier = ''.join(random.choice(list(string.ascii_uppercase + string.digits)) for _ in range(6))
    raw_affinities_file = os.path.join(TEMP_DIR, 'raw_affinities.{0}_{1}'.format(mutation.id, raw_identifier))


    trash_file = os.path.join(TEMP_DIR, 'trash.{0}_{1}'.format(mutation.id, raw_identifier))

    # Run command
    cmd = '{0} -a {1} -f {2} -xls -xlsfile {3} > {4}'.format(NETMHCIIPAN31_PATH,
                                                                   allele.id,
                                                                   mutation.restricted_fasta_fileII,
                                                                    raw_affinities_file,
                                                                    trash_file)
    os.system(cmd)

    # Alter output file
    df = pd.read_csv(raw_affinities_file, sep='\t',
               header=1)
    df = df[['Peptide', 'Rank']]

    # TODO: Reduce to the peptides containing the residue

    df = df[df.Peptide.isin(mutation.peptidesII)]

    # Save re-formatted output file
    formatted_affinities_file = os.path.join(TEMP_DIR, 'formatted_affinities.{0}_{1}'.format(mutation.id, raw_identifier))

    df.to_csv(formatted_affinities_file)
    return formatted_affinities_file
