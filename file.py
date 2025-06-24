from collections import Counter
from string import punctuation
from typing import TextIO


words = ["a", "happy", "hello", "a", "world", "happy"]

word_counts = Counter(words)
print(word_counts)


def load_text(input_file: TextIO) -> str:
    """
    Load text from a text file and return as a string.

    Args:
        input_file: Accepts a .txt file.

    Returns:
       A string of text as it is read from the source.

    """

    with open(input_file, "r") as file:
        text = file.read()

    return text


def clean_text(text: str) -> str:
    """
        Lowercase and remove punctuation from a string.

        Args:
            text: Accepts a string

        Returns:
            A string without punctuation and all letters lowercase
   """

    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file):
    """
    Gets and prints the spreadsheet's header columns

    :param file_loc: The file location of the spreadsheet
    :type file_loc: str
    :param print_cols: A flag used to print the columns to the console
        (default is False)
    :type print_cols: bool
    :returns: a list of strings representing the header columns
    :rtype: list



















    AAA
    """ 

    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)


