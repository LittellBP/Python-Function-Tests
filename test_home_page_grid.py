import unittest
import os
import random
import time

from selenium import webdriver
from base import TestCase


class FrontendTestCase(TestCase):

    #Not my code

class TestHomePageElements(FrontendTestCase):

    def test_featured_banner_visible(self):
        self.get_path('path', "/")
        element = self.driver.find_element_by_class_name('home-navi')
        assert element.is_displayed

    def test_prod_image_visible(self):
        self.get_path('path', "/")
        image1 = self.driver.find_element_by_class_name('front-image')
        # front-big-image shouldnt display on desktop
        # can be implemented for mobile testing
        assert image1.is_displayed

    def test_prod_image_works(self):
        self.get_path('path', "/")
        alinks = self.driver.find_elements_by_tag_name('a')
        product_img_links = [
            link for link in alinks if 'product' in link.get_attribute('id')]
        random.choice(product_img_links).click()
        element = self.driver.find_element_by_class_name('product-name')
        assert element.is_displayed

    def test_prod_price_visible(self):
        self.get_path('path', "/")
        element = self.driver.find_element_by_class_name('price')
        assert element.is_displayed

    def test_addcart_visible(self):
        self.get_path('path', "/")
        div = self.driver.find_element_by_class_name('box-product-buttons')
        element = div.find_element_by_class_name('buttons-cart')
        assert element.is_displayed

    def test_addcart_works(self):
        self.get_path('path', "/")
        div = self.driver.find_element_by_class_name('box-product-buttons')
        element = div.find_element_by_class_name('buttons-cart')
        element.click()
        element = self.driver.find_element_by_id('ajaxcartpro-add-confirm')
        assert element.is_displayed

    def test_showmore_visible(self):
        self.get_path('path', "/")
        div = self.driver.find_element_by_class_name('showmore')
        element = div.find_element_by_css_selector('a')
        assert element.is_displayed

    def test_showmore_works(self):
        self.get_path('path', "/")
        div = self.driver.find_element_by_class_name('showmore')
        element = div.find_element_by_css_selector('a')
        element.click()
        assert (self.driver.current_url ==
                'http://localhost:8810/allproducts?limit=24'
                )

    def test_wishlist_button_hidden(self):
        self.get_path('path', "/")
        element = self.driver.find_element_by_class_name('buttons-wish')
        # javascript changes element display, confused is_displayed method
        self.assertIn('none', element.value_of_css_property('display'))
