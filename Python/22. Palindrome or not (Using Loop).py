x = input("Enter a string : ").lower()
temp =""
i=0
while i<len(x):
    temp=x[i]+temp
    i+=1
if (temp == x):
    print("Palindrome..")
else:
    print("Not Palindrome..")