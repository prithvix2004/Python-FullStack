a = int(input("Enter first number : "))
b = int(input ("Enter second number : "))
c = int(input("Enter third number : "))
if (a>b and a>c):
    if b>c:
        print("b is second")
    else:
        print("c is second")
elif b>a and b>c:
    if a>c:
        print("a is second")
    else:
        print("c is second")
else:
    if a>b:
        print("a is second")
    else:
        print("b is second")