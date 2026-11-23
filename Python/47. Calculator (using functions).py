a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
operator = input("Enter operator : ")

def sum(a, b):
    sum = a + b
    print("Addition : ", sum)

def sub(a, b):
    sub = a - b
    print("Subtraction : ", sub)

def mul(a, b):
    mul = a * b
    print("Multiplication : ", mul)

def div(a, b):
    div = a / b
    print("Division : ", div)

def mod(a, b):
    mod = a % b
    print("Modulus : ", mod)

if(operator == "+"):
    sum(a, b)

elif(operator == "-"):
    sub(a, b)

elif(operator == "*"):
    mul(a, b)

elif(operator == "/"):
    div(a, b)

elif(operator == "%"):
    mod(a, b)

else:
    print("Invalid Operator..")