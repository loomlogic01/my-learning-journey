#1.create a new file "practice.txt",using python.add the following data in it.

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nWe are learning File I/O\nusing java\nI like programing in java")

#2.waf tha replace occurences of "java" with "python" in above file

# with open("practice.txt", "r") as f:
#     data=f.read()

# new_data=data.replace("java", "python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if (data.find(word) != -1):
#             print("Found")
#         else:
#             print("not found")

# check_for_word()

# waf to find in which line does the word learnig occur first print-1 if word not found 

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()

# form a file  containing numbers separated  by comma, print the count of even number.
count=0
with open("practice.txt", "r") as f:
    data= f.read()
    

# basic method
# num= ""
# for i in range(len(data)):
#     if (data[i] == ","):
#         print(int(num))
#         num = ""
#     else:
#         num +=data[i]

# 2nd method

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count+=1

    print(count)