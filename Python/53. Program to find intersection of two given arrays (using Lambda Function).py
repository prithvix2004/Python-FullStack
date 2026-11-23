array_1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_2 = [1, 2, 4, 8, 9]

intersection = list(filter(lambda x : x in array_2, array_1))

print("Intersection of said arrays : ", intersection)