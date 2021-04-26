"""
py module created on python 3.7.9 and analyses the given text and finds the frequency of occurence
"""
import re
from collections import OrderedDict
from text_processor.Test import IWordFrequency, IWordFrequencyAnalyzer


class TestProcessor(IWordFrequency, IWordFrequencyAnalyzer):
    """
    Class to process given text
    """
    word = ""
    frequency = []
    _instance = None

    def __new__(cls):
        """Check if an instance exists: this is to create singleton class"""
        if not cls._instance:
            print("New instance created!")
            # Create new instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    @classmethod
    def __string_counter(cls, text):
        """
        A class method to perform count of string in given text
        :param text: Input text from user
        :return: tuple of word frequency and highest frequecy of word
        """
        cls.word = ""
        cls.frequency = []

        cls.word = re.findall(r"[a-z|A-Z]+", text.lower())
        for word in cls.word:
            cls.frequency.append(cls.word.count(word))
        word_count = OrderedDict(set(zip(cls.word, cls.frequency)))
        unique_values = sorted(set(word_count.values()), reverse=True)
        word_count_list = []
        for value in unique_values:
            temp = []
            temp = sorted(list(filter(
                lambda item: item[1] == value, word_count.items())))
            word_count_list += temp
        return word_count_list, unique_values[0]

    def calculate_highest_frequency(self, text: str) -> list:
        """
         function returns the highest frequency of word in the text
        :param text: str, User input text
        :return: list, word with highest frequecy
        """
        ret_val = TestProcessor.__string_counter(text)
        return [item[0] for item in filter(
            lambda item: item[1] == ret_val[1], ret_val[0])]

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """
        function returns frequency of word in given text
        :param text: str, User input text
        :param word: str, frequency for the word to be determined
        :return: int, frequecy of the word
        """
        try:
            return dict(TestProcessor.__string_counter(text)[0])[word]
        except KeyError:
            return f"err: '{word}' is not present in the given string"

    def calculate_most_frequent_n_word(self, text: str, n: int) -> list:
        """
        function returns the 1st 'n' words with frequency
        :param text: str, User input text
        :param n: int, number from the input
        :return: list of tuple (words and its frequecy)
        """
        return TestProcessor.__string_counter(text)[0][0:n]
