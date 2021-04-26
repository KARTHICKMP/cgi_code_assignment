**CGI CODE ASSIGNMENT**

**Introduction:**
This file describes about the usage of project - text processing library. 
This project is built using python version3.7.9 and used pytest framework to create and execute the test cases

**SetUp**:
1. Clone the repo (or)
2. Download the project as zip file and unzip the project

**File, Folder Descriptions & Usage**

_text_processor_ folder: contains 
    Test.py - contains the abstract class, which is used text_processor_lib.py
    text_processor_lib.py - contains the main code for text processing

_unittest_ folder: contains
    test_text_processing.py - contains test cases written in pytest framework for testing text processing methods 
        written in text_processor_lib.py module

_venv_ folder:
    **SHOULD NOT BE DELETED ANYTHING HERE** as this contains mainly the python and it's support python package for this 
        project
    **NOTE**: to run this project virtual environment needs to be activated. Below file should be executed
   
    cgi_code_assignment\venv\Scripts\activate

    to deactivate the environment, run below command in the terminal
    deactivate

_requirements.txt_:
    contains all the packages installed and used for this project
    **Note**: incase if the above mentioned virtual environment is not used the run below command, to install python package
    
    pip install -r requirements.txt

_setup.py_: 
    file used to create as package
    **Note**: incase if the above mentioned virtual environment is not used the run below command,

    pip install -e .

_htmlcov_ folder:
    open "index.html" in browser to see the test coverage for the created library
    
**CODE FORMATTING**:
    This project is formatted using pylint, flake8 and bandit
    
**TO EXECUTE TEST CASES**:
    Navvigate inside "cgi_code_assignment" and execute below command
    `pytest unittest\ -v`
   
Below is how the results will be displayed
`============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.7.9, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- c:\experiment\python\cgi_code_assignment\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Experiment\Python\cgi_code_assignment
plugins: cov-2.11.1, forked-1.3.0, xdist-2.2.1
collected 9 items
unittest/test_text_processing.py::test_match_highest_frequency_word PASSED                                                                                                [ 11%]
unittest/test_text_processing.py::test_frequency_for_a_word_ispresent PASSED                                                                                              [ 22%]
unittest/test_text_processing.py::test_highest_n_frequency_word PASSED                                                                                                    [ 33%]
unittest/test_text_processing.py::test_frequency_for_a_word_is_not_present PASSED                                                                                         [ 44%]
unittest/test_text_processing.py::test_unmatch_highest_frequency_word XFAIL (Given list of words doesn't match with expected)                                             [ 55%]
unittest/test_text_processing.py::test_highest_frequency_word_return_list PASSED                                                                                          [ 66%]
unittest/test_text_processing.py::test_puntuation_are_eliminated PASSED                                                                                                   [ 77%]
unittest/test_text_processing.py::test_mixed_string_case_counted PASSED                                                                                                   [ 88%]
unittest/test_text_processing.py::test_is_singleton PASSED                                                                                                                [100%]
=================================================================== 8 passed, 1 xfailed in 0.45s ================================================================================`

Where _PASSED_ - Test case executed successfully
_XFAIL_ - Test case executed successfully but with expected failure (Negative scenario test)

**TEST COVERAGE**:
:Below is the test coverage details
`Coverage report: 100% Show keyboard shortcuts
filter...
Module	                                    statements	missing	excluded	coverage
Total	                                            47	    0	    0	        100%
text_processor\Test.py	                            11	    0	    0	        100%
text_processor\__init__.py	                        0	    0	    0	        100%
text_processor\text_processor_lib.py	            36	    0	    0	        100%
coverage.py v5.5, created at 2021-04-24 22:07 +0530`
