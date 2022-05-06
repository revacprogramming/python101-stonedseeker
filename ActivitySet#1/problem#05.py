def computepay(hrs, rate):
    if(hrs < 40):
        pay = hrs * rate
    else:
        pay = 40 * rate + 1.5 * rate * (hrs - 40)
    return pay

hrs = float(input("Enter hours\n"))
rate = float(input("Enter rate\n"))

p = computepay(hrs,rate)

print("Pay = ",p)
