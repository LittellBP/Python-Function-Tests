import unittest
import os
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import TestCase


class FrontendTestCase(TestCase):

    #not my code

class TestPrimeDiscount(FrontendTestCase):

    def check_homepage(self):
        # User loads the homepage with the PRIME discount active
        self.get_path('path', "/?coupon_code=PRIME")

        # User sees that all 8 featured products have a discount price
        origPrice = self.driver.find_elements_by_class_name('regular-price')
        discount = self.driver.find_element_by_class_name('price-couponCode')
        assert discount.is_displayed

    def check_product(self):
        # User clicks a random product on the homepage
        alinks = self.driver.find_elements_by_tag_name('a')
        product_img_links = [
            link for link in alinks if 'product' in link.get_attribute('id')]
        random.choice(product_img_links).click()

        # User sees message regarding free shipping for Prime Users
        element = self.driver.find_element_by_class_name('primeship')
        assert element.is_displayed

    def check_prime_msg_cart(self):

        # User adds the product to their cart
        element = self.driver.find_element_by_id('button-cart')
        element.click()

        # User sees a message message about free shipping for Prime members
        self.get_path('ki_com', '/checkout/cart/')
        msg = self.driver.find_element_by_id('shipMessage')
        assert msg.is_displayed()

    def check_cart_discount(self):
        # User sees a discount has been applied to the total
        discount = float(self.driver.find_element_by_css_selector(
            '#shopping-cart-totals-table > tbody > '
            'tr:nth-child(2) > td:nth-child(2) > span'
        ).text.replace('$', ''))
        origPrice = float(self.driver.find_element_by_css_selector(
            '#shopping-cart-totals-table > tbody > '
            'tr:nth-child(1) > td:nth-child(2) > span'
        ).text.replace('$', ''))
        checkPrice = round(origPrice * 0.3, 2)
        assert checkPrice == discount

    def checkout(self):
        # User keeps the discount active and proceeds to checkout
        element = self.driver.find_element_by_css_selector('button.check')
        element.click()

        # User sees that standard shipping is $0.00
        price = self.driver.find_element_by_css_selector(
            '#checkout-shipping-method-loadding > dd > ul > '
            'li:nth-child(1) > label > span'
        )

        # User sees a discount in their order review
        discount = float(self.driver.find_element_by_css_selector(
            '#checkout-review-table > tfoot > tr:nth-child(2) > '
            'td:nth-child(2) > span'
        ).text.replace('-$', ''))
        total = float(self.driver.find_element_by_css_selector(
            '#checkout-review-table > tfoot > tr:nth-child(1) > '
            'td:nth-child(2) > span'
        ).text.replace('$', ''))
        checkPrice = round(total * 0.3, 2)

        assert price.text == '$0.00'
        assert discount == checkPrice

    def test_prime(self):
        self.check_homepage()
        self.check_product()
        self.check_prime_msg_cart()
        self.check_cart_discount()
        self.checkout()

class TestPrimeCoupons(FrontendTestCase):

    def add_prime_coupon(self):
        self.get_path('path', "/?coupon_code=PRIME")

    def check_gift_cat(self):
        # User navigates to the gift card page with the PRIME discount active
        self.get_path('path', "/gourmet-foods/gift-certificates/")

        # User sees gift card category page
        element = self.driver.find_element_by_class_name(
            'category-gift-certificates'
        )

        # User sees that the gif cards don't have a Prime discount
        prices = self.driver.find_elements_by_class_name('price-couponCode')
        assert len(prices) == 0

    def check_gift_search(self):
        # Need to fix the experiment for search for this to work
        # User does a search for giftcards
        search = self.driver.find_element_by_id('simple_search_input')
        search.send_keys('certificate')
        search.send_keys(Keys.ENTER)

        # User sees the gift card results have no discount
        prices = self.driver.find_elements_by_class_name('price-couponCode')
        assert len(prices) == 0

    def check_gift_page(self):
        # User clicks a random gift card
        alinks = self.driver.find_elements_by_tag_name('a')
        product_img_links = [
            link for link in alinks if 'product' in link.get_attribute('id')]
        random.choice(product_img_links).click()

        # User sees the standard price with no discount
        element = self.driver.find_elements_by_class_name('price-couponCode')
        assert len(element) == 0

    def check_gift_checkout(self):
        # User decides to add a gift card to their cart
        element = self.driver.find_element_by_id('button-cart')
        element.click()
        # User sees Ajax pop-up and clicks View Cart
        element = self.driver.find_element_by_id('ajaxcartpro-add-confirm')
        # User goes to the View Cart page
        self.get_path('path', '/checkout/cart/')
        page = self.driver.find_element_by_class_name(
            'checkout-cart-index'
        )

        # User sees their coupon field is empty
        coupon = self.driver.find_element_by_id('coupon_code')
        coupon = coupon.get_attribute('value')

        assert coupon == ''

    def test_double_coupon(self):
        # User adds a different item to their cart
        self.get_path('path', "/optigrill/?coupon_code=PRIME")
        element = self.driver.find_element_by_id('button-cart')
        element.click()
        # User sees Ajax pop-up and clicks View Cart
        element = self.driver.find_element_by_id('ajaxcartpro-add-confirm')
        # User goes to the View Cart page
        self.get_path('path', '/checkout/cart/')
        page = self.driver.find_element_by_class_name(
            'checkout-cart-index'
        )
        # User sees their Prime discount is reapplied on the new item
        coupon = self.driver.find_element_by_id('coupon_code')
        couponPrime = coupon.get_attribute('value')
        discountPrime = float(self.driver.find_element_by_css_selector(
            '#shopping-cart-totals-table > tbody > '
            'tr:nth-child(2) > td:nth-child(2) > span'
        ).text.replace('$', ''))

        assert couponPrime == 'coupon'

        # User tries to enter an additional code
        coupon.clear()
        coupon = self.driver.find_element_by_id('coupon_code')
        coupon.send_keys('special15')
        coupon.send_keys(Keys.ENTER)

        # User sees only the new code is active
        coupon = self.driver.find_element_by_id('coupon_code')
        couponSpecial = coupon.get_attribute('value')
        discountSpecial = float(self.driver.find_element_by_css_selector(
            '#shopping-cart-totals-table > tbody > '
            'tr:nth-child(2) > td:nth-child(2) > span'
        ).text.replace('$', ''))

        assert couponSpecial == 'special15'
        assert discountPrime > discountSpecial

    def test_prime_coupons_with_giftcard(self):
        self.add_prime_coupon()
        self.check_gift_cat()
        self.check_gift_search()
        self.check_gift_page()
        self.check_gift_checkout()
