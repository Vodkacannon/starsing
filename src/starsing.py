# Some of these functions may be reinventing the wheel.

from math import log2
from math import log
from collections import Counter

def find_index_of_1st(char: chr, string: str) -> int:
    for i in range(len(string)):
        if string[i] == char:
            return index

        
def is_element_at(i: int, char: chr, string: str) -> bool:
    return (string[i] == char)


def count_occurence(char: chr, string: str) -> int:
    return sum((char == original ) for original in string)


def contains(char: chr, string: str) -> bool:
    return (char in string)


def contains(substring: str, string: str) -> bool:
    return (substring in string)


def is_homogenous(string: str) -> bool:
    for i in range(len(string)):
        if string[i] == [i + 1]:
            continue
        else:
            return False
    return True


def is_only_alpha(string: str) -> bool:
    for char in string:
        if char.isalpha():
            continue
        else:
            return False
    return True


def is_only_numeric(string: str) -> bool:
    for char in string:
        if char.isdigit():
            continue
        else:
            return False
    return True


def is_alphanumeric(string: str) -> bool:
    for char in string:
        if char.isdigit() or char.isalpha():
            continue
        else:
            return False
    return True


def is_non_alphanumeric(string: str) -> bool:
    for char in string:
        if not(char.isdigit() and char.isalpha()):
            return False
    return True


def remove_front_and_back_whitespace():
    pass


# This function has not correct output.
def word_count(string: str, separator=' ') -> int:
    count = 0
    for i in range(len(string)):
        if (string[i] == separator and i == 0) or string[i] != separator:
            continue
        if string[]
        if string[i] == separator:
            count += 1
    return count


def histogram(string: str) -> dict:
    histogram = {}
    for i in range(len(string)):
        histogram[i] = histogram.get(i, 0) + 1
    return histogram


# Not making right output.
def get_entropy(string: str) -> bool:
    my_histogram = histogram(string)#Counter(string)
    probs = my_histogram.values()
    return sum((prob * log2(prob)) for prob in probs)
