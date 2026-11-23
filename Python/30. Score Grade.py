score = float(input("Enter your score : "))
grade = 0

if score >= 0.9 and score <= 1.0 :
    print("Grade : a")

elif score >= 0.8 and score <= 0.9:
    print("Grade : b")

elif score >= 0.7 and score <= 0.8:
    print("Grade : c")

elif score >= 0.6 and score <= 0.7:
    print("Grade : d")

elif score < 0.6 :
    print("Grade : f")

else :
    print("Invalid score..")