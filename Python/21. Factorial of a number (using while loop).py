num = int(input("Enter a number : "))

def factorial(num) :
    while (num != 0) :
        return num * factorial(num - 1)
    
    else :
        return 1

print(factorial(num))