p = int(input("Enter Principle : "))
n = int(input("Enter Number of Months : "))
r = int(input("Enter Rate of Interest : "))

emi = (p*r*(1 + r)^n) / ((1 + r)^n - 1)

print("EMI : ", emi)