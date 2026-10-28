# recursive function
# def show(n):
#     if (n==0): #base case
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(5) # 5 = n, 4 = n-1, 3 = n-2, 2 = n-3, 1 = n-4

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(6))

# write  a recursive  function to calculate  the sum of first n natural numbers.
# def calc_sum(n):
#     if (n==0):
#         return 0
#     return calc_sum(n-1) + n

# sum=calc_sum(4)
# print(sum)

# write a recusive function to print  all elements  in list
# Hint: use list  and index as parameter

index=0
def print_list(list, index=0):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)

# index=0
fruits=["mango", "bannana", "litchi", "apple"]
print_list(fruits)
