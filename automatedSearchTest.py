import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_url(self):
		driver = self.driver
		driver.get("http://localhost:8810")

	def test_search_success(self):
		driver = self.driver
		driver.get("http://localhost:8810")
		search = driver.find_element_by_class_name("title")
		search.click()
		search = driver.find_element_by_id("simple_search_input")
		assert search.is_displayed
		search.send_keys("Cuisinart")
		search.send_keys(Keys.RETURN)
		search = driver.find_element_by_class_name("box-product-item")
		assert search.is_displayed

	def test_search_fail(self):
		driver = self.driver
		driver.get("http://localhost:8810")
		search = driver.find_element_by_class_name("title")
		search.click()
		search = driver.find_element_by_id("simple_search_input")
		assert search.is_displayed
		search.send_keys("!@#")
		search.send_keys(Keys.RETURN)
		search = driver.find_element_by_class_name("note-msg")
		assert search.is_displayed
		
	def tearDown(self):
		self.driver.close()