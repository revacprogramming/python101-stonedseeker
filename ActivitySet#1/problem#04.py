hrs = float(input("Enter hours"))
rate = float(input("Enter rate"))

if hrs <= 40:
 pay = hrs * rate
else: pay = (40 * rate + 1.5 * rate * (hrs - 40))

print(pay)
