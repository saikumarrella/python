# def add(a,b):
#     return a+b
# z=add(2,5)
# print(z)
"""lamda"""
# z=lambda a,b:a+b
# x=z(2,7)
# print(x)
"""filter"""
# a=[1,2,3,4,5,6,7,8]
# z=list((filter(lambda n:n%2==0,a)))
# print(z)
"""map"""
# a=91,2,3,44
"""reduce"""
from functools import reduce
a=[1,2,3,4,5,4]
z=reduce(lambda a,b:a+b,a)
print(z)