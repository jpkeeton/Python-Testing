# #PyTest Studying

# Docs to Study
## https://code.visualstudio.com/docs/python/testing
## https://www.lambdatest.com/blog/selenium-python-pytest-testing-tutorial/#:~:text=Advantages%20Of%20pytest%20Framework,-Here%20are%20some&text=The%20Selenium%20test%20automation%20framework,(or%20unittest)%20and%20Nose2.

# OneNote Notes are here: 
# https://onedrive.live.com/view.aspx?resid=788E0015DB38AC9B%21106&id=documents&wd=target%28Python.one%7CF1DC2E5A-D693-48B0-866B-20034F96C260%2FTesting%20with%20Python%20unittest%20and%20pytest%7C1983A56F-432C-4BC3-89DB-F60ACAC0B591%2F%29
# onenote:https://d.docs.live.net/788e0015db38ac9b/Documents/My%20Notebook/Python.one#Testing%20with%20Python%20unittest%20and%20pytest&section-id={F1DC2E5A-D693-48B0-866B-20034F96C260}&page-id={1983A56F-432C-4BC3-89DB-F60ACAC0B591}&end

# Pytest Arugments
# --tb=[auto/long/short/line/native/no]: Controls the traceback style.
# -v  --verbose: Displays all the test names, passing or failing.
# -l  --showlocals: Displays local variables alongside the stacktrace.
# -lf  --last-failed: Runs just the tests that failed last.
# -x  --exitfirst: Stops the tests session with the first failure.
# --pdb: Starts an interactive debugging session at the point of failure.



print ("\nStudying Pytest\n")

# file test_documentation.py
def test_fail():
    print ("this test is going to fail")
    assert True


# def test_pass():
#     print ("this test is going to pass")
#     assert True


# def test_SomeFunction():
#     assert 1==1

import unittest

class TestSum(unittest.TestCase):
# convert the test functions into methods by adding self as the first argument
    def test_sum(self):
# create the 
        self.assertEqual(sum([1, 2, 2]), 5, "Result should be 5")
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 3, 4)), 8, "tuple result should be 8")
        
# if __name__ == '__main__':
#     unittest:main()

def test_AssertTrue():
    assert True



# incrementer
# so here is the function
def increment(x):
    return x + 1
# and here is the test
# the function adds 1, when you test with an argument of 3 does it equal 4?
def test_increment_integer_3():
    assert increment(3) == 4
# same w another example
def test_increment_integer_10():
    assert increment(10) == 11



# https://testautomationu.applitools.com/pytest-tutorial/chapter1.html
# 'test_' is test indicator

# 'python -m pytest' should find and run tests, it automatically adds current directory to sys.path
# so all modules in the project can be discovered
# . (dot) for each passing test
# that's not working so.. will just use my usual 'pytest .\[filename].py' 

# so from video 2 there is a 1+2 test we'll create
# this is a failing test
def test_one_plus_two():
    a = 1
    b = 2
    # c = 0
    c = 3
    assert a + b == c # which will be wrong
    # so change the C to 3



# another example from https://docs.pytest.org/en/stable/assert.html

# create the function
def f():
    return 3

# create the test function
def test_fx():
    assert f() == 4
# now run the test



