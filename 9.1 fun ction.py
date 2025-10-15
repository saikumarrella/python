"""Write a function to print "Hello, World!"."""
# def hello():
#     print(" hello world ")
# hello()
"""Write a function that takes a name as input and prints "Hello, <name>"."""
# def name(name1):
#     print(f"hello {name1}")
# n=input("enter the name :")
# a=name(n)
"""Write a function to add two numbers and return the result."""
# def add(a,b):
#     sum=a+b
#     return sum
# a=add(4,5)
# print(a)
"""Write a function that returns the square of a number."""
# def square(a):
#     s=a**2
#     return s
# a=square(4)
# print(a)
"""Write a function to find whether a number is even or odd."""
# def even(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input("enter the number"))
# a=even(n)
# print(a)
"""Write a function to calculate the area of a circle (use math.pi)."""
# import math
# def area_circle(r):
#     area=math.pi*r*r
#     return area
# r=float(input("enter the redius :"))
# a=area_circle(r)  
# print(a)
"""Write a function that takes a string and returns its length."""
# def lenth_str(a):
#     return len(a)
# b=input("enter nthe string :")
# b=lenth_str(b)
# print(b)
"""Write a function to find the maximum of three numbers."""
# def maxmum_num(a,b,c):
#    if a!=b and a!=c and b!=c:
#         if a>b and a>c:
#             return "a is max"
#         elif b>c:
#             return "b is max"
#         else:
#             return "c is max mum"
#    elif a==b and a!=c:
#        if a>c:
#            return "a,b is maxmum"
#        else:
#            return "c is maxmum"
#    elif a==c and a!=b:
#        if a>b:
#            return "a,c is maxmum"
#        else:
#            return "b is maxmum"
#    elif c==b and c!=a:
#        if a>c:
#            return "c,b is maxmum"
#        else:
#            return "a is maxmum"
#    else:
#         return "all are equal"
# a=int(input(" enter the number :"))
# b=int(input(" enter the number :"))
# c=int(input(" enter the number :"))
# a=maxmum_num(a,b,c)
# print(a)
"""Write a function to return the factorial of a number."""
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# a=int(input("enter the number :"))
# a=fact(a)
# print(a)
"""
Write a function to check whether a number is prime."""
# import math
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#          prime=True
#          return prime
#     else:
#          prime=False
#          return prime
# a=int(input("enter the number :"))
# a=prime(a)    
# print(a)
"""print the prime numbers"""
# def print_prime(n):
#     ans=[]
#     for i in range(n+1):
#         if prime(i)==True:
#             ans.append(i)
#     return ans
# b=int(input(" enter the nuber :"))
# a=print_prime(b)
# print(a)
"""Write a function to generate the Fibonacci sequence up to n terms."""
# def Fibonacci(n,a,b):
#     ans=[]
#     for i in range(1,n+1):
#         ans.append(a)
#         c=a+b
#         a=b
#         b=c
#     return ans
# a=int(input("enter the number (starting number):"))
# b=int(input(" enter the number(second number) :"))
# n=int(input(" enter the number what size you want "))
# a=Fibonacci(n,a,b)
# print(a)
"""Write a function to count the number of vowels in a string."""
# def vowels(n):
#     ab="aeiouAEIOU"
#     count=0
#     for i in n:
#         if i in ab:
#          count+=1
#     return count
# b=input("enter the string :")
# a=vowels(b)
# print(a)
"""
Write a function to reverse a string."""

# def reverse_string(n):
#     a=len(n)
#     str=""
#     for i in range(a-1,-1,-1):
#         str+=n[i]
#     return str
# n=input("enter the string :")
# b=reverse_string(n)
# print(b)
"""
revers of the nuber"""
def reverse(n):
    rev_num=0
    while n>0:
        rev=n%10
        rev_num=rev_num*10+rev
        n= n//10
    return rev_num
# n=int(input("enter the number :"))
# a=reverse(n)
# print(a)
"""Write a function that checks if a word is a palindrome (same forward & backward)."""
# def palindrome (n):
#     if n==reverse(n):
#         return  True
#     else:
#         return False
# b=int(input(" enter the number :"))
# a=palindrome(b)
# print(a)
"""gcd"""
a=int(input("enter the number :"))
b=int(input("enter the number :"))
while a%b==0:
    num=a%b
    gcd=a%num
print(gcd)















"""

Write a function that takes a list of numbers and returns the sum.

Write a function to return the largest element in a list."""
        
    
        
        
    
    