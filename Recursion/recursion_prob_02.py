

# Write a python program to convert an integer to a
# string in any base.


def string_num(n,base):
    convert='0123456789abcdef'
    if n<base:
        return convert[n]
    else:
        return string_num(n // base,base) + convert[n % base]

print(string_num(2232,15))







