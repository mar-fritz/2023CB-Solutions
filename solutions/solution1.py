from collections import Counter


def remove_duplicates(elements: list):
    """
    Function that detects duplicate elements in elements list
    :return: list of duplicate elements
    """
    # count occurrences of each element
    element_counts = Counter(elements)
    # add to solution letters which occurred more than one time
    # (Counter preserves insertion order, so order is preserved while iterating)
    return [element for element in element_counts if element_counts[element] > 1]
