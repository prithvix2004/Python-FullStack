str = ("Enter a string 'Open Source Lab'")

#1. Length of string
length = len(str)
print("Length of string is : ", len)

#2. Take substring 'source' in the string
print(str[5:12])

#3. Repeat the string 3 times
string3=str*3
print("String repeated 3 times : ", string3)

#4. Character in the 4th position
str[3]

#5. Extract 4 characters starting at index 6
print(str[6:10])

#6. Print all the characters except the last two
print(str[:-2])

#7. Append another string 'Programs' to the existing string
print("String 'Programs' added to the string : ", str+'Programs')

#8. Change the letter 'e' to '&'
print("String 'e' replaced to '&' : ", str.replace("e", "&"))

#9. Split the string using the letter 'o'
print("String splitted by using the letter 'o' : ", str.split('o'))

#10. Join the string using '#' symbol
print("Joined String : ", '#'.join(str))

#11. Justified the string (left and right)
j1 = str.ljust(10)
j2 = str.rjust(10)
print("Left Justify : ", j1)
print("Right Justify", j2)

#12. Change the case of the string
u = str.upper()
l = str.lower()
print("Uppercase : ", u)
print("Lowercase : ", l)