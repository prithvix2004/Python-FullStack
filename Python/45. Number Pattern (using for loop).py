row = 4
num = 1
i = 1

for x in range(i, row + 1):
    j = 1
    for y in range(j, i + 1):
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1