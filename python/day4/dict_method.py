# Dictionary Methods
# myDict.keys( ) #returns all keys
student={
    "name" : "loom logic",
    "subjects":{
        "phy":98,
        "math":97,
        "chem":96
    }
}

# print(student.keys())
# print(list(student.keys()))
# print(len(student.keys()))

# myDict.values( ) #returns all values
# print(student.values())
# print(list(student.values()))


# myDict.items( ) #returns all (key, val) pairs as tuples
# print(student.items())
# print(list(student.items()))

# pair=list(student.items()) #it will give tuple pair
# print(pair)
# print(pair[1])


# myDict.get("key") #returns the key according to value
# print(student["name2"]) #--> error
# print(student.get("name2")) # no error => None

# myDict.update( newDict ) #inserts the specified items to the dictionary/
# student.update({"city" : "delhi"})
# print(student)




