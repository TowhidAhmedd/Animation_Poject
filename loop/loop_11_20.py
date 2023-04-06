

#  11. Write a Pyton Write a Python program that takes two digits m (row) and n (column)
#  as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1



# 12.Write a Pyton program that accepts a sequence of lines (blank line to
# terminate) as input and prints the lines as output (all characters in lower case).

# line=[]
# while True:
#     user=input("ENTER: ")
#     if user:
#         line.append(user.upper())
#     else:
#         break
#
# for i in line:
#     print(i)



# 13. Write a  Python program that acceptt sequence of comma separated 4 digit binary numbers as its input.The program wil print the numbers that divisible by 5 in a comma seperated sequence.

# item=[]
# num=[x for x in input().split(',')]
# for i in num:
#     x=int(i,2)
#     if x%5==0:
#         item.append(i)
# print(','.join(item))



#  14. Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data; Python 3.2
# Letters 6
# Digits 2

# user_input=input("Input a string: ")
# d=a=0
#
# for i in user_input:
#     if i.isdigit():
#         d+=1
#     elif i.isalpha():
#         a+=1
#     else:
#         pass
# print("Letter",a)
# print("Digits",d)




# 15. Write a Python program to check the validity of passwords input by users.

# import re
# p=input("Enter password: ")
# x=True
#
# while x:
#     if (len(p)<6 and len(p)>12):
#         break
#     elif not re.search('[a-z]',p):
#         break
#     elif not re.search('[A-Z]',p):
#         break
#     elif not re.search('[0-9]',p):
#         break
#     elif not re.search('@#$',p):
#         break
#     elif re.search('\s',p):
#         break
#     else:
#         print("Valid Password")
#         x=False
#         break
#
# if x:
#     print("Not a livid")

# 16. . Write a Python program to find numbers between 100 and 400
# (both included) where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence.

# item=[]
# for i in range(100,401):
#     if i %2==0:
#         item.append(i)
# print(item)




# 17. Write Python program to print the alphabet pattern 'A'.




# result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);




# for row in range(7):
#     for col in range(5):
#         if (col==0 or col==4) or ((row == 0 or row == 3 or row == 6) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=' ')
#     print()

# for row in range(7):
#     for col in range(5):
#         if (col==0) or (col==4 and row!=0 and row !=3 and row!=6) or ((row == 0 or row == 3 or row == 6) and (col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# A
# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0 or(row==0 or row==3) and(col>0 and col<4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()




# B
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or (row ==0 or row ==3 or row ==6) and (col>0 and col<4):
            print("*",end="")
        else:
            print(end=" ")
    print()

















