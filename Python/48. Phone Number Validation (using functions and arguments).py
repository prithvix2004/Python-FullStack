def p_no(ph_no):
    if(len((ph_no))== 10) and ph_no.isdigit() and ph_no[0] in ["9","8","7","6"]:
        return True #Function returns Boolean value.

    else:
        return False    #Function returns Boolean value.

phone_number = (input("Enter a phone number : "))

if p_no(phone_number):
    print("Valid Phone Number..")   #When function returns True. 

else:
    print("Invalid Phone Number..") #When function returns False.