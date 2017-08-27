# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# retrieve HTML string from the url
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")

# use .children tag to find only descendants that are children
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
