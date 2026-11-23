temperature = float(input("Enter Temperature : "))
tunit = input("Enter Unit : ")
if tunit=="c":
    fahrenheit=(temperature*(9/5))+32
    print("Fahrenheit : ", fahrenheit)
else:
    celsius=(temperature-32)*5/9
    print("Celsius : ", celsius)