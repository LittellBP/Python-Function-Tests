import unittest
import os

from selenium import webdriver
from base import TestCase


class FrontendTestCase(TestCase):

    #Not my code

class TestAllProductsPageElements(FrontendTestCase):

    def test_product_limit(self):
        self.get_path('path', "/allproducts?limit=24")
        elements = self.driver.find_elements_by_class_name('box-product-item')
        assert len(elements) == 24

    def test_breadcrumbs_visible(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('breadcrumbs')
        assert element.is_displayed

    def test_title_visible(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('page-item-title')
        assert element.is_displayed

    def test_pagebar(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('pager')
        assert element.is_displayed

    def test_pagebar_pagelist(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('pages')
        pages = self.driver.find_element_by_class_name('current')
        assert element.is_displayed and pages.is_displayed

    def test_pagebar_sort(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('selectbox')
        default = (self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[2]'
            '/div[1]/div/div[1]/span/div[1]/div')
        )
        assert element.is_displayed and default.text == 'Position'

    def test_pagebar_limit(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('limiter')
        default = (self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[2]'
            '/div[1]/div/div[3]/span/div[1]/div')
        )
        assert element.is_displayed and default.text == '24'

    def test_sidebar(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_class_name('col-left')
        assert element.is_displayed

    def test_sidebar_brands(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_id('filterlabel2')
        brands = self.driver.find_element_by_xpath(
            '//*[@id="narrow-by-list"]/dd[1]')
        assert element.is_displayed and brands.is_displayed

    def test_sidebar_price(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_id('filterlabel3')
        prices = self.driver.find_element_by_xpath(
            '//*[@id="narrow-by-list"]/dd[2]')
        assert element.is_displayed and prices.is_displayed

    def test_sidebar_categories(self):
        self.get_path('path', "/allproducts?limit=24")
        element = self.driver.find_element_by_id('filterlabel4')
        categories = self.driver.find_element_by_xpath(
            '//*[@id="narrow-by-list"]/dd[3]')
        assert element.is_displayed and categories.is_displayed
