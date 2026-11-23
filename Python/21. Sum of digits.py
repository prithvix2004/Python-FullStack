a = int(input("Enter a number : "))
sum = 0
while (a > 0):
    sum += a % 10
    a //= 10
print("Sum of digits : ", sum)