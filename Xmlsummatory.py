import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input ('Enter Location: ')  #user input url
print('Retrieving: ', url)
uh = urllib.request.urlopen(url, context=ctx) #opening url

data = uh.read()    #read the data
print('Retrieved', len(data), 'characters')  # we display the lenght od the xml

tree = ET.fromstring(data)

counts = tree.findall('comments/comment')  #we find everycomment
print ('Count: ',len(counts))    #how many comments there are
summary=list()            #we create a list
for item in counts:
  summary.append(int(item.find('count').text))   #for loop on the xml  so we can take any value of it

print ('Sum:',sum(summary))
