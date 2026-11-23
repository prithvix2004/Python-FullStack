import math
def quadratic() :
    print("This program finds the real solutions to a quadratic equation..")
    
    try :
        a = int(input("Enter coefficients of a : "))
        b = int(input("Enter coefficients of b : "))
        c = int(input("Enter coefficients of c : "))
        
        d = int(b ** 2 - 4 * a * c)
        
        if d == 0 :
            x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            print("This equation has one solutions : ", x)
        
        else :
            x1 = int((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            x2 = int((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            print("This equation has two solutions : ", x1, x2)
        
    except ValueError :
        print("No real roots..")

quadratic()