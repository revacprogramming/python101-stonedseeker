# Dictionaries

#filename = "dataset/mbox-short.txt"

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = {}

for line in handle:
    if line.startswith('From'):
        name = line.split()
        d = name[1][2]
        d[name[2]] = d.get(name,0) + 1

user = max(d.items())
