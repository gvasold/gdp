"These module contains some additional functions for string manipulation."



def reverse(s):
    "Reverts string s."
    return s[::-1]


def distinct_len(s):
    "Counts number of distinct chars in string s."
    return len(set(s))
