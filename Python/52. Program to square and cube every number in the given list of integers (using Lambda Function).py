my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_result = list(map(lambda x : x**2, my_list))
print("Square every number of the said list", square_result)

cube_result = list(map(lambda x : x**3, my_list))
print("Cube every number of the said list : ", cube_result)