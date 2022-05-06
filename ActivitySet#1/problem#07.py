# Strings

# text = "X-DSPAM-Confidence:    0.8475"
fname = input("Enter File Name")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        x = line.find(":")
        y = line[x+1:]
        s = float(y)
        total = total + s 
        continue
    average = total / count

    print("Average spam confidence:",average)

fh.close
