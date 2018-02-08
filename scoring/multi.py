

def best_rank(allele_scores):
    """
    Determine the best rank score from the patient's alleles.
    :param allele_scores: List of scores for patient's six alleles
    :return: A best rank score
    """

    # Return the minimum
    return min(allele_scores)
