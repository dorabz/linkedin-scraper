from selenium import webdriver
from bs4 import BeautifulSoup
import time, re
import unittest

class InputFormsCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_singleInputField(self):
        user = "gahaha@gmail.com"
        pas = "ballalla"
        url = "https://linkedin.com/uas/login"
        driver=self.driver
        driver.maximize_window()
        driver.get(url)
        assert "Linkedin" in driver.title
        elem = driver.find_element_by_id("username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("password")
        elem.send_keys(pas)
        elem.send_keys(Keys.RETURN)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()