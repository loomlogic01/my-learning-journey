
# wap to input user's first name and print its length
first_name=input("enter your first name=")
len=len(first_name) #imp
print(len)


# wap to find the occurance of $ in the sting
str="$ i have 88 $"
print(str.count("$"))

# WAP to check if a number entered by the user is odd or even.
num=int(input("enter the number"))
if(num%2 == 0):
    print("even")
else:
    print("odd")


# WAP to find the greatest of 3 numbers entered by the user.
a=int(input("enter 1st no."))

b=int(input("enter 2nd no."))

c=int(input("enter 3rd no."))

if(a > b and a > c):
    print(a,"is greater no.")
elif(b > c):
    print(b," is the greater no.")
else:
    print(c ,"is the greater no.")

# WAP to check if a number is a multiple of 7 or not.

num=int(input("enter  the number:"))
if(num % 7 == 0):
    print(num,"is the is multiple of 7 ")
else:
    print(num," is not the multiple of 7")





