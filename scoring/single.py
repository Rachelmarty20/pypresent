import pandas as pd


def best_rank(affinity_data_file, mutation, MHC_class='I'):
    """
    Import a dataframe with two columns: Peptide and Rank.
    Return the minimum rank containing the residue.
    :param affinity_data_file: location of file with affinity data
    :return: A best rank score
    """

    # Import data frame
    df = pd.read_csv(affinity_data_file, index_col=0)

    # Restrict to peptides containing mutation
    peptides = mutation.get_peptides_containing_residue(MHC_class)
    df = df[df.Peptide.isin(peptides)]

    # Return the minimum
    return min(df.Rank)

