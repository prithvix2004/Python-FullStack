a = int(input("Enter a number : "))
temp = a
sum_power = 0
n = len(str(a))

while temp > 0:
    digit = temp % 10
    sum_power += digit ** n
    temp = temp // 10

if (sum_power == a):
    print("Armstrong..")
else:
    print("Not Armstrong..")