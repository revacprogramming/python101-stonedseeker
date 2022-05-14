# Strings

# text = "X-DSPAM-Confidence:    0.8475"
count = 0;
total = 0;
fname = input("Enter file name\n")
f = open(fname)
for line in f:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        i = line.find(":")
        data = float(line[i+1:])
        total += data

avg = (total/count)

print("Average spam confidence:",avg)
f.close
