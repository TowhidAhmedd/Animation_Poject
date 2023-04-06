

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# lst=[]
# for i in range(1500,2700+1):
#     if i%7==0 and i%5==0:
#         lst.append(i)
# print(lst)



# 2. Write a Python progtam to convert temperatures to and from Celsius and Fahrenheit.


# 3. Write a Python program to guess a number between 1 and 9.

# number=int(input("Enter a number: "))
# import random
# for i in range(1,10):
#     if i!=5:
#         number = int(input("Enter again number: "))
#     else:
#         print("Well")


# 4. Write a Python program to construct the following pattern, using a nested for loop.

# num=5
# for i in range(num):
#     for j in range(i):
#         print("* ",end=" ")
#     print(' ')
#
# for i in range(num,0,-1):
#     for j in range (i):
#         print("* ",end=" ")
#     print(' ')

# num=10
# for i in range(num):
#     for j in range(i):
#         print(" * ",end='')
#     print(" ")
# for i in range(num,0,-1):
#     for j in range(i):
#         print(" * ",end='')
#     print(" ")




# 5. Write a Python progtam that accepts a word from the user and reverses it.

# num=input("Enter : ")
#
# for char in range(len(num)-1,-1,-1):
#     print(num[char],end=" ")


# 6. Write a Python program to count the number of even and odd numbers
# in a series of numbers. Sample: numbers(1,2,3,4,5), odd=3, and even=2

# num=(1,2,3,4,5,6,7,8,9)
# count_even=0
# count_odd=0
#
# for find in num:
#     if find%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
#
# print("Number of even numbers: ",count_even)
# print("Number of odd numbers: ",count_odd)



# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List: datalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V',"section":'A'}]


# datalist=[1452,11.23,1+2j,True,'w3resorce',(0,-1),[5,12],{"class":'V',"section":"A"}]
#
# for item in datalist:
#     print("Type of",item," is ",type(item))


# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# number=[0,1,2,3,4,5,6]
#
# for i in number:
#     if i==2 or i==6:
#         continue
#     print(i,end=" ")


# 9. Write a Pyton program to get the Fibonacci series between 0 and 50.


# number1=0
# number2=1
# print(number1)
# print(number2)
#
# for item in range(1,50+1):
#     sum=number1+number2
#     number1=number2
#     number2=sum
#     print(sum)



# 10. Write a Python program that iterates the integers from 1 to 50.


# num=50
#
# for i in range(51):
#
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#         continue
#     elif i%3==0:
#         print('Fizz')
#         continue
#     elif i%5==0:
#         print("Buzz")
#         continue


















