age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible for voting..")
    if age >= 60:
        print(" and you are a senior citizen..")
else:
    print("You are not eligible for voting..")