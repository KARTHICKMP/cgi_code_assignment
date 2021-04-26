"""
py module created on python 3.7.9 and has only abstract class
"""
from abc import ABC, abstractmethod


class IWordFrequency(ABC):
    """
    An Abstract class, which will be implemented in text_processor_lib module
    """
    word: str
    frequency: int


class IWordFrequencyAnalyzer(ABC):
    """
    An Abstract class, which will be implemented in text_processor_lib module
    """
    @abstractmethod
    def calculate_highest_frequency(self, text: str) -> list:
        """abstract methods to calculate highest frequency words"""

    @abstractmethod
    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """abstract methods to calculate frequecy for given word"""

    @abstractmethod
    def calculate_most_frequent_n_word(self, text: str, n: int) -> list:
        """abstract methods to get the n most frequent word"""
