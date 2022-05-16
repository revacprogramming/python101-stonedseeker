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
    numbers = re.findall('[0-9]+',str(tags))

sum = 0
for i in range(0,len(x)):
    sum = sum + int(numbers[i])
 
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
