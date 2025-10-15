"""Print numbers from 1 to 10 using a for loop."""
# a=int(input("enter the number :"))
# for i in  range(a):
#     print(i)
"""Print even numbers between 1 and 50."""
"""one"""
# for i in range (2,51,2):
#     print(i)
"""two"""
# for i in range(51):
#     if i%2==0:
#         print(i)
"""Print the square of numbers from 1 to 10."""
# for i in range(1,11,1):
#     print(i**2)
"""Print the multiplication table of a given number."""
# a=int(input("enter the number :"))
# for i in range(1,11):
#     print(a,"*",i,"=",i*a)
"""Find the sum of numbers from 1 to n."""
# sum=0
# n=int(input("enter the number :"))
# for i in range(n+1):
#     sum+=i
# print(sum)
"""Find the factorial of a given number using for loop."""
# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)    
"""revers"""
# n=int(input(' enterr the number :'))
# fact=1
# for i in range(n,0,-1):
#     fact*=i
# print(fact)
"""Print all alphabets from A to Z."""
# for i in range(97,122+1):
#     print( chr(i))
"""Calculate the sum of digits of a number (convert number to string and loop through digits)."""
# n=549
# sum=0
# count=0
# while n>1:
#    num=n%10
#    print(num)
#    count+=1
#    n= n//10
#    print("n values",n)
#    sum+=num
# print(f"sum of the digits is {sum}")
# print(f"count is {count}")
"""aonther"""
# n=int(input(" enter the number"))
# a=str(n)
# sum=0
# for i in a:
#     # print(i)
#     sum+=int(i)
# print(sum)  
"""Reverse a string using a for loop."""
# n="SAI"
# rev=""
# for i in range(len(n)-1,-1,-1):
#     print(n[i])
#     rev+=n[i]
# print(rev)
# print(type(rev))
# print(len(rev))
"""fibinoises series"""
# a=0
# b=1
# n=int(input(" enter the number :"))
# if n==1:
#   print(a)
# elif n==2:
#     print(b)
# else:
#  for i in range(2,n,1):
#     c=a+b
#     a=b
#     b=c
#  print(c)
"""another"""
# a,b=0,1
# n=int(input(" enter the number :"))
# for i in  range(n-1):
#     c=a+b
#     a,b=b,c
# print(f"{n} number is the :{a}")
"""prime number check"""
# n=int(input(" enter the number :"))
# for i in range(2,n-1):
#     if n%i==0:
#       print(f"not prime number  of {i}")
#       break
#     else:
#         print("prime number")
"""print the prime numbers"""
# n=int(input(" enterr the nummber :"))
# for i in range(2,n+1):
    
#     for j in range(2,i):
#         if i%j==0 :
#             break
#     else:
#             print(i)
"""sqrt"""
# import math
# n=int(input(" enter the number :"))
# for i in  range(2,n+1):
#      for j in range(2,int(math.sqrt(i)+1)):
#          if i%j==0:
#              break
#      else:
#       print(i)
"""count"""
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#          return True
#     else:
#          return False
# n=int(input(" enter the number :"))
# a=[]
# for i in range(1,n+1):
#     if prime(i)==True:
#         a.append(i)
# print(a)
    
    