try:
    filename = input("Enter the filename : ")
    with open("filename", "r") as file:
        content = file.read()
        print(content)
    
except FileNotFoundError:
    print("Error : The file you are trying to open does not exist..")

except Exception as e:
    print(f"An unexpected error occured : {e}")

finally:
    print("File Handling completed..")