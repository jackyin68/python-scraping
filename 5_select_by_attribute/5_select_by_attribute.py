# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# grab the entire page
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")
# use findAll to select tags containing a particular attribute
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
