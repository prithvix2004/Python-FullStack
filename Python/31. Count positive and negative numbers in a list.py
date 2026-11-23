list_1 = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10,0,9]

positive_num = 0
negative_num = 0
zero_count=0

for i in list_1:
    if i>0:
        positive_num+=1
    elif i==0:
        zero_count+=1
    else:
        negative_num+=1

print(positive_num)
print(negative_num)
print(zero_count)