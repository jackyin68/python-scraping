# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup

# retrieve HTML string from the url
html = urlopen("http://www.pythonscraping.com/pages/page2.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")
# retrieve tags with two attibutes
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
# iterate throuth all tags
for tag in tags:
	print(tag)
