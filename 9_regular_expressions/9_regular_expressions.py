# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup
# import the regular expressions library
import re

# retrieve HTML string from the url
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# create a BeautifulSoup object
bsObj = BeautifulSoup(html, "html.parser")
# find the images at path starting with ../img/gi s/img and ending in .jpg
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# iterate throuth all images in images
for image in images:
    print(image["src"])
