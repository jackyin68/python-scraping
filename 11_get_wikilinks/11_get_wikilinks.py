# import the urlopen library
from urllib.request import urlopen
# import the BeautifulSoup library
from bs4 import BeautifulSoup
# import mudule datetime
import datetime
# import module random to generate random numbers
import random
# import module regular expressions
import re

# set the random number generator seed with the current system time
random.seed(datetime.datetime.now())
# define getLinks() function
def getLinks(articleUrl):
    # retrieve HTML string from a wiki article url with /wiki/... prepends the wikipedia domain name
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    # create a BeautifulSoup object
    bsObj = BeautifulSoup(html, "html.parser")
    # extract a list of article link tags
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
# set a list of article link tags to the list of links in the initial page  https://en.wikipedia.org/wiki/Kevin_Bacon
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    # find a random article link tag in the page, extract the href attribute from it
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    # print the page
    print(newArticle)
    # get a new list of links from the extracted url
    links = getLinks(newArticle)
