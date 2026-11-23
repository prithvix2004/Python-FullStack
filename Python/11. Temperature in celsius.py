def temp_convert(var) :
    try :
        var = int(var)
        fnht = 9.0/5.0*var+32
        print("In Fahrenheit : ", fnht)

    except ValueError :
        print("The argument does not contain numbers..")
        print("Error message : ")
    
clus = input("Enter temperature in Celsius : ")
temp_convert(clus)