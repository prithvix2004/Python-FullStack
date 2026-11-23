fruits = ['apple', 30, 'orange', 40]
print("Fruits list : ", fruits)

#1. Add the items 'grape, apple, 50' to the list
f = ['grape', 'apple', 50]
fruits.extend(f)
print("New Fruits : ", fruits)

#2. Find the lowest index in list that 'apple' appears
print("Lowest index of apple : ", fruits.index('apple'))

#3. Find the total number of occurences of item 'apple' in the list
print("Total occurences of 'apple' is: ", fruits.count('apple'))

#4. Remove the last item from the list
print("Last item removed from the list : ", fruits.pop())

#5. Remove '30' from the list
print("The element '30' removed from the list", fruits.remove(30))

#6. Sort the list in ascending and descending order
fruits2 = [str(x) for x in fruits]

fruits2.sort()
print("List in ascending order : ", fruits2)

fruits2.sort(reverse=True)
print("List in descending order : ", fruits2)

#7. Using append and extend functions, create copies of the list
f1 = []
f1.append('apple')
f1.append(30)
f1.append('orange')
f1.append(40)
print("Copy of list using append : ", f1)

f2 = ['apple', 30, 'orange', 40]
f2.extend(f1)
print("Copy of list using extend : ", f2)