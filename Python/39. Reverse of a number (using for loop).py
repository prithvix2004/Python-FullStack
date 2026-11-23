a = int(input("Enter a number : "))
rev = 0

for x in range(len(str(a))):
    last_a = a % 10
    rev = (rev * 10) + last_a
    a = a // 10

print("Reversed Number : ", rev)