my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_result = list(filter(lambda x : x % 2 == 0, my_list))
print("Even numbers from the said list : ", even_result)

odd_result = list(filter(lambda y : y % 2 != 0, my_list))
print("Odd numbers from the said list : ", odd_result)