import unittest
import os
import random

from selenium import webdriver
from base import TestCase


class FrontendTestCase(TestCase):

    #Not my code

class TestProductPageElements(FrontendTestCase):

    def get_product(self):
        # User goes to the KI store and clicks a random product
        self.get_path('path', "/")
        alinks = self.driver.find_elements_by_tag_name('a')
        product_img_links = [
            link for link in alinks if 'product' in link.get_attribute('id')]
        random.choice(product_img_links).click()

    def check_breadcrumbs_visible(self):
        # User sees a list of links showing what pages they went through to get
        # here
        element = self.driver.find_element_by_class_name('breadcrumbs')
        assert element.is_displayed

    def check_title_visible(self):
        # User sees a the product name at the top of the page
        element = (self.driver.find_element_by_class_name('product-name'))
        assert element.is_displayed

    def check_price_visible(self):
        # User sees the price for the product
        element = self.driver.find_element_by_class_name('price')
        assert element.is_displayed

    def check_add_cart(self):
        # User clicks the add-to-cart button
        self.driver.find_element_by_id('button-cart').click()
        # User is taken to their cart and sees a message letting them know the
        # addition was successful
        element = self.driver.find_element_by_id('ajaxcartpro-add-confirm')
        assert element.is_displayed

    def check_shortDescription_visible(self):
        # User sees a short description of the product
        element = self.driver.find_element_by_class_name('short-description')
        assert element.is_displayed

    def check_longDescription_visible(self):
        # User sees the full description of the product
        element = self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/div[2]/div/div/div/section[1]')
        assert element.is_displayed

    def check_coupons_visible(self):
        # User clicks a random product on the KI home page, and has a coupon
        self.get_path('path', "/?coupon_code=PRIME")
        alinks = self.driver.find_elements_by_tag_name('a')
        product_img_links = [
            link for link in alinks if 'product' in link.get_attribute('id')]
        random.choice(product_img_links).click()
        # User sees a new price reflecting their active coupon
        element = self.driver.find_element_by_class_name('price-couponCode')
        assert element.is_displayed

    def test_product_page(self):
        self.get_product()
        self.check_breadcrumbs_visible()
        self.check_title_visible()
        self.check_price_visible()
        self.check_shortDescription_visible()
        self.check_longDescription_visible()
        self.check_add_cart()
        self.check_coupons_visible()


class TestRecentlyViewed(FrontendTestCase):

    def check_recent_hidden(self):
        # User goes to the home page and clicks an item
        self.get_path('ki_com', "/")
        alinks = self.driver.find_elements_by_tag_name('a')
        product_img_links = [
            link for link in alinks if 'product' in link.get_attribute('id')]
        random.choice(product_img_links).click()
        # user doesn't see the recently viewed box
        element = self.driver.find_elements_by_id('recently-viewed-items')
        assert len(element) == 0

    def check_repeat_hidden(self):
        current = self.driver.current_url
        # User goes back to the home page, but chooses to go back to the item
        self.get_path('ki_com', "/")
        self.driver.get(current)
        # User doesnt see the recently viewed box
        element = self.driver.find_elements_by_id('recently-viewed-items')
        assert len(element) == 0

    def check_recent(self):
        # User goes back to the home page and clicks a different item
        self.get_path('ki_com', "/")
        item2 = self.driver.find_element_by_id('productimgover48')
        item2.click()
        # User sees the recently viewed box
        element = self.driver.find_element_by_xpath(
            '//*[@id="product_addtocart_form"]/div[7]')
        assert element.is_displayed

    def check_recent_title(self):
        # User sees a title describing the new box on the page
        element = self.driver.find_element_by_class_name('block-title')
        assert element.is_displayed

    def check_recent_image(self):
        # User sees an image of the product they just looked at
        element = self.driver.find_element_by_class_name('product-image')
        assert element.is_displayed

    def check_recent_limit(self):
        # User browses 7 items in the KI store
        self.get_path('path', "/tablet")
        self.get_path('path', "/bakingsteel")
        self.get_path('path', "/optigrill")
        self.get_path('path', "/actifry")
        self.get_path('path', "/cuisinart-smartstick-hand-blender-sapphire")
        self.get_path('path', "/cuisinart-anodized-12-in-griddle")
        self.get_path(
            'path', "/kalorik-stainless-steel-2-slice-panini-grill")
        # User sees only 5 of those products in Recently Viewed
        elements = self.driver.find_elements_by_class_name('product-image')
        assert len(elements) == 5

    def check_recent_link_functions(self):
        # User clicks the first image in the list to view that item again
        element = self.driver.find_element_by_xpath(
            '//*[@id="recently-viewed-items"]/li[1]/p/a')
        link = element.get_attribute("href")
        element.click()
        # User is taken to the selected item page
        assert self.driver.current_url == link

    def test_recently_viewed(self):
        self.check_recent_hidden()
        self.check_repeat_hidden()
        self.check_recent()
        self.check_recent_title()
        self.check_recent_image()
        self.check_recent_limit()
        self.check_recent_link_functions()
