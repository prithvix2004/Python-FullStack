a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

try :
    res = a / b
    print("Result : ", res)

except ZeroDivisionError :
    print("Error : Division by zero..")