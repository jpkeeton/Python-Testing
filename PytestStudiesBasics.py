# #PyTest Studying

# Docs to Study
## https://code.visualstudio.com/docs/python/testing
## https://www.lambdatest.com/blog/selenium-python-pytest-testing-tutorial/#:~:text=Advantages%20Of%20pytest%20Framework,-Here%20are%20some&text=The%20Selenium%20test%20automation%20framework,(or%20unittest)%20and%20Nose2.

# OneNote Notes are here: 
# https://onedrive.live.com/view.aspx?resid=788E0015DB38AC9B%21106&id=documents&wd=target%28Python.one%7CF1DC2E5A-D693-48B0-866B-20034F96C260%2FTesting%20with%20Python%20unittest%20and%20pytest%7C1983A56F-432C-4BC3-89DB-F60ACAC0B591%2F%29
# onenote:https://d.docs.live.net/788e0015db38ac9b/Documents/My%20Notebook/Python.one#Testing%20with%20Python%20unittest%20and%20pytest&section-id={F1DC2E5A-D693-48B0-866B-20034F96C260}&page-id={1983A56F-432C-4BC3-89DB-F60ACAC0B591}&end


# print ("\nStudying Pytest\n")

# # file test_documentation.py
# def test_fail():
#     print ("this test is going to fail")
#     assert False


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
        self.assertEqual(sum([1, 2, 2]), 6, "Result should be 6")
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 3, 4)), 6, "tuple result should be 6")
        
# if __name__ == '__main__':
#     unittest:main()




