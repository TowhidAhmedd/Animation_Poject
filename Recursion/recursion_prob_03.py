

# Write a python program to sum recursion lists.
#
#
# def list_sum(lst):
#     total=0
#     for i in lst:
#         if type(i) == type([]):
#             total=total + list_sum(i)
#         else:
#             total=total + i
#     return total
#
# lst=[2,4,[3,5],[5,3]]
# print(list_sum(lst))




def sum(lst):
    total=0
    for i in lst:
        if type(i) == type([]):
            total=total + sum(i)
        else:
            total+=i
    return total

lst=[1,2,[3,4],[5,8]]
print(sum(lst))
















