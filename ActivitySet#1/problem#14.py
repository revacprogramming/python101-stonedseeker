# Using Web Services
# https://www.py4e.com/lessons/servces
# # Using Web Services
# # https://www.py4e.com/lessons/servces

# import urllib.request, urllib.parse, urllib.error
# import re
# from bs4 import BeautifulSoup
# #counts = dict()
# fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1397976.html')
# print(str(fhand))


# # numbers = re.findall('[0-9]+',fhand)
# # print(numbers)

# # sum = 0

# # for i in range(0,len(numbers)):
# #     sum += int(numbers[i])

# # print(sum)

# # for line in fhand:
# #     words = line.decode().strip()
# #     for word in words:
# #         counts[word] = counts.get(word, 0) + 1
# # print(counts)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page1.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href',None))
