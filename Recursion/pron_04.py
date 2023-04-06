

# Write a Python program to get the factorial of a non-negative integer.



# s=0
# def sum(n):
#     global s
#     if n<0:
#         s+=n
#         return sum(n+1)
#     return s
#
# print(sum(-5))







def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(5))




























