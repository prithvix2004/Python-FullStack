tuple1 = ('perl', 'c', 'cpp', 'java', 'php', 'python')

#1. Display only the elements cpp, java, php
print("Elements are : ", tuple[2:5])

#2. Find the number of elements in the tuple
print(len(tuple1))

#3. Find the largest and smallest element
print("Largest Element : ", max(tuple1))
print("Smallest Element :", min(tuple1))

#4. Repeat the tuple elements two times
print("Repeated tuples", tuple1*2)

#5.Delete the tuple elements
del tuple1
print("Tuple Deleted..")