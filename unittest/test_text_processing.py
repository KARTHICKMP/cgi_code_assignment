from text_processor.text_processor_lib import TestProcessor
import pytest

def test_match_highest_frequency_word():
    """test to check if the function returns highest frequency words"""
    test_string = "the sun shines over the lake and shines every where"
    obj = TestProcessor()
    assert ["shines", "the"] == obj.calculate_highest_frequency(test_string), "Check if the highest frequecy words are correct"

def test_frequency_for_a_word_ispresent():
    """test to check if the function returns frequency for a word which is present"""
    test_string = "the sun shines over the lake and shines every where"
    obj = TestProcessor()
    ret_val = obj.calculate_frequency_for_word(test_string, "the")
    assert 2 == ret_val, f"Check if the frequecy of the word is {ret_val} matches with expected value 2"

def test_highest_n_frequency_word():
    """test to check if the function returns n(n=3) highest frequency words"""
    test_string = "the sun shines over the lake and shines every where"
    obj = TestProcessor()
    ret_val = obj.calculate_most_frequent_n_word(test_string, 3)
    assert len(ret_val) == 3, f"returned number of string doesnt match"
    assert [('shines', 2), ('the', 2), ('and', 1)] == ret_val,  f"returned list of string doesnt match"

def test_frequency_for_a_word_is_not_present():
    """test to check if the function returns frequency for a word which is not present"""
    test_string = "the sun shines over the lake and shines every where"
    obj = TestProcessor()
    assert "err: 'then' is not present in the given string" == obj.calculate_frequency_for_word(test_string, "then"), "check if the error expected text is not present"

@pytest.mark.xfail(reason="Given list of words doesn't match with expected", raises=AssertionError)
def test_unmatch_highest_frequency_word():
    """negative test to check if the function returns highest frequency words"""
    test_string = "the sun shines over the lake and shines every where"
    obj = TestProcessor()
    assert ["shines", "then"] == obj.calculate_highest_frequency(test_string), "check if highest frequency word doesn't match"

def test_highest_frequency_word_return_list():
    """test to check if the function returns list of words"""
    test_string = "the sun shines over the lake and shines every where"
    obj = TestProcessor()
    assert list == type(obj.calculate_highest_frequency(test_string)), "returned value is not a type of list"

def test_puntuation_are_eliminated():
    """test if puntuations are eliminated on counting words"""
    obj = TestProcessor()
    print(obj.word)
    ret_val = obj.calculate_highest_frequency("Hi there! how are you?")
    print(ret_val)
    assert ['are', 'hi', 'how', 'there', 'you'] == ret_val, "Check if the puntuations are eliminated while considering word count"

def test_mixed_string_case_counted():
    """test to check string with different case are counted"""
    test_string = "THE sun shines over the lake and SHINES every where"
    obj = TestProcessor()
    ret_val = obj.calculate_frequency_for_word(test_string, "the")
    assert 2 == ret_val, f"Check if the frequecy of the word is {ret_val} matches with expected value 2"
    ret_val = obj.calculate_frequency_for_word(test_string, "shines")
    assert 2 == ret_val, f"Check if the frequecy of the word is {ret_val} matches with expected value 2"

def test_is_singleton():
    """test to check if class is singleton"""
    obj = TestProcessor()
    obj1 = TestProcessor()
    assert obj is obj1, "check if Objects are same as this is singleton class"