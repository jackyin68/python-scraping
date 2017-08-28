import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Firefox/55.0 (Macintosh; Intel macOS High Sierra 10.13 Beta) AppleWebKit 2.16.6 (KHTML, like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"
req = session.get(url, headers=headers)

bsObj = BeautifulSoup(req.text, "lxml")
print(bsObj.find("table",{"class":"table-striped"}).get_text)
