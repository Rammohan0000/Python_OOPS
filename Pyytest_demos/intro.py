# pytest is a testing framework that makes it easy to write simple tests, and run them with a single command.
# some key features of pytest are: 
    # 1. Fixtures: functions that set up and tear down resources needed for tests. They help manage test dependencies and ensure that the necessary setup is done before tests run and cleaned up afterward.
    # 2. Assertions: pytest uses assertions to validate test expectations.
    # 3. Markers: pytest markers are used to add metadata to the test functions.
    # 4. Parametrization: pytest allows you to run the same test with different inputs
# to install pytest, run the following command: pip install pytest, to check the version of pytest, run the following command: pytest --version, pytest -h
# To run all tests in a directory, navigate to that directory in your terminal and run the command: pytest. Pytest will automatically discover and execute all files starting with test_ or ending with _test.py.
# Pytest requires the test function names to start with test. 
# Function names which are not of format test* are not considered as test functions by pytest. We cannot explicitly make pytest consider any function not starting with test as a test function
# example 1
import math
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5
def testsquare():
    num = 7
    assert 7*7 == 40
def tesequality():
    assert 10 == 11

# run the test by running the command: pytest intro.py , if we use file_name as test, no need to mention file name explicitly, we can use pytest command to run the test
# The function tesequality is not executed because pytest will not consider it as a test since its name is not of the format test*.   
# use pytest -v intro.py to check verbose output
# use pytest -v -s intro.py to check verbose output with print statements

##Execute subset of test cases
#we will have multiple test files and each file will have a number of tests. 
# Tests will cover various modules and functionalities. 
# Suppose, we want to run only a specific set of tests; how do we go about it?
# to execute a specific test, we can use the -k option followed by the test name.
# pytest -v -k "test_square" intro.py


## Grouping multiple tests in a class
# pytest markers are used to group multiple tests in a class.
# pytest.mark is used to group multiple tests in a class.
# example:
import pytest
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

# to run the tests in a class, we can use the -m option followed by the marker name.          
