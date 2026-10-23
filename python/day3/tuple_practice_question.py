# # QuesNo.1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# # type1
# movies=[]
# mov1=input("enter movie no.1 : ")
# mov2=input("enter movie no.2 : ")
# mov3=input("enter movie no.3 : ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# # type 2
# movies=[]
# mov1=input("enter movie no.1 : ")
# movies.append(mov1)
# mov2=input("enter movie no.2 : ")
# movies.append(mov2)
# mov3=input("enter movie no.3 : ")
# movies.append(mov3)
# print(movies)


# # type 3
# movies=[]
# movies.append(input("enter mov1"))
# movies.append(input("enter mov2"))
# movies.append(input("enter mov3"))
# print(movies)


# #Ques.No2. WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# list=[1, 2, 3, 2, 1]
# # list=["a", "m", "m", "a"]
# copy_list=list.copy()
# copy_list.reverse()

# if(copy_list == list):
#     print("palindrome")
# else:
#     ("not palidrome")


# WAP to count the number of students with the “A” grade in the following tuple.

grade=["C","D","A","A","B","B","A"]
print(grade.count("A"))

# Store the above values in a list & sort them from “A” to “D”

# Store values in a list
values = ["D", "B", "A", "C"]

# Sort the list alphabetically (A → D)
values.sort()

# Display the sorted list
print("Sorted list:", values)
