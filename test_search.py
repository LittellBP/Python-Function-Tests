import sys
import unittest
import os
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from base import TestCase

class FrontendTestCase(TestCase):
    
    #Not my code

class TestSearch(FrontendTestCase):

    def test_search_success(self):
        self.get_path('path', "/")
        # self.driver.find_element_by_xpath('//*[@id="simple_search"]/span').click()
        search = self.driver.find_element_by_xpath('//*[@id="simple_search_input"]')
        search.send_keys("Cuisinart")
        search.send_keys(Keys.RETURN)
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[3]/div[2]/div[1]')ed

    def test_search_fail(self):
        self.get_path('path', "/")
        # self.driver.find_element_by_xpath('//*[@id="simple_search"]/span').click()
        search = self.driver.find_element_by_xpath('//*[@id="simple_search_input"]')
        search.send_keys("!@#")
        search.send_keys(Keys.RETURN)
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[1]/p')
        assert search.is_displayed