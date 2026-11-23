calls = float(input("Enter a number : "))
charge = 0

if calls < 100 : #Minimum Rs : 200 for up to 100 calls
    charge = 200 + calls

elif calls >= 100 and calls < 150 :    #Plus, Rs : 0.60 per call for next 50 calls
    charge = 200 + (calls - 100) * 0.60

elif calls <= 200 :   #Plus, Rs : 0.50 per call for next 50 calls
    charge = 200 + (calls - 100) * 0.50

else :
    charge = 200 + (calls - 100) * 0.40

print("Telephone Bills : ", charge)