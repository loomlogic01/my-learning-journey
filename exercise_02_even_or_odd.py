# Odd Or Even 
# input if types int equality comparison numbers mod
'''
Exercise 2 (and Solution)
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
'''

# Solution 1=>

num=int(input("enter a no."))

if(num % 2 == 0):
    print("even")

else:
    print("odd")


# ===== Solution 2: Simplified Even/Odd Check =====

# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("You picked an odd number.")
# else:
#     print("You picked an even number.")


# Solution 3 =>

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

# if num % 4 == 0:
#     print(num, "is a multiple of 4")
# elif num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")


# if num % check == 0:
#     print(num, "divides evenly by", check)
# else:
#     print(num, "does not divide evenly by", check)
