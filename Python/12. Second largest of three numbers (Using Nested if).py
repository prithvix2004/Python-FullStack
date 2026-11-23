a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if (a > b and a > c):
    if (b > c):
        print(b, " is second largest..")
    else:
        print(c, " is second largest..")

elif (a < b and b > c):
    if (a > c):
        print(a, " is the second largest..")
    else:
        print(c, " is the second largest..")

else:
    if(a > b):
        print(a, " is the second largest..")
    else:
        print(b, " is the second largest..")