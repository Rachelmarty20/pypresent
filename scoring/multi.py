import scipy.stats as sp


def best_rank(allele_scores):
    """
    Determine the best rank score from the patient's alleles.
    :param allele_scores: List of scores for patient's six alleles
    :return: A best rank score
    """

    # Return the minimum
    return min(allele_scores)


def harmonic_mean(allele_scores):
    """
    Determine the harmonic mean score from the patient's alleles.
    :param allele_scores: List of scores for patient's six alleles
    :return: A harnmonic mean rank score
    """

    # Return the harmonic mean
    return sp.hmean(allele_scores)


def geometric_mean(allele_scores):
    """
    Determine the geometric mean score from the patient's alleles.
    :param allele_scores: List of scores for patient's six alleles
    :return: A geometric mean score
    """

    # Return the harmonic mean
    return sp.mstats.gmean(allele_scores)

