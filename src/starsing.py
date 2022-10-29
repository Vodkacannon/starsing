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


def is_homogenous(string: str) -> bool:
    for index in range(len(string)):
        if string[i] == [i + 1]:
            continue;
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
        if char.isdigit() and char.isalpha():
            continue
        else:
