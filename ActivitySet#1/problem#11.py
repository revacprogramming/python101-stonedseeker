# Tuples

#filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = {}

for line in handle:
    if line.startswith("From "):
        
        line = line.split()
        line = line[5]
        line = line[0:2]
        di[line]=di.get(line,0)+1
        
lst = list()
for v,c in di.items():
    lst.append((v,c))

lst.sort()

for v,c in lst:    
 print(v,c)
