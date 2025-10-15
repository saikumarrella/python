"""Find the factorial of a number using recursion."""
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# a=fact(5)
# print(a)
"""Calculate the sum of first n natural numbers using recursion."""
# def natural_number(n):
#      if n==1:
#         return 1
#      return n+natural_number(n-1)
# b=int(input(" enter the number :"))
# a=natural_number(b)
# print(a)
"""Print numbers from 1 to n using recursion."""
"""desinding order"""
# def numbers(n):
#     print(n)
#     if n==1:
#         return 1
    
#     return  numbers(n-1)
# a=numbers(5)
"""asending order"""
# def number(n):
#     if n==1:
#         return [1]
       
#     b=number(n-1)
#     b.append(n)
#     return b
# a=number(5)
# print(a)
"""Find the nth Fibonacci number using recursion."""
# def fibonacci(n,a,b):
#     if n==1:
#         return a
#     c=a+b
#     a=b
#     b=c
#     return fibonacci(n-1,a,b)
# n=int(input(" enter the number :"))
# a=int(input(" enter the number :"))
# b=int(input(" enter the number :"))
# z=fibonacci(n,a,b)
# print(z)
"""print the Fibonacci number  using the recursion"""
# def fibonacci_series(n, a=0, b=1):
#     if n == 0:
#         return
#     print(a, end=" ")
#     fibonacci_series(n-1, b, a+b)

# # Example run
# n = int(input("Enter how many terms: "))
# fibonacci_series(n)
""" fibonacci"""
# def fib(n):
#     if n==0:
#       return 0
#     elif n==1:
#         return 1
#     else:
#        return fib(n-1)+fib(n-2)
# n=int(input(" enter the number :"))
# for i in range(n):
#  z=fib(i)
#  print(z)

           
    