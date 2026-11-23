i = 1
sum = 0
for x in range(2, 101):
    j = 1
    count = 0

    for y in range(j, i + 1):
        if(i % j == 0):
            count += 1
        j += 1
    
    if(count == 2):
        sum += i
    i += 1

print("Sum : ", sum)