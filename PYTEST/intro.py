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
# pytest -m great marker.py

# ->Fixtures
#Fixtures are functions, which will run before each test function to which it is applied. 
# Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. 
# Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
# Fixtures are defined using the pytest.fixture() decorator.
# Fixtures are used to manage the test setup and teardown.
# we have a fixture function named input_value, which supplies the input to the tests. To access the fixture function
# Pytest while the test is getting executed, will see the fixture name as input parameter. 
# It then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test.
# Fixtures with parameters
# Fixtures can be used to pass arguments to the test functions.
# Example:
import pytest
@pytest.fixture
def input_value():
   input = 39
   return input
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
# to run the test, use the command: pytest -v intro.py
# pytest -k "test_divisible_by_3" intro.py is used to run a specific test case in the file  

#Pytest- Conftest.py
# conftest.py is used to share fixtures among multiple test files.
# conftest.py is used to define fixtures or hooks that are shared across multiple test files.
# Create a new file conftest.py and add the below code into it
# conftest.py
import pytest
@pytest.fixture
def input_value():
   input = 39
   return input
# Now, we can use the fixture in multiple test files.
# test_sample(remove fixture from the test file)
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
# Create a new file test_div_by_13.py −
# test_div_by_13.py
def test_divisible_by_13(input_value):
    assert input_value % 13 == 0
# Now, we can run the tests in both the files using the command: pytest -v
# The fixture input_value is shared between the two test files.
# pytest -k "test_divisible_by_3" test_div_by_13.py is used to run a specific test case in the file

#Pytest.fixture(scope='module')
import pytest
@pytest.fixture(scope='module')
def setup_module():
    print("\n[SETUP] Initializing module-level resource")
    data = {"name": "pytest", "version": "7.0"}
    yield data  
    print("\n[CLEANUP] Tearing down module-level resource")

def test_case1(setup_module):
    print("Running test_case1")
    assert setup_module["name"] == "pytest"

def test_case2(setup_module):
    print("Running test_case2")
    assert setup_module["version"] == "7.0"

# The setup_module fixture is executed only once before all the test functions in the module.
# output:
'''
[SETUP] Initializing module-level resource
Running test_case1
[CLEANUP] Tearing down module-level resource
[SETUP] Initializing module-level resource
Running test_case2
[CLEANUP] Tearing down module-level resource
'''

# Parametrizing Tests
# Parametrizing tests allows you to run the same test with different inputs.
# we can use the pytest.mark.parametrize decorator to pass the input values to the test functions.
# Example:
# test_parametrize.py
import pytest 
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
    assert 11*num == output
# to run the test, use the command: pytest -v test_parametrize.py
# pytest -k "test_multiplication_11" test_parametrize.py is used to run a specific test case in the file
# The test_multiplication_11 test is run four times with different input values.

# Pytest - Xfail/Skip Tests
# Sometimes, we may want to skip some tests or mark them as xfail,  but it will not be considered as part failed.
# pytest.mark.skip is used to skip the test.
# pytest.mark.xfail is used to mark the test as xfail.
# Example:
# test_xfail.py
import pytest
@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
   num = 100
   assert num < 200
# to run the test, use the command: pytest -v test_xfail.py
# pytest -k "test_failed" test_xfail.py is used to run a specific test case in the file
# The test_failed test is marked as xfail and the test_skipped test is skipped.
'''
test_compare.py::test_greater xfail
test_compare.py::test_greater_equal XPASS
test_compare.py::test_less SKIPPED
============================ 1 skipped, 1 xfailed, 1 xpassed in 0.06 seconds
'''

# Pytest - Stop Test Suite after N Test Failures
# Sometimes, we may want to stop the test suite after N number of test failures.
# The -x option is used to stop the test suite after the first failure.\
# Example:
# test_stop_after_n_failures.py
import pytest
def test_failed():
   assert 1 == 2
def test_failed_2():
    assert 2 == 3
def test_failed_3():
    assert 3 == 4
# to run the test, use the command: pytest -v test_stop_after_n_failures.py maxfail=2(after 2 failures, the test suite will stop)


##Pytest - HTML Reports
# Pytest can generate HTML reports for the test results.
# The pytest-html plugin is used to generate HTML reports.
# To install pytest-html, run the command: pip install pytest-html
# Example:
# test_html_report.py
import pytest
def test_passing():
   assert (1,2,3) == (1,2,3)
def test_failing():
    assert (1,2,3) == (3,2,1)
# to run the test, use the command: pytest -v test_html_report.py --html=report.html

#Pytest - Run Tests in Parallel
# Pytest can run tests in parallel to reduce the execution time.
# The pytest-xdist plugin is used to run tests in parallel.
# To install pytest-xdist, run the command: pip install pytest-xdist
# Example:
# test_parallel.py
import pytest
import time
def test_parallel_1():
   time.sleep(5)
   assert 1 == 1
def test_parallel_2():
    time.sleep(5)
    assert 2 == 2
# to run the test, use the command: pytest -v -n 2 test_parallel.py