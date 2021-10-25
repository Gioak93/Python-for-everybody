# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
wordsofthearticule=list()
counts=dict()
url = input('Enter - ')


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')

print (len(tags))
numero=len(tags)
n=0
for words in range(0,numero):
    words= tags[n].text.rstrip()
    wordsofthearticule.append(words)
    n=n+1

print(wordsofthearticule)
