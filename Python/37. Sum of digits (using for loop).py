a = int(input("Enter a number : "))
sum = 0

for x in range(len(str(a))):
    sum += a % 10
    a //= 10
print("Sum of digits : ", sum)