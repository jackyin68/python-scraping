# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup
# retrieve HTML string from the url
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")

# use next_siblings() to find all rows of products from the product table except the first row
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
