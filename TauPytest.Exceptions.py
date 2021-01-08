# https://testautomationu.applitools.com/pytest-tutorial/chapter3.html

# Writing a test with an exception

# * Remember - any raised exception that is not handled within a test case function will cause that test case to report a failure

# So how to verify that a piece of code successfully raises an exception?

# Ex. 
# verify that dividing by zero raises an Exception
def test_exception_zero_division():
    num = 1 / 0 


