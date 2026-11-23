a = input("Enter a string : ").lower()
temp =""
i=0


for x in range(len(str(a))):
    temp = a[i] + temp
    i += 1

if(temp == a):
    print("Palindrome..")

else:
    print("Not Palindrome..")