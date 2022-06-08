# Files

#filename = "dataset/mbox-short.txt"

fname = input("Enter File Name")
fh = open(fname)
lst = list()
for line in fh:
    line=line.split()
    for word in line:   
     if word not in lst:
        lst.append(word) 

lst.sort()
print(lst)
