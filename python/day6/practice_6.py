# waf to print the length of list.(list is the parameter)
cities=["delhi", "pune", "mumbai", "noida", "gurgaon", "chennai"]
heroes=["thor", "ironman", "captain america", "shaktiman"]  

def print_len(list):
    print(len(list))

# #write a function to print the element of the list  in a single  line (list in parameter)
  

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print_list(heroes)

# # waf to find factorial of n (n is the parameter)

def cal_fact(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
    print("factorial=", fact)
    return fact

# cal_fact(5)

# # write a function to convert USD to INR

def con_usd(usd_value):
    inr_value= usd_value * 95
    print(usd_value , "USD=", inr_value, "INR")

con_usd(1)

# home work => number input --> function --> if num is odd - string "odd"
                                      #  --> if num is even - string "even"

def input_num(num):
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")

input_num(6)                                    










