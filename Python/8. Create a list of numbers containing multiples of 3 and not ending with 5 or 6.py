def multi(mn,mx) :
    l = []
    for i in range(mn, mx + 1) :
        
        if(i % 3 == 0) :
            rem = int(i % 10)
            
            if(rem != 5 and rem != 6) :
                l.append(i)
        
    print("The list is : \n", l)
    
a = int(input("Enter minimum limit : "))
b = int(input("Enter maximum limit : "))
multi(a, b)