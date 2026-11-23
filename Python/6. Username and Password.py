username = "user12345"
password = "pass12345"
u = input("Enter username : ")
p = input("Enter password : ")
if(u == username and p == password):
    print("Access Granted..")
elif(u != username and p == password):
    print("Invalid Username.. Try Again..")
elif(u == username and p != password):
    print("Invalid Password.. Try Again..")
else:
    print("Access Denied..")