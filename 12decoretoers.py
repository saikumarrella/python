"""first"""
# def say_hi(sai):
#     def hi():
#         print("hi ra")
#         sai()
#         print("bye ra")
#     return hi
# @say_hi
# def say_hello():
#     print("hello")
# say_hello()
"""addtion"""
# def sub(fun):
#     def add(*args,**kwrags):
#         print("hello ")
#         fun(*args,**kwrags)
#         print("bye")
#     return add
# @sub
# def addtion(n,m):
#     print(f" addtion of the {n},{m} is {n+m} ")
# addtion(3,5)
"""multiplication"""
# def sai(fun):
#     def sub(*args,**krags):
#         print("heloo")
#         fun(*args,**krags)
#         print("bye")
#     return sub
# def mul(n,m):
#     print(f"mui is {n*m}")
# mul(2,3)
"""Logging Decorator
Write a decorator that prints the name of a function every time it is called."""
from functools import wraps
def sub(fun):
    @wraps(fun)
    def hi():
        print(f"name of the function :{fun.__name__}")
        fun()
    return hi
@sub
def sai():
    print("sai rela")
sai()