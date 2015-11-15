import unittest
import os
from selenium import webdriver
from base import TestCase

class FrontendTestCase(TestCase):

    #Not my code

    def get_path(self, store, path):
        return self.driver.get(self.base_urls[store] + path)
    
class TestCss(FrontendTestCase):

    def test_css_font(self):
        self.get_path('path', "/")
        element = self.driver.find_element_by_xpath('//*[@id="header_menu"]/a')
        assert element.value_of_css_property("font-size") == "13px"

    def test_css_display(self):
        self.get_path('path', "/")
        element = self.driver.find_element_by_xpath('//*[@id="header_menu"]/a')
        assert element.value_of_css_property("display") == 'block'

