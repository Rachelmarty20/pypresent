'''
Calls affinity prediction tools for MHC-I

All output should be in the form of a dataframe with the following columns:
peptide, rank

'''

import os
import time
import random
import string
import pandas as pd

import config

NETMHCPAN30_PATH, TEMP_DIR = config.setup_MHCI()

def run_netmhcpan30(allele, mutation):
    """
    To run netMHCpan3.0 and return a cleaned dataframe
    :param allele: an Allele object
    :param mutation: a Mutation object
    :return: A cleaned output dataframe path
    """
    # create unique identifier
    raw_identifier = ''.join(random.choice(list(string.ascii_uppercase + string.digits)) for _ in range(6))
    raw_affinities_file = '{0}raw_affinities.{1}_{2}'.format(TEMP_DIR, mutation.id,
                                                         raw_identifier)
    
    trash_file = '{0}trash.{1}_{2}'.format(TEMP_DIR, mutation.id,
                                                         raw_identifier)

    # Run command
    cmd = '{0} -a {1} -f {2} -xls -xlsfile {3} > {4}'.format(NETMHCPAN30_PATH,
                                                                   allele.id,
                                                                   mutation.restricted_fasta_fileI,
                                                                    raw_affinities_file,
                                                                    trash_file)
    os.system(cmd)

    # Alter output file
    df = pd.read_csv(raw_affinities_file, sep='\t',
               header=1)
    df = df[['Peptide', 'Rank']]

    # TODO: Reduce to the peptides containing the residue

    df = df[df.Peptide.isin(mutation.peptidesI)]

    # Save re-formatted output file
    formatted_affinities_file = os.path.join(TEMP_DIR, 'formatted_affinities.{0}_{1}'.format(mutation.id, raw_identifier))

    df.to_csv(formatted_affinities_file)
    return formatted_affinities_file
