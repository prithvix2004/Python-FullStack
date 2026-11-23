grade = float(input("Enter your grade : "))
if(grade >= 90):
    print("A Grade..")
elif(grade < 90 and grade >= 80):
    print("B Grade..")
elif(grade < 80 and grade >= 70):
    print("C Grade..")
elif(grade < 70 and grade >= 60):
    print("D Grade..")
else:
    print("Fail..")