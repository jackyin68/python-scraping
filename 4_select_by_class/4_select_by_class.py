# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# grab the entire page
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")
# use findAll to select text in <span class="green"></span> tags
nameList = bsObj.findAll("span", {"class":"green"})
# iterate throuth all names in namelist
for name in nameList:
    print(name.get_text())
