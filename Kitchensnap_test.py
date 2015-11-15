from selenium import webdriver
import sys

browser = webdriver.Firefox()
#Go to web page provided in command line
browser.get(sys.argv[1])

assert 'KitchenSnap' in browser.title

#locate price
element = browser.find_elements_by_class_name("regular-price")

#if price is present pass and print value to console, else fail and display error message
if len(element) <= 4:
	print(element[0].text)
else:
	print("Page not for a specific item.")

browser.quit()