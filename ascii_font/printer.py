import itertools
from functools import reduce

from ascii_font.font import ASCII_ABC


def print_ascii(word: str):
    word_ascii = [ASCII_ABC[key] for key in word]  # get ascii maps for each letter
    word_ascii = list(zip(*word_ascii))  # transpose (rotate right) the list of tuples

    ## use reduce to add a tuple (" ",) as sperator between each letter row:
    # (("*", "***", "*"), ("*", "   ", " "), , ("*", "   ", " "),("*", "***", "*")) ->
    #       (("*", "***", "*"), (" ",) ("*", "   ", " "), (" ",), ("*", "   ", " "), (" ",), ("*", "***", "*"))
    ## use chain to flatten the collection of collection into one continous collecton
    # (("*", "***", "*"), (" ",) ("*", "   ", " "), (" ",), ("*", "   ", " "), (" ",), ("*", "***", "*")) ->
    #   ("*", "***", "*", " ", "*", "   ", " ", " ", "*", "   ", " ", " ", "*", "***", "*")
    ## join each row into a string:
    # ("*", "***", "*", " ", "*", "   ", " ", " ", "*", "   ", " ", " ", "*", "***", "*") ->
    #       -> "**** *     *     *****"
    # do this for each 6 lines in the resulted word
    return ("".join(list(itertools.chain(reduce(lambda a, b: a + (" ",) + b, line)))) for line in word_ascii)


if __name__ == '__main__':
    print(*print_ascii('abba'), sep='\n')

