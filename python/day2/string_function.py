# String Functions
str = "i am a coder."

print(str.endswith("er.")) #returns true if string ends with substr
print(str.endswith("co"))


str = str.capitalize()
# print(str.capitalize()) #capitalizes 1st char
print(str)

print(str.replace("o","a")) #replaces all occurrences of old with new
print(str.replace("coder","programer"))


print(str.find("o")) #returns 1st index of 1st occurrence
print(str.find("x"))


print(str.count("a")) #counts the occurrence of substr in string
