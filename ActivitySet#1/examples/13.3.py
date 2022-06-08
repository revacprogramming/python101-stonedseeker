# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = ('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# x = {}
# # Retrieve all of the anchor tags
# tags = soup.find_all('a')
# for tag in tags:
#    x = (tag.contents[0])

# print(x)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve all of the anchor tags
url = input('Enter URL:')
c=input('Enter counts:')
p=input('Enter position:')

ct=int(c)
ps=int(p)
count=1

while True:
    if count > ct:
        break
    #print('O',url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count=count+1
    #print(count)
    ls=list()

    for tag in tags:
        urls=tag.get('href', None)
        #print(urls)
        # name=tag.contents[0]
        #print(name)
        ls.append(urls)
        #print(ls)
    url=ls[ps-1]
    #print('R',url)
print(url)