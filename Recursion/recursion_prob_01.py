

# Write a python program to calculate the sum of a list of numbers.

#
# def sum(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum(lst[1: ])
#
# lst=[2,3,4,5,3]
# print(sum(lst))




# def sum(lst):
#     total=0
#     for i in lst:
#         total+=i
#     return total
#
#
#
# lst=[1,2,4,2,5,4]
# print(sum(lst))







# def sum(lst):
#     total=0
#     if len(lst)==1:
#         pass
#         # return lst[0]
#     else:
#         return lst[0] + sum(lst[1: ])
#     return lst[0]
# lst=[1,3,5,3]
# print(sum(lst))
#





def sum(lst):
    if len(lst)==1:
        pass
        # return lst[0]
    else:
        return lst[0] + sum(lst[1: ])
    return lst[0]
lst=[1,2,3,4,5]
print(sum(lst))






