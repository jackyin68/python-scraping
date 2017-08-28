from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import unittest

class TestAddition(unittest.TestCase):
    browser = None
    def setUp(self):
        global browser
        #REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
        # driver = webdriver.PhantomJS(executable_path='/Users/sam/ws/python-scraping/phantomjs-2.1.1-macosx/bin/phantomjs')
        #driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
        browser = webdriver.Firefox()
        url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        browser.get(url)

    def tearDown(self):
        print("Tearing down the test")

    def test_drag(self):
        global browser
        element = browser.find_element_by_id("draggable")
        target = browser.find_element_by_id("div2")
        actions = ActionChains(browser)
        actions.drag_and_drop(element, target).perform()

        self.assertEqual("You are definitely not a bot!", browser.find_element_by_id("message").text)

if __name__ == '__main__':
    unittest.main()
