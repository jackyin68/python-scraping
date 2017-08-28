from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

#REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
# driver = webdriver.PhantomJS(executable_path='/Users/sam/ws/python-scraping/phantomjs-2.1.1-macosx/bin/phantomjs')
# driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
browser = webdriver.Firefox()

browser.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')

print(browser.find_element_by_id("message").text)

element = browser.find_element_by_id("draggable")
target = browser.find_element_by_id("div2")
actions = ActionChains(browser)
actions.drag_and_drop(element, target).perform()

print(browser.find_element_by_id("message").text)
