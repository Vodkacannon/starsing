# Some of these functions may be reinventing the wheel.

def find_index_of_1st(char: chr, string: str) -> int:
    for index in range(len(string)):
        if string[index] == char:
            return index

def is_element_at(index: int, char: chr, string: str) -> bool:
    return (string[index] == char)

def count_occurence(char: chr, string: str) -> int:
    return sum((char == original ) for original in string)

def contains(char: chr, string: str) -> bool:
    return (char in string)

def contains(substring: str, string: str) -> bool:
    return (substring in string)

