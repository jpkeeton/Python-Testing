# --------------------------------------------------------
# Parameterization
# https://testautomationu.applitools.com/pytest-tutorial/chapter4.html

# Testing Multiplication Ideas
# 2 positive integers
# Identity: multiplying any number by 1
# Zero: multiplying any number by 0
# Positive by negative
# Negative by negative
# Multiply floats
# These are all equivalence classes
#  Unique input and unique output
#  Good test suite provides one test case per equivalence class

# So you only need 1 test for identity, one test for floats, etc
# So writing out all these individual tests becomes repetitive
# Here: https://testautomationu.applitools.com/pytest-tutorial/chapter4.html
# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6

# def test_multiply_identity():
#     assert 2 * 1 == 2
#
#
# def test_multiply_zero():
#     assert 2 * 0 == 0
#
#
# def test_multiply_two_positive_ints():
#     assert 2 * 0 == 0


# this doesn't work, commenting out
# def test_multiply_two_floats():
#     assert 3.1 * 2.2 == 6.82

# So this approach is redundant
# Let's use pytest.mark.parameterize instead -> docs are here: https://docs.pytest.org/en/stable/parametrize.html

import pytest


#


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("5-4", 1), ("6*6", 36)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# and here's the example from TAU.
# Each tuple represents an equivalence class of inputs

products = [
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -2, -6),  # positive by negative
    (-4, -4, 16),  # negative by negative
    # (4.5, 3.1, 13.95)  # floats
]


# @pytest.mark.parameterize is a decorator for the test_multiplication function

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


# So now to practice, do Sums
sums = [
    (2, 3, 5),  # positive integers
    (1, 99, 100),  # identity - but is that identity?
    (-1, -2, -3),  # negative integers
    (1, -4, -3),  # One positive, one negative
]


@pytest.mark.parametrize('a, b, sum', sums)
def test_addition(a, b, sum):
    assert a + b == sum

# There are lots of other cool things you can do w parameters, like pulling in data from a .csv.
# Check out Hypothesis -> https://hypothesis.readthedocs.io/en/latest for lots of other craziness