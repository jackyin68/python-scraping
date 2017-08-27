# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup
# import module regular expressions
import re

# construct a new empty set object
pages = set()
# define getLinks()
def getLinks(pageUrl):
    # pages are to be interpreted as globals
    global pages
    # retrieve HTML string from url
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    # create a BeautifulSoup object
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        # <h1> title tag
        print(bsObj.h1.get_text())
        # find text content in the div#mw-content-text →p, selecting the first paragraph only
        print(bsObj.find(id ="mw-content-text").findAll("p")[0])
        # find links in the li#ca-edit tag, under li#ca-edit → span → a
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    # check for AttributeError
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']
                # print dashes for clarity, separating the printed content
                print("----------------\n"+newPage)
                # add element newPage to set pages
                pages.add(newPage)
                # call getLinks
                getLinks(newPage)
# initial page is http://en.wikipedia.org, with pageUrl blank
getLinks("")
