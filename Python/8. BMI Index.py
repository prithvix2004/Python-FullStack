weight = float(input("Enter your weight : "))
heightincm = float(input("Enter your height in cm : "))
heightinm = heightincm / 100
bmi = weight / (heightinm**2)
if(bmi <= 18.9):
    print("Underweight..")
elif(bmi>18.9 and bmi<=24.5):
    print("Normal..")
elif(bmi>24.5 and bmi<=30):
    print("Overweight..")
else:
    print("Obese..")