list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, list_1, list_2))

print("Result after adding two lists:", result)