import requests

params = {'firstname': 'Sam', 'lastname': 'Zhu'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)
