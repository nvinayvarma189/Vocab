# import urllib2
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
word = 'irreversible'
url = 'https://en.wiktionary.org/wiki/'+word
page = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
page = page.text
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('span', attrs={'class': 'form-of-definition'})
try:
    price = name_box.text
    print(price)
    print("Headword:",price.split()[-1])
except:
    print(word)
print(url)
