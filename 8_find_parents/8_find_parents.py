# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# retrieve HTML string from the url
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")
# find the price of the object represented by the image at ../img/gifts/img1.jpg
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
