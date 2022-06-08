# # Object Oriented Programming
# # https://www.py4e.com/lessons/Objects

# # To run this, download the BeautifulSoup zip file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import requests
# import ssl
# # import webbrowser
# import re

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # count = input("Enter the count till which you want to run the loop")
# # pos = input("Enter the pos till which you want to run the loop")
# # # Retrieve all of the anchor tags
# # tags = soup('a')

# # for tag in tags:
# #      for tags in range(3):
# #         tags()
# #     #print(re.findall(r".+known_by_*",str(tags)))

# #print(soup.prettify())

# article = re.findall(r".*/known_by_+",str(html))
# print(article)
# #print(anchor.prettify)

# #name = href.a.text

###freeCodeCamp
import ssl
import urllib.request, urllib.parse, urllib.error
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
from bs4 import BeautifulSoup
url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'lxml')
import re
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

content = soup.html

tags = soup.find_all('a')

for tags in tegs:
# for tags in tags:
#     #names = re.findall(r"/known_by_.+",str(html))
#     names = soup.find_all("")


