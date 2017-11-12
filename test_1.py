import requests
from BeautifulSoup import BeautifulSoup


url = 'http://lbc.care'
response = requests.get(url)
html = response.content
print (html)
