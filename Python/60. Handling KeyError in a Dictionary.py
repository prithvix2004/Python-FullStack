try:
    dictionary = {'name' : 'Alice', 'age' : 25}
    key = input("Enter key you want to access : ")
    print(f"Value : {dictionary[key]}")

except KeyError:
    print("Error : Key does not exist in dictionary..")

finally:
    print("Dictionary access completed..")