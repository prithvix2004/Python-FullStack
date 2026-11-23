animal = {
    "A" : "Ant",
    "B" : "Bee",
    "C" : "Cat",
    "D" : "Dog",
    "E" : "Eagle"
}

#1. Display all the words
print("The words are :", animal.keys())

#2. Display all word meanings
print("The meanings are : ", animal.values())
print("A : ", animal["A"])
print("B : ", animal["B"])
print("C : ", animal["C"])
print("D : ", animal["D"])
print("E : ", animal["E"])

#3. Display all key value pairs in a neat format with the help of the built in function


#4. Use all dictionary built in functions
animal1={
    "A" : "Ant",
    "F" : "Fox"
}

print("Using built in functions : ")

print(len(animal))

print("String representation of a dictionary : ", str(animal))

print("The type is : ", type(animal))

print("Copy of dictionary : ", animal.copy())

print("Clearing dictionary elements : ", animal1.clear())

seq = {1, 2, 3, 4, 5}
print(animal.fromkeys(seq, "Ant"))

print("Value of C is : ", animal.get("Cat"))
print("Check whether D is present or not : ")
if "D" in animal:
    print("Yes, D is present")
else :
    print("No, D is not present")

print("Dictionary Items : ", animal.items())

print("List of keys : ", animal.keys())

print("Adding new keys : ", animal.setdefault("F", "Fox"))

animal2 = {"G" : "Goat"}
print("After updatin : ", animal.update(animal2))
print(animal)

#5. Update the dictionary by adding key value "compute"
new = {"compute" : "calculate"}
print("After adding compute : ", animal.update(new))
print(animal)

#6. Delete the item with key value "compute"
print("After deleting compute : ", animal.pop("compute"))   #pop() deletes specific item, while popitem() deletes last item from dictionary.

#7. Delete all the items of the dictionary with the help of a built in function
print("Deleting all items in dictionary..", animal.clear())

#8. Delete the entire dictionary
print("Deleting dictionary..")
del animal