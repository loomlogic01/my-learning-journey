# Exercise 1 (and Solution)
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# solution =>
name=input("enter your name:")
age=int(input("how old are you:"))
current_year=2026
year_turn_100=current_year + (100-age)
print(name,"your age is ",age)
print("current_year is :",current_year,"\nyou will turn 100 years old on",year_turn_100)
# print(f"Hello {name}, you are {age} years old.")
# print(f"You will turn 100 years old in the year {year_turn_100}.")


