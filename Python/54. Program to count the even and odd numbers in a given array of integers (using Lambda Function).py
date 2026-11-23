my_list = [1, 2, 3, 5, 7, 8, 9, 10]

even_result = list(filter(lambda x : x % 2 == 0, my_list))
print("Number of even numbers in the above array", len(even_result))

odd_result = list(filter(lambda y : y % 2 != 0, my_list))
print("Number of odd numbers in the above array : ", len(odd_result))