p = float(input("Enter Principle : "))
n = float(input("Enter Number of Months : "))
y = n/12
r = float(input("Enter Rate of Interest : "))

amount = p * (1 + (r / 100)) * y

print("Compound Interest : ", amount)