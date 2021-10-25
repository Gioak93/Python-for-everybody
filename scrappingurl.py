# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

x=0

repeat = int(input('Enter Repeat:  ',))
count =  int(input('Enter count:  ',))
url = input('Enter - ')

links=list()

for x in range(0,repeat):
    links.clear()

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    n=0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        link=tag.get('href', None)
        links.append(link)
        n=n+1
        if n == count:
            print(links[count-1])
            url=links[count-1]
            continue
