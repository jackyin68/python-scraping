from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains


# REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
# driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')
# driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver')
browser = webdriver.Firefox()

browser.implicitly_wait(5)
browser.get('http://thestakeholdercompany.com/home/')
browser.get_screenshot_as_file('screenshot.png')
