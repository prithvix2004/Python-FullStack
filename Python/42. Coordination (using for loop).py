a = 0
b = 0

for x in range(a, 3):
    b = 0
    
    for y in range(b, 3):
        print(f"({x},{y})",end="")  #end is used for horizontal output
        y+=1
    print() #print() is used for displaying output.
    x+=1