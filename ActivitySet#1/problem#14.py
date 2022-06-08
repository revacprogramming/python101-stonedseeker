<<<<<<< HEAD
# # Using Web Services
# # https://www.py4e.com/lessons/servces

import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
#counts = dict()
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1397976.html')

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1397976.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

for tag in tags:
    x = re.findall('[0-9]+',str(tags))

sum = 0
for i in range(0,len(x)):
    sum = sum + int(x[i])

print(sum)

# print(str(fhand))


# numbers = re.findall('^span [0-9]+',str(fhand))
# print(numbers)

# sum = 0

# for i in range(0,len(numbers)):
#     sum += int(numbers[i])

# print(sum)

# # for line in fhand:
# #     words = line.decode().strip()
# #     for word in words:
# #         counts[word] = counts.get(word, 0) + 1
# # print(counts)
=======
# Object Oriented Programming
# https://www.py4e.com/lessons/Objects

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import ssl
# import webbrowser
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# count = input("Enter the count till which you want to run the loop")
# pos = input("Enter the pos till which you want to run the loop")
# # Retrieve all of the anchor tags
# tags = soup('a')

# for tag in tags:
#      for tags in range(3):
#         tags()
#     #print(re.findall(r".+known_by_*",str(tags)))

#print(soup.prettify())

article = re.findall(r".*/known_by_(.*)\..*",str(html))
print(article)
#print(anchor.prettify)

#name = href.a.text
>>>>>>> 81ea93cf55ff3b4a15b73c140f5184a6f0bd29f9
