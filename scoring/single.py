import pandas as pd
import scipy.stats as sp


def _import_dataframe(affinity_data_file, mutation, mhc_class='I'):
    """
    Import a dataframe with two columns: Peptide and Rank.
    :param affinity_data_file:
    :param mutation:
    :param mhc_class:
    :return:
    """

    # Import data frame
    df = pd.read_csv(affinity_data_file, index_col=0)

    # Restrict to peptides containing mutation
    peptides = mutation.get_peptides_containing_residue(mhc_class)
    df = df[df.Peptide.isin(peptides)]
    return df

def best_rank(affinity_data_file, mutation, mhc_class='I'):
    """
    Import a dataframe with two columns: Peptide and Rank.
    Return the minimum rank containing the residue.
    :param affinity_data_file: location of file with affinity data
    :return: A best rank score
    """

    df = _import_dataframe(affinity_data_file, mutation, mhc_class)

    # Return the minimum
    return min(df.Rank)


def harmonic_mean(affinity_data_file, mutation, mhc_class='I'):
    """
    Import a dataframe with two columns: Peptide and Rank.
    Return the harmonic mean rank containing the residue.
    :param affinity_data_file: location of file with affinity data
    :return: A best rank score
    """

    df = _import_dataframe(affinity_data_file, mutation, mhc_class)

    # Return the minimum
    return sp.hmean(df.Rank)
