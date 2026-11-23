a = int(input("Enter a number : "))
temp = a
sum_Power = 0
n = len(str(a))

while temp > 0:
    digit = temp % 10
    sum_Power += digit ** n
    temp = temp // 10

if (sum_Power == a):
    print("Armstrong..")
else:
    print("Not Armstrong..")