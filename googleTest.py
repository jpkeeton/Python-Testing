
# Source: https://www.lambdatest.com/blog/generating-xml-and-html-report-in-pyunit-for-test-automation/
# https://blog.testproject.io/2020/07/15/getting-started-with-testproject-python-sdk/
# https://github.com/testproject-io/python-sdk
# https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
# https://blog.testproject.io/2019/07/16/create-pytest-html-test-reports/



import unittest
from selenium import webdriver
import time
from time import sleep

class GoogleSeachTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_GoogleSearch(self):
        driver_firefox = self.driver
        driver_firefox.maximize_window()
        driver_firefox.get('http://www.google.com')

        # Perform search operation
        elem = driver_firefox.find_element_by_name("q")
        elem.send_keys("Lambdatest")
        elem.submit()

        sleep(10)

    def tearDown(self):
        # Close the browser.
        self.driver.close()

if __name__ == '__main__':
    unittest.main()