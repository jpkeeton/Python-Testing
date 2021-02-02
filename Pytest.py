# https://testautomationu.applitools.com/pytest-tutorial/
# Code is here: https://github.com/AndyLPK247/tau-intro-to-pytest

# https://docs.pytest.org/en/stable/


# Pytest is core test framework
# Let's you write test cases as functions
# Executes tests and compiles pass/fail results
# Similar to other test frameworks, like Python's nunit and Java's junit, Javascript's Jasmine
# But, has other cool stuff that we'll cover


# First Test
# https://github.com/AndyLPK247/tau-intro-to-pytest/tree/example/1-first-test


# See my Onenotes on this
# I can still run Pytest from the command line

# TODO https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter
# TODO Run these

# print('running tests')
# print('rebooting PyTestEfforts here')

# # TODO Create directories per TAU's first lesson

# <<<<<<<<<<<<<

# https://testautomationu.applitools.com/pytest-tutorial/chapter3.html

# Writing a test with an exception

# * Remember - any raised exception that is not handled within a test case function will cause that test case to report a failure

# So how to verify that a piece of code successfully raises an exception?


# >>>>>>>>>>>>>
# this is a nice recourse
# https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm
# >>>>>>>>>>>>>>>

def test_AssertTrue():
    assert True


def test_exception_zero_division():
    num = 0 / 1


# # here's a basic math operation
def test_1Plus1():
    assert 1 + 1 == 2


# 'normal' function here
# def multiply(a, b):
#     return a * b

def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# Back here again: https://testautomationu.applitools.com/pytest-tutorial/chapter3.html
# we could write our own try/catch, but PyTest has it's own way


# -----------------------------------------------------------------------
# test function that verifies an exception
# using the 'raises' option
import pytest


def test_divide_by_zeroz():
    with pytest.raises(ZeroDivisionError) as e:
        # with pytest.raises(AssertionError) as e:
        # the 'with' is a special statement for automatically handling extra 'enter' and 'exit' logic for a caller
        # commonly used for file input & output. the enter logic opens the file, the body reads/writes, and the exit logic closes the file
        # for pytest.raises the enter logic makes the code catch any exceptions.
        # and the exit logic asserts if the desired exception type was actually raised
        # in this case the divide by zero should raise a the 'ZeroDivisionError'.
        # so pytest.raise should catch the exception and keep running the test as if there were now problem
        # Pytest.raises looks for an exception of a specific type. If the steps w/in the 'with' statement's body do not raise the desired exception,
        # then it will raise an assertion error to fail the test
        # so that means I can stick a different error type in the with bit
        # see what that does
        # makes test code more concise, avoids repetitive try/catch blocks

        num = 1 / 0
    assert 'division by zero' in str(e.value)


# Also from https://docs.pytest.org/en/stable/assert.html
# Using pytest.raises() is likely to be better for cases where you are testing exceptions your own code is deliberately raising,
# whereas using @pytest.mark.xfail with a check function is probably better
# for something like documenting unfixed bugs (where the test describes what “should” happen) or bugs in dependencies.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import unittest


class TestSum(unittest.TestCase):
    # convert the test functions into methods by adding self as the first argument

    def test_sum(self):
        # create the
        self.assertEqual(sum([1, 2, 2]), 5, "Result should be 5")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 3, 4)), 8, "tuple result should be 8")


print('this is the TestSum bit')

if __name__ == '__main__':
    unittest: main()
# dunno why this part is working when running the tests, but not when just running the .py file 'normally'


# --------------------------------------------------------
# Parameterization
# https://testautomationu.applitools.com/pytest-tutorial/chapter4.html

## Multiplication ideas
# 2 positive integers
# identity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by negative
# negative by negative
# multiply floats
# these are all equivalence classes
#  unique input and unique output
#  good test suite provides one test case per equivalence class

# so you only need 1 test for identity, one test for floats, etc
# So writing out all these indivudal tests becomes repetetive
# here: https://testautomationu.applitools.com/pytest-tutorial/chapter4.html
# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6

# def test_multiply_identity():
#     assert 2 * 1 == 2

# def test_multiply_zero():
#     assert 2 * 0 == 0

# def test_multiply_two_positive_ints():
#     assert 2 * 0 == 0

# def test_multiply_two_positive_ints():
#     assert 2 * 0 == 0









