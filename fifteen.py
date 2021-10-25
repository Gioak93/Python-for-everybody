# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


z = 0 #contador


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')  #ingresamos url
count =  int(input('Enter count:  ',)) #definimos el nummero en el cual se entrara al link
repeat = int(input('Enter Repeat:  ',)) #definimos el numero de veces que se hara el proceso


while z <= repeat:                        #se establece el while para repetir el proceso varias veces
    n=0                                  #definimos el contador para establecer la posicion
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    indice=list()
    # Retrieve all of the anchor tags
    tags = soup('a')
    print('redirecting:', url)
    for tag in tags:
        url=tag.get('href', None) #redefinimos url para que ahora sea el nuevo link
        indice.append(url)
        n = n + 1
        if n == count:
            z=z+1
            print (indice)
            url=indice[count-1]
            continue




# print (len(indice))
        # n = n + 1
    #     if n == count:
    #          z = z + 1  #conteo para deficnir el numero de veces que se hara el proceso
    #          print(url)
    #          continue
    # continue
