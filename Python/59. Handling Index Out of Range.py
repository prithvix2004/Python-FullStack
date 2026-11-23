try:
    lst = [1, 2, 3]
    index = int(input("Enter index you want to access : "))
    print(lst[index])

except IndexError:
    print("Error : Index out of range..")

except ValueError:
    print("Error : Invalid input.. Enter an integer..")

finally:
    print("List access completed..")