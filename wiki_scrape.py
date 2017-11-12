import urllib.request
from bs4 import *


soup = BeautifulSoup(urllib.request.urlopen("http://en.wikipedia.org/wiki/Steve_Jobs"), "html.parser")
title = soup.title.text
name = soup.find('span', {'class': 'nickname'}).text
bday = soup.find('span', {'class': 'bday'}).text
birthplace = soup.find('span', {'class': 'birthplace'}).text

print(name)
print(bday)
print(birthplace)
