a = 1
def num() :
        
        for i in range(1, 101) :
            
            if(i % 5 == 0):
                continue
            print(i)

print("Numbers from 1 to 100 without multiples of 5 : \n", a)
num()