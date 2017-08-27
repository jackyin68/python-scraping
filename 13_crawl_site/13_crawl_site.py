# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup
# import module regular expressions
import re
# import module datetime to get the current system time
import datetime
# import module random to generate random numbers
import random

# initialize blank set
pages = set()
# set the random number generator seed with the current system time
random.seed(datetime.datetime.now())

# retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    # initialize blank array
    internalLinks = []
    # finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                # append a new link with attribute href to the end of the array internalLinks
                internalLinks.append(link.attrs['href'])
    return internalLinks

# retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    # initialize blank array
    externalLinks = []
    # finds all links that start with "http" or "www" that do
    # not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                # append a new link with attribute href to the end of the array externalLinks
                externalLinks.append(link.attrs['href'])
    return externalLinks

# splite address to get addressParts
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

# function get random external link
def getRandomExternalLink(startingPage):
    # retrieve HTML string from the url
    html = urlopen(startingPage)
    # create a BeautifulSoup object
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,
                                  len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

# call followExternalOnly with parameter http://oreilly.com
followExternalOnly("http://oreilly.com")
