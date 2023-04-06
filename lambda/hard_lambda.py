
# 9. Write a Python program to check whether a given string is a number or not using Lambda.

#  pass



# 10. Write a Python program to create Fibonacci series up to n using Lambda.
# you should try again

# from functools import reduce
#
# fib_series = lambda n: reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1])
#
# print(fib_series(2))
# print(fib_series(5))



# 11. Write a Python program to find the intersection of two given arrays using Lambda.

# lst=[1,2,3,5,7,8,9,10]
# lst2=[1,2,4,8,9]
# lst3=[]
#
# result=filter(lambda num:num in lst,lst2)
# print(list(result))





# 12, Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#
# lst=[-1, 2, -3, 5, 7, 8, 9, -10]
# positive=sorted(lst,key = lambda i:0 if i==0 else -1/i)
# print(positive)











