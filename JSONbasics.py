import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total=list()

url= input ('Enter Location: ')  #user input url
print('Retrieving: ', url)
uh = urllib.request.urlopen(url, context=ctx) #opening url

data = uh.read()    #read the data
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info['comments']))
x = info['comments']

for items in x:

    y= (items['count'])
    total.append(int(y))

print ('Sum :', sum(total))
