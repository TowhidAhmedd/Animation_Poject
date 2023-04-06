
#  w3resource

# 1. Write a Python program to create a lambda function that adds 15 to a given number
# passed in as an argument, also create a lambda function that
# multiplies argument x with argument y and prints the result.


# sum=lambda num: num+15
# print(sum(10))
#
# mul=lambda x,y: x*y
# print(mul(8,6))



# 2. Write a Python program to create a function that takes
# one argument, and that argument will be multiplied
# with an unknown given number.

# num=int(input("Enter a number:  "))
#
# mul=lambda n: n*15
# print(mul(num))


# 2. Another way to solve question 2

# def func_compute(num,n):
#     return lambda num: num * n
#
# num=int(input("Enter a number: "))
# result=func_compute(2,2)
# print(result(15))
#


# 3. Write a Python program to sort a list of tuples using Lambda.

# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:


# 4. lst=[('English',88),('Science',90),("Maths",97),("Social Scienses",82)]
#
# lst.sort(key = lambda x: x[1])
# print(type(lst))
# print(lst)



# 4. Write a Python program to sort a list of dictionaries using Lambda.


# dic=[{'make':'Nokia','model':216,'color':'bla'}, {'make':'Samsung','model':7,"color":'Blue'}]
#
# sort_dic=sorted(dic,key=lambda x: x['color'])
# print(sort_dic)





# 5. Write a Python program to filter a list of integers using Lambda.

# lst=[1,2,3,4,5,6,7,8,9,10]
#
# even_lst=filter(lambda num:num%2==0,lst)
# odd_lst=filter(lambda num:num%2!=0,lst)
#
# print(list(even_lst))
# print(list(odd_lst))



# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.


# lst=[1,2,3,4,5,6,7,8,9,10]
#
# sqr_lst = map(lambda num: num**2 , lst)
# cube_lst = map(lambda num: num**3 , lst)
#
# print(list(sqr_lst))
# print(list(cube_lst))
#



# 7. Write a Python program to find if a given string starts with a given character using Lambda.

# st_with=lambda cha: True if cha.startswith("P") else False
# end_with=lambda cha: True if cha.endswith("a") else False
#
# print(st_with("Python"))
# print(end_with("PHP"))

# 8. Write a Python program to extract year,month,date and time using Lambda.

# import datetime
# now=datetime.datetime.now()
# print(now)
#
# year=lambda y:y.year
# month=lambda m:m.month
# day=lambda d:d.day
# t=lambda t:t.time()
#
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))



# 9. Write a Python program to check whether a given string is a number or not using Lambda.

#
# pass
#
#
#
#
#
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


# # 12, Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#
# lst=[-1, 2, -3, 5, 7, 8, 9, -10]
# positive=sorted(lst,key = lambda i:0 if i==0 else -1/i)
# print(positive)




# 13.Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

#
# lst=[]
# end=int(input("How many numbers do you want: "))
#
# for item in range(end):
#     num=int(input("Enter any number: "))
#     lst.append(num)
# print(lst)
# #lst=[1,2,3,4,5,6,7,8,9]
# even_lst=len(list(filter(lambda num: (num%2==0),lst)))
# odd_lst=len(list(filter(lambda num: (num%2!=0),lst)))
#
# print(even_lst)
# print(odd_lst)





# 14. Write a Python program to filter a given list to determine if the values in the list have alength of 6 using Lambda.

# weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','sunday']
#
# days=list(filter(lambda day:day if len(day)==6 else None,weekdays))
#
# # print(days)
# for d in days:
#     print(d)




# 15. Write  a Python program to add two given lists using map and lambda.

# lst=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
#
# add=list(map(lambda x,y: x+y,lst,lst2))
# print(add)























