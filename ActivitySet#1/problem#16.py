# Databases
# https://www.py4e.com/lessons/database

import urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_1397978.xml"

data = urllib.request.urlopen(url).read().decode()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

lst = list()

for i in counts:
    num = int(i.text)
    lst.append(num)

print(f"sum = {sum(lst)}")
