# import the urlopen library
from urllib.request import urlopen
# import the HTTPError library
from urllib.error import HTTPError
# import the BeautifulSoup library
from bs4 import BeautifulSoup
# import module system-specific parameters and functions
import sys

# function getTitle, returns either the title of the page or a None object
def getTitle(url):
    try:
        html = urlopen(url)
    # check for an HTTPError (the server is not found, url is down or mistyped)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    # check for AttributeError (the server doesn't exist, html is a None object)
    except AttributeError as e:
        return None
    return title

# get title by passing url to function getTitle
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
