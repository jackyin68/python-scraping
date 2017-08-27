# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# retrieve HTML string from the url
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html.read(), "html.parser")
# call h1 tag from the BeautifulSoup object
print(bsObj.h1)
