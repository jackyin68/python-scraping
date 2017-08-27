# import the urlopen library
from urllib.request import urlopen
# retrieve HTML string from the URL
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# print the HTML content of the page
print(html.read())
