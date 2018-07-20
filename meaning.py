import urllib.request
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import textwrap
word = input('Enter the word of which you want to find the meaning: ')

# Get the meaning by scrapping www.vocabulary.com
url = "https://www.vocabulary.com/dictionary/" + word + ""
page = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
page = page.text
soup = BeautifulSoup(page, 'html.parser')
for i in range(20):
    try:
        definition = soup.find_all('h3', attrs={'class': 'definition'})[i]
        definition = definition.text
    except:
        pass
print("-" * 65)
for j in range(20):
    try:
        f=0
        instance = soup.find_all('dl', attrs={'class': 'instances'})[j]
        instance = instance.text
        if(instance.split()[0] == "Synonyms:"):
            print(instance)
        elif(instance.split()[0] == "Type"):
            print(instance)
            f=1
        if(f==1):
            print("-" * 65)
    except:
        exit()
