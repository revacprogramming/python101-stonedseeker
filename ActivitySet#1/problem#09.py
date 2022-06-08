# Lists

#filename = "dataset/romeo.txt"

fh = open("mbox-short.txt")
count = 0
for line in fh:
    if line.startswith("From") and "From:" not in line:
        count +=1
        words = line.split()
        print(words[1])


print("There were", count, "lines in the file with From as the first word")
