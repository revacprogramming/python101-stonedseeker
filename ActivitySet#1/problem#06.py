big = 0
small = 9999999999999999
#ypur code doesnt work  for negative numbers or numbers beyound range!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
#you are a total idiot
