try:
    num = int(input("Enter a number : "))
    print(num = 5)  #This will raise a TypeError if num is a string.

except TypeError:
    print("Error : Cannot add a string and an integer..")

finally:
    print("Type handling completed..")