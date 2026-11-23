unit = int(input("Enter a number : "))
charge = 0

if unit < 100 : #No charge
    print("No charge..")

elif unit >= 100 and unit < 200 :    #Rs : 5 per unit
    charge = unit + 5

elif unit >= 200 :   #Rs : 10 per unit
    charge = unit + 10

print("Electricity Charge : ", charge)