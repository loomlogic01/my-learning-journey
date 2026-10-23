#Q1. #store following word meanings in python dictionary:
#table:"a piece of furniture", " list of facts and figures"
#cat:"a small animal"
dict={
    "table":["a piece of furniture","list of fact and figure"],
    "cat":"a small animal"


}

print(dict)

"""Q2.You are given a list of subject for student. assume one classroom is required for 1
subject. How many classroom are needed by all student.
"python","java","c++","python", "javascript", "java", "python","java", "c++", "c"
"""
# dict=set(["python","java","c++","python", "javascript", "java", "python","java", "c++", "c"])
# print(len(dict))

subject={
    "python","java","c++","python", "javascript", "java", "python","java", "c++", "c"
}
print(subject)
print(len(subject))

# Q3 WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}

x=int(input("enter physics marks:"))

marks.update({"physics": x})

y=int(input("enter chemistry marks:"))

marks.update({"chemistry": y})

z=int(input("enter math marks:"))

marks.update({"math": z})

print(marks)

#Figure out a way to store 9 and 9.0 as separate value in the set
# (you can take help of built in data type)
values={
    ("float",9.0),
    ("int",9)

}
print(values)