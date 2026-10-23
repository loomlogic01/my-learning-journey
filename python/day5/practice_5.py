# using for 

#1 print the element in the following list
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in list:
#     print(el)

#2 search fo a number x in this tuple using loop
# tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16)
# x=16
# # find x
# idx=0 
# for el in tup:
#     if (el==16):
#         print ("x found at index",idx)
#         break
#     idx+=1

# use for and range
# 1.print no. from 1 to 100
# 2.print no. from 100 to 1
# 3.print multiplication table of a number n

# 1.
# for i in range(1, 101):
#     print(i)

# # 2
# for i in range(100, 0, -1):
#     print(i)

#3.
# n=2
# for i in range(0, 11, 1):
#     print(n*i)

# 4.write a program to find the the 1st  n  number(using while)

# using for
# n=5
# sum=0
# for i in range(1, n+1):
#     sum+= i
# print("sum is :",sum)

# using while
# n=6
# i=1
# sum=0
# while i<n:
#     sum+=i
#     i+=1
# print("sum is :", sum)

# 5.
# n=6
# i=1
# fact=1
# while i<n:
#     fact*=i
#     i+=1
# print("fact is :", fact)

n=6
i=1
fact=1
for i in range(1, n):
    fact*=i
print("fact is :", fact)




