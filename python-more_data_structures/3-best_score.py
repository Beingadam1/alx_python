def best_score(a_dictionary):
    # check if the dict is empty, return None if yes.
    if a_dictionary is None:
        return None

    # use max to find the highest value and return None if it empty.
    b_score = max(a_dictionary.values(), default=None)

    # loop over the dict to check if the current iteration is equal to b_score and return the key.
    for key, value in a_dictionary.items():
        if value == b_score:
            return key