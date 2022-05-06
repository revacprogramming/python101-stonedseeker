big = 0
small = 9999999999999999

while True:
    num = input("Enter a number\n")
    if num == 'done':
        break
    try:
        n = int(num)
    except:
     print("Invalid Num")

    if(n > big): big = n
    elif(n < small): small = n

print("Big = ", big)
print("Small = ",small)
